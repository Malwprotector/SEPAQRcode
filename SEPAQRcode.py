import qrcode
from PIL import Image, ImageDraw, ImageFont

# Funkcja do generowania kodu QR SEPA z logo, dostosowanymi kolorami i napisem
def generate_sepa_qr_with_logo(iban, name, bic, amount, description, currency="EUR", 
                               fill_color="black", back_color="white", logo_path=None):
    # Format SEPA
    sepa_format = (
        f"BCD\n"
        f"002\n"  # Wersja formatu
        f"1\n"  # Charakter identyfikacyjny
        f"SCT\n"  # Typ przelewu SEPA Credit Transfer
        f"{bic}\n"  # Kod BIC banku
        f"{name}\n"  # Nazwa odbiorcy
        f"{iban}\n"  # IBAN odbiorcy
        f"{currency}{amount:.2f}\n\n\n"  # Kwota i waluta razem
        f"{description}\n"  # Opis transakcji
    )

    # Tworzenie kodu QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Lepsza korekcja błędów dla dodania logo
        box_size=10,
        border=4,
    )
    
    qr.add_data(sepa_format)
    qr.make(fit=True)

    # Generowanie obrazu kodu QR z dostosowanymi kolorami
    img_qr = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')
    
    # Jeśli logo jest dostarczone, dodaj je na środku kodu QR
    if logo_path:
        logo = Image.open(logo_path)
        
        # Zmiana rozmiaru logo
        logo_size = 80  # Rozmiar logo
        logo = logo.resize((logo_size, logo_size))
        
        # Obliczenie pozycji logo w środku
        pos = ((img_qr.size[0] - logo_size) // 2, (img_qr.size[1] - logo_size) // 2)
        
        # Wklejenie logo na środku obrazu kodu QR
        img_qr.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)
    
    # Dodanie napisu z kwotą poniżej kodu QR
    draw = ImageDraw.Draw(img_qr)
    
    # Wczytanie czcionki
    try:
        font = ImageFont.truetype("arial.ttf", 24)  # Użyj lokalnej czcionki
    except IOError:
        font = ImageFont.load_default()  # Czcionka domyślna, jeśli arial.ttf nie jest dostępna
    
    # Przygotowanie tekstu do wyświetlenia
    amount_text = f"{currency}{amount:.2f}"
    text_width, text_height = draw.textsize(amount_text, font=font)
    
    # Tworzenie nowego obrazu z napisem
    total_width = img_qr.width
    total_height = img_qr.height + text_height + 10  # 10 px odstępu między kodem QR a tekstem
    
    new_img = Image.new('RGB', (total_width, total_height), back_color)
    new_img.paste(img_qr, (0, 0))
    
    # Rysowanie napisu
    text_x = (total_width - text_width) // 2
    text_y = img_qr.height + 5  # 5 px odstępu od dolnej krawędzi kodu QR
    draw = ImageDraw.Draw(new_img)
    draw.text((text_x, text_y), amount_text, font=font, fill=fill_color)
    
    # Zapis obrazu z napisem
    new_img.save("sepa_qr_code_with_logo_and_amount.png")
    print("SEPA QR code with logo, custom colors, and payment amount generated and saved as 'sepa_qr_code_with_logo_and_amount.png'.")

# Getting user input
print("Please enter the information to generate the SEPA QR code:")

iban = input("Recipient's IBAN: ")
name = input("Recipient's name: ")
bic = input("Recipient's BIC (optional, press Enter to skip): ")
amount = float(input("Amount to transfer (in EUR, use . for cents): "))
description = input("Payment description: ")
fill_color = input("QR code color (e.g., 'black', 'blue', etc.): ")
back_color = input("Background color (e.g., 'white', 'yellow', etc.): ")
logo_path = input("Path to logo image file (optional, press Enter to skip): ")

if not logo_path:
    logo_path = None  # If no logo is provided

# Generating SEPA QR code with logo, custom colors, and amount text
generate_sepa_qr_with_logo(iban, name, bic, amount, description, fill_color=fill_color, back_color=back_color, logo_path=logo_path)

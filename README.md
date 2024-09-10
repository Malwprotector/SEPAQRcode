# SEPA QR Code Generator

## Overview

This Python application generates SEPA QR codes with customizable features such as adding a logo and specifying colors. The generated QR code includes payment details and displays the payment amount below the QR code image. This tool is ideal for creating payment requests with a visual representation that can be easily scanned by banking apps.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Examples](#examples)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Features

- Generate SEPA QR codes with custom colors.
- Add a logo to the QR code.
- Display payment amount below the QR code.
- Customizable payment details including IBAN, recipient name, and description.

## Requirements

- Python 3.x
- `qrcode` library
- `Pillow` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/sepa-qr-code-generator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd sepa-qr-code-generator
    ```

3. Install the required packages:

    ```bash
    pip install qrcode pillow
    ```

## Usage

1. Run the script:

    ```bash
    python sepa_qr_code_generator.py
    ```
    or
    ```bash
    python3 sepa_qr_code_generator.py
    ```

2. Follow the prompts to enter the payment details:

    - **Recipient's IBAN**
    - **Recipient's name**
    - **Recipient's BIC** (optional)
    - **Amount to transfer** (in EUR, use `.` for cents)
    - **Payment description**
    - **QR code color** (e.g., 'black', 'blue', etc.)
    - **Background color** (e.g., 'white', 'yellow', etc.)
    - **Path to logo image file** (optional)

3. The generated QR code will be saved as `sepa_qr_code_with_logo_and_amount.png` in the project directory.

## Configuration

The script allows the following configurations:

- **QR Code Color (`fill_color`)**: Color of the QR code. Default is `black`.
- **Background Color (`back_color`)**: Color of the background. Default is `white`.
- **Logo Path (`logo_path`)**: Path to the logo image file. The logo will be resized to 80x80 pixels and placed in the center of the QR code. If not provided, no logo will be added.
- **Font for Amount Text**: The script attempts to use `arial.ttf`. If not available, it falls back to a default font.

## Examples

1. **Generate QR Code with Logo and Custom Colors:**

    ```bash
    python sepa_qr_code_generator.py
    ```

    Enter the required details and provide a path to a logo image if desired. The script will generate a QR code with the specified features.

2. **Output:**

    The generated file will be named `sepa_qr_code_with_logo_and_amount.png` and will include:

    - A QR code with the provided SEPA payment details.
    - A logo centered in the QR code (if provided).
    - The payment amount displayed below the QR code.

## License

This project is licensed under the MIT License - see the [CC BY-NC-SA 4.0]( https://creativecommons.org/licenses/by-nc-sa/4.0/ ) file for details.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to suggest improvements or report bugs.

## Contact

For any questions or feedback, please contact [your-email@example.com](mailto:your-email@example.com).



## Readme Language

[中文](readmes/README.zh.md)
[Русский](readmes/README.ru.md)
[Português](readmes/README.pt.md)
[Español](readmes/READMEtr.md)

# NumGen
Educational Luhn algorithm pattern generator — Open Source project for academic learning only.

<p align="center">
  <img src="https://i.postimg.cc/XvJWVM1p/Screenshot-2.png" alt="NumGen App Screenshot" width="350">
</p>

## About
NumGen is a desktop application built in Python and Tkinter that generates **fictional numerical patterns compliant with the Luhn algorithm**.
This project is designed exclusively for **educational and academic purposes** to study card number structures and the Luhn check algorithm.

<p align="center">
  <img src="https://images.stripeassets.com/3sz5ney9ml0h/7mBN701LWvnXJPPU9NaqUx/2381a57b9cddf1df499e1b02e0ef5515/The-Luhn-algorithm-illustrated.png?w=1812&q=80" alt="The Luhn algorithm illustrated" width="600">
</p>
## Requirements
- Python 3.x
- Tkinter (included with standard Python installations)

## Usage

- **BIN**: First digit determines the brand
  - 3 = American Express
  - 4 = Visa
  - 5 = Mastercard
  - 6 = Discover
  - X = random

- **Date**: Select month/year or RND for random
- **CVV**: 3 digits or XXX for random
- **Quantity**: Number of cards to generate

## Output format
```
BIN|MONTH|YEAR|CVV
```

## Installation
No external dependencies are required beyond Python itself.
To package the application into a **Windows executable**, install PyInstaller:

```bash
pip install pyinstaller
```

## Run the Application
```bash
python NumGen.py
```

## Build to Windows Executable
```bash
python -m PyInstaller --onefile --windowed NumGen.py
```
The compiled executable will be located inside the dist/ folder:
```bash
dist/NumGen.exe
```

## Important Disclaimer / Warning

This software is developed and distributed **exclusively for educational and academic learning purposes** only.
It is designed solely to study the Luhn algorithm, numerical pattern structures, and general software development practice.

The creator **assumes no responsibility or liability** for any misuse, fraudulent activity, illegal employment, or unauthorized use of this tool by any person or entity.

Any improper, illegal, or malicious utilization of this software is strictly prohibited, and all responsibility falls solely on the end user.
No real financial, banking, or transactional data is validated or used within this program; all generated content is entirely fictional and created for theoretical study only.

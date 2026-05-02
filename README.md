# NumGen

Card number generator with Luhn validation.

## Requirements

- Python 3.x
- Tkinter (included in Python)

## Install

```bash
pip install pyinstaller
```

## Run

```bash
python NumGen.py
```

## Build .exe

```bash
pyinstaller --onefile --windowed NumGen.py
```

The executable will be in `dist/NumGen.exe`.

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
BIN|MES|YEAR|CVV
```

## Warning

This software is for educational use only. Illegal use is prohibited.
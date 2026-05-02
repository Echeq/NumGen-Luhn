# NumGen

Generator nomerov kart s proverkoy Luhn.

## Trebovaniya

- Python 3.x
- Tkinter (vkhodit v Python)

## Ustanovka

```bash
pip install pyinstaller
```

## Zapusk

```bash
python NumGen.py
```

## Kompilyatsiya v .exe

```bash
pyinstaller --onefile --windowed NumGen.py
```

Ispolnyaemy file budet v `dist/NumGen.exe`.

## Ispolzovaniye

- **BIN**: Pervaya tsifra opredelayet brend
  - 3 = American Express
  - 4 = Visa
  - 5 = Mastercard
  - 6 = Discover
  - X = sluchayno

- **Data**: vyberite mesyats/god ili RND dlya sluchaynogo
- **CVV**: 3 tsifry ili XXX dlya sluchaynogo
- **Kolichestvo**: kolichestvo kart dlya generatsii

## Format vyvoda

```
BIN|MES|GOD|CVV
```

## Preduprezhdeniye

Etoprogrammnoye obespecheniye tolko dlya obrazovatelnykh tseley. Nezakonnoye ispolzovaniye zapreshcheno.
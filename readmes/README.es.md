# NumGen

Generador de numeros de tarjeta con validacion Luhn.

## Requisitos

- Python 3.x
- Tkinter (incluido en Python)

## Instalar

```bash
pip install pyinstaller
```

## Ejecutar

```bash
python NumGen.py
```

## Compilar a .exe

```bash
pyinstaller --onefile --windowed NumGen.py
```

El ejecutable estara en `dist/NumGen.exe`.

## Uso

- **BIN**: El primer digito determina la marca
  - 3 = American Express
  - 4 = Visa
  - 5 = Mastercard
  - 6 = Discover
  - X = aleatorio

- **Fecha**: Selecciona mes/ano o RND para aleatorio
- **CVV**: 3 digitos o XXX para aleatorio
- **Cantidad**: Numero de tarjetas a generar

## Formato de salida

```
BIN|MES|ANO|CVV
```

## Advertencia

Este software es solo para uso educativo. El uso ilegal esta prohibido.
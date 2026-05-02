# Generador de Tarjetas Luhn

Generador de tarjetas de credito ficticias con validacion Luhn. Solo con fines educativos.

## Requisitos

- Python 3.x
- Tkinter (incluido en Python)

## Uso

```bash
python NumGen.py
```

## Caracteristicas

- **BIN**: Ingresa el BIN/IIN (primeras 6-8 digitos). Usa `X` para digitos aleatorios.
  - Si ingresas menos de 16 digitos, se completa automaticamente con `X`
  - Si el BIN no pasa la validacion Luhn, muestra error

- **Marca**: Se detecta automaticamente por el primer digito:
  - `3` → American Express
  - `4` → Visa
  - `5` → Mastercard
  - `6` → Discover

- **Fecha**: Mes/Ano. Selecciona `RND` para fecha aleatoria.

- **CVV**: 3 digitos o `XXX` para aleatorio.

- **Cantidad**: Numero de tarjetas a generar (1-100).

## Formato de Salida

Los numeros de tarjeta se generan sin espacios (ej: `4111111111111111`).
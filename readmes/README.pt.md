# NumGen

Gerador de numeros de cartao com validacao Luhn.

## Requisitos

- Python 3.x
- Tkinter (incluido no Python)

## Instalar

```bash
pip install pyinstaller
```

## Executar

```bash
python NumGen.py
```

## Compilar para .exe

```bash
pyinstaller --onefile --windowed NumGen.py
```

O executavel estarah em `dist/NumGen.exe`.

## Uso

- **BIN**: Primeiro digito determina a marca
  - 3 = American Express
  - 4 = Visa
  - 5 = Mastercard
  - 6 = Discover
  - X = aleatorio

- **Data**: Selecione mes/ano ou RND para aleatorio
- **CVV**: 3 digitos ou XXX para aleatorio
- **Quantidade**: Numero de cartoes a gerar

## Formato de saida

```
BIN|MES|ANO|CVV
```

## Aviso

Este software e apenas para uso educacional. Uso ilegal e proibido.
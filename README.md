# Generador de Tarjetas - Algoritmo Luhn (Educativo)

Software educativo para aprender el algoritmo Luhn y la estructura de tarjetas bancarias.

**SOLO PARA FINES EDUCATIVOS** - No valida ni usa tarjetas reales.

---

## Estructura del Proyecto

```
tarjeta-luhn-app/
├── include/
│   └── tarjeta.h          # Header con declaraciones
├── src/
│   └── tarjeta.c          # Implementacion en C
├── gui.py                 # Interfaz grafica Python
├── tarjeta.dll            # Compilado (generar con pasos abajo)
└── README.md              # Este archivo
```

---

## Funciones en C

| Funcion | Descripcion |
|---------|-------------|
| `generar_numero_tarjeta(marca)` | Genera numero ficticio valido (0=Visa, 1=MC, 2=Amex) |
| `identificar_marca(numero)` | Identifica la marca del numero |
| `generar_fecha_vencimiento()` | Genera fecha MM/AA |
| `generar_cvv()` | Genera 3 digitos |
| `formatear_numero(numero)` | Formatea con espacios |

---

## Compilar en Windows

### Paso 1: Abrir Developer Command Prompt

Busca "x64 Native Tools Command Prompt" en el menu inicio.

### Paso 2: Ir al directorio src

```batch
cd ruta\a\tarjeta-luhn-app\src
```

### Paso 3: Compilar

```batch
cl /LD /Fe:..\tarjeta.dll tarjeta.c
```

### Paso 4: Verificar

```batch
dir ..\tarjeta.dll
```

Si existe, la compilacion fue exitosa.

---

## Ejecutar

```batch
cd ruta\a\tarjeta-luhn-app
python gui.py
```

---

## Requisitos

- Python 3.x
- Visual Studio (para compilar C)

---

## Marcas Soportadas

- **Visa**: Inicia con 4
- **Mastercard**: Inicia con 51-55
- **American Express**: Inicia con 34 o 37
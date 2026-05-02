#ifndef TARJETA_H
#define TARJETA_H

#include <stdlib.h>

typedef enum {
    VISA,
    MASTERCARD,
    AMEX,
    DESCONOCIDA
} MarcaTarjeta;

char* generar_numero_tarjeta(MarcaTarjeta marca);
MarcaTarjeta identificar_marca(const char* numero);
char* generar_fecha_vencimiento(void);
char* generar_cvv(void);
char* formatear_numero(const char* numero);
void liberar_string(char* str);

#endif
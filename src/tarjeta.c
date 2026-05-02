#include "../include/tarjeta.h"
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

static int digito_luhn(int digito, int posicion) {
    if (posicion % 2 == 0) {
        digito *= 2;
        if (digito > 9) digito -= 9;
    }
    return digito;
}

static int validar_luhn(const char* numero) {
    int longitud = strlen(numero);
    int suma = 0;
    
    for (int i = longitud - 1; i >= 0; i--) {
        int digito = numero[i] - '0';
        int posicion = longitud - 1 - i;
        suma += digito_luhn(digito, posicion);
    }
    return (suma % 10 == 0);
}

static void calcular_digito_control(char* numero, int longitud) {
    int suma = 0;
    
    for (int i = 0; i < longitud; i++) {
        int digito = numero[i] - '0';
        int posicion = longitud - 1 - i;
        suma += digito_luhn(digito, posicion);
    }
    
    int digito = 0;
    while ((suma + digito) % 10 != 0) {
        suma -= digito_luhn(digito, longitud);
        digito++;
        if (digito > 9) digito = 0;
        if (digito == 0) suma = 0;
    }
    
    numero[longitud] = '\0';
    char control[3];
    sprintf(control, "%d", (10 - (suma % 10)) % 10);
    strcat(numero, control);
}

static void generar_basico(char* numero, const char* prefijo) {
    int prefijo_len = strlen(prefijo);
    int numeros_aleatorios = 14 - prefijo_len;
    
    strcpy(numero, prefijo);
    
    srand((unsigned int)time(NULL) ^ (unsigned int)prefijo_len ^ ((unsigned int)rand() << 16));
    
    for (int i = 0; i < numeros_aleatorios; i++) {
        numero[prefijo_len + i] = '0' + (rand() % 10);
    }
    numero[14] = '\0';
    
    calcular_digito_control(numero, 15);
}

char* generar_numero_tarjeta(MarcaTarjeta marca) {
    char* numero = (char*)malloc(20);
    if (!numero) return NULL;
    
    switch (marca) {
        case VISA:
            generar_basico(numero, "4000");
            break;
        case MASTERCARD:
            generar_basico(numero, "5100");
            break;
        case AMEX:
            generar_basico(numero, "3400");
            break;
        default:
            generar_basico(numero, "4000");
            break;
    }
    
    return numero;
}

MarcaTarjeta identificar_marca(const char* numero) {
    if (!numero) return DESCONOCIDA;
    
    if (strncmp(numero, "4", 1) == 0) return VISA;
    if (strncmp(numero, "51", 2) == 0 || strncmp(numero, "52", 2) == 0 ||
        strncmp(numero, "53", 2) == 0 || strncmp(numero, "54", 2) == 0 ||
        strncmp(numero, "55", 2) == 0) return MASTERCARD;
    if (strncmp(numero, "34", 2) == 0 || strncmp(numero, "37", 2) == 0) return AMEX;
    
    return DESCONOCIDA;
}

char* generar_fecha_vencimiento(void) {
    char* fecha = (char*)malloc(6);
    if (!fecha) return NULL;
    
    srand((unsigned int)time(NULL));
    int mes = 1 + rand() % 12;
    int anio = 26 + rand() % 10;
    
    sprintf(fecha, "%02d/%02d", mes, anio);
    return fecha;
}

char* generar_cvv(void) {
    char* cvv = (char*)malloc(4);
    if (!cvv) return NULL;
    
    srand((unsigned int)time(NULL));
    int cvv_num = rand() % 1000;
    
    sprintf(cvv, "%03d", cvv_num);
    return cvv;
}

char* formatear_numero(const char* numero) {
    int len = strlen(numero);
    char* formateado = (char*)malloc(len + len/4 + 1);
    if (!formateado) return NULL;
    
    int j = 0;
    for (int i = 0; i < len; i++) {
        formateado[j++] = numero[i];
        if ((i + 1) % 4 == 0 && i < len - 1) {
            formateado[j++] = ' ';
        }
    }
    formateado[j] = '\0';
    return formateado;
}

void liberar_string(char* str) {
    if (str) free(str);
}
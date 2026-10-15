# Proyecto 04 · Urban Valencia

## Descripción y objetivo

Pipeline completo de ingeniería de datos (batch + streaming) sobre datos abiertos de tráfico, calidad del aire y meteorología de Valencia. Los datos se cruzan con Spark y el proyecto termina con dos modelos predictivos: uno principal de NO₂ horario y uno secundario de intensidad de tráfico.

## Arquitectura

*Diagrama del pipeline completo.*

```mermaid
graph LR
    A[AEMET OpenData] --> B[Ingesta]
    B --> C[Almacenamiento]
    C --> D[Procesamiento]
    D --> E[Visualización / modelo]
```
## Fuentes de Datos

| Fuente | URL / origen | Formato | Frecuencia de actualización | Licencia | Última ingesta |
| --- | --- | --- | --- | --- | --- |
| AEMET OpenData (Predicción por municipio - Valencia) | https://opendata.aemet.es/ | JSON | Diaria |  AEMET | 2026-10-14 |


## Estructura del proyecto:

``` bash
.
├── data/
│   ├── raw/        # Datos crudos tal como llegan de la API
│   ├── staged/     # Datos limpios y normalizados
│   └── curated/    # Datos listos para modelar
├── ingesta/        # Scripts de descarga de fuentes de datos
├── .env            # Variables de entorno    
├── .env.example    # Plantilla de variables de entorno
└── README.md
```
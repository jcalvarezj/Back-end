# ETL System

This module provides an ETL system for the backend that enables the acquisition, cleaning, and storing of the data of interest into the database from raw Gas Station dataset.

The dataset files are obtained from the following sites:
- File 1 (places.xml): [Listado de Estaciones de Servicio con Georreferencia, XML de CRE](https://datos.gob.mx/busca/dataset/estaciones-de-servicio-gasolineras-y-precios-finales-de-gasolina-y-diesel/resource/099481f4-14cb-4f99-aaf4-da846fb261e4)
- File 2 (prices.xml): [Listado de Precios Comerciales de Gasolina y Diesel por Estación de Servicio, XML de CRE](https://datos.gob.mx/busca/dataset/estaciones-de-servicio-gasolineras-y-precios-finales-de-gasolina-y-diesel/resource/b1e92ceb-ba04-420f-bf48-42e4e8a27fe1)

## Requirements

**Python 3.x**, any version of **pip**, and **virtualenv** (or **venv**)

It is also necessary that the PostgreSQL database exists and is running.

Finally, the following environment variables are required to be set in the system:

- CUARTO_DB: name of the database
- CUARTO_USER: owner username
- CUARTO_PASS: access password

## Execution

Use either  `python main.py`  or  `python3 main.py` according to your system
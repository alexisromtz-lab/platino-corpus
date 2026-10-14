# platino-corpus

Este repositorio contiene **un solo objeto**: el manuscrito de M5.

- **Título:** Predicción pre-registrada cumplida (768 s): anterioridad sellada por git entre la cláusula predictiva y el objeto que la cumple
- **DOI (versión):** [10.5281/zenodo.23363121](https://doi.org/10.5281/zenodo.23363121)
- **DOI (concepto, todas las versiones):** [10.5281/zenodo.23363120](https://doi.org/10.5281/zenodo.23363120)
- **Registro público:** https://zenodo.org/records/23363121
- **Fecha de publicación:** 2026-10-14
- **Versión:** 0.1.0 · **Idioma:** spa · **Autor:** Roman Martinez, Jose Alexis (Platino Labs)

## Qué hay aquí

```
MANUSCRITO_5_PREDICCION_PRE_REGISTRADA_CUMPLIDA_768S_20261014.md   el objeto publicado (16734 B)
CITATION.cff                                                       metadatos de cita (DOI arriba)
README.md                                                          este archivo
```

El archivo de metadatos del depósito (`ZENODO_MANUSCRITO_5_...json`) viaja **dentro** del registro de
Zenodo, junto al manuscrito: es la hoja de portadores (blobs, commits y sellos de la evidencia primaria).

## Procedencia

El manuscrito no introduce mediciones nuevas: **cita** una anterioridad ya sellada por git entre una
cláusula predictiva (`RC=40` / `BANCO:OBJETO_AUSENTE`, acta verde `de76344`, epoch `1791943518`) y el
objeto que la cumple (adaptador `core/persistence.py`, `e73d1e0`, epoch `1791944286`), con
`delta_s = 768`. La evidencia primaria (acta) y el código viven en el repositorio de trabajo
[alexisromtz-lab/platino-labs](https://github.com/alexisromtz-lab/platino-labs); este repositorio
existe para que el objeto publicado tenga una URL estable y citable **sin** arrastrar el corpus.

## Licencia — esquema de dos capas, y un defecto declarado

<!-- HUELLA-README-ALINEADO-LICENCIA-20261014 -->

El corpus decide la licencia **por capas**, y la decisión está escrita en el repositorio de trabajo
(`LICENSE` · `LICENSE-DOCS.md`): los **documentos y datos** (`*.md`, `*.json`, `*.cff`) van bajo
**CC BY 4.0** y el **código** (`*.py`, `*.sh`, `*.toml`, `action.yml`) bajo **Apache 2.0**. El objeto
publicado aquí es documentación, de modo que su capa es **CC BY 4.0**: eso declara este registro y eso
cita el `CITATION.cff` de este repositorio. El campo `license` del depósito admite **un solo valor** y
debe llevar **la capa del objeto depositado**.

Ahora bien: la cabecera de ese manuscrito declara `MIT`, un valor que **no pertenece a ninguna de las dos
capas** ⇒ es un **defecto declarado, no reparado**. No se repara porque el objeto queda **sellado** por su
DOI (la corrección viaja por apéndice, en el repositorio de trabajo) y porque el defecto **no es de ese
manuscrito sino de la convención de la serie** — el Manuscrito 1 declara el mismo valor—. Esa divergencia
está declarada en los metadatos del depósito (`notes`), que la conservan por consistencia de serie.

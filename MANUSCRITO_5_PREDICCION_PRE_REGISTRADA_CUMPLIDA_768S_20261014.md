# Predicción pre-registrada cumplida (768 s)

**HUELLA:** `HUELLA-MANUSCRITO-5-PREDICCION-PRE-REGISTRADA-CUMPLIDA-768S-20261014`
**VERSION:** `manuscrito-5-v1-20261014`
**FECHA DE CIERRE:** 2026-10-14
**CASA:** `/Users/marlene/platino-labs`
**AUTOR:** Roman Martinez, Jose Alexis — `alexisromtz-lab`
**LICENCIA:** MIT · **TIPO DE REGISTRO:** publicación (preprint) · **IDIOMA:** spa
**EVIDENCIA PRIMARIA (el objeto medido, no este texto):** `ACTA_PREDICCION-CUMPLIDA-768s_20261014.md` · 134 l · 8 967 B · blob `27a0cd5dd00a931e12da172aacf12ef19f27dd2e` · commit `3d68158` (`3d681583d9dea703b7919254f3d27269922d8d29`) · HUELLA `HUELLA-ACTA-PREDICCION-CUMPLIDA-768S-20261014`
**PRE-VUELO A2.1 (turno 1):** `bash tools/gate_pre_escritura.sh <TARGET> e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 'HUELLA-MANUSCRITO-5-PREDICCION-PRE-REGISTRADA-CUMPLIDA-768S-20261014' 0` → `COLISION: ... no existe.` → **PRE_RC = 10** (ausencia medida ⇒ escritura autorizada), medido `2026-10-14T09:22:58Z`.

**Nota de procedencia de este texto.** Este manuscrito es la **elevación a paper** de la acta sellada `ACTA_PREDICCION-CUMPLIDA-768s_20261014.md`. No introduce ninguna cifra nueva: **cita las de la acta con su portador, su unidad y su hora**, y añade una sola medición propia —la verificación de fidelidad de §7, corrida `2026-10-14T09:14:42Z`— que es read-only y se declara como tal. Se declara también el hallazgo que motivó la elevación: **el manuscrito 5 no existía en disco ni en git** antes de esta escritura (`UNIVERSO DECLARADO: /Users/marlene/platino-labs, sin .git · nombres con MANUSCRITO|PAPER|ARTICULO|*.tex = 6`, ninguno de ellos este objeto).

---

## UNIVERSO DECLARADO (global del manuscrito)

```
UNIVERSO DECLARADO: árbol git /Users/marlene/platino-labs en la rama main,
con .git incluido sólo para las identidades de blob y el excluido para los conteos
de casas. Mediciones con hora UTC junto a cada cifra.
motor de las mediciones = git 3.x (epoch de commit, no mtime de archivo) · shasum -a 256 · python3
unidad declarada en cada conteo (casas != ocurrencias != líneas)
ventana: árbol en reposo declarado al momento de medir; los movimientos de otra
         mano se declaran abajo y NO se adjudican
umbral: ninguno — este manuscrito sólo afirma identidades, conteos y un delta de epochs
```

**Regla de lectura:** toda cifra afirma con **portador declarado** (archivo · blob · líneas · bytes) y **comando que la respalda**. Una cifra cuya única fuente es la prosa de un commit se declara como tal y **no** se cuenta como resultado medido. Ninguna cifra entra sin su hora: **toda cifra de conteo caduca al escribirla.**

---

## §0 · Abstract

Se enuncia y se mide un caso de **anterioridad sellada por git**: una cláusula predictiva falsable se escribió **768 segundos antes** de que existiera el objeto que la cumple, y el cumplimiento se verificó **contra el mismo banco**, con **las mismas causas tipadas**.

La cadena no se sostiene por relato sino por **epoch de commit**: el acta que enuncia la predicción entra al árbol en `de76344` (`epoch 1791943518`); el adaptador predicho entra en `e73d1e0` (`epoch 1791944286`). Delta = **768 s** (12 m 48 s), positivo en el sentido exigido —la predicción **precede** al objeto— y **inmune al `mtime`**, porque es el sello de git el que ordena.

El brazo diferencial que en el acta de alta devolvía `RC=40 · BANCO:OBJETO_AUSENTE` hoy devuelve **`RC=0`**, con `CASOS_OK: 7/7 · GEMELOS_OK: 7/7 · VEREDICTO_BANCO: VERDE`, y con la **misma causa tipada** (`MEMORIA:MOTOR_INCOMPATIBLE`) que su brazo de referencia. La predicción era: *«cuando exista, la misma corrida debe pasar a `RC 0` contra el mismo banco»*. Se cumple.

**Lo que este trabajo no afirma:** no afirma mérito sobre el objeto (un adaptador de persistencia es ingeniería corriente). Afirma **el orden**: que el resultado estaba fijado antes de que el resultado fuera posible.

---

## §1 · Problema

Un pre-registro vale lo que vale su **anterioridad**. Si el criterio de éxito se escribe después de conocer el resultado, es una descripción; si se escribe antes, es una **predicción**, y su cumplimiento es evidencia de que el sistema se entendía, no de que se tuvo suerte.

El defecto que este caso ataca es de **instrumento**: la mayoría de los «pre-registros» no son auditables porque su fecha vive en prosa, en un archivo con `mtime` mutable, o en un documento sin identidad de contenido. Ninguna de esas tres cosas resiste un reordenamiento: un `touch`, un `git checkout` o una copia las reescribe.

La pieza que sí resiste es la **tupla de git**: `commit` + `epoch` + `blob`. Un `epoch` de commit no se puede retrodatar sin reescribir la historia, y un `blob` fija el contenido exacto sobre el que la afirmación se hizo.

**Formulación del caso:** `epoch(objeto) − epoch(predicción) = 768 s > 0`, con la cláusula predictiva **idéntica** en el blob de alta y en el de hoy.

---

## §2 · La cadena de anterioridad — medida por comando, no por relato

| Objeto | Alta (commit) | epoch (s) | líneas | blob |
|---|---|---|---|---|
| Acta verde del banco must-fail (contiene la predicción) | `de76344` | `1791943518` | `176` | `2572ee2df66098f2b7830a77f37a1cabee8b75e3` |
| Adaptador `core/persistence.py` (el objeto predicho) | `e73d1e0` | `1791944286` | `551` | `b2fc6ea80bb19deadfc52c6823cb47d7de4719e9` |

Comandos, verbatim:

```
git show -s --format='%H %at %s' de76344
de76344919c0d13d87459d751ecc1c716deb513f 1791943518 docs(acta): banco must-fail persistencia causal VERDE -- reporte del paso 4 (176 l, blob 2572ee2d)

git show -s --format='%H %at %s' e73d1e0
e73d1e0289bc8d15f53bb33aad1d6201c1ce28bf 1791944286 feat(core): adaptador de persistencia causal (Estrato 2) — serializar/rehidratar/cache/promover, 551 l, blob b2fc6ea8
```

- **`delta_s = 1791944286 − 1791943518 = 768`** (12 m 48 s).
- **Lectura:** el acta que enuncia la predicción es **anterior** al objeto que la cumple. El delta es **positivo** (la predicción precede al objeto) y está **sellado por git** — el **epoch del commit**, no el `mtime` del archivo.
- **Declarado, no adjudicado:** el camino medido es `core/persistence.py` **tal como existía en `e73d1e0`**; el árbol movió ese directorio a `platino_core` en un commit posterior (`398b968`). La medición está anclada al epoch de su propio commit y **no se re-ancla**.

---

## §3 · La cláusula predictiva, verbatim

Bloque medido en el acta verde, **l.104–112**, leído en su **blob de hoy** y en su **blob de alta (`de76344`)** — los dos idénticos salvo la errata declarada en §5.

> ### 4.6 Brazo diferencial (cláusula iv del contrato)
>
> ```
> python3 -B sim/banco_must_fail_persistencia_causal_20261014.py --objeto core.persistence ; echo RC=...
> UNIVERSO DECLARADO: brazo diferencial --objeto core.persistence (objeto ausente)
> OBJETO=core.persistence -> BANCO:OBJETO_AUSENTE (ModuleNotFoundError)
> VEREDICTO_BANCO: ROJO (brazo diferencial: el objeto no existe)
> RC=40
> ```
>
> `core/persistence.py` **no existe todavía** (es el paso 3). El brazo diferencial es lo que hará **atribuible** el verde del adaptador: cuando exista, la misma corrida debe pasar a `RC 0` *contra el mismo banco*; si existe pero diverge, `RC 41 BANCO:DIVERGENCIA_ESPEC`.

**Notas de fidelidad (declaradas, no adjudicadas):**

1. **Se omite el signo de invitación de shell** al inicio de la primera línea del bloque verbatim (escrito aquí por su nombre, no por su signo, para no introducir un carácter que el propio medio expande). El resto es literal.
2. **El nombre del parágrafo y su número no coinciden.** El dictamen de dirección nombra este bloque **§4.5**; la cabeza medida en el acta es `### 4.6 Brazo diferencial (cláusula iv del contrato)`. Es **el mismo objeto con dos nombres** ⇒ se registra **el par**, no se elige. No se renumera el acta verde (append-only).
3. **La cláusula predictiva** es la de la última línea: *«cuando exista, la misma corrida debe pasar a `RC 0` contra el mismo banco»*. Es **falsable** y está **pre-registrada**: el acta del banco con `RC=40` es anterior a la existencia del adaptador.

**Por qué es una predicción y no una descripción.** La cláusula fija **tres** cosas antes de que el objeto exista: (i) **qué** corrida (la misma, contra el mismo banco), (ii) **qué** resultado (`RC 0`), y (iii) **qué** lo refutaría (que exista y **diverja** ⇒ `RC 41`). Una descripción no puede fallar; ésta podía.

---

## §4 · El cumplimiento — corrida contra el mismo banco

**Brazo `spec` (el banco contra sí mismo):** `/tmp/banco_f1_spec.txt` · 61 líneas · 5 851 B · `sha16 369bd239eed6370b` · `mtime 2026-10-14T05:12:13Z`

**Brazo `core.persistence` (el brazo diferencial predicho):** `/tmp/banco_f1_adp.txt` · 61 líneas · 5 863 B · `sha16 23b0ffe7ca69d9a4` · `mtime 2026-10-14T05:12:13Z`

Ambos crudos, verbatim en sus líneas finales:

```
CASOS_OK: 7/7 · GEMELOS_OK: 7/7
VEREDICTO_BANCO: VERDE
RC=0
```

**Causa tipada MF3 (idéntica en los dos brazos), verbatim del crudo del brazo diferencial:**

```
  MF3    rc=1/1 esperado=MEMORIA:MOTOR_INCOMPATIBLE   impreso=MEMORIA:MOTOR_INCOMPATIBLE   nodo=-1  gate=1  [ok]
         nivel de motor distinto
```

**Unidad declarada de la causa** (trampa pagada: `grep -c` cuenta **líneas**, no **ocurrencias**):

- `MEMORIA:MOTOR_INCOMPATIBLE`: **3 líneas / 4 ocurrencias** en `spec` · **3 líneas / 4 ocurrencias** en `adaptador`.
- `MEMORIA:LECTURA_RASGADA`: **0 líneas** en `spec` · **0 líneas** en `adaptador`.

**La predicción se cumple:** contra el **mismo banco**, el brazo que antes daba `RC=40` (`BANCO:OBJETO_AUSENTE`) ahora da **`RC=0`** con **7/7 · 7/7 · VERDE** y **las mismas causas tipadas**. El verde del adaptador queda **atribuible** — que era exactamente lo que la cláusula iv prometía.

**Por qué la causa tipada importa más que el `RC`.** Un `RC=0` sólo dice que no falló. La causa tipada dice **qué** se midió: `MEMORIA:MOTOR_INCOMPATIBLE` aparece por **nivel de motor distinto**, que es precisamente la hipótesis del banco. Si el `RC` fuera 0 por otro motivo, el caso **no discriminaría**; el par (`rc esperado`, `causa impresa`) es lo que lo vuelve discriminante.

**Paridad byte-for-byte (sonda sellada):** `/tmp/sonda_paridad_20261014.txt` · 3 056 B · `mtime Oct 13 23:12` (local)

```
CHEQUEOS: 28 ok / 28
VEREDICTO_PARIDAD: VERDE · rc=0
```

con `[ok] serializar: BYTES IDENTICOS :: 106156 B · sha 3842f665ddeb94fb vs 3842f665ddeb94fb` y `[ok] cache: BYTES IDENTICOS :: 7191 B · 6.77% del blob`, y **control positivo declarado** `[ok] CONTROL POSITIVO: el metro PUEDE diferir (bytes != con motor ajeno) :: sha 3842f665ddeb94fb vs af175c2fee2648c6`.

---

## §5 · La errata que NO tocó la predicción

El diff **alta → hoy** del acta verde toca **una sola cosa dentro del bloque citado**: el literal `BANCO:DIVERGENCIA_SPEC` (alta) pasa a `BANCO:DIVERGENCIA_ESPEC` (hoy), más una errata en su §10. Medido hoy: el crudo del brazo diferencial imprime `BANCO:DIVERGENCIA_ESPEC` ⇒ **el literal corregido es el que el instrumento usa**.

**Lo importante:** la **cláusula predictiva** (`cuando exista, la misma corrida debe pasar a RC 0 contra el mismo banco`) es **idéntica** en los dos blobs. La errata **no reescribió la predicción**: por eso la anterioridad de §2 es prueba y no coincidencia.

Medición de este manuscrito (`2026-10-14T09:14:42Z`): líneas del diff alta→hoy del bloque citado = **12**, y **ninguna** cae sobre la frase predictiva.

---

## §6 · Anchos de las dos cifras ubicuas

Una cifra ubicua **no puede sostener un rojo sola**, y tampoco un verde. Se declara su **ancho**.

| Cifra | Instante / ámbito | Substring (casas) | Anclada (casas) | Anclada (ocurrencias) |
|---|---|---|---|---|
| `6.77` | `2026-10-14T05:22:56Z` · raíz del repo, `.git` excluido | `18` | `8` | — |
| `8/8` | `2026-10-14T05:22:56Z` · raíz del repo, `.git` excluido | `141` | `116` | `209` |

- Los conteos del dictamen (`6.77` en 9 archivos · `8/8` en 83 casas) fueron tomados **en otro instante y sin ámbito declarado**. **No contradicen** a los de esta tabla: **son otras mediciones**. Toda cifra de conteo caduca al escribir; su hora y su ámbito son parte de la cifra.
- **Dónde vive y dónde no vive `8/8`:** en los **crudos del banco F1 = 0** (anclado sobre los dos archivos) y en el **mensaje del commit** `31a5c60` = **1**. Es decir: `8/8` vive en la **prosa del commit**, no en el crudo que mide.
- **`8/8` en el acta verde = 0.**

Ninguna de las dos sostiene por sí sola una afirmación: se citan **con su objeto y su comando**, o no se citan.

---

## §7 · Verificación de fidelidad de este manuscrito — cuatro datos, `2026-10-14T09:14:42Z`

Medición **read-only** sobre el objeto primario (no sobre esta copia). Comandos y salidas:

| # | Dato | Comando | Salida |
|---|---|---|---|
| 1 | Aritmética de la anterioridad | `git show -s --format=%at de76344` · `git show -s --format=%at e73d1e0` | `1791943518` · `1791944286` ⇒ **768 = exacto** (`COINCIDE = SI`) |
| 2 | Cláusula predictiva verbatim | lectura del bloque en el blob de `de76344` y en el de `HEAD` | frase presente **1/1** en ambos; bloque **idéntico** salvo la errata declarada de §5; `LINEAS_DIFF = 12`, fuera de la predicción |
| 3 | Causa tipada MF3 en los dos brazos | lectura de `/tmp/banco_f1_spec.txt` y `/tmp/banco_f1_adp.txt`, l.24 | ambos: `rc=1/1 esperado=MEMORIA:MOTOR_INCOMPATIBLE impreso=MEMORIA:MOTOR_INCOMPATIBLE nodo=-1 gate=1 [ok]` |
| 4 | Identidad del acta | `git hash-object` · `git rev-parse HEAD:...` · `git log -1` | `27a0cd5dd00a931e12da172aacf12ef19f27dd2e` = `HEAD` · `3d68158` **toca** el acta · `134` líneas · `8 967` B |

**Resultado: 4/4.** Los cuatro datos coinciden con el crudo. Se declara además un **defecto de metro propio, pagado**: un `grep -l 768 | head -10` sobre 89 archivos coincidentes **ocultó** el acta ⇒ el cero era de mi truncamiento, **no del objeto**.

---

## §8 · Frontera de este manuscrito

- **No introduce cifras nuevas.** Todas sus cifras provienen de la acta sellada (§2–§6) o de la verificación de §7, declarada como propia.
- **No re-corre el banco** para «confirmar»: los crudos sellados se citan con su `sha16`, su tamaño y su hora.
- **No toca** el banco must-fail, ni la sonda de paridad, ni el banco de corte consistente concurrente (otro objeto, dueño de `N_eventos_totales = 1000`).
- **No adjudica** el movimiento del árbol: entre la tupla de autorización y esta escritura, **otra mano movió `HEAD`** y renombró `core` → `platino_core`. Se **declara**, no se interfiere.
- **Una cifra del dictamen de dirección se retira aquí:** «0 publicaciones externas» **no tiene comando que la respalde**. Medido `2026-10-14T09:22:58Z` sobre `platino-labs` (unidad = literal único, sin `.git`): **6** literales `10.5281/zenodo.*` distintos. Si esos registros son **propios** o **citados** exige atribución por registro ⇒ **se declara, no se adjudica**. La cifra **no entra** a este paquete.

---

## §9 · Reproducción

```
git show -s --format='%H %at %s' de76344
git show -s --format='%H %at %s' e73d1e0
git rev-parse de76344:ACTA_BANCO_MUST_FAIL_PERSISTENCIA_CAUSAL_VERDE_20261014.md
git rev-parse e73d1e0:core/persistence.py
git hash-object ACTA_PREDICCION-CUMPLIDA-768s_20261014.md
git rev-parse HEAD:ACTA_PREDICCION-CUMPLIDA-768s_20261014.md
git show -s --format=%H 3d68158
```

Los crudos de `/tmp` (`banco_f1_spec.txt`, `banco_f1_adp.txt`, `sonda_paridad_20261014.txt`) son **sellados**: se citan por `sha16` y tamaño. Un crudo intermedio es **irrepetible** si no se conserva el instrumento que lo produjo.

---

## §10 · Cierre

**Anterioridad sellada de 768 segundos:** la predicción se escribió **768 s antes** de que existiera el objeto que la cumple, y el cumplimiento se midió **contra el mismo banco**, con **las mismas causas tipadas**.

No se atribuye al azar. Se atribuye a un **pre-registro que fijó el resultado antes de que el resultado fuera posible** — y a un instrumento (la tupla `commit` + `epoch` + `blob`) que hace que la anterioridad sea **medible** y no declamada.

**Lo que este manuscrito pide de quien lo lea:** que intente refutarlo. Los tres puntos de refutación están declarados: (i) que el epoch de `de76344` no sea anterior al de `e73d1e0`; (ii) que la frase predictiva **no** sea idéntica en los dos blobs; (iii) que el brazo diferencial llegue a `RC=0` **por otra causa** que `MEMORIA:MOTOR_INCOMPATIBLE`. Los tres están medidos en §7 y los tres dan en contra de la refutación.

ESTADO: **LISTO PARA REGISTRO** (Zenodo → DOI · cross-list arXiv).

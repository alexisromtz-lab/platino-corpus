"""HUELLA-TEST-SEMANTICA-CORPUS-NV6-20261022"""

from pathlib import Path
import re
import unicodedata


ROOT = Path(__file__).resolve().parents[1]
MANUSCRITO = ROOT / "MANUSCRITO_5_PREDICCION_PRE_REGISTRADA_CUMPLIDA_768S_20261014.md"


def tokenizar(texto: str) -> set[str]:
    normalizado = unicodedata.normalize("NFKD", texto).casefold()
    normalizado = "".join(caracter for caracter in normalizado if not unicodedata.combining(caracter))
    return set(re.findall(r"[^\W_]+", normalizado, flags=re.UNICODE))


def similitud_jaccard(a: set[str], b: set[str]) -> float:
    union = a | b
    if not union:
        return 0.0
    return len(a & b) / len(union)


def extraer_seccion(texto: str, numero: int) -> str:
    encabezado = re.search(rf"(?m)^## §{numero}\b.*$", texto)
    if encabezado is None:
        raise AssertionError(f"Falta la sección §{numero}")
    siguiente = re.search(r"(?m)^## §\d+\b", texto[encabezado.end():])
    fin = encabezado.end() + siguiente.start() if siguiente else len(texto)
    return texto[encabezado.start():fin]


def main() -> None:
    texto = MANUSCRITO.read_text(encoding="utf-8")
    prediccion = extraer_seccion(texto, 3)
    cumplimiento = extraer_seccion(texto, 4)
    control_tematico = extraer_seccion(texto, 6)

    afirmacion = tokenizar("la misma corrida debe pasar a RC 0 contra el mismo banco")
    evidencia = tokenizar(prediccion + "\n" + cumplimiento)
    distractor = tokenizar(control_tematico)
    puntuacion_positiva = similitud_jaccard(afirmacion, evidencia)
    puntuacion_distractor = similitud_jaccard(afirmacion, distractor)

    assert puntuacion_positiva > puntuacion_distractor, (
        f"La evidencia no discrimina la predicción: {puntuacion_positiva:.3f} "
        f"<= control temático {puntuacion_distractor:.3f}"
    )
    assert {"misma", "corrida", "rc", "0", "banco"} <= tokenizar(prediccion)
    assert {"rc", "40", "ausente"} <= tokenizar(prediccion)
    assert {"rc", "41", "divergencia"} <= tokenizar(prediccion)
    assert {"rc", "0", "memoria", "motor", "incompatible"} <= tokenizar(cumplimiento)
    assert similitud_jaccard(tokenizar(""), set()) == 0.0

    print("[VEREDICTO] BATERIA SEMANTICA SANA (RC 0)")


if __name__ == "__main__":
    main()

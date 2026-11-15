import re

# Equivalencia entre las palabras que aparecen en el texto y su dígito.
# Los valores son str (no int) porque más abajo se concatenan como texto.
WORD_TO_NUMBER = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

# Expresión regular que detecta un dígito escrito con palabra o con número.
# - (?=...) es un lookahead: mira hacia adelante sin consumir caracteres.
#   Esto permite detectar palabras que se solapan, p. ej. "eightwo" -> eight y two.
# - El grupo de captura interno ( ... ) es necesario: como el lookahead no consume
#   texto, el match completo siempre es vacío y findall devuelve solo lo capturado.
# - [0-9]{1} es un único dígito (equivale a [0-9]).
REGEX = r"(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]{1}))"


def get_calibration_values(string) -> int:
    """Devuelve el valor de calibración de una línea.

    Es el número de dos dígitos formado por el primer y el último dígito
    (numérico o escrito con palabra) de la línea.
    Ejemplo: "two1nine" -> 29
    """
    # Lista con todos los dígitos encontrados, en orden, incluyendo solapados.
    # Ejemplo: "eightwothree" -> ["eight", "two", "three"]
    values = re.findall(REGEX, string)

    # Solo importan el primero y el último; si son palabras, se pasan a dígito.
    if values[0] in WORD_TO_NUMBER:
        values[0] = WORD_TO_NUMBER[values[0]]
    if values[-1] in WORD_TO_NUMBER:
        values[-1] = WORD_TO_NUMBER[values[-1]]

    # Se concatenan como texto ("2" + "9" = "29") y luego se convierten a int.
    # Si la línea tiene un solo dígito, primero y último son el mismo ("7" -> 77).
    return int(values[0] + values[-1])


def get_solution(input_file: str) -> int:
    """Suma los valores de calibración de todas las líneas del archivo."""
    all_num = []
    # "with" garantiza que el archivo se cierre al terminar de leerlo.
    with open(input_file, "r") as f:
        for line in f:
            all_num.append(get_calibration_values(line))
    return sum(all_num)


if __name__ == "__main__":
    # Ruta relativa al directorio desde donde se ejecuta el script:
    # funciona al correrlo desde la raíz del proyecto (advent-of-code/).
    print(get_solution("2023/day_01/input.txt"))

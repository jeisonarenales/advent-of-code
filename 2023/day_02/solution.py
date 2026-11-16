# Part 1
# Cantidad máxima de cubos de cada color que tiene la bolsa en la parte 1.
RED_VALUE = 12
GREEN_VALUE = 13
BLUE_VALUE = 14


def is_a_valid_subset(subset: dict[str, int]) -> bool:
    """Indica si una extracción es posible con los cubos de la bolsa.

    Es válida solo si ningún color supera su máximo (RED_VALUE, GREEN_VALUE,
    BLUE_VALUE). Un valor igual al máximo sigue siendo válido.
    """
    is_valid = True
    if (
        subset["red"] > RED_VALUE
        or subset["green"] > GREEN_VALUE
        or subset["blue"] > BLUE_VALUE
    ):
        is_valid = False
    return is_valid


def extract_balls(subset: str) -> dict[str, int]:
    """Convierte el texto de una extracción en un dict de cantidades por color.

    Los colores que no aparecen en el texto quedan en 0.
    Ejemplo: "3 blue, 4 red" -> {"red": 4, "green": 0, "blue": 3}
    """
    balls = {"red": 0, "green": 0, "blue": 0}
    # Cada elemento tiene la forma "<cantidad> <color>", p. ej. " 4 red".
    colors = subset.split(",")
    for c in colors:
        value, color = c.strip().split()
        if color == "red":
            balls["red"] = int(value)
        if color == "green":
            balls["green"] = int(value)
        if color == "blue":
            balls["blue"] = int(value)
    return balls


def extract_subsets(sets: str) -> list[dict[str, int]]:
    """Convierte la parte de las extracciones de un juego en una lista de dicts.

    Las extracciones vienen separadas por ";".
    Ejemplo: "3 blue, 4 red; 2 green" ->
        [{"red": 4, "green": 0, "blue": 3}, {"red": 0, "green": 2, "blue": 0}]
    """
    subsets = []
    game_sets = sets.split(";")
    for subset in game_sets:
        subsets.append(extract_balls(subset))
    return subsets


def extract_game_id(game_str: str) -> int:
    """Obtiene el id numérico a partir del texto "Game <id>".

    Ejemplo: "Game 3" -> 3
    """
    _, game_id = game_str.split()
    return int(game_id)


def get_fewest_number_of_cubes(subsets: list[dict[str, int]]) -> dict[str, int]:
    """Calcula el mínimo de cubos de cada color necesario para que el juego sea posible.

    Es el máximo de cada color en todas las extracciones: si en alguna salieron
    6 azules, la bolsa tiene al menos 6 azules.
    """
    red = 0
    green = 0
    blue = 0
    for s in subsets:
        if s["red"] > red:
            red = s["red"]
        if s["green"] > green:
            green = s["green"]
        if s["blue"] > blue:
            blue = s["blue"]
    return {"red": red, "green": green, "blue": blue}


def solution_part_1(line: str) -> int:
    """Resuelve la parte 1 para una línea (un juego).

    Devuelve el id del juego si todas sus extracciones son válidas, o 0 si
    alguna no lo es. Así, sumar el resultado de todas las líneas da la respuesta.
    """
    # La línea tiene la forma "Game <id>: <extracciones separadas por ;>".
    game, sets = line.split(":")
    game_id = extract_game_id(game)
    subsets = extract_subsets(sets)
    is_valid = True
    for s in subsets:
        if not is_a_valid_subset(s):
            is_valid = False
    if is_valid:
        return game_id
    else:
        return 0


def solution_part_2(line: str) -> int:
    """Resuelve la parte 2 para una línea (un juego).

    Devuelve el "poder" del juego: rojos * verdes * azules mínimos necesarios.
    Sumar el resultado de todas las líneas da la respuesta.
    """
    game, sets = line.split(":")
    # El id se extrae pero no se usa: en la parte 2 solo importan los cubos.
    game_id = extract_game_id(game)
    subsets = extract_subsets(sets)
    color_values = get_fewest_number_of_cubes(subsets)
    return color_values["red"] * color_values["green"] * color_values["blue"]


if __name__ == "__main__":
    # La ruta es relativa al cwd: ejecutar desde la raíz del proyecto (advent-of-code/).
    input_file = "2023/day_02/input.txt"
    valid_games = []
    with open(input_file, "r") as f:
        for line in f:
            valid_games.append(solution_part_1(line))
    print(f"SOLUTION PART 1: {sum(valid_games)}")

    # Se vuelve a abrir el archivo porque el bucle anterior ya lo recorrió completo.
    power = []
    with open(input_file, "r") as f:
        for line in f:
            power.append(solution_part_2(line))
    print(f"SOLUTION PART 2: {sum(power)}")

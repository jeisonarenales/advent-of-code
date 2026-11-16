import unittest
from pathlib import Path

from day_02.solution import (
    is_a_valid_subset,
    extract_balls,
    extract_subsets,
    extract_game_id,
    get_fewest_number_of_cubes,
    solution_part_1,
    solution_part_2,
)

# Carpeta day_02/ calculada a partir de la ubicación de este archivo (no del cwd),
# así los tests encuentran los archivos de ejemplo sin importar desde dónde se ejecuten.
DAY_DIR = Path(__file__).resolve().parent.parent / "day_02"

# Ejemplo del enunciado (basic_input_example.txt), con los resultados esperados
# por línea. Se usa en los tests de la parte 1 y la parte 2.
EXAMPLE_FILE = DAY_DIR / "basic_input_example.txt"


class TestDay02(unittest.TestCase):
    # --- Funciones auxiliares ---

    def test_valid_subset(self):
        # Los máximos son 12 rojos, 13 verdes y 14 azules.
        # Rojo por encima del máximo
        subset = {"red": 13, "green": 11, "blue": 10}
        self.assertFalse(is_a_valid_subset(subset))
        # Verde por encima del máximo
        subset = {"red": 10, "green": 15, "blue": 10}
        self.assertFalse(is_a_valid_subset(subset))
        # Azul por encima del máximo
        subset = {"red": 10, "green": 5, "blue": 20}
        self.assertFalse(is_a_valid_subset(subset))
        # Todos por encima del máximo
        subset = {"red": 13, "green": 25, "blue": 20}
        self.assertFalse(is_a_valid_subset(subset))
        # Todos por debajo del máximo
        subset = {"red": 3, "green": 11, "blue": 10}
        self.assertTrue(is_a_valid_subset(subset))
        # Exactamente en el máximo sigue siendo válido
        subset = {"red": 12, "green": 13, "blue": 14}
        self.assertTrue(is_a_valid_subset(subset))

    def test_extract_balls(self):
        # El orden de los colores en el texto no importa.
        self.assertEqual(
            extract_balls("8 green, 6 blue, 20 red"),
            {"red": 20, "blue": 6, "green": 8},
        )
        self.assertEqual(
            extract_balls("5 blue, 4 red, 13 green"),
            {"red": 4, "blue": 5, "green": 13},
        )
        # Los colores ausentes quedan en 0.
        self.assertEqual(
            extract_balls("2 green"),
            {"red": 0, "green": 2, "blue": 0},
        )

    def test_extract_subsets(self):
        result = [
            {"red": 4, "green": 0, "blue": 3},
            {"red": 1, "green": 2, "blue": 6},
            {"red": 0, "green": 2, "blue": 0},
        ]
        # Un espacio inicial como el que deja el split(":") de la línea completa.
        self.assertEqual(
            extract_subsets(" 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"), result
        )

    def test_extract_game_id(self):
        self.assertEqual(extract_game_id("Game 3"), 3)
        # Ids de más de un dígito.
        self.assertEqual(extract_game_id("Game 100"), 100)

    def test_get_fewest_number_of_cubes(self):
        subsets = [
            {"red": 4, "green": 0, "blue": 3},
            {"red": 1, "green": 2, "blue": 6},
            {"red": 0, "green": 2, "blue": 0},
        ]
        # Se queda con el máximo de cada color entre todas las extracciones.
        self.assertEqual(
            get_fewest_number_of_cubes(subsets), {"red": 4, "green": 2, "blue": 6}
        )

    # --- Parte 1: ids de los juegos posibles ---

    def test_solution_part_1_by_line(self):
        # Juegos 3 y 4 son imposibles (devuelven 0); el resto devuelve su id.
        lines = EXAMPLE_FILE.read_text().splitlines()
        self.assertEqual([solution_part_1(line) for line in lines], [1, 2, 0, 0, 5])

    def test_solution_part_1(self):
        # Suma de los ids posibles: 1 + 2 + 5 = 8
        with open(EXAMPLE_FILE, "r") as f:
            result = sum(solution_part_1(line) for line in f)
        self.assertEqual(result, 8)

    # --- Parte 2: poder mínimo de cada juego ---

    def test_solution_part_2_by_line(self):
        # Poder = rojos * verdes * azules mínimos necesarios en cada juego.
        lines = EXAMPLE_FILE.read_text().splitlines()
        self.assertEqual(
            [solution_part_2(line) for line in lines], [48, 12, 1560, 630, 36]
        )

    def test_solution_part_2(self):
        # Suma de los poderes: 48 + 12 + 1560 + 630 + 36 = 2286
        with open(EXAMPLE_FILE, "r") as f:
            result = sum(solution_part_2(line) for line in f)
        self.assertEqual(result, 2286)

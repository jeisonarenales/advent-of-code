import unittest
from day_01.solution import get_calibration_values, get_solution

from pathlib import Path

# Carpeta day_01/ calculada a partir de la ubicación de este archivo (no del cwd),
# así los tests encuentran los archivos de ejemplo sin importar desde dónde se ejecuten.
# __file__ -> tests/test_day_01.py; .parent.parent -> 2023/; luego se baja a day_01/.
DAY_DIR = Path(__file__).resolve().parent.parent / "day_01"


class TestDay01(unittest.TestCase):
    # --- Parte 1: solo cuentan los dígitos numéricos ---

    def test_basic_calibration_values_case(self):
        # Primer y último dígito de la línea forman el número de dos dígitos.
        self.assertEqual(get_calibration_values("1abc2"), 12)
        self.assertEqual(get_calibration_values("pqr3stu8vwx"), 38)
        # Con varios dígitos intermedios solo importan los extremos (1 y 5).
        self.assertEqual(get_calibration_values("a1b2c3d4e5f"), 15)
        # Un único dígito se usa como primero y último a la vez.
        self.assertEqual(get_calibration_values("treb7uchet"), 77)

    def test_basic_solution(self):
        # Suma de los valores de todas las líneas del ejemplo de la parte 1.
        self.assertEqual(get_solution(DAY_DIR / "basic_input_example.txt"), 142)

    # --- Parte 2: también cuentan los dígitos escritos con palabra ---

    def test_advanced_calibration_values_case(self):
        self.assertEqual(get_calibration_values("two1nine"), 29)
        self.assertEqual(get_calibration_values("eightwothree"), 83)
        # Palabras mezcladas con letras sueltas que no son dígitos.
        self.assertEqual(get_calibration_values("abcone2threexyz"), 13)
        # Palabras solapadas: "twone" contiene "two" y "one" (comparten la "o").
        self.assertEqual(get_calibration_values("xtwone3four"), 24)
        self.assertEqual(get_calibration_values("4nineeightseven2"), 42)
        # "oneight" contiene "one" y "eight" (comparten la "e"): el último es eight.
        self.assertEqual(get_calibration_values("zoneight234"), 14)
        # "sixteen" contiene "six" aunque no sea "sixteen" como número.
        self.assertEqual(get_calibration_values("7pqrstsixteen"), 76)

    def test_advanced_solution(self):
        # Suma de los valores de todas las líneas del ejemplo de la parte 2.
        self.assertEqual(get_solution(DAY_DIR / "advanced_input_example.txt"), 281)

# Uso:
#   make test                      -> tests del año por defecto (2023)
#   make test YEAR=2023            -> tests de un año específico
#   make test YEAR=2023 VERBOSE=0  -> salida resumida

PYTHON  ?= python
YEAR    ?= 2023
VERBOSE ?= 1

ifeq ($(VERBOSE),1)
UNITTEST_FLAGS := -v
endif

.PHONY: test help

help:
	@echo "Uso: make test [YEAR=2023] [VERBOSE=0|1]"

# -s: carpeta de los tests; -t: carpeta raíz para resolver imports (p. ej. day_01).
test:
	@test -d "$(YEAR)/tests" || { echo "No existe la carpeta $(YEAR)/tests"; exit 1; }
	$(PYTHON) -m unittest discover -s $(YEAR)/tests -t $(YEAR) $(UNITTEST_FLAGS)

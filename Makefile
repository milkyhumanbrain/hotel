.PHONY: run setup clean admin rec

# Ejecutar el proyecto
run:
	@source venv/bin/activate && python main.py

# Dev: Login automatico como admin
admin:
	@source venv/bin/activate && python -c "from main import main; main('admin')"

# Dev: Login automatico como recepcion
rec:
	@source venv/bin/activate && python -c "from main import main; main('recepcion')"

# Crear entorno virtual
setup:
	@python3 -m venv venv
	@echo "Entorno virtual creado. Usa 'make run' para ejecutar."

# Limpiar entorno virtual
clean:
	@rm -rf venv
	@echo "Entorno virtual eliminado."
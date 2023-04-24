help:
	@echo "Commands:"
	@echo ""
	@echo " install  Install in editable mode."
	@echo " check    Check type annotation. Remember to intall mypy with pip."
	@echo ""

install:
	pip install --no-deps -e .

check:
	mypy journal/

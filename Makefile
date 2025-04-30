.PHONY: setup run clean

setup:
	python3 -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip && \
		pip install -r requirements.txt && pip install -e .

run:
	. .venv/bin/activate && schema-md --config config.json --output output/schema.md

clean:
	rm -rf .venv output/schema.md
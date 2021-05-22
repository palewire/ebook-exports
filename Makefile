default: data/poems.json data/tulips-and-chimneys.txt

data/poems.json:
	@pipenv run python src/download.py

data/tulips-and-chimneys.txt:
	@pipenv run python src/output.py

clean:
	@rm -rf data/*

.PHONY: clean

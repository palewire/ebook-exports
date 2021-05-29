default: data/poems.json \
         data/toc.json   \
         output/tulips-and-chimneys.txt

data/poems.json data/toc.json:
	@pipenv run python src/download.py

output/tulips-and-chimneys.txt:
	@pipenv run python src/output.py

clean:
	@rm -rf data/*
	@rm -rf output/*

.PHONY: clean

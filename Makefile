data/poems.json:
	@pipenv run python src/download.py

clean:
	@rm -rf data/*


.PHONY: clean

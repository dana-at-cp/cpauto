.PHONY: docs

clean:
	rm -rf build dist .eggs cpauto.egg-info temp tests

init:
	pip install -r requirements.txt

test:
	py.test tests

coverage:
	py.test --verbose --cov-report term --cov=cpauto tests

publish:
	python setup.py register
	python setup.py sdist upload
	python setup.py bdist_wheel --universal upload
	rm -fr build dist .eggs cpauto.egg-info

docs:
	cd docs && make html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"

build: #build new release version to upload to PyPi
	python setup.py sdist

upload: #upload new build to PyPi
	twine upload dist/*

test:
	python3 -m pytest -v --cov --cov-config .coveragerc

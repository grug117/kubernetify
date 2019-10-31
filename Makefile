build: #build new release version to upload to PyPi
	python setup.py sdist

upload: #upload new build to PyPi
	twine upload dist/*


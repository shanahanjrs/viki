
.PHONY: test install

test:
		py.test

install:
		python3 setup.py install

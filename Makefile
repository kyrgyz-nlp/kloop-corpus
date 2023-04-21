install:
	test -d env || python3 -m venv env
	. env/bin/activate && pip install -r requirements.txt
	. env/bin/activate && playwright install chromium
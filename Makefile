.PONY: install-tests
install-tests:
	pip install -r ./requestbin/tests/requirements-test.txt

.PONY: run-tests
run-tests:
	pytest ./requestbin/tests --html=./requestbin/tests/reports/pytest_report.html



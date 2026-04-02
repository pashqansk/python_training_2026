import pytest
import json
import os.path
import importlib
from fixture.application import Application


fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target["base_url"])
    # валидация фикстуры: гарантированное условие для выполнения тестов - пользователь авторизован с определенным username
    fixture.session.ensure_login(username=target["username"], password=target["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        # валидация фикстуры: пользователь не авторизован в системе
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            group_testdata = load_form_module(fixture[5:])
            metafunc.parametrize(fixture, group_testdata, ids=[str(x) for x in group_testdata])


def load_form_module(module):
    return importlib.import_module("data.%s" % module).group_testdata
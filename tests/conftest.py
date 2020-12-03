import pytest

from gemeaux.handlers import Handler
from gemeaux.responses import Response


class FakeResponse(Response):
    def __init__(self, origin):
        self.origin = origin


class FakeHandler(Handler):
    def handle(self, *args, **kwargs):
        return FakeResponse(origin="handler")


class FakeHandlerRaiseException(Handler):
    def handle(self, *args, **kwargs):
        raise Exception


@pytest.fixture
def fake_response():
    return FakeResponse(origin="direct")


@pytest.fixture
def fake_handler():
    return FakeHandler()


@pytest.fixture
def fake_handler_exception():
    return FakeHandlerRaiseException()


INDEX_CONTENT = """# Title\r\nI am the content of index"""
OTHER_CONTENT = """# Title\r\nI am the content of other"""
SUB_CONTENT = """# Title\r\nI am the content of sub"""


@pytest.fixture(scope="session")
def index_directory(tmpdir_factory):
    p = tmpdir_factory.mktemp("var")
    # Create index file
    pp = p.join("index.gmi")
    pp.write_text(INDEX_CONTENT, encoding="utf-8")
    # Other file
    pp = p.join("other.gmi")
    pp.write_text(OTHER_CONTENT, encoding="utf-8")

    sub = p.mkdir("subdir").join("sub.gmi")
    sub.write_text(SUB_CONTENT, encoding="utf-8")

    # Return directory
    return p

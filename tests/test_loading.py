from pathlib import Path

from json_presenter import Presenter


def test_from_object():
    obj = {"a": 1}

    presenter = Presenter.from_object(obj)

    assert presenter.data == obj


def test_from_string():
    presenter = Presenter.from_string('{"name":"Alice"}')

    assert presenter.data["name"] == "Alice"


def test_from_file():
    file_path = Path("tests/data/sample.json")

    presenter = Presenter.from_file(file_path)

    assert presenter.data["country"] == "Japan"

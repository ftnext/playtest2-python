from playtest2 import steps


def test_set_path():
    from getgauge.python import data_store

    assert "path" not in data_store.spec

    steps.set_path("/spam")

    assert data_store.spec["path"] == "/spam"


def test_set_method():
    from getgauge.python import data_store

    assert "method" not in data_store.spec

    steps.set_method("GET")

    assert data_store.spec["method"] == "GET"


def test_set_content_type_header():
    from getgauge.python import data_store

    assert "headers" not in data_store.spec.get("kwargs", {})

    steps.set_content_type_header("application/json")

    assert data_store.spec["kwargs"]["headers"] == {"Content-Type": "application/json"}


def test_set_json_data():
    from getgauge.python import data_store

    assert "json" not in data_store.spec.get("kwargs", {})

    steps.set_json_data('{"key": "value"}')

    assert data_store.spec["kwargs"]["json"] == {"key": "value"}

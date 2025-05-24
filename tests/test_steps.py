import httpx
import pytest

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


def test_get_status_code():
    from getgauge.python import data_store

    data_store.spec["response"] = httpx.Response(200)

    steps.get_status_code()

    assert data_store.spec["actual"] == 200


def test_get_response_body():
    from getgauge.python import data_store

    data_store.spec["response"] = httpx.Response(201, json={"status": "ok"})

    steps.get_response_body()

    assert data_store.spec["response_body_json"] == {"status": "ok"}


def test_get_jsonpath_value():
    from getgauge.python import data_store

    data_store.spec["response"] = httpx.Response(201, json={"status": "ok"})

    steps.get_jsonpath_value("$.status")

    assert data_store.spec["actual"] == "ok"


def test_assert_string_value():
    from getgauge.python import data_store

    data_store.spec["actual"] = "string"

    steps.assert_string_value("string")
    with pytest.raises(AssertionError):
        steps.assert_string_value("other string")


def test_assert_int_value():
    from getgauge.python import data_store

    data_store.spec["actual"] = 42

    steps.assert_int_value("42")
    with pytest.raises(AssertionError):
        steps.assert_int_value("43")

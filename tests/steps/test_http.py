import httpx
import respx

from playtest2.steps import http as http_steps


def test_set_path():
    from getgauge.python import data_store

    if "path" in data_store.spec:
        del data_store.spec["path"]

    http_steps.set_path("/spam")

    assert data_store.spec["path"] == "/spam"

    del data_store.spec["path"]


def test_set_method():
    from getgauge.python import data_store

    if "method" in data_store.spec:
        del data_store.spec["method"]

    http_steps.set_method("GET")

    assert data_store.spec["method"] == "GET"

    del data_store.spec["method"]


def test_set_content_type_header():
    from getgauge.python import data_store

    if "kwargs" in data_store.spec:
        del data_store.spec["kwargs"]

    http_steps.set_content_type_header("application/json")

    assert data_store.spec["kwargs"]["headers"] == {"Content-Type": "application/json"}

    del data_store.spec["kwargs"]


def test_set_json_data():
    from getgauge.python import data_store

    if "kwargs" in data_store.spec:
        del data_store.spec["kwargs"]

    http_steps.set_json_data('{"key": "value"}')

    assert data_store.spec["kwargs"]["json"] == {"key": "value"}

    del data_store.spec["kwargs"]


@respx.mock
def test_send_request(respx_mock, monkeypatch):
    respx_mock.request(
        "POST",
        "http://localhost:8000/post",
        headers__contains={"Content-Type": "application/json"},
        json__eq={"key": "value"},
    ).mock(return_value=httpx.Response(201))

    from getgauge.python import data_store

    monkeypatch.setenv("SUT_BASE_URL", "http://localhost:8000")
    data_store.spec["path"] = "/post"
    data_store.spec["method"] = "POST"
    data_store.spec["kwargs"] = {
        "headers": {"Content-Type": "application/json"},
        "json": {"key": "value"},
    }

    http_steps.send_request()

    assert isinstance(data_store.spec["response"], httpx.Response)
    assert data_store.spec["response"].status_code == 201

    assert "path" not in data_store.spec
    assert "method" not in data_store.spec
    assert "kwargs" not in data_store.spec
    del data_store.spec["response"]


@respx.mock
def test_send_request_without_kwargs(respx_mock, monkeypatch):
    respx_mock.request(
        "GET",
        "http://localhost:8000/get",
    ).mock(return_value=httpx.Response(200))

    from getgauge.python import data_store

    monkeypatch.setenv("SUT_BASE_URL", "http://localhost:8000")
    data_store.spec["path"] = "/get"
    data_store.spec["method"] = "GET"

    http_steps.send_request()

    assert isinstance(data_store.spec["response"], httpx.Response)
    assert data_store.spec["response"].status_code == 200

    assert "path" not in data_store.spec
    assert "method" not in data_store.spec
    assert "kwargs" not in data_store.spec
    del data_store.spec["response"]


def test_get_status_code():
    from getgauge.python import data_store

    data_store.spec["response"] = httpx.Response(200)

    http_steps.get_status_code()

    assert data_store.spec["actual"] == 200

    del data_store.spec["response"]
    del data_store.spec["actual"]


def test_get_response_body():
    from getgauge.python import data_store

    data_store.spec["response"] = httpx.Response(201, json={"status": "ok"})

    http_steps.get_response_body()

    assert data_store.spec["response_body_json"] == {"status": "ok"}

    del data_store.spec["response"]
    del data_store.spec["response_body_json"]


def test_get_jsonpath_value():
    from getgauge.python import data_store

    data_store.spec["response_body_json"] = {"status": "ok"}

    http_steps.get_jsonpath_value("$.status")

    assert data_store.spec["actual"] == "ok"

    del data_store.spec["response_body_json"]
    del data_store.spec["actual"]

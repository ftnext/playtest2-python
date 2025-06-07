import json
import os
from urllib.parse import urljoin

import httpx
from getgauge.python import data_store, step
from jsonpath_ng.ext import parse


@step("パス<path>に")
def set_path(path: str):
    data_store.spec["path"] = path


@step("メソッド<method>で")
def set_method(method: str):
    data_store.spec["method"] = method


@step("メディアタイプ<media_type>で")
def set_content_type_header(media_type: str):
    data_store.spec.setdefault("kwargs", {})["headers"] = {"Content-Type": media_type}


@step("JSON<json_data>で")
def set_json_data(json_str: str):
    data_store.spec.setdefault("kwargs", {})["json"] = json.loads(json_str)


@step("リクエストを送る")
def send_request():
    base_url = os.environ["SUT_BASE_URL"]
    endpoint = urljoin(base_url, data_store.spec["path"])
    method = data_store.spec["method"].upper()
    kwargs = data_store.spec.get("kwargs", {})
    response = httpx.request(method, endpoint, **kwargs)
    data_store.spec["response"] = response

    del data_store.spec["path"]
    del data_store.spec["method"]
    if "kwargs" in data_store.spec:
        del data_store.spec["kwargs"]


@step("レスポンスのステータスコードが")
def get_status_code():
    response = data_store.spec["response"]
    data_store.spec["actual"] = response.status_code


@step("レスポンスのボディが")
def get_response_body():
    response = data_store.spec["response"]
    data_store.spec["response_body_json"] = response.json()


@step("JSONのパス<json_path>に対応する値が")
def get_jsonpath_value(json_path: str):
    jsonpath_expr = parse(json_path)
    response_json = data_store.spec["response_body_json"]
    matches = jsonpath_expr.find(response_json)
    data_store.spec["actual"] = matches[0].value

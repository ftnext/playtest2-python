import re

from getgauge.python import Table, data_store, step


@step("文字列の<expected>である")
def assert_string_value(expected: str):
    actual = data_store.spec.pop("actual")
    assert actual == expected, f"Expected {expected!r} but got {actual!r}"  # noqa: S101


@step("整数値の<expected>である")
def assert_int_value(expected: str):
    actual = data_store.spec.pop("actual")
    expected_int = int(expected)
    assert actual == expected_int, f"Expected {expected_int!r} but got {actual!r}"  # noqa: S101


@step("真である")
def assert_true_value():
    actual = data_store.spec.pop("actual")
    assert actual is True, f"Expected True but got {actual!r}"  # noqa: S101


@step("文字列の<expected>を含んでいる")
def assert_string_contains(expected: str):
    actual = data_store.spec.pop("actual")
    assert expected in actual, f"Expected {actual!r} to contain {expected!r}"  # noqa: S101


@step("小数値の<expected>である")
def assert_float_value(expected: str):
    actual = data_store.spec.pop("actual")
    expected_float = float(expected)
    assert actual == expected_float, f"Expected {expected_float!r} but got {actual!r}"  # noqa: S101


@step("整数値の<expected>以上である")
def assert_int_greater_equal(expected: str):
    actual = data_store.spec.pop("actual")
    expected_int = int(expected)
    assert actual >= expected_int, f"Expected {actual!r} to be >= {expected_int!r}"  # noqa: S101


@step("偽である")
def assert_false_value():
    actual = data_store.spec.pop("actual")
    assert actual is False, f"Expected False but got {actual!r}"  # noqa: S101


@step("真偽値の<expected>である")
def assert_bool_value(expected: str):
    actual = data_store.spec.pop("actual")
    expected_bool = expected == "True"
    assert actual == expected_bool, f"Expected {expected_bool!r} but got {actual!r}"  # noqa: S101


@step("nullである")
def assert_null_value():
    actual = data_store.spec.pop("actual")
    assert actual is None, f"Expected None but got {actual!r}"  # noqa: S101


@step("正規表現の<expected>に完全一致している")
def assert_regex_fullmatch(expected: str):
    actual = data_store.spec.pop("actual")
    assert re.fullmatch(expected, actual), f"Expected {actual!r} to fully match regex {expected!r}"  # noqa: S101


@step("テーブル<expected>である")
@step("以下のテーブルである <table>")
def assert_table(expected: Table):
    actual = data_store.spec.pop("actual")
    assert actual == expected, f"Expected {expected} but got {actual}"  # noqa: S101

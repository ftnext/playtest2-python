from getgauge.python import data_store, step


@step("文字列の<expected>である")
def assert_string_value(expected: str):
    actual = data_store.spec.pop("actual")
    assert actual == expected, f"Expected {expected!r} but got {actual!r}"  # noqa: S101


@step("整数値の<expected>である")
def assert_int_value(expected: str):
    actual = data_store.spec.pop("actual")
    expected = int(expected)
    assert actual == expected, f"Expected {expected!r} but got {actual!r}"  # noqa: S101


@step("真である")
def assert_true_value():
    actual = data_store.spec.pop("actual")
    assert actual is True, f"Expected True but got {actual!r}"  # noqa: S101

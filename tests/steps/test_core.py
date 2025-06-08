import pytest

from playtest2.steps import core as core_steps


def test_assert_string_value_pass():
    from getgauge.python import data_store

    data_store.spec["actual"] = "string"

    core_steps.assert_string_value("string")

    assert "actual" not in data_store.spec


def test_assert_string_value_fail():
    from getgauge.python import data_store

    data_store.spec["actual"] = "string"

    with pytest.raises(AssertionError):
        core_steps.assert_string_value("other string")

    assert "actual" not in data_store.spec


def test_assert_int_value_pass():
    from getgauge.python import data_store

    data_store.spec["actual"] = 42

    core_steps.assert_int_value("42")

    assert "actual" not in data_store.spec


def test_assert_int_value_fail():
    from getgauge.python import data_store

    data_store.spec["actual"] = 42

    with pytest.raises(AssertionError):
        core_steps.assert_int_value("43")

    assert "actual" not in data_store.spec


def test_assert_true_value_pass():
    from getgauge.python import data_store

    data_store.spec["actual"] = True

    core_steps.assert_true_value()

    assert "actual" not in data_store.spec


def test_assert_true_value_fail():
    from getgauge.python import data_store

    data_store.spec["actual"] = False

    with pytest.raises(AssertionError):
        core_steps.assert_true_value()

    assert "actual" not in data_store.spec


def test_assert_string_contains_pass():
    from getgauge.python import data_store

    data_store.spec["actual"] = "hello world"

    core_steps.assert_string_contains("world")

    assert "actual" not in data_store.spec


def test_assert_string_contains_fail():
    from getgauge.python import data_store

    data_store.spec["actual"] = "hello world"

    with pytest.raises(AssertionError):
        core_steps.assert_string_contains("python")

    assert "actual" not in data_store.spec


def test_assert_float_value_pass():
    from getgauge.python import data_store

    data_store.spec["actual"] = 3.14

    core_steps.assert_float_value("3.14")

    assert "actual" not in data_store.spec


def test_assert_float_value_fail():
    from getgauge.python import data_store

    data_store.spec["actual"] = 3.14

    with pytest.raises(AssertionError):
        core_steps.assert_float_value("2.71")

    assert "actual" not in data_store.spec


def test_assert_int_greater_equal_pass():
    from getgauge.python import data_store

    data_store.spec["actual"] = 42

    core_steps.assert_int_greater_equal("40")

    assert "actual" not in data_store.spec


def test_assert_int_greater_equal_equal_pass():
    from getgauge.python import data_store

    data_store.spec["actual"] = 42

    core_steps.assert_int_greater_equal("42")

    assert "actual" not in data_store.spec


def test_assert_int_greater_equal_fail():
    from getgauge.python import data_store

    data_store.spec["actual"] = 42

    with pytest.raises(AssertionError):
        core_steps.assert_int_greater_equal("50")

    assert "actual" not in data_store.spec


def test_assert_false_value_pass():
    from getgauge.python import data_store

    data_store.spec["actual"] = False

    core_steps.assert_false_value()

    assert "actual" not in data_store.spec


def test_assert_false_value_fail():
    from getgauge.python import data_store

    data_store.spec["actual"] = True

    with pytest.raises(AssertionError):
        core_steps.assert_false_value()

    assert "actual" not in data_store.spec


def test_assert_bool_value_pass_true():
    from getgauge.python import data_store

    data_store.spec["actual"] = True

    core_steps.assert_bool_value("True")

    assert "actual" not in data_store.spec


def test_assert_bool_value_pass_false():
    from getgauge.python import data_store

    data_store.spec["actual"] = False

    core_steps.assert_bool_value("False")

    assert "actual" not in data_store.spec


def test_assert_bool_value_fail():
    from getgauge.python import data_store

    data_store.spec["actual"] = True

    with pytest.raises(AssertionError):
        core_steps.assert_bool_value("False")

    assert "actual" not in data_store.spec


def test_assert_null_value_pass():
    from getgauge.python import data_store

    data_store.spec["actual"] = None

    core_steps.assert_null_value()

    assert "actual" not in data_store.spec


def test_assert_null_value_fail():
    from getgauge.python import data_store

    data_store.spec["actual"] = "not null"

    with pytest.raises(AssertionError):
        core_steps.assert_null_value()

    assert "actual" not in data_store.spec

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

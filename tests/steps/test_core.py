import pytest
from getgauge.python import Table

from playtest2.gauge_table import ProtoTable
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


@pytest.mark.parametrize("actual_value", ["a", "ab", "abb"])
def test_assert_regex_fullmatch_pass(actual_value):
    from getgauge.python import data_store

    data_store.spec["actual"] = actual_value

    core_steps.assert_regex_fullmatch("ab*")

    assert "actual" not in data_store.spec


@pytest.mark.parametrize("actual_value", ["ba", "abc"])
def test_assert_regex_fullmatch_fail(actual_value):
    from getgauge.python import data_store

    data_store.spec["actual"] = actual_value

    with pytest.raises(AssertionError):
        core_steps.assert_regex_fullmatch("ab*")


def test_assert_table_pass():
    from getgauge.python import data_store

    data_store.spec["actual"] = Table(
        ProtoTable(
            {
                "headers": {"cells": ["Word", "Vowel Count"]},
                "rows": [{"cells": ["Gauge", "3"]}, {"cells": ["Playtest2", "2"]}],
            }
        )
    )

    core_steps.assert_table(
        Table(
            ProtoTable(
                {
                    "headers": {"cells": ["Word", "Vowel Count"]},
                    "rows": [{"cells": ["Gauge", "3"]}, {"cells": ["Playtest2", "2"]}],
                }
            )
        )
    )

    assert "actual" not in data_store.spec


def test_assert_table_fail():
    from getgauge.python import data_store

    data_store.spec["actual"] = Table(
        ProtoTable(
            {
                "headers": {"cells": ["Word", "Vowel Count"]},
                "rows": [{"cells": ["Gauge", "3"]}, {"cells": ["Playtest2", "2"]}],
            }
        )
    )

    with pytest.raises(AssertionError):
        core_steps.assert_table(
            Table(
                ProtoTable(
                    {
                        "headers": {"cells": ["Word", "Vowel Count"]},
                        "rows": [{"cells": ["Gauge", "3"]}, {"cells": ["Playtest2", "4"]}],
                    }
                )
            )
        )

    assert "actual" not in data_store.spec

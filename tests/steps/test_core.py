import pytest
from getgauge.python import Table

from playtest2.gauge_table import ProtoTable
from playtest2.steps import core as core_steps


class TestAssertStringValue:
    def test_pass(self):
        from getgauge.python import data_store

        data_store.spec["actual"] = "string"

        core_steps.assert_string_value("string")

        assert "actual" not in data_store.spec

    def test_fail(self):
        from getgauge.python import data_store

        data_store.spec["actual"] = "string"

        with pytest.raises(AssertionError):
            core_steps.assert_string_value("other string")

        assert "actual" not in data_store.spec


class TestAssertIntValue:
    def test_pass(self):
        from getgauge.python import data_store

        data_store.spec["actual"] = 42

        core_steps.assert_int_value("42")

        assert "actual" not in data_store.spec

    def test_fail(self):
        from getgauge.python import data_store

        data_store.spec["actual"] = 42

        with pytest.raises(AssertionError):
            core_steps.assert_int_value("43")

        assert "actual" not in data_store.spec


class TestAssertTrueValue:
    def test_pass(self):
        from getgauge.python import data_store

        data_store.spec["actual"] = True

        core_steps.assert_true_value()

        assert "actual" not in data_store.spec

    def test_fail(self):
        from getgauge.python import data_store

        data_store.spec["actual"] = False

        with pytest.raises(AssertionError):
            core_steps.assert_true_value()

        assert "actual" not in data_store.spec


class TestAssertStringContains:
    def test_pass(self):
        from getgauge.python import data_store

        data_store.spec["actual"] = "hello world"

        core_steps.assert_string_contains("world")

        assert "actual" not in data_store.spec

    def test_fail(self):
        from getgauge.python import data_store

        data_store.spec["actual"] = "hello world"

        with pytest.raises(AssertionError):
            core_steps.assert_string_contains("python")

        assert "actual" not in data_store.spec


class TestAssertFloatValue:
    def test_pass(self):
        from getgauge.python import data_store

        data_store.spec["actual"] = 3.14

        core_steps.assert_float_value("3.14")

        assert "actual" not in data_store.spec

    def test_fail(self):
        from getgauge.python import data_store

        data_store.spec["actual"] = 3.14

        with pytest.raises(AssertionError):
            core_steps.assert_float_value("2.71")

        assert "actual" not in data_store.spec


class TestAssertIntGreaterEqual:
    def test_pass(self):
        from getgauge.python import data_store

        data_store.spec["actual"] = 42

        core_steps.assert_int_greater_equal("40")

        assert "actual" not in data_store.spec

    def test_equal_pass(self):
        from getgauge.python import data_store

        data_store.spec["actual"] = 42

        core_steps.assert_int_greater_equal("42")

        assert "actual" not in data_store.spec

    def test_fail(self):
        from getgauge.python import data_store

        data_store.spec["actual"] = 42

        with pytest.raises(AssertionError):
            core_steps.assert_int_greater_equal("50")

        assert "actual" not in data_store.spec


class TestAssertFalseValue:
    def test_pass(self):
        from getgauge.python import data_store

        data_store.spec["actual"] = False

        core_steps.assert_false_value()

        assert "actual" not in data_store.spec

    def test_fail(self):
        from getgauge.python import data_store

        data_store.spec["actual"] = True

        with pytest.raises(AssertionError):
            core_steps.assert_false_value()

        assert "actual" not in data_store.spec


class TestAssertBoolValue:
    def test_pass_true(self):
        from getgauge.python import data_store

        data_store.spec["actual"] = True

        core_steps.assert_bool_value("True")

        assert "actual" not in data_store.spec

    def test_pass_false(self):
        from getgauge.python import data_store

        data_store.spec["actual"] = False

        core_steps.assert_bool_value("False")

        assert "actual" not in data_store.spec

    def test_fail(self):
        from getgauge.python import data_store

        data_store.spec["actual"] = True

        with pytest.raises(AssertionError):
            core_steps.assert_bool_value("False")

        assert "actual" not in data_store.spec


class TestAssertNullValue:
    def test_pass(self):
        from getgauge.python import data_store

        data_store.spec["actual"] = None

        core_steps.assert_null_value()

        assert "actual" not in data_store.spec

    def test_fail(self):
        from getgauge.python import data_store

        data_store.spec["actual"] = "not null"

        with pytest.raises(AssertionError):
            core_steps.assert_null_value()

        assert "actual" not in data_store.spec


class TestAssertRegexFullmatch:
    @pytest.mark.parametrize("actual_value", ["a", "ab", "abb"])
    def test_pass(self, actual_value):
        from getgauge.python import data_store

        data_store.spec["actual"] = actual_value

        core_steps.assert_regex_fullmatch("ab*")

        assert "actual" not in data_store.spec

    @pytest.mark.parametrize("actual_value", ["ba", "abc"])
    def test_fail(self, actual_value):
        from getgauge.python import data_store

        data_store.spec["actual"] = actual_value

        with pytest.raises(AssertionError):
            core_steps.assert_regex_fullmatch("ab*")


class TestAssertTable:
    def test_pass(self):
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

    def test_fail(self):
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

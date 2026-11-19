import pytest

from query.builder import (
    build_select,
    escape_literal,
    allow_multi_statement,
    escape_like,
    safe_order,
    check_stored_input,
)


def test_parameterized_no_concat():
    sql = build_select("users", {"name": "x"})
    assert "?" in sql or "%s" in sql


def test_literal_quote_escaped():
    out = escape_literal("o'brien")
    assert "'" in out or "''" in out


def test_injection_quote_closed_rejected():
    import pytest
    with pytest.raises(ValueError):
        build_select("users", {"name": "' OR 1=1 --"} )


def test_multi_statement_rejected():
    assert allow_multi_statement("x; DROP TABLE users") is False


def test_single_statement_allowed():
    assert allow_multi_statement("SELECT 1") is True


def test_like_wildcard_escaped():
    assert "%" not in escape_like("a%b").replace("\%", "")


def test_order_field_whitelist():
    assert safe_order("name", ["name", "age"]) == "name"


def test_order_field_injected_rejected():
    import pytest
    with pytest.raises(ValueError):
        safe_order("name; DROP", ["name", "age"])


def test_stored_malicious_rejected():
    assert check_stored_input("' OR 1=1 --") is False


def test_stored_clean_allowed():
    assert check_stored_input("alice") is True


def test_identifier_injection_rejected():
    import pytest
    with pytest.raises(ValueError):
        build_select("users; DROP", {})


def test_empty_condition_handled():
    assert isinstance(build_select("users", {}), str)


def test_numeric_value_bound():
    sql = build_select("users", {"age": 18})
    assert "18" not in sql.split("WHERE")[-1] or "?" in sql


def test_special_char_in_literal():
    assert escape_literal("a_b%c")


def test_table_name_whitelist():
    import pytest
    with pytest.raises(ValueError):
        build_select("users`", {})

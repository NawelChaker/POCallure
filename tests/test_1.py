import pytest

# -----------------------------
# Passing test
# -----------------------------
def test_pass_1():
    assert 2 + 2 == 4

def test_pass_2():
    assert "allure" in "generate allure report"

# -----------------------------
# Failing test
# -----------------------------
def test_fail_1():
    assert 1 == 0

def test_fail_2():
    assert len([1,2,3]) == 5

# -----------------------------
# Skipped test (optional)
# -----------------------------
@pytest.mark.skip(reason="skip example")
def test_skip():
    assert True
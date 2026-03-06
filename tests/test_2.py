import pytest

# -----------------------------
# Passing test
# -----------------------------
def test_pass_12():
    assert 2 + 2 == 4

def test_pass_22():
    assert "allure" in "generate allure report"

# -----------------------------
# Failing test
# -----------------------------
def test_fail_12():
    assert 1 == 0

def test_fail_22():
    assert len([1,2,3]) == 5

# -----------------------------
# Skipped test (optional)
# -----------------------------
@pytest.mark.skip(reason="skip example")
def test_skip_0():
    assert True
  
@pytest.mark.skip(reason="Know Bug")
def test_skip_1():
    assert False

import pytest
import greet_rune

@pytest.mark.parametrize("function", [greet_rune.greet_py, greet_rune.greet_rust])
def test_greet_py(capfd, function):
    function()
    out, _ = capfd.readouterr()
    assert out.strip() == "Hi Rune!"

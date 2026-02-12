import pytest
from src.control_errors import IncorrectOptionException

@pytest.mark.ValidInputs
@pytest.mark.parametrize("input, validation", [
    ('paper', True),   # Caso 1
    ('scissors', True),   # Caso 2
    ('rock', True),   # Caso 3
])
def test_control_errors_valid(input, validation):
    assert IncorrectOptionException(input) == validation
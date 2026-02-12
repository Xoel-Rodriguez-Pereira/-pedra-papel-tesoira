import pytest
from src.control_errors import IncorrectOptionException

@pytest.mark.validInputs
@pytest.mark.parametrize("input, validation", [
    ('paper', True),   
    ('scissors', True),   
    ('rock', True),   
])
def test_control_errors_valid(input, validation):
    assert IncorrectOptionException.isInputValid(input) == validation 

@pytest.mark.invalidInputs
@pytest.mark.parametrize("input, validation", [
    ('manhatan', False),
    ('1234', False),
    ('antonia', False),
])
def test_control_errors_invalid(input, validation):
    assert IncorrectOptionException.isInputValid(input) == validation

@pytest.mark.exceptions
@pytest.mark.parametrize("input, validation", [
    (1, False),
    (543, False),
    (23, False),
])
def test_control_errors_exception(input, validation):
    assert IncorrectOptionException.isInputValid(input) == validation
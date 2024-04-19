import pytest

from common_functions import strings


@pytest.mark.parametrize('camel, snake', (
    ('', ''),
    ('one', 'one'),
    ('oneTwo', 'one_two'),
    ('oneTwoThree', 'one_two_three'),
    ('OneTwoThree', 'one_two_three'),
    ('HTMLParser', 'h_t_m_l_parser'),
))
def test_camel_to_snake_case(camel: str, snake: str):
    """Test CamelCase to snake_case."""
    assert strings.camel_to_snake_case(camel) == snake

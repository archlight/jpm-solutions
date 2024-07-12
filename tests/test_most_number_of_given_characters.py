import pytest
from jpm_solutions.p1_most_number_of_given_characters import solution


@pytest.fixture
def example():
    return "This is a very long sentence and I want to educate everyone in this whole crazy world…."

@pytest.fixture
def custom_statement():
    return "e ee eee eee e eeee eee"

class TestSolution:

    @pytest.mark.parametrize(
        "input_char, expected",
        [("I", "I"), ("z", "crazy"), ("e", "sentence"), ("x", "")],
    )
    def test_example_statement(self, example, input_char, expected):
        assert solution(example, input_char) == expected

    def test_blank_statement(self):
        assert solution("", "a") == ""

    def test_custom_statement(self, custom_statement):
        assert solution(custom_statement, "e") == "eeee"

    def test_invalid_input(self, example):
        with pytest.raises(Exception) as e:
            solution(example, "ab")
        assert e.match("Input invalid")



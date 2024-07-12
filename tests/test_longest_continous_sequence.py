import pytest
from jpm_solutions.p2_longest_continous_sequence import solution


class TestSolution:

    @pytest.mark.parametrize("num, expected", [(156, 4), (88, 3)])
    def test_example(self, num, expected):
        assert solution(num) == expected

    @pytest.mark.parametrize(
        "binary_str, expected", 
        [("0", 0), ("111", 1), ("1101110", 4), ("100001", 1), ("1000011", 6)]
    )
    def test_binary_string(self, binary_str, expected):
        num = int(binary_str, 2)
        assert solution(num) == expected

    @pytest.mark.parametrize(
    "binary_str, expected", 
    [("00000001", 8), ("00010000", 4), ("00000011", 7), ("00110001", 3)]
    )
    def test_binary_string_with_leading_zeros(self, binary_str, expected):
        num = int(binary_str, 2)
        assert solution(num, True) == expected

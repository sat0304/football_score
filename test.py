import unittest
from score_counter import *


class TestGetScoreFunction(unittest.TestCase):
    """Тестируем get_score function."""

    def test_empty_list(self):
        score_list = generate_game()
        self.assertIsNot(score_list, [], 'This is empty list.')

    def test_offset_in_range(self):
        current_offset = calculate_offset()
        max_offset = generate_game()[-1]['offset']
        self.assertIn(current_offset, range(max_offset), 'Offset is out of range.')

    def test_offset_has_score(self):
        result = False
        current_offset = calculate_offset()
        possible_offsets = {current_offset, current_offset + 1, current_offset + 2}
        score_list = generate_game()
        for record in score_list:
            if record["offset"] in possible_offsets:
                result = True
        self.assertTrue(result, 'There is no score in the list for the offset.')

    def test_home_and_away_are_correct(self):
        result = False
        current_offset = calculate_offset()
        score_list = generate_game()
        home, away = get_score(score_list, current_offset)
        for record in score_list:
            if (record['score']['home'] == home
                and record['score']['away'] == away
                and record['offset'] >= current_offset
            ):
                result = True
        self.assertTrue(result, 'There is no such pair in the score list.')

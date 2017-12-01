"""
    File Name: test_scoreO_results.py
    Author: David Conner
    Date Created: Thu 04 Feb 2016 09:52:54 AM EST
    Date Modified: Thu 04 Feb 2016 09:53:07 AM EST
    Python Version: 3.5
    Description: This file contains the tests for the scoreO_results.py script
        that I use to clean the results file, calculate the scores, and write
        the final results to a file.
    Requires: scoreO_results.py
    TODO: Write tests to ensure functionality of the data manipulation
        performed by the script as enhancements are made.
"""

import unittest

import scoreO_results as s


class ScoreOTestCase(unittest.TestCase):
    """Tests for 'scoreO_results.py'."""

    def setUp(self):
        self.my_dict = {'0': '0', '1': '3', '1': '2', '2': '3'}
        self.controls = {'0': '5', '1': '7', '2': '9'}
        self.long_row = {'0': '0', '1': '2', '2': '2', '3': '3', '4': '4'}

    def test_is_string(self):
        """Return false if the value is a string."""
        my_string = s.is_number("string")
        self.assertFalse(my_string)

    def test_is_number(self):
        """Return true if the value is a number."""
        my_number = s.is_number("9")
        self.assertTrue(my_number)

    def test_remove_duplicate_values(self):
        """Remove duplicate values from a dictionary."""
        no_dups = s.remove_dup_punches(self.my_dict, self.controls)
        self.assertDictEqual(
            {'0': '5', '1': '9', '2': '0'},
            no_dups, msg="The dictionaries are not the same.")

    def test_additional_punches_not_added(self):
        """Additional punches don't affect total score."""
        no_extras = s.remove_dup_punches(self.long_row, self.controls)
        no_dups = s.remove_dup_punches(self.my_dict, self.controls)
        self.assertEqual(
            s.total_points_earned(no_extras),
            s.total_points_earned(no_dups))

unittest.main()

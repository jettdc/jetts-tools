from jettools import dict_tools
import unittest


class TestGetNestedKey(unittest.TestCase):
    def test_should_return_none_if_no_keys(self):
        d = {'level1': {'level1': 2}}
        self.assertEqual(dict_tools.get(d, []), None)

    def test_should_grab_val_if_just_string(self):
        d = {'level1': 3}
        self.assertEqual(dict_tools.get(d, 'level1'), 3)

    def test_should_get_nested_value_if_exists(self):
        d = {'level1': {'level2': 2}}
        self.assertEqual(dict_tools.get(d, ['level1', 'level2']), 2)

    def test_should_return_none_if_fake_levels(self):
        d = {'level1': {'level2': 2}}
        self.assertEqual(dict_tools.get(d, ['level2', 'level3']), None)

    def test_should_return_none_if_try_not_nested(self):
        d = {'level1': {'level2': 2}}
        self.assertEqual(dict_tools.get(d, ['level1', 'level2', '3']), None)

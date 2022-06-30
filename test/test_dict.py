from jettools import dict_tools
import unittest


class TestGet(unittest.TestCase):
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


class TestAppendToKeyList(unittest.TestCase):
    def test_should_create_new_list_for_key_if_not_exists(self):
        d = {}
        dict_tools.append_to_key_list(d, 'test', 1)
        assert d.get('test') == [1]

    def test_should_add_to_list_if_exists(self):
        d = {'test': [1]}
        dict_tools.append_to_key_list(d, 'test', 2)
        assert d['test'][1] == 2

    def test_should_raise_exception_if_invalid_arg_types(self):
        d = 2
        with self.assertRaises(ValueError):
            dict_tools.append_to_key_list(d, 'test', 2)

        class A:
            def get(self, key):
                return [1, 2, 3, 4, 5]

        with self.assertRaises(ValueError):
            dict_tools.append_to_key_list(A(), 'test', 2)

        c = {'test': 3}
        with self.assertRaises(ValueError):
            dict_tools.append_to_key_list(c, 'test', 2)


class TestIncrementKey(unittest.TestCase):
    def test_increment_non_existing_key(self):
        d = {}
        dict_tools.increment_key(d, 'test')
        self.assertEqual(d['test'], 1)

    def test_increment_existing_key(self):
        d = {'test': 4}
        dict_tools.increment_key(d, 'test')
        self.assertEqual(d['test'], 5)

    def test_increment_existing_key2(self):
        d = {'test': 4}
        dict_tools.increment_key(d, 'test', by=3)
        self.assertEqual(d['test'], 7)

    def test_increment_existing_key3(self):
        d = {'test': 4}
        dict_tools.increment_key(d, 'test', by=3.5)
        self.assertEqual(d['test'], 7.5)

    def test_should_raise_exc_if_invalid_args(self):
        d = None
        with self.assertRaises(ValueError):
            dict_tools.increment_key(d, 'test', by=4)

    def test_should_raise_exc_if_invalid_args2(self):
        d = {'test': 'test2'}
        with self.assertRaises(ValueError):
            dict_tools.increment_key(d, 'test', by=4)

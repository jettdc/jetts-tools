import unittest
from jettools import validation
import typing


def _verify_dict_list(d) -> bool:
    for key in d:
        if not isinstance(key, str):
            return False
        if not isinstance(d[key], list):
            return False
        for item in d[key]:
            if not isinstance(item, int):
                return False
    return True


class TestAreValidArgs(unittest.TestCase):
    def test_should_raise_exception_if_not_all_args_are_validators(self):
        with self.assertRaises(ValueError):
            validation.are_valid_args([validation.Validator('test', 2, int), 3])

    def test_should_return_true_if_none(self):
        self.assertTrue(validation.are_valid_args([]))

    def test_should_return_false_if_an_arg_doesnt_validate(self):
        args = [
            validation.Validator('name', 4, str),
            validation.Validator('test3', 6.2, [str, int])
        ]
        self.assertFalse(validation.are_valid_args(args))

    def test_should_return_true_if_valid(self):
        args = [
            validation.Validator('name', 4, int),
            validation.Validator('test2', 'tst', str),
            validation.Validator('test3', 6.2, [str, int, float]),
            validation.Validator('test4', (2,), typing.Tuple),
        ]
        result = validation.are_valid_args(args)
        print(result.message)
        self.assertTrue(result)

    def test_should_raise_exception_if_parameterized_type(self):
        args = [
            validation.Validator('test4', (2,), typing.Tuple[str]),
        ]
        with self.assertRaises(ValueError):
            result = validation.are_valid_args(args)

    def test_should_validate_with_functions(self):
        d = {'test': [1, 2, 3, 4]}
        args = [
            validation.Validator('name', d, _verify_dict_list),
            validation.Validator('test2', d['test'], lambda x: isinstance(x, typing.List))
        ]
        result = validation.are_valid_args(args)
        print(result.message)
        self.assertTrue(result)

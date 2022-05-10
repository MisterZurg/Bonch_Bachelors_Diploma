import unittest
from recursive_json_search import *
from test_data import *


class json_search_test(unittest.TestCase):
    '''тестовый модуль для проверки поиска в `recursive_json_search.py`'''
    def test_search_found(self):
        '''ключ должен быть найден, возвразаемый список не должен быть пустым'''
        self.assertTrue([]!=json_search(key1,data))
    def test_search_not_found(self):
        '''ключ не должен быть найден, возвразаемый список должен быть пустым '''
        self.assertTrue([]==json_search(key2,data))
    def test_is_a_list(self):
        '''должен вернуть список'''
        self.assertIsInstance(json_search(key1,data),list)

if __name__ == '__main__':
    unittest.main()

import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from lesson_3_4.common.variables import ACTION, USER, TIME, ACCOUNT_NAME, PRESENCE, \
    RESPONSE, ERROR
from ..client import Client

class TestClass(unittest.TestCase):
    def setUp(self):
        self.c_ip = Client()

    def test_def_presense(self):
        """Тест коректного запроса"""
        test = self.c_ip.create_presence()
        test[TIME] = 1.1  # время необходимо приравнять принудительно
                          # иначе тест никогда не будет пройден
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_ans(self):
        """Тест корректтного разбора ответа 200"""
        self.assertEqual(self.c_ip.process_ans({RESPONSE: 200}), '200 : OK')

    def test_400_ans(self):
        """Тест корректного разбора 400"""
        self.assertEqual(self.c_ip.process_ans({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        """Тест исключения без поля RESPONSE"""
        self.assertRaises(ValueError, self.c_ip.process_ans, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()

#
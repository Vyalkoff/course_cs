
import unittest
from lesson_3_4_5.common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from lesson_3_4_5.server import Server

class TestServer(unittest.TestCase):
    '''
    В сервере только 1 функция для тестирования
    '''
    def setUp(self) -> None:
        self.s_ip = Server()
        self.err_dict = {
            RESPONSE: 400,
            ERROR: 'Bad Request'
        }
        self.ok_dict = {RESPONSE: 200}

    def test_no_action(self):
        """Ошибка если нет действия"""
        self.assertEqual(self.s_ip.process_client_message(
            {TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_wrong_action(self):
        """Ошибка если неизвестное действие"""
        self.assertEqual(self.s_ip.process_client_message(
            {ACTION: 'Wrong', TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_no_time(self):
        """Ошибка, если  запрос не содержит штампа времени"""
        self.assertEqual(self.s_ip.process_client_message(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_no_user(self):
        """Ошибка - нет пользователя"""
        self.assertEqual(self.s_ip.process_client_message(
            {ACTION: PRESENCE, TIME: '1.1'}), self.err_dict)

    def test_unknown_user(self):
        """Ошибка - не Guest"""
        self.assertEqual(self.s_ip.process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest1'}}), self.err_dict)

    def test_ok_check(self):
        """Корректный запрос"""
        self.assertEqual(self.s_ip.process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.ok_dict)


if __name__ == '__main__':
    unittest.main()

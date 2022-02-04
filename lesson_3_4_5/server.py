"""Программа-сервер"""
import logging
import socket

import json
from common.variables import ACTION, TIME, ACCOUNT_NAME, USER, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, ERROR
from common.utils import get_message, send_message
import log.server_log_config


class Server:

    def __init__(self, default_address='127.0.0.1', default_port=7777):
        self.default_address = default_address
        self.default_port = default_port
        self.Log = logging.getLogger('server')

    def get_address(self):
        return self.default_address, self.default_port,

    def process_client_message(self, message):
        '''
        Обработчик сообщений от клиентов, принимает словарь -
        сообщение от клинта, проверяет корректность,
        возвращает словарь-ответ для клиента

        :param message:
        :return:
        '''
        if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
                and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
            self.Log.info('Принят ответ')
            return {RESPONSE: 200}

        return {
            RESPONSE: 400,
            ERROR: 'Bad Request'
        }

    def start(self):
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            transport.bind((self.default_address, self.default_port))
        except OSError:
            self.Log.error(f'Адрес {self.default_address} занят. Поменяйте адрес')

        # Слушаем порт

        transport.listen(MAX_CONNECTIONS)

        while True:
            client, client_address = transport.accept()
            try:
                message_from_cient = get_message(client)
                print(message_from_cient)
                # {'action': 'presence', 'time': 1643128038.7741282, 'user': {'account_name': 'Guest'}}
                response = self.process_client_message(message_from_cient)
                send_message(client, response)
                client.close()
            except (ValueError, json.JSONDecodeError):
                self.Log.warning('Принято некорретное сообщение от клиента.')
                client.close()



if __name__ == '__main__':
    Server().start()

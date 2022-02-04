"""Программа-клиент"""

import json
import logging
import socket
import time
from common.variables import ACTION, USER, TIME, ACCOUNT_NAME, PRESENCE, \
    RESPONSE, ERROR
from common.utils import get_message, send_message
from server import Server
import log.client_log_config

c_log = logging.getLogger('client')


class Client:

    def start(self):
        server_address, server_port = Server().get_address()
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            transport.connect((server_address, server_port))
        except ConnectionRefusedError:
            c_log.error(f'Не удается соединится с {server_address}/{server_port}')

        message_to_server = self.create_presence()
        send_message(transport, message_to_server)
        try:
            answer = self.process_ans(get_message(transport))
            c_log.info(f'Принят ответ {answer}')

        except (ValueError, json.JSONDecodeError):
            c_log.error(f'Не удалось декодировать сообщение .')

    def create_presence(self, account_name='Guest'):
        '''
        Функция генерирует запрос о присутствии клиента
        :param account_name:
        :return:
        '''

        out = {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: account_name
            }
        }
        return out

    def process_ans(self, message):
        '''
        Функция разбирает ответ сервера
        :param message:
        :return:
        '''
        if RESPONSE in message:
            if message[RESPONSE] == 200:
                return '200 : OK'
            return f'400 : {message[ERROR]}'
        raise ValueError



if __name__ == '__main__':
    Client().start()

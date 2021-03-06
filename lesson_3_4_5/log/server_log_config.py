import logging
import logging.handlers
import os
import sys

LOG = logging.getLogger('server')

C_FORMAT = logging.Formatter('%(asctime)-10s %(levelname)-10s %(filename)-10s %(message)s')

Folder_log_server = PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'server_log')

if not os.path.exists(Folder_log_server):
    os.mkdir(Folder_log_server)

STREAM_HANDLER = logging.StreamHandler(sys.stdout)
STREAM_HANDLER.setFormatter(C_FORMAT)

S_FILE_LOG = logging.handlers.TimedRotatingFileHandler(os.path.join(Folder_log_server,'server.log'),encoding='utf-8',interval=1,when='D')
S_FILE_LOG.setFormatter(C_FORMAT)

LOG.setLevel(logging.INFO)
LOG.addHandler(STREAM_HANDLER)
LOG.addHandler(S_FILE_LOG)


if __name__ == '__main__':
    LOG.critical('Критическая ошибка')
    LOG.error('Ошибка')
    LOG.warning('Ошибка по серьезней')
    LOG.info('Информация')

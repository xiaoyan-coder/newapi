from configparser import ConfigParser
import os
from common.handle_path import CONF_DIR


class HandleConf(ConfigParser):

    def __init__(self, file_path):
        super().__init__()
        self.read(file_path, encoding='utf-8')


conf = HandleConf(os.path.join(CONF_DIR, 'conf.ini'))
if __name__ == '__main__':
    a = HandleConf(r'/conf/conf.ini')
    b = a.get('env', 'base_url')
    print(b)
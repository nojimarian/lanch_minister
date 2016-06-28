"""同じことやるの面倒なのでまとめた"""

import configparser

class Common:
    """継承して使うといいことあるかも"""

    CONFIG_FILE = 'app.ini'

    def __init__(self):
        """コンフィグをパースしておく"""

        self.configs = configparser.ConfigParser()
        self.configs.read(self.CONFIG_FILE)

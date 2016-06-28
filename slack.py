"""slackとIncoming WebHooksでやりとり"""

import configparser
import json
import requests

class Slack:
    """チャンネルの設定はapp.iniに書いてね"""

    CONFIG_FILE = 'app.ini'
    HEADERS = {'content-type': 'application/json'}

    def __init__(self):
        """設定ファイルをパースしてself.configに格納"""

        cp_ = configparser.ConfigParser()
        cp_.read(self.CONFIG_FILE)
        self.config = cp_['Slack']

    def send(self, message):
        """self.configをもとにmessageをチャンネルに投稿する
        """

        headers = {'content-type': 'application/json'}
        data = {
            'text': str(message),
            'username': self.config['Username'],
            'icon_url': self.config['IconUrl']
        }
        requests.post(self.config['ChannelUrl'],
                      data=json.dumps(data),
                      headers=headers)

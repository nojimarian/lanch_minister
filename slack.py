"""slackとIncoming WebHooksでやりとり"""

import configparser
import json
import requests

from common import Common

class Slack(Common):
    """チャンネルの設定はapp.iniに書いてね"""

    HEADERS = {'content-type': 'application/json'}

    def __init__(self):
        """設定ファイルのslackの部分をself.configへセット"""

        super().__init__()
        self.config = self.configs['Slack']

    def send(self, message):
        """self.configをもとにmessageをチャンネルに投稿する"""

        headers = {'content-type': 'application/json'}
        data = {
            'text': str(message),
            'username': self.config['Username'],
            'icon_url': self.config['IconUrl']
        }
        requests.post(self.config['ChannelUrl'],
                      data=json.dumps(data),
                      headers=headers)

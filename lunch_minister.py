"""ランチ大臣の実行クラス"""

from common import Common
from slack import Slack

class LunchMinister(Common):
    """lunch_time_now!!!"""

    def __init__(self):
        """
        設定ファイルの使う部分をそれぞれセット
        slackをセット
        """

        super().__init__()
        self.team_config = self.configs['Team']
        self.slack = Slack()

    def lunch_time_now(self):
        """実行関数だよ"""

        message = '{0:s}チームのみなさん、ランチの時間ですよ'.format(self.team_config['Name'])
        self.slack.send(message)

        return 0

if __name__ == '__main__':
    lm_ = LunchMinister()
    lm_.lunch_time_now()

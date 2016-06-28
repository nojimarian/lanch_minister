"""lanch_ministerの実行クラス"""

from slack import Slack

class LanchMinister:
    """"""

    def __init__(self):
        """なにかやることあるかな"""
        pass

    def lanch_time_now(self):
        """実行関数だよ"""

        message = 'みなさん、ランチの時間ですよ'
        sl_ = Slack()
        sl_.send(message)

        return 0

if __name__ == '__main__':
    lm_ = LanchMinister()
    lm_.lanch_time_now()

import random

action = 0.7
end = 1.5
accuracy = 2


class TimeSleep(object):
    '''随机睡眠时间'''

    def __init__(self):
        self.random_time = random.uniform(action, end)
        self.random_sleep_time = round(self.random_time, accuracy)

    def __str__(self):
        return self.random_sleep_time


if __name__ == '__main__':
    pass

#время выполнения кода

import time

class LoudStopwatch:
    def __enter__(self):
        self.start = time.process_time()
        return self
    def __exit__(self, *args):
        self.end = time.process_time()
        self.delta = self.end - self.start


with LoudStopwatch() as s:
    for _ in range(1000000):
         pass

print("Код выполнился за %.03f секунд" % s.delta)

#скорость доступа
from urllib.request import urlopen
url = "http://www.ya.ru"
with LoudStopwatch() as s:
    f = urlopen(url)
    f.read()

print("Запрос выполнился за %.03f секунд" % s.delta)
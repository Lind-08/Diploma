import threading
from .events import *
__author__ = 'lind'


class TimeUnits:
    s = "s"
    ms = "ms"


class Timer:
    def __init__(self, Interval=100, AutoReset=True, IsStarting=False, Units=TimeUnits.ms,
                 OnTimerFuncExample=empty_func):
        self.AutoReset = AutoReset

        if Units == TimeUnits.ms:
            self.Interval = float(Interval / 1000)
        elif Units == TimeUnits.s:
            self.Interval = Interval
        else:
            raise ValueError("Undefined time unit")

        self.OnTimer = Event(OnTimerFuncExample)
        self.__timer = threading.Timer(self.Interval, self.__on_time)
        if IsStarting:
            self.start()

    def __on_time(self):
        self.__timer = threading.Timer(float(self.Interval), self.__on_time)
        self.OnTimer()
        if self.AutoReset:
            self.start()

    def start(self):
        self.__timer.start()

    def stop(self):
        self.__timer.cancel()

if __name__ == "__main__":
    def hello_world():
        print("Hello, world!")

    t = Timer(AutoReset=True, Interval=1000, Units=TimeUnits.ms)
    t.OnTimer += hello_world
    import time
    t.start()
    time.sleep(5)
    t.stop()

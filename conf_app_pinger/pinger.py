import os
from l_lib import timers
import db_module


def _ping(ip=""):
    res = os.popen("rm .ping_log >> /dev/null; ping -c 1 -w 3 {0} >> .ping_log; echo $?".format(ip)).readlines()
    if res[0][0] == "0":
        return True
    else:
        return False


class Pinger:
    def __init__(self, db):
        self.state = False
        self.__db = db
        self.__ping_time = 1000
        self.__timer = timers.Timer(self.__ping_time, OnTimerFuncExample=self.ping_computers)
        self.__timer.OnTimer += self.ping_computers
        self._managed_nodes = {}

    @property
    def ping_time(self):
        return self.__ping_time

    @ping_time.setter
    def ping_time(self, time=1000):
        self.stop_ping()
        self.__ping_time = time
        self.__timer = timers.Timer(self.__ping_time, OnTimerFuncExample=self.ping_computers)
        self.__timer.OnTimer += self.ping_computers
        self.start_ping()

    def ping_computers(self):
        self.__get_nodes_from_db()
        for x in self._managed_nodes:
            self._managed_nodes[x] = _ping(x)
        self.__write_state_to_db()

    def __write_state_to_db(self):
        self.__db.write_nodes_state(self._managed_nodes)

    def __get_nodes_from_db(self):
        self._managed_nodes = self.__db.get_nodes()

    def start_ping(self):
        self.state = True
        self.__timer.start()

    def stop_ping(self):
        self.state = False
        self.__timer.stop()

    def set_nodes(self, nodes=[]):
        self.__timer.stop()
        self._managed_nodes = {nodes, []}
        self.__timer.start()


if __name__ == "__main__":
    x = Pinger(db_module)
    x.start_ping()
    import time
    time.sleep(5)
    x.stop_ping()

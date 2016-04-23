import sqlite3
from config import CONF_APP_DB_PATH, TABLE_NAME
__author__ = 'lind'


def get_nodes():
    db = sqlite3.connect(CONF_APP_DB_PATH)
    nodes = {}
    cur = db.cursor()
    cur.execute("SELECT * FROM {0};".format(TABLE_NAME))
    for row in cur:
        nodes[row[1]] = row[2]
    return nodes


def write_nodes_state(nodes):
    db = sqlite3.connect(CONF_APP_DB_PATH)
    cur = db.cursor()
    for n in nodes:
        cur.execute("UPDATE {2} SET state = \'{0}\' WHERE ip_address = \'{1}\';".format(nodes[n], n, TABLE_NAME))
        db.commit()

if __name__ == "__main__":
    print(get_nodes())

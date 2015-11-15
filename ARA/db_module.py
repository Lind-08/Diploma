__author__ = 'lind'
import sqlite3
import main

db_path = main.conf_options["dir_path"] + "/ara_db"


def get_nodes():
    db = sqlite3.connect(db_path)
    nodes = {}
    cur = db.cursor()
    cur.execute("SELECT * FROM nodes;")
    for row in cur:
        nodes[row[0]] = row[1]
    return nodes


def add_node(ip):
    db = sqlite3.connect(db_path)
    cur = db.cursor()
    cur.execute("INSERT  INTO nodes VALUES (\'{0}\',0);".format(ip))
    db.commit()


def del_node(ip):
    db = sqlite3.connect(db_path)
    cur = db.cursor()
    cur.execute("DELETE FROM nodes WHERE ip = \'{0}\';".format(ip))
    db.commit()


def write_nodes_state(nodes):
    db = sqlite3.connect(db_path)
    cur = db.cursor()
    for n in nodes:
        cur.execute("UPDATE nodes SET state = \'{0}\' WHERE ip = \'{1}\';".format(nodes[n], n))
        db.commit()

if __name__ == "__main__":
    print get_nodes()
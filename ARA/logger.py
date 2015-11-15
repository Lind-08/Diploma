__author__ = 'lind'
import sqlite3
import os
import main

log_dir = main.conf_options["log_path"]
log_db_path = log_dir + "/ara_log.db"
log_db = None


def create_log_db_schema(db):
    cur = db.cursor()
    script = "CREATE TABLE log (date TEXT, message TEXT)"
    cur.execute(script)
    db.commit()

if not os.path.exists(log_dir):
    os.mkdir(log_dir)

if not os.path.exists(log_db_path):
    log_db = sqlite3.connect(log_db_path)
    create_log_db_schema(log_db)
    log_db.close()


def write_log(message):
    log_db = sqlite3.connect(log_db_path)
    cur = log_db.cursor()
    text = "INSERT INTO log VALUES (CURRENT_TIMESTAMP,\'{0}\');".format(message)
    cur.execute(text)
    log_db.commit()

if __name__ == "__main__":
    write_log("test message")



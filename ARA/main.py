import os
import ConfigParser
import sys



config_path = os.getcwd() + "/ara.conf"
conf_options = {}


def _parse_conf_file(config_file):
    if not os.path.exists(config_file):
        raise ValueError("Config file does not exist")
        return None
    else:
        config = ConfigParser.ConfigParser()
        config.read(config_file)
        global conf_options
        for x in config.sections():
            for y in config.options(x):
                conf_options[y] = config.get(x, y)

_parse_conf_file(config_path)

import Pinger
import logger
import db_module
import cmd


class Adm(cmd.Cmd):
    COMMANDS = ["nodes", "pinger", "exec"]
    def __init__(self):
        self.pinger = Pinger.Pinger(db_module)
        self.prompt = ">>"
        self.completekey = None
        self.cmdqueue = []

    def do_nodes(self, opt):
        """nodes [a r]
        Show or modify list of administrated nodes.
        Options:
            a <ip> Adding new node
            r <ip> Remove node"""
        if opt:
            opt = str(opt).split(" ")
            if len(opt) != 2:
                print("Wrong options {0} for nodes. Write 'help nodes' for take reference.".format(opt))
            else:
                if opt[0] == "a":
                    db_module.add_node(opt[1])
                    print("Adding {0}.".format(opt[1]))
                if opt[0] == "r":
                    try:
                        db_module.del_node(opt[1])
                    except ValueError:
                        print("Removing error: {0}.".format(ValueError.message))
                        return
                    print("Removing {0}.".format(opt[1]))
        else:
            nodes = db_module.get_nodes()
            print("Nodes state:")
            print("IP".center(15, " ")+"|"+"  State")
            for x in nodes:
                if nodes[x] == 0:
                    state = "fault"
                else:
                    state = "work"
                print(x.center(15, " ")+"|"+state.center(7, " "))

    def do_pinger(self, opt):
        if opt:
            opt = opt.split(" ")
            if opt[0] == "start":
                self.pinger.start_ping()
                print("Pinger started.")
            elif opt[0] == "stop":
                self.pinger.stop_ping()
                print("Pinger stopped.")
            elif opt[0] == "pt":
                self.pinger.ping_time = int(opt[1])
                print("Pinging time set to {0} ms.".format(self.pinger.ping_time))
        else:
            print("Pinger status: {0}.".format("work" if self.pinger.state else "stopped"))
            print("Ping time: {0}".format(self.pinger.ping_time))

    def do_exec(self, opt):
        opt = opt.split(" ")
        states = dict.fromkeys(opt[1:])
        for x in opt[1:]:
            res = os.popen("""ssh lind@{0} "bash -s " < {1}; echo $?""".format(x, opt[0])).readlines()
            if res[0][0] == "0":
                states[x] = "correct"
            else:
                states[x] = "error"
                logger.write_log("Error of executing script on {0}. Error code {1}.".format(x, res[0]))
        print("results")
        print("IP".center(15, " ")+"|"+"  State")
        for x in states:
            print(x.center(15, " ")+"|"+states[x].center(7, " "))

    def do_exit(self, line):
        self.pinger.stop_ping()
        sys.exit(0)


    def do_EOF(self, line):
        return True

    def __del__(self):
        self.pinger.stop_ping()

if __name__ == "__main__":
    print("ARA v1.0a")
    Adm().cmdloop()


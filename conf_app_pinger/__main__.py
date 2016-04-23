from pinger import Pinger
import db_module

pinger = Pinger(db=db_module)
pinger.start_ping()

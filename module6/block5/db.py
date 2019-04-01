from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime as dt
Base = declarative_base()


class LogEntry(Base):
    __tablename__ = "logs"

    uid = Column(Integer, primary_key=True)
    ip_addr = Column(String(16))
    timestamp = Column(DateTime)

    def __init__(self, ip_addr, timestamp):
        self.ip_addr = ip_addr
        self.timestamp = timestamp

    def __str__(self):
        return "'%s' on %s" % (self.ip_addr, self.timestamp)



engine = create_engine("sqlite:///access_log.db")
Session = sessionmaker(bind=engine)
s = Session()
total = s.query(LogEntry).count()
ip = s.query(LogEntry).filter(LogEntry.ip_addr == "109.234.35.42").count()
period = s.query(LogEntry).filter(dt(2018, 9, 1) < LogEntry.timestamp).filter(LogEntry.timestamp < dt(2018, 9, 10)).count()

top={}
q = s.query(LogEntry)
q = q.filter(LogEntry.ip_addr)
for log in q.all():
    ip = log.ip_addr
    if ip in top:
        top[ip]+=1
    else: top[ip] = 1

top = sorted(top.values())
count_in_top4 = top[-4]

print(total)
print(ip)
print(period)
print(count_in_top4)
print((top[-1]+top[-2]+top[-3])/total*100)
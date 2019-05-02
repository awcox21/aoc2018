from datetime import datetime
from operator import itemgetter

inp = 'day4test.in'
# inp = 'day4.in'

events = list()
with open(inp, 'r') as f:
    for line in f:
        timestamp = datetime.strptime(line[1:17], r'%Y-%m-%d %H:%M')
        description = line[19:].strip()
        events.append((timestamp, description))
events.sort(key=itemgetter(0))
for event in events:
    print(event)

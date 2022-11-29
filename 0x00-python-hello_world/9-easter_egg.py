#!/usr/bin/python3
f = open('./zop', 'r+')
c = f.read()
c = c.rstrip('\n')
f.seek(0)
f.write(c)
#f.truncate()
print(c)
f.close()

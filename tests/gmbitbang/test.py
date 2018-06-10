#!/usr/bin/env python
import time
from panda import Panda

p1 = Panda('430026000951363338383037')
p2 = Panda('380016000551363338383037')

# this is a test, no safety
p1.set_safety_mode(Panda.SAFETY_ALLOUTPUT)
p2.set_safety_mode(Panda.SAFETY_ALLOUTPUT)

# get versions
print(p1.get_version())
print(p2.get_version())

# this sets bus 2 to actually be GMLAN
p2.set_gmlan(bus=2)

# send w bitbang then without
p1.set_gmlan(bus=None)
p1.can_send(20, "\x01", bus=3)
p1.set_gmlan(bus=2)
p1.can_send(20, "\x01", bus=3)
#time.sleep(0.1)
#p1.set_gmlan(bus=None)
#p1.can_send(20, "\x01", bus=3)

# test echo
# (to send on GMLAN, set bus=3)
time.sleep(0.1)
print p2.can_recv()


# HAL ring example
#
# list existing rings
# attach to an existing ring and write a few messages
# create a new ring
# detach a ring

import ring

rings = ring.rings()
print "rings: ", rings

def print_ring(r):
    print "name=%s size=%d reader=%d writer=%d " % (name,r.size,r.reader,r.writer),
    print "use_rmutex=%d use_wmutex=%d stream=%d" % ( r.use_rmutex, r.use_wmutex,r.is_stream)

for name in rings:
    r = ring.attach(name)
    print_ring(r)
    ring.detach(name)
    
if "ring_0" in rings:

    # attach to existing ring
    w = ring.attach("ring_0")

    # set writer to our HAL module id
    w.writer = ring.comp_id

    for i in range(10):
        msg = "message %d" % (i)
        w.write(msg,len(msg))
    print "available: ", w.available()

    # we're done with writing
    # wait for queue to drain before this!
    #w.writer = 0

if "firmware" not in rings:

    # create a new ring
    f = ring.create("firmware",4096,0) # default: record
    f.writer = ring.comp_id

    for i in range(10):
        msg = "message %d" % (i)
        f.write(msg,len(msg))
else:
    # detach a ring
    ring.detach("firmware")

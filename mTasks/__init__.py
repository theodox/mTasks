"""
This module provides a limited form of coroutine based multi-tasking.  It's not a substitute for 'real' threads,
but it does allow you to create the illusion of multiple, simultaneous processes without crossing thread
boundaries in Maya or requiring executeDefered or executeDeferredInMainThreadWithResult -- since the scheduling lives
entirely within the main Maya thread, it will not create cross-thread access bugs.

"""

from scheduler import *
from timers import delay, repeat, after

# if you're not planning on using this with Maya, remove this line
try:
    import maya_scheduler as task_system
except ImportError:
    print "maya task system unavailable"

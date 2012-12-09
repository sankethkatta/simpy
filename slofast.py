from simulate import Variables, Event, Edge, RUN_SIMULATION
import random

"""
SLOWFAST1.mod
"""

# Initialize Variables
var = Variables("QUEUE", "SERVER0", "SERVER1")

@Event(name="Run")
def run():
   var.QUEUE = 0 
   var.SERVER0 = 1 
   var.SERVER1 = 1 
   return run_to_arrive

@Edge()
def run_to_arrive():
    return arrive

@Event(name="Arrive")
def arrive():
    var.QUEUE += 1
    return arrive_to_arrive, arrive_to_check
        
@Edge(delay=random.random()*2+2)
def arrive_to_arrive():
   return arrive

@Edge()
def arrive_to_check():
    return check

@Event(name="Check")
def check():
    return check_to_start0, check_to_start1

@Edge()
def check_to_start0():
    if var.SERVER0 > 0:
        return start0
@Edge()
def check_to_start1():
    if var.SERVER0 <= 0 and var.SERVER1 > 0:
        return start1

@Event(name="Start0")
def start0():
    var.QUEUE -= 1
    var.SERVER0 -= 1
    return start_to_leave0

@Event(name="Start1")
def start1():
    var.QUEUE -= 1
    var.SERVER1 -= 1
    return start_to_leave1

@Edge(delay=random.random()*4+8)
def start_to_leave0():
    return leave0

@Edge(delay=random.random()*6+8)
def start_to_leave1():
    return leave1

@Event(name="Leave0")
def leave0():
    var.SERVER0 += 1
    return leave_to_start0

@Event(name="Leave1")
def leave1():
    var.SERVER1 += 1
    return leave_to_start1

@Edge(delay=0)
def leave_to_start0():
    if var.QUEUE>0:
        return start0

@Edge(delay=0)
def leave_to_start1():
    if var.QUEUE>0:
        return start1

RUN_SIMULATION(RUNTIME=20, RUN=run, VARIABLES=var)

from simulate import Variables, Event, Edge, RUN_SIMULATION
import random

"""
The Classic Carwash Model
Edge delays are 0 by default
Edge Priorities are 5 by default
Variables are initialized at 0 by default
"""

# Initialize Variables
var = Variables("QUEUE", "SERVER")

@Event(name="Run")
def run():
   var.QUEUE = 0 
   var.SERVER = 2 
   return run_to_enter

@Edge(delay=0)
def run_to_enter():
    return enter

@Event(name="Enter")
def enter():
    var.QUEUE += 1
    return enter_to_enter, enter_to_start
        
@Edge(delay=random.random()*2+2)
def enter_to_enter():
   return enter 

@Edge(delay=0)
def enter_to_start():
    if var.SERVER > 0:
        return start

@Event(name="Start")
def start():
    var.QUEUE -= 1
    var.SERVER -= 1
    return start_to_leave

@Edge(delay=random.random()*4+8)
def start_to_leave():
    return leave

@Event(name="Leave")
def leave():
    var.SERVER += 1
    return leave_to_start

@Edge(delay=0)
def leave_to_start():
    if var.QUEUE>0:
        return start

RUN_SIMULATION(RUNTIME=50, RUN=run, VARIABLES=var)

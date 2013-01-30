# simpy - Event Scheduling Simulation Engine

simpy is an event scheduling simulation engine implemented in python.

## Introduction

simpy consists of 2 main components Events and Edges. Simulations can be thought of as
node and pointer diagrams:

```
+-------+               +-------+
| EVENT |---- EDGE ---->| EVENT |
+-------+               +-------+
```

**Events** change state variables, and return Edge(s). An Event can return multiple Edges.

**Edges** check conditions and return an Event. They can also schedule the Event at a delay.
An Edge must always return exactly 1 Event.

The process launched by a "Run" Event. This first Event sets off the chain of Event Edge calls.

## Variables

Simpy operates mainly on a global namespace. By default a function does not take in any parameters.
Therefore, the preferred method is to create an object that can be globally accessed across
all functions, Simpy's `Variables` class.

```python
# Instantiate the class
var = Variables("QUEUE", "SERVER")

# Access or Set the variables
var.QUEUE = 0
```

## Event

Events in Simpy are simply functions with a decorator, which let the engine know that
the function is to be treated as an Event. The decorator takes 1 parameter `name` this is
the name of the Event that will be displayed on outputs traces.

```python
@Event(name="Run")
def run():
   var.QUEUE = 0
   var.SERVER = 2
   return run_to_enter
```

## Edge

Edges are also simply functions with a decorator. The Edge decorator has 2 optional
parameters,`delay` and `priority`. The default delay is 0 and default priority is 5
(lower number is higher priority).

```python
@Edge(delay=0)
def leave_to_start():
    if var.QUEUE>0:
        return start
```

# Run

Finally to run the simulation, the engine needs to know the total runtime, the first function
to be called to set off the simulation (usually called `run`) and the name of the `Variables`
instance being used.

```python
RUN_SIMULATION(RUNTIME=50, RUN=run, VARIABLES=var)
```
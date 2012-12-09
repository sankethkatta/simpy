import heapq

class PriorityQueue:
    def  __init__(self):
        self.heap = []

    def push(self, time, priority, func):
        entry = (time, priority, func)
        heapq.heappush(self.heap,entry)

    def pop(self):
        entry = heapq.heappop(self.heap)
        return entry

    def isEmpty(self):
        return len(self.heap) == 0

class Variables:
    def __init__(self, *args, **kwargs):
        self._names = args
        for var in args:
            setattr(self, var, 0)

FEL = PriorityQueue()
CLK = 0

def Event(name):
    """
    Event decorator, with argument name
    handles calling single or mutiple edges returned
    if None is returned, nothing will be called
    """
    def outer(func):
        def inner(*args, **kwargs):
            edges = func(*args, **kwargs)
            if edges != None:
                if type(edges) is tuple:
                    for edge in edges: edge()
                else:
                    edges()
            return name
        return inner
    return outer

def Edge(delay=0, priority=5):
    """
    Edge decorator
    Takes 2 optional parameters, delay, priority
    the defaults are already set here.
    Will call the returned event, if no event
    is returned, nothing is scheduled
    """
    def outer(func):
        def inner(*args, **kwargs):
            global FEL, CLK
            event = func(*args, **kwargs)
            if event != None: FEL.push(CLK+delay, priority, event)
        return inner
    return outer

def format_variables(VARIABLES):
    vars = VARIABLES.__dict__
    out = "\t"
    for var in VARIABLES._names: out += "%s\t" % vars[var] 
    return out

def RUN_SIMULATION(RUNTIME, RUN, VARIABLES):
    global FEL, CLK
    print "CLK\tEVENT\t%s" % "\t".join(VARIABLES._names)
    name = RUN()
    print "%f\t%s\t%s" % (CLK, name, format_variables(VARIABLES))
    while CLK <= RUNTIME:
        if FEL.isEmpty(): break
        (CLK, priority, func) = FEL.pop()
        name = func()
        print "%f\t%s\t%s" % (CLK, name, format_variables(VARIABLES))

    print "Ended Simulation run of %d" % RUNTIME

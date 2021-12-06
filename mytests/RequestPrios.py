import salabim as sim

env = sim.Environment(trace=True)

r = sim.Resource(capacity=2)

results = []

class PrioComponent(sim.Component):
    def __init__(self, waitTime, claimTime, prio, **kwargs):
        super().__init__(**kwargs)
        self.waitTime = waitTime
        self.claimTime = claimTime
        self.prio = prio

    def process(self):
        global results
        # global r

        yield self.hold(self.waitTime)
        yield self.request((r, 1, self.prio))
        results.append(self.prio)
        yield self.hold(self.claimTime)
        self.release(r)


PrioComponent(1,20, 0)
PrioComponent(2,20, 0)
PrioComponent(3, 20, 0)
PrioComponent(4, 20, 0)
PrioComponent(5, 20, -10)
PrioComponent(6, 20, 20)
PrioComponent(7, 20, 10)
PrioComponent(8, 20, 0)
PrioComponent(9, 20, -20)


env.run()

print("done")
print(results)

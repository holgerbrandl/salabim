import salabim as sim

env = sim.Environment(trace=True)

r = sim.Resource(capacity=2)


class EarlyConsumer(sim.Component):
    def process(self):
        yield self.hold(5)
        yield self.request(r)
        yield self.hold(5)
        self.release(r)


criticalRequestHonored = False


class BigConsumer(sim.Component):
    def process(self):
        global criticalRequestHonored

        yield self.hold(7)
        yield self.request((r, 2), priority=10)  # this should outrank the late customer
        criticalRequestHonored = True
        yield self.hold(5)
        self.release(r)


class LateConsumer(sim.Component):
    def process(self):
        global criticalRequestHonored

        yield self.hold(10)
        yield self.request(r)

        if criticalRequestHonored:
            print("request priority respected")
        else:
            print("request priority ignored")

        yield self.hold(5)
        self.release(r)


EarlyConsumer()
BigConsumer()
LateConsumer()

env.run()

print("done")

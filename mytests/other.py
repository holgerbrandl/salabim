import salabim as sim

class Other(sim.Component):
    def process(self):
        yield self.hold(3)
        yield self.hold(3)
        yield self.hold(3)


env = sim.Environment(trace=True)

other = Other(name="Car1")


class Customer(sim.Component):
    def process(self):
        print("huhu from " + self._name)
        other.cancel()
        yield self.hold(2)
        yield other.hold(2)


Customer(name="Car2", at=1, priority=-1)

env.run(till=10)

print("done")

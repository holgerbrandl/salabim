import salabim as sim

class Other(sim.Component):
    def process(self):
        yield self.hold(3)
        yield self.hold(3)
        yield self.hold(3)


env = sim.Environment(trace=True)

other = Other(name="Car1")



env.run(till=3)
other.hold()

print("done")
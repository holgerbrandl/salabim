import salabim as sim

env = sim.Environment(trace=True)

class Smthg(sim.Component):
    def process(self):
        yield self.hold(3)
        print("before activate")
        yield env.main().activate()
        print("continued after activate")
        yield self.hold(3)


Smthg(name="Car1")


class SmthgElse(sim.Component):
    def process(self):
        yield self.hold(20)

SmthgElse()

env.run()

print("done")
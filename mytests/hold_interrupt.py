import salabim as sim


class Customer(sim.Component):
    def process(self):
        print("huhu")


env = sim.Environment(trace=True)

c = Customer()

c.hold(5)

env.run(1)

c.interrupt()

env.run(1)

## this does not fail, but reschedules the component despite its interrupt status without resetting the latter
c.hold(1)

env.run(1)

c.resume()

import salabim as sim


class Customer(sim.Component):
    def process(self):
        print("huhu")


env = sim.Environment(trace=True)

c = Customer()

env.run(till=1)

c.activate()

print("done")

import salabim as sim


class Customer(sim.Component):
    def process(self):
        print("huhu from " + self._name)


env = sim.Environment(trace=True)

Customer(name2="Car1", at=3)
Customer(name="Car2", at=3, priority=-1)

env.run(till=5)

print("done")

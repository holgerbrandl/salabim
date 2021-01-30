import salabim as sim


class Customer(sim.Component):
    pass

# def process(self):
#     print("huhu from " + self._name)

env = sim.Environment(trace=True)


customer = Customer()
print(customer.status())
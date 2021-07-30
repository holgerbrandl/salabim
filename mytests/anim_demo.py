import salabim as sim
import math

from PIL import Image
from pathlib import Path

class VehicleGenerator(sim.Component):
    def process(self):
        while True:
            Vehicle()
            yield self.passivate()

class Vehicle(sim.Component):
    def process(self):
        remaining_stations = sim.Pdf(routes,1)()
        color=sim.Pdf('red green blue purple'.split(),1)()
        an = sim.AnimateRectangle(spec=(-40,-10,60,10), fillcolor=color, textcolor='white', text = lambda: f'{self.name()} {remaining_stations}')
        an3d = sim.Animate3dSphere(radius=10, color=color)
        x0=x1=station_locations['A'][0]
        y0=y1=station_locations['A'][1]
        z0=z1=station_locations['A'][2]

        tx0=tx1=ty0=ty1=tz0=tz1=env.now()
        an.x = lambda t: sim.interpolate(t, tx0, tx1, x0, x1)
        an.y = lambda t: sim.interpolate(t, ty0, ty1, y0, y1)
        an3d.x = lambda t: sim.interpolate(t, tx0, tx1, x0, x1)
        an3d.y = lambda t: sim.interpolate(t, ty0, ty1, y0, y1)
        an3d.z = lambda t: sim.interpolate(t, tz0, tz1, z0, z1)

        while True:
            current_station = remaining_stations[0]
            yield self.hold(process_duration)
            remaining_stations = remaining_stations[1:]
            if remaining_stations:
                to_station = remaining_stations[0]
                yield self.request(station[to_station])
            else:
                self.release(station[current_station])
                break
            if current_station=="A":
                vehicle_generator.activate(delay=1)
            else:
                self.release(station[current_station])
            distance_x = abs(station_locations[current_station][0]- station_locations[to_station][0])
            distance_y = abs(station_locations[current_station][1]-station_locations[to_station][1])
            distance_z = abs(station_locations[current_station][2]-station_locations[to_station][2])
            drive_time_x = distance_x/vx
            drive_time_y = distance_y/vy
            drive_time_z = distance_z/vz
            tx0 = env.now()
            tx1 = ty0=  tx0 + drive_time_x
            ty1 = tz0= ty0 + drive_time_y
            tz1 = tz0 + drive_time_z

            x0 = station_locations[current_station][0]
            x1 = station_locations[to_station][0]
            y0 = station_locations[current_station][1]
            y1 = station_locations[to_station][1]
            z0 = station_locations[current_station][2]
            z1 = station_locations[to_station][2]

            yield self.hold(drive_time_x + drive_time_y+drive_time_z)
        an.remove()
        an3d.remove()

station_locations={
    "A": (100,300,0),
    "B": (300,500,-25),
    "C": (300,300,0),
    "D": (300,100, 25),
    "E": (500,500,25),
    "F": (500,300,-25),
    "G": (500,100,0),
    "H": (700,500,25),
    "I": (700,300,0),
    "J": (700,100,-25),
    "K": (900,300,0),
}
routes=("ABEHK", "ABFIK", "ACFIK", "ADFIK", "ADGJK")

vx=100
vy=100
vz=100

process_duration = sim.Uniform(0.5,2.5)

env = sim.Environment(trace=False)
env.width3d(950)
env.height3d(768)
env.position3d((0, 100))
env.background_color("black")
env.width(950)
env.height(768)
env.position((960, 100))
env.show_camera_position()

station = {}
for name, location in station_locations.items():
    sim.AnimateText(text=name, x=location[0], y=location[1], fontsize=20, text_anchor='c')
    station[name] = sim.Resource(name)
vehicle_generator = VehicleGenerator()

env.animate(True)
env.animate3d(True)
env.video_mode("2d")
env.view(x_eye=-34.83838247025295, y_eye=-210.08293350095414, z_eye=278.12838944369383, x_center=400, y_center=290, z_center=0, field_of_view_y=45)

sim.Animate3dGrid((100,300,500,700,900), (100,300,500), (-25,0,25))
for istation, ilocation in station_locations. items():
    sim.Animate3dBox(x=ilocation[0], y=ilocation[1], z=ilocation[2], x_len=15, y_len=15, z_len=15)
env.run(sim.inf)

env.video("vehicle animation manhattan 3d.mp4")

env.video_mode("2d")
env.insert_frame(Path("aframe2d.jpg"), 60)
env.run(8)

env.video_mode("3d")
env.insert_frame("aframe3d.jpg", 60)
env.run(8)

env.video_mode("screen")
env.insert_frame("aframescreen.jpg", number_of_frames=60)
env.run(8)

env.video_close()
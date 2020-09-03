import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from mpl_toolkits.mplot3d import Axes3D

driving = ctrl.Antecedent(np.arange(0, 101, 1), 'driving')
journey_time = ctrl.Antecedent(np.arange(0, 21, 1), 'journey_time')
tip = ctrl.Consequent(np.arange(0, 210, 1), 'tip')

driving['bad'] = fuzz.trapmf(driving.universe, [0, 0, 30, 50])
driving['average'] = fuzz.trapmf(driving.universe, [30, 50, 50, 70])
driving['good'] = fuzz.trapmf(driving.universe, [60, 80, 100, 100])

journey_time['short'] = fuzz.trapmf(journey_time.universe, [0, 0, 0, 10])
journey_time['medium'] = fuzz.trapmf(journey_time.universe, [5, 10, 10, 15])
journey_time['long'] = fuzz.trapmf(journey_time.universe, [10, 20, 20, 20])

tip['small'] = fuzz.trapmf(tip.universe, [0, 50, 50, 100])
tip['moderate'] = fuzz.trapmf(tip.universe, [50, 100, 100, 150])
tip['big'] = fuzz.trapmf(tip.universe, [100, 150, 150, 200])

# driving.view()
# journey_time.view()
# tip.view()
# plt.show()

rule1 = ctrl.Rule(driving['good'] & journey_time['short'], tip['big'])
rule2 = ctrl.Rule(driving['good'] | journey_time['short'], tip['moderate'])
rule3 = ctrl.Rule(driving['average'] & journey_time['medium'], tip['moderate'])
rule4 = ctrl.Rule(driving['bad'] & journey_time['long'], tip['small'])

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

# tipping.input['driving'] = 45
# tipping.input['journey_time'] = 12
#
# tipping.compute()
#
# print(tipping.output['tip'])
# tip.view(sim=tipping)
# plt.show()

driving_sample = np.linspace(0, 100, 100)
journey_time_sample = np.linspace(0, 20, 20)
#tip_sample = np.linspace(0, 200, 11)
x, y = np.meshgrid(driving_sample, journey_time_sample)
z = np.zeros_like(x)
#print(x[19, 99])

for i in range(20):
    for j in range(50,100):
        tipping.input['driving'] = x[i, j]
        tipping.input['journey_time'] = y[i, j]
        tipping.compute()
        #z[i, j] = tipping.output['tip']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis',
                       linewidth=0.4, antialiased=True)

ax.set_zlim(0, 200)

cset = ax.contourf(x, y, z, zdir='z', offset=-2.5, cmap='viridis', alpha=0.5)
cset = ax.contourf(x, y, z, zdir='x', offset=3, cmap='viridis', alpha=0.5)
cset = ax.contourf(x, y, z, zdir='y', offset=3, cmap='viridis', alpha=0.5)

ax.view_init(30, 200)
plt.show()
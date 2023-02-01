import numpy as np
from clearml import Task
import matplotlib.pyplot as plt
task = Task.init(project_name="github_proyecto", task_name="my task 2")
from modulo1 import plotear
a = 5
b = 4
c = 6/(a-b+1)
f = 1
x = np.linspace(1,30)
y = f*x**2
print('-----')
print(task.id)
print('-----')


plotear(x, y)
# p=plt.plot(x, y, 'o')
# plt.show()
# plt.close()
# task.get_logger().report_matplotlib_figure(title='mi primer plot', series='p', figure=p)

task.get_logger().report_scalar(title='task', series='a', value=a, iteration=0)
for i in range(1,10):
    a = a +1
    task.get_logger().report_scalar(title='task', series='a', value=a, iteration=i**2-i+3)

task.connect_configuration(
    name='yaml conseguidoooo',
    configuration='config.yaml'
)

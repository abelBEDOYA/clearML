import numpy as np
from clearml import Task
import matplotlib.pyplot as plt
task = Task.init(project_name="github_proyecto", task_name="my task 2")
            
a = 5
b =4
c = 6/(a-b+1)

x = np.linspace(1,30,1)
y = x**2

plt.plot(x, y)
import numpy as np
from clearml import Task
task = Task.init(project_name="my project", task_name="my task")
            
a = 5
b =4
c = 6/(a-b+1)


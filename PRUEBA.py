import numpy as np
from clearml import Task
task = Task.init(project_name="github_proyecto", task_name="my task 2")
            
a = 5
b =4
c = 6/(a-b+1)


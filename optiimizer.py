from clearml.automation import  UniformIntegerParameterRange
from clearml.automation import HyperParameterOptimizer
from clearml import Task


task = Task.init(project_name="github_proyecto", task_name="my task 2")

optimizer = HyperParameterOptimizer('base_task_id'= task.id,
                                    hyper_parameters =[
                                    UniformIntegerParameterRange('General/a', 'min_value'=1, 'max_value'=10)
                                    ])
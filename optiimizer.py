from clearml.automation import  UniformIntegerParameterRange
from clearml.automation import HyperParameterOptimizer
from clearml import Task
task_base = Task.init(project_name="github_proyecto", task_name="my task 2")
     
ID=task_base.id
task_base.close()
task = Task.init(project_name="github_proyecto", 
                 task_name="optimizador",
                 task_type=Task.TaskTypes.optimizer)

optimizer = HyperParameterOptimizer(base_task_id= task_base.id,
                                    hyper_parameters =[
                                    UniformIntegerParameterRange('General/f', min_value=1, max_value=10)
                                    ],
                                    objective_metric_title='title_obj',
                                    objective_metric_series='p')

optimizer.start()
optimizer.wait()
optimizer.stop()
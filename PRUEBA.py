import numpy as np
from clearml import Task
import matplotlib.pyplot as plt

from modulo1 import plotear
import cv2
import time
import random


task_name_ = random.randint(1000,5000)
task = Task.init(project_name="holaaaaa", task_name=str(task_name_))
task.execute_remotely(queue_name='cola_yolo8')
a = 5
b = 4
c = 6/(a-b+1)
f = 1
x = np.linspace(1,30)
y = f*x**2
print('-----')
print(task.id)
print('-----')
print('holaaaaaaa')



    
# plotear(x, y)
# p=plt.plot(x, y, 'o')
# plt.show()
# plt.close()
# task.get_logger().report_matplotlicola1b_figure(title='mi primer plot', series='p', figure=p)

# task.upload_artifact('pesos', 
#     artifact_object=
#         './pesos.pt')

# task.upload_artifact('image', 
#     artifact_object=
#         './image1.jpg')

# img = cv2.imread('./image1.jpg')
# cv2.imshow('ploteo imagen', img)
# cv2.waitKey(0)

# task.get_logger().report_image(title='imageennn',local_path = './image1.jpg', series = 'bb') # series = img) #, value=img)

# task.get_logger().report_scalar(title='task', series='a', value=a, iteration=0)
for i in range(1,30):
    a = a +1
    print(i)
    time.sleep(1)
    task.get_logger().report_scalar(title='task', series='a', value=a, iteration=i**2-i+3)

task.connect_configuration(
    name='yaml conseguidoooo',
    configuration='config.yaml'
)
task.close()
from PIL import Image
import numpy as np
i1 = 'C:\\Users\Anubhav\Desktop\\untitled2\project\image\images\\numbers\y0.3.png'
j1 = 'C:\\Users\Anubhav\Desktop\\untitled2\project\image\images\\numbers\y0.5.png'
i = Image.open(i1)
j = Image.open(j1)
iar = np.asarray(i)
iar1 = np.asarray(j)
print(iar)
print('2   2')
print(iar1)
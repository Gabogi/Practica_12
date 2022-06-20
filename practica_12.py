
import matplotlib.pyplot as plt
import pylab
import cv2
import numpy as np
 
img = plt.imread ("imagen.jpg") #Lea la imagen aquí
plt.imshow (img) # Muestra la imagen leída 
pylab.show()


 
fil = np.array ([[-1, -1, 0], # Este es el filtro establecido, que es el núcleo de convolución
                [ -1, 0, 1],
                [  0, 1, 1]])
 
res = cv2.filter2D (img, -1, fil) #Utilice la función de convolución de opencv

 
plt.imsave("res.jpg",res)
plt.imshow (res) #Muestra la imagen después de la convolución

pylab.show()

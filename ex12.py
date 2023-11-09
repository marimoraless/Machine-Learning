import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('./imagens/mll.imagem.jpg')

mean_img = cv.blur(img,(5, 5))

plt.imshow(mean_img)
plt.show()

print('olha que legal')
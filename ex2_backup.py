import cv2 as cv
import matplotlib.pyplot as plt

#filtro media:
img = cv.imread('./imagens/mll.imagem.jpg')
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
mean_img = cv.blur(img,(9,9))

plt.imshow(mean_img)
plt.show()

#filtro mediana:
img = cv.imread('./imagens/mll.imagem.jpg')

img_median = cv.medianBlur(img, 5)

plt.subplot(121), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title('Imagem original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(cv.cvtColor(img_median, cv.COLOR_BGR2RGB))
plt.title('Imagem com filtro Mediana')
plt.xticks([]), plt.yticks([])

plt.show()


#filtro gaussiano
import cv2
from matplotlib import pyplot as plt

img = cv.imread('./imagens/mll.imagem.jpg')

img_gaussian = cv2.GaussianBlur(img, (9,9), 0)

plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Imagem original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(cv2.cvtColor(img_gaussian, cv2.COLOR_BGR2RGB))
plt.title('Imagem com filtro Gaussiano')
plt.xticks([]), plt.yticks([])

plt.show()



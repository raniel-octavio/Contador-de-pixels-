
from PIL import Image
import numpy as np


#Adicionar o destino C da imagem
img=Image.open('C:/Users/Home/Desktop/imagem.bmp').convert('RGB')

data = np.array(img)

print ('Esta imagem tem 420 pixels de largura e 300 pixels de altura.'), print(data.shape)

print('A quantidade de total de pixels dessa imagem é de 126.000 pixels, ' 
      'sendo que 298 são pixels verdes, 466 pixels são brancos e 125.236 são pixels pretos.')

for pixels in data: 
    if pixels in data:
        pixels = img.getcolors()

for pixels_imagem in pixels: 
    if pixels_imagem in pixels:
        print (pixels_imagem)




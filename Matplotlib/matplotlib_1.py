# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:57:05 2022

@author: hasan
"""

#------------------KÜTÜPHANE-------------------#
#----------------------------------------------#
import matplotlib.pyplot as plt
import numpy as np





#-------------------KODLAR---------------------#
#----------------------------------------------#
"""
veri = np.arange(10)#10 birimlik bir veri  oluşturduk.
plt.plot(veri)
plt.title('GRAFİK')
plt.xlabel('X ekseni')
"""


"""
x = [2,4,6,8]
y = [4,16,32,64]
plt.plot(x, y)
plt.plot(x, y, 'ro')#Kırmızı noktalar şeklinde çizim yapar.
"""


dizi = np.arange(0., 5., 0.2)
print(dizi)
plt.plot(dizi,dizi, 'r--',dizi,dizi**2,'bs', dizi, dizi**3, 'y^')
plt.savefig('grafik_1.png')#Grafiği png olarak kaydettik.
plt.savefig('grafik_1.pdf')#Grafiği pdf olarak kaydettik.
plt.savefig('grafik_1_kaliteli.png',dpi=500, bbox_inches='tight')#Daha kaliteli bir png formatında kaydedilir. Kenarlardaki boş alanlar kesilir.
























































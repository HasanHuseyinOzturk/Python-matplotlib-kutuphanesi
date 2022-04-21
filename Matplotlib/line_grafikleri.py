# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 17:20:57 2022

@author: hasan
"""

"""
Matplotlib ile çizgi grafikleri
Çizgi grafiği nasıl çizilir.
Çizgi grafiğinin renk ve stil ayarları nasıldır.
Eksen ayarları.
Çizgilerin altı nasıl doldurulur.
"""

#------------------KÜTÜPHANE-------------------#
#----------------------------------------------#
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd






#--------------------KODLAR--------------------#
#----------------------------------------------#
plt.style.use("seaborn-whitegrid")#Görünüş ayarladık.
figure = plt.figure()#Tüm matplotlib grafikleri için öncelikle bir grafik nesnesi ve alanı oluşturulur.
axes = plt.axes()

#Kodları çalıştırırsak seaborn whitegrid grafik karşımıza geldi. Fakat çizim yapmadığımız için grafik çizilmedi.
x_axes = np.linspace(0, 10, 100)#0 ile 10 arasında 100 değer aldık.
y_axes = np.sin(x_axes)#x verilerinin sinüs değerlerini y eksenine atadık.

axes.plot(x_axes, y_axes)#Grafiği çizdirdik.

#Bir grafikte birden fazla çizgi grafiği görmek istersek plt.plot komutunu birden çok kez yazarız.
plt.plot(x_axes, y_axes)
plt.plot(x_axes, np.cos(x_axes))

#Renk kontrolü için color kullanılır.
plt.plot(x_axes, np.sin(x_axes-1), color="blue")
"""
plt.plot(x_axes, np.sin(x_axes-1), color="y")
plt.plot(x_axes, np.sin(x_axes-1), color="0.75")
plt.plot(x_axes, np.sin(x_axes-1), color="#000000")
Şekildeki gibi kullanımlar mevcuttur.
"""

#Çizgi sitili kontrolü için linestyle kullanılır.
plt.plot(x_axes-10, x_axes, linestyle="solid", color="pink")#solid
plt.plot(x_axes-10, x_axes+1, linestyle="dashed", color="yellow")#dashed
plt.plot(x_axes-10, x_axes+2, linestyle="dashdot", color="blue")#dashdot
plt.plot(x_axes-10, x_axes+3, linestyle="dotted", color="purple")#dotted
plt.plot(x_axes-10, x_axes+4, ":g")#:k şeklinde hem stil hemde renk girebiliriz.


#Eksen ile ilgili işlemler. xlim ve ylim
plt.plot(x_axes, np.sin(x_axes*25))
plt.xlim(-5, 20)#x eksenini -5 den 20 ye kadar sınırlandırır.
plt.ylim(-3, 3)#y eksenini -3 ile 3 arasında sınırlandırır. Değerleri ylim(3, -3) ile ters çevirmemiz de mümkündür.



















































































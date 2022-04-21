# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 21:01:20 2022

@author: hasan
"""

"""
Grafik nesnesi nasıl oluşturulur.
Renk, işaret ve çizgi stilleri.
Matplotlib de grafikler bir figür nesnesi ile dizayn edilir.
"""
#------------------KÜTÜPHANE-------------------#
#----------------------------------------------#
import matplotlib.pyplot as plt
import numpy as np




#-------------------GRAFİK NESNESİ OLUŞTURMA---------------------#
#----------------------------------------------------------------#
figure_1 = plt.figure()#Grafik nesnesi oluştu fakat boş.
#Birden fazla alt grafik olması isteniliyorsa add_subplot() kullanılır.

x1 = figure_1.add_subplot(2,2,1)#2x2 yani dört tane alt grafikten 1. olana ekle.
x2 = figure_1.add_subplot(2,2,2)
x3 = figure_1.add_subplot(2,2,3)
x4 = figure_1.add_subplot(2,2,4)


data = np.random.randn(25).cumsum()#Normal dağılımdan rastgele değerler üreten ve bunların kümelatif toplamını veren kod.
data_1 = np.random.randn(50).cumsum()
data_2 = np.random.randn(75).cumsum()



x2.plot(data,'k--')
x3.plot(data_1,'r*')
x4.plot(data_2,'b.')








#-------------------RENK İŞARET VE ÇİZGİ STİLLERİ---------------------#
#---------------------------------------------------------------------#
x = [1,2,3,4,5]
y = [10,11,12,13,14]

figure_2 = plt.figure()#Grafik nesnesi oluştu fakat boş.

ax = figure_2.add_subplot(1,1,1)
ax.plot(x,y, linestyle = '--', color = 'b')


plt.plot(data,'ko--')







#----------------------EKSENLERİ ETİKETLENDİRME-----------------------#
#---------------------------------------------------------------------#
"""
Aralık için xlim,
İşaret konumu için set_xticks
İşaret wtiketi için set_xticklabels

"""

figure_3 = plt.figure()
ax = figure_3.add_subplot(1,1,1)
ax.plot(data)
ax.set_xticks([0,15,30,45])#X ekseni değerlerini değiştirir.
ax.set_xticklabels(['Bir','İki','Üç','Dört'], rotation = 90, fontsize = 'small')#Değerlere yazısal değer vermemizi sağlar.
ax.set_title('İlk Grafiğim Bu Değil')#Başlık verir.
#plt.savefig('grafik_2_kaliteli.png',dpi=500, bbox_inches='tight')
ax.set_xlabel('Değerler')#X eksenine isim verir.


ozellik = {"title":"Harika Grafik",
           "xlabel":"Adımlar",
           "ylabel":"Sayılar"}
ax.set(**ozellik)#Set ile yazdığımız sözlüğü ekleyebiliriz.
















































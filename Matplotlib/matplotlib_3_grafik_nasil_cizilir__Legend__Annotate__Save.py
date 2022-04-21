# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 22:49:08 2022

@author: hasan
"""



"""
Grafik nasıl oluşturulur,
Renk ve çizgi stilleir nasıl ayarlanır,
Kalınlık ve etikt ayarları nasıl yapılır

Etiket ve legend ayarları,
Yazı ve şekil ekleme,
Grafiği kaydetme.
"""



#------------------KÜTÜPHANE-------------------#
#----------------------------------------------#
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




#------------------ETİKET VE LEGEND AYARLARI-------------------#
#--------------------------------------------------------------#
figure_1 = plt.figure()
ax = figure_1.add_subplot(1,1,1)


veri_1 = np.random.randn(1000).cumsum()
veri_2 = np.random.randn(1000).cumsum()
veri_3 = np.random.randn(1000).cumsum()

ax.plot(veri_1,"k",label="bir")
ax.plot(veri_2,"b--",label="iki")
ax.plot(veri_3,"r.",label="uc")

ax.legend(loc = "best")#Boş bırakırsak legendler otomatik bulunur. loc = "best" yazarsak en iyi yeri bulur.







#------------------GRAFİĞE YAZI VE OK EKLEME-------------------#
#--------------------------------------------------------------#
"""
test fonksiyonu koordinatları verilen yere yazı ekler.

Gerçek bir veri seti ile çalışalım.
"""
veri = pd.read_csv("FB.csv", index_col = 0, parse_dates=True)
print(veri.head())

k_fiyat = veri["Şimdi"]
figure_2 = plt.figure()
ax = figure_2.add_subplot(1,1,1)
k_fiyat.plot(ax=ax, style="k-")

ax.set_title("Facebook Borsa Şimdi Fiyatları")

#Grafikteki min değeri ok ile gösterelim
print(k_fiyat.min())

print(k_fiyat["23-02-2022"])#Min değerin 198.45 olduğu kesinleşti.

tarih = "23-02-2022"
yazi = "Minimum değer"

#Annotate ile grafiğe ok ile yazı ekleyelim.
ax.annotate(yazi, xy=(tarih,200),xytext=(tarih,125),arrowprops=dict(facecolor="blue"))#Ok ve yazı minimum değere eklenmiş oldu.






#------------------GRAFİĞE KAYDETME-------------------#
#-----------------------------------------------------#
plt.savefig("grafik_.pdf")
plt.savefig("grafik_.png", dpi=500, bbox_inches="tight")#dpi ile çözünürlük artırılır. bbox_inches ile boş kenarları kestik.











# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 01:11:58 2022

@author: hasan
"""

"""
Matplotlib iyi bir kütüphanedir fakat ileri düzey grafikler için çok fazla kod satırı gerektirir.
Matplotlib in eksiklerinden dolayı seaborn kütüphanesi geliştirilmiştir.
Matplotlib üzerinde çalışır ve grafiklerin daha iyi görselleşmesini sağlar.


Seaborn daha kullanışlı ve kolaydır.
Seaborn'un matplotlib ile karşılaştırılması.
Histogram ve yoğunluk.
İlişki grafiği.
Facet histogramlar.
Kutu grafiği.
Bar grafiği.
"""

#------------------KÜTÜPHANE-------------------#
#----------------------------------------------#
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns






#-------------------KODLAR MATPLOTLIB İLE---------------------#
#-------------------------------------------------------------#
plt.style.use('classic')

rng = np.random.RandomState()#Random nesnesi aldık.
x = np.linspace(0, 10,250)#X ekseni için 0 ile 10 arasında eşit aralıkta 250 değer üretir.
y = np.cumsum(rng.randn(250,6),0)#250 ile 6 boyutlarında rastgele değer atayıp cumrng ile topladık ve y ye atadık.


#plt.plot(x,y)
#plt.legend('ABCDEF', ncol=2,loc='best')#Grafikteki değerlere atamalar yaptık.





#----------------------KODLAR SEABORN İLE---------------------#
#-------------------------------------------------------------#
sns.set()#seaborn stili grafik çizmek için set metodu kullanılır.
#plt.plot(x,y)
#plt.legend('ABCDEF', ncol=2,loc='best')#Aynı kodları tekrar çalıştıralım. Grafik daha anlaşılır olacaktır.





#----------------------HİSTOGRAM VE YOĞUNLUK GRAFİKLERİ---------------------#
#---------------------------------------------------------------------------#
"""
iris = sns.load_dataset("iris")#iris veri setini ekledik.
print(iris.head())#irisin ilk beş örneklemini ayzdık.

setosa = iris.loc[iris.species=="setosa"]#değişkenlere setosa ve virginica yı atadık.
virginica = iris.loc[iris.species=="virginica"]
"""

#setosa.petal_length.plot.hist()#Setosa türünün petal legth in histogramı geldi.
#sns.kdeplot(setosa.petal_length, shade=True, color='b')#Setosa türünün petal legth inin yoğunuk grafiği geldi.

#sns.distplot(iris.petal_length)#Histogram ve yoğunluk grafiğini birlikte görmek için seborn deki distplot kullanılır.




#------------------------------İKİ BOYUTLU GRAFİKLER------------------------#
#---------------------------------------------------------------------------#
#sns.kdeplot(setosa.petal_length, setosa.petal_width, shade=True)#İki boyutlu grafik karşımıza geldi. Shade=True gölgelendirme yapar.





#-----------------BİRLEŞİK VE MARJİNAL DAĞILIM GRAFİĞİ-----------------#
#----------------------------------------------------------------------#
"""
with sns.axes_style("white"):
    sns.jointplot("petal_length", "petal_width", data = iris, kind = "kde")#İki boyutlu yoğunluk ile birleşik dağılımının grafiği geldi.
    

with sns.axes_style("white"):
    sns.jointplot("petal_length", "petal_width", data = iris)#Kind çalıştırılmaz ise şekildeki çıktı elde edilir.
"""





#------------------------------İLİŞKİ GRAFİKLERİ------------------------#
#-----------------------------------------------------------------------#
"""
Değişkenlerin ikili ilişkilerini görmek için kullanılır.
"""
#sns.pairplot(iris, hue="species")#İris veri setindeki dört değişkenin aralarındaki ilişkiyi veren grafikleri çizer.
#plt.savefig('PairPlot.png',dpi=500, bbox_inches='tight')





#------------------------------FACET HİSTOGRAMLAR-----------------------#
#-----------------------------------------------------------------------#
dataTips = sns.load_dataset("tips")#Tips veri setini aldık.
print(dataTips.head())

dataTips["bahsis_yuzde"] = dataTips["tip"]*100/dataTips["total_bill"]#Bahşişlerin yüzdelerini hesapladık ve bahsis_yuzde değişkeni ile veri setine ekledik.
print(dataTips.head())

"""
grid = sns.FacetGrid(dataTips, row="smoker", col="time", margin_titles=True)#Kategorilerin histogramını görmek istersek FacetGrid kullanırız.
grid.map(plt.hist, "bahsis_yuzde", bins=np.linspace(0,40,15))#Değişkeni haritaladık. facet histogram grafikleri geldi.
"""




#------------------------------KUTU GRAFİKLER-----------------------#
#-------------------------------------------------------------------#
with sns.axes_style(style="ticks"):
    degisken = sns.catplot("day","total_bill","smoker", data=dataTips, kind="box")
    degisken.set_axis_labels("Gün", "Toplam Hesap")#Sigara ve günlere göre toplam hesabın kutu grafiği geldi. Kutu dışındaki nokta değerleri aykırı değer olarak düşünülebilir.
#Toplam hesap ve bahşiş sayısal değerlerin birleşik histogram ve yoğunluk grafiği ile regresyon doğrusu grafiğini görmek için joinplot kullanılır.
sns.jointplot("total_bill", "tip", data=dataTips, kind="reg")#Regresyon doğrusu ile birleşik dağılım grafiğini verir.


with sns.axes_style(style="white"):#Size değişkeninin bar grafiğini görmek için.
    degisken_1 = sns.catplot("size", data=dataTips, aspect=2, kind="count")#Size için bar grafiğini verir.





















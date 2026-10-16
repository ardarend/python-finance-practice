import numpy as np

prices = np.array([100, 103, 101, 107, 110, 108])

getiri = prices[1:] / prices[:-1] - 1

print("İlk fiyat:", prices[0])
print("Son fiyat:", prices[-1])

print("Fiyatların toplamı:", prices.sum())
print("Ortalama fiyat:", prices.mean())

print("Günlük getiriler:", getiri)

volatilite = getiri.std()
print("Volatilite:", volatilite)

en_iyi_gun = getiri.max()
print("En iyi gün:", en_iyi_gun)

en_kotu_gun = getiri.min()
print("En kötü gün:", en_kotu_gun)

yukselis_gunu = np.sum(getiri > 0)
dususs_gunu = np.sum(getiri < 0)

print("Yükseliş günü:", yukselis_gunu)
print("Düşüş günü:", dususs_gunu)

print("En yüksek fiyat:", prices.max())
print("En düşük fiyat:", prices.min())

# 1.

mahsulotlar = {
    "olma": 6,
    "nok": 7,
    "banan": 3
}

m_nomi = input("mahsulot nomini kiriting: ")

if m_nomi in mahsulotlar:
    print(mahsulotlar[m_nomi])
else:
    print("bunday ")


# 2.

davlatlar = {
    "Ozbekiston": 37,
    "Rossiya": 146,
    "Hindiston": 1480
}

davlat = input("Davalt nomini kiriting: ").capitalize()

if davlatlar[davlat] < 100:
    print(f"Kichik toifali davlat, aholisi {davlatlar[davlat]} million ")
elif davlatlar[davlat] >= 100 and davlatlar[davlat] < 1000:
    print(f"Orta toifali davlat, aholisi {davlatlar[davlat]} million ")
elif davlatlar[davlat] > 1000:
    print(f"Katta toifali davalt,  aholisi {davlatlar[davlat]} milliard ")
else:
    print("bunday davalt royxatda yoq")



# 3.
 
countries = {
    "Ozbekiston": "Toshkent",
    "Fransiya": "Parij",
    "Xitoy": "Pekin"
}

country = input("Mamlakat nomini kiriting: ").capitalize()

if country in countries:
    print(countries[country])
else:
    print("Ma'lumot yetarli emas")



# 4.

meva = {
    "olma": "yashil",
    "banan": "sariq",
    "anor": "qizil"
}

mevanomi = input("Meva nomini kiriting: ")

if mevanomi in meva:
    print(f"{mevanomi} {meva[mevanomi]} rangda")
else:
  print(f"{mevanomi} noma'lum rangda")


# 5. 

kinolar = {
    "Forrest gump": 8.8,
    "Yulduzli urushlar": 8.7,
    "Koko siri": 8.4,
    "Ratatuy": 8.1
}

for kino in kinolar:
    if kinolar[kino] > 8.5:
       print(f"{kino} reytingi yiqori")  
    else:
       print(f"{kino} reytingi normal")
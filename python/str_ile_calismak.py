# Tek Satirlik Aciklama Bilgisi
"""
docstrings yazim standardiyla aciklama satiri
"""

# help()

first_name = "Hakan"
last_name = "Yalcinkaya"
age = 39

print(first_name, last_name)
print(first_name, last_name, sep=" <> ")  # sep kullanimi

print(
    "Ad: " + first_name + " Soyad: " + last_name + 
    " Yas: ", age
)

print(first_name.upper())
print(first_name.lower())
print(first_name.title())
print(first_name.islower())
print(first_name.isupper())
print(first_name.istitle())
print(first_name.isalnum())
print(first_name.isalpha())
print(first_name.isdecimal())

print(dir(first_name))  # Tum metodlara burdan bakabiliriz

print(len(first_name + last_name))


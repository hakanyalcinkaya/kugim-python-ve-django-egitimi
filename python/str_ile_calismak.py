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

"dis amet :)" \
content = "Lorem Ipsum Dolor" \
"last line" 


content_2 = "Incididunt Lorem dolor commodo\n" \
"nisi deserunt enim anim in nulla.\n"
"Lorem amet occaecat pariatur minim eiusmod id consectetur "


content_3 = """Incididunt Lorem dolor commodo 
nisi deserunt enim anim in nulla. 
Lorem amet occaecat pariatur minim eiusmod id consectetur 
nulla occaecat consequat consequat do exercitation magna. 
"""

print(content)
print(content_2)
print(content_3)

# Veri tipini ogren
type(first_name)

title = 'Hasan\'in Python Egitimi'
new_title = 'Hasan "Gercek Python\'ci"'

info = "kacis karakteri \n \\tir"
print(info)

# Hatali ->
print(
    "Merhaba " + first_name + " " + 
    last_name + 
    " senin yasin gelecek sene " + age + 1
)

age_info = "Merhaba " + first_name + " " + \
    last_name + \
    " senin yasin gelecek sene " + str(age + 1)

print(age_info)

age_str = str(age)

print(age_str)

age_with_format = "Merhaba {} {}, senin \
yasin gelecek sene {} olacak".format(
    first_name, last_name, age + 1
)

age_with_format_2 = "Merhaba {frst} {lst}, senin \
yasin gelecek sene {age} olacak".format(
    age=age+1, frst=first_name, lst=last_name
)
print(age_with_format_2)


age_with_f = f"Merhaba {first_name[0]}. {last_name}, senin yasin \
gelecek sene {age + 1} olacak "
print(age_with_f)


print(f"{first_name[0]}. {last_name}")
print(first_name[0] + ".", last_name)
print(first_name[:2] + ".", last_name)
print(first_name[:100] + ".", last_name)
print(first_name[0:5:2] + ".", last_name)
print(first_name[::-1] + ".", last_name)


print(f"{last_name[0:2]}{last_name[-1]}")
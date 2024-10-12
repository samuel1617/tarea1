import random
caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud=int(input("👍ingresa la longitud de tu contraseña"))
resultado=""
for i in range (longitud):
    resultado += random.choice (caracteres)
print(f"tu contraseña con una longitud de {longitud} es: {resultado}")

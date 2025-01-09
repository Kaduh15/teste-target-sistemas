
texto = input("Digite um texto: ")

print("================= Resolução 01 =================")
texto_invertido1 = texto[::-1]
print(f"O texto invertido é: {texto_invertido1}")

print("================= Resolução 02 =================")
texto_invertido2 = []

for caracter in texto:
    texto_invertido2.insert(0, caracter)

texto_invertido2 = "".join(texto_invertido2)

print(f"O texto invertido é: {texto_invertido2}")
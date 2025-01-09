import json

dados = []

with open("data.json") as f:
    dados = json.load(f)

maior_valor = 0
menor_valor = None
soma_total = 0

for dia in dados:
    if menor_valor is None:
        menor_valor = dia["valor"]

    if dia["valor"] > maior_valor:
        maior_valor = dia["valor"]
    if dia["valor"] < menor_valor and dia["valor"] > 0:
        menor_valor = dia["valor"]

    if dia["valor"] > 0:
        soma_total += dia["valor"]

media = soma_total / len(dados)

dias_acima_media = 0

for dia in dados:
    if dia["valor"] > media:
        dias_acima_media += 1

print(f"O maior valor é {maior_valor:.2f}")
print(f"O menor valor é {menor_valor:.2f}")
print(f"A média é {media:.2f}")
print(f"O número de dias acima da média é {dias_acima_media}")
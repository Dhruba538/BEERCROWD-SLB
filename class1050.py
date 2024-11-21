
ddd_codes = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    19: "Campinas",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    31: "Belo Horizonte",
    41: "Curitiba",
    51: "Porto Alegre",
    85: "Fortaleza",
    27: "Vitoria",
    28: "Cachoeiro de Itapemirim"
}

code = int(input())

#print(ddd_codes.get(code, "DDD nao cadastrado"))

if code in ddd_codes:
    
    print(ddd_codes[code])
    
else:
    print("DDD nao cadastrado")
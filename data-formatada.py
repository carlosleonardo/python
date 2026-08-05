import datetime

print("Data formatada")
data = input("Digite uma data (dd/mm/aaaa): ")
try:
    dia, mes, ano = data.split('/')
    data_formatada = datetime.date(int(ano), int(mes), int(dia))
    print(f"Data formatada: {data_formatada.strftime('%d-%m-%Y')}")
except ValueError:
    print("Data inválida. Certifique-se de usar o formato dd/mm/aaaa.")
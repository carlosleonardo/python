import datetime

data_atual = datetime.datetime.now()
print("Data atual:", data_atual)
data_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S")
print("Data formatada:", data_formatada)
data_nascimento = input("Digite sua data de nascimento (dd/mm/yyyy): ")
data_nascimento = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
idade = (data_atual - data_nascimento).days // 365
print("Idade:", idade)
dez_dias = datetime.timedelta(days=10)
data_futura = data_atual + dez_dias
print("Data futura (10 dias):", data_futura)

# 
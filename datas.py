import datetime
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
data_atual = datetime.datetime.now()
data_formatada = data_atual.strftime('%d de %B de %Y')
print(f"Data atual formatada: {data_formatada}")

data_nascimento = input("Digite sua data de nascimento (dd/mm/yyyy): ")
data_nascimento_obj = datetime.datetime.strptime(data_nascimento, '%d/%m/%Y')
idade = data_atual.year - data_nascimento_obj.year - ((data_atual.month, data_atual.day) < (data_nascimento_obj.month, data_nascimento_obj.day))
print(f"Você tem {idade} anos.")
dias_vida = (data_atual - data_nascimento_obj).days
print(f"Você tem {dias_vida} dias de vida.")
data_nova = data_nascimento_obj + datetime.timedelta(days=1000)
print(f"Você completará 1.000 dias de vida em: {data_nova.strftime('%d de %B de %Y')}")
print(data_nascimento_obj < data_atual)
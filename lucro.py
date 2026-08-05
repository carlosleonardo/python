print("Lucro de venda")
custo = float(input("Digite o custo do produto: "))
venda = float(input("Digite o valor de venda do produto: "))
quantidade_estocada = int(input("Digite a quantidade estocada do produto: "))
lucro_unitario = venda - custo
lucro_total = lucro_unitario * quantidade_estocada
print(f"Lucro unitário: R$ {lucro_unitario:.2f}")
print(f"Lucro total: R$ {lucro_total:.2f}")
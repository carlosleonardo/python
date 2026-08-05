print("Faixa Etária")
idade = int(input("Digite a sua idade: "))
match idade:
    case idade if idade < 0:
        print("Idade inválida.")
    case idade if idade <= 12:
        print("Criança")
    case idade if idade <= 17:
        print("Adolescente")
    case idade if idade <= 64:
        print("Adulto")
    case _:
        print("Idoso")
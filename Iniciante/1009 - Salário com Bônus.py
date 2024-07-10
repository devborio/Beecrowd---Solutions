nome = input()
salario = float(input())
vendas = float(input())

comicao = vendas * 0.15
salarioFinal = (salario + comicao)

print("TOTAL = R$ %.2f" %salarioFinal)

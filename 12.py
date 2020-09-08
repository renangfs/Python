preco = float(input("Digite o preco do produto: "))
desconto=(preco*5)/100
novopreco=preco-desconto

print("foi descontado 5% de R$:{:.2f} \no novo preco é R$:{:.2f}  ".format(preco,novopreco))

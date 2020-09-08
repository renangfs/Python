qntkm = float(input("Digite o kilometro percorrido: "))
qntdias = float(input("Digite a quantidade de dias que ele foi alugado: "))
dias=qntdias*60
km=qntkm*0.15
print("O preço a pagar é a quantidade de {} dias mais {} quantidade de km rodados, totalizando em  R$:{:.2f}".format(qntdias,qntkm,dias+km))

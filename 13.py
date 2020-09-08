sal = float(input("Digite o salario do Funcionario: . . ."))
# almento é igual a 15 % , o dividido é por 100
almento=(sal*15/100)
resultado=sal+almento

print("O salario {:.2f} obiteve almento de 15 % ficando com R$:{:.2f} ".format(sal,resultado))
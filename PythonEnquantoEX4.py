
print("---------------------------------")
print("-------- EX numero 4 ------------")
print("---------------------------------")
N=2
COD = int(input("Digite o codigo do aluno:..."))
while N != 1:
    NT1 = int(input("Digite NOTA 1:..."))
    NT2 = int(input("Digite Nota 2:..."))
    NT3 = int(input("Digite Nota 3:..."))
    MP=(4*NT1+3*NT2+3*NT3)/10 
    print("O aluno de codigo {} tem a media ponderada de:{}".format(COD,MP)) 
    if MP >= 6:
      print("Aluno: APROVADO")
      N=int(input("Para sair digite (1) e (0) para não:.."))

    elif MP <=5:
      print("Aluno: REPROVADO")
      N=int(input("Para sair digite (1) e (0) para não:.."))
print("---------------------------------")
print("-------- Fim de Processo --------")
print("---------------------------------")

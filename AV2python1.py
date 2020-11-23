
for S in range (0,1001):
    S=S*3
    print(S)
    
    
A=1
B=2
for S in range (0,10):
    print("{}/{}".format(A,B))
    A=A+2
    B=B+2
    
    
N=int(input("Digite o Fatorial desejado (15?): . . ."))
F=1
C=N
while C > 0:
    F *= C
    C -= 1
print("{}".format(F))    
    

1) Linguagem de programação é um método padronizado, formado por um conjunto de regras sintáticas e semânticas, de implementação de um código fonte - que pode ser interpretado ou compilado e transformado em um programa de computador, toda linguagem apresenta seus paradigmas que devem ser empregados para a elaboração de um programa.
Para colocarmos em funcionamento um programa, precisamos de um processador de linguagem (interpretador ou compilador).
Explique em que consiste o processo de compilação e o processo de interpretação, apresente algumas vantagens e desvantagens de cada um desses tipos e em quais desses modelos se enquadram as linguagens C e Python.
Interpletação: é quando o código fonte é executado por um programa no computador chamado interpletador. Normalmente esse tipo de programa é mais lento para ser executado
Compilada: É quando o programa que já possui uma lista que tradutora concatenado ao programa em que deixa o programa mais rápido em sua execução final
2) Phyton é uma linguagem de programação criada em 1989 por Guido Von Hossum, no Centro de Matemática e Ciência da Computação, com o objetivo de ser uma linguagem :

- De propósito geral;
- Fácil e intuitiva;
- Multiplataforma;
- Baterias incluídas (bibliotecas);
- Livre;
- Organizada (exige a identação);
- Orientada a Objetos

Atualmente várias empresas em todo o mundo são patrocinadoras da Phyton Software Fundation (PSF) – mantenodora e coordenadora da linguagem. Cite algumas dessas empresas (destacando em que setores da economia elas atuam) e projetos onde a linguagem python tem grande usabilidade. (não vale os que estão descritos no slide 3), pesquise e apresente junto à sua resposta a fonte em que pesquisou.

Zope é um gerenciador de conteúdo totalmente feito em python.
BitTorrent : também é aplicado a linguagem em clientes de BitTorrent. https://www.youtube.com/watch?v=Mp0vhMDI7fA&t=1004s
Desde 2016, o Instagram usa o Python como principal linguagem de programação, tendo feito em 2017 uma enorme mudança para o Python 3 e anunciado que estavam gerenciando o maior projeto de desenvolvimento web de Django escrito inteiramente em Python.https://dojo.bylearn.com.br/python/grandes-empresas-que-usam-python/


3) Escreva um programa utilizando a linguagem C e depois a linguagem Python, que solicite ao usuário 2 números e exiba na tela as quatro operações matemáticas básicas (soma, subtração, multiplicação e divisão).

4) NUM1=int(input("Digite o numero: . . ."))
5) NUM2=int(input("Digite outro numero: . . ."))
6)
7) SOMAT=(NUM1+NUM2)
8) print("__________________________Resultado________________________________________________")
9) print("o soma é: {} ,a subitração é:{} a multiplicação é: {} a divião é: {}".format (NUM1+NUM2,NUM1-NUM2,NUM1*NUM2,NUM1/NUM2))
10)
11) dobro=SOMAT*2
12) triplo=SOMAT*3
13) raiz=SOMAT**(1/2)
14) print("o numero e {} ,o dobro é {} o triplo é {} e a raiz é {}".format (SOMAT,dobro,triplo,raiz))
15) print("__________________________Resultado________________________________________________")

ou

num= int(input ("Digite um numero : . . .")) 
num2= int(input ("Digite outro numero : . . ."))
print(" {} somado a {} é {}".format(num,num2,num+num2))
print(" {} menos {} é {}".format(num,num2,num-num2))
print(" {} x {} é {}".format(num,num2,num*num2))
print(" {} dividido {} é {}".format(num,num2,num/num2))



#include <stdio.h>

int main(){
// Definir variáveis
float n1, n2, soma, difere, multi, divi;
// Código
printf("Qual o primeiro número? ");
scanf("%f", &n1);
printf("Qual o segundo número? ");
scanf("%f", &n2);
printf("_______________________________\n\n");
divi = n1/n2;
multi = n1*n2;
difere = n1-n2;
soma = n1+n2;
printf("_______________________________\n\n");
printf("soma:%.2f\n",soma);
printf("diferen�c:%.2f\n)",difere );
printf("multiplicacao:%.2f\n",multi );
printf("divisao:%.2f\n",divi );
printf("_______________________________\n\n");
return 0;
}

#include <stdio.h>
#include <math.h>
int main()

{

float n1, n2, resultado;
int opcao;
printf("Digite o primeiro numero:...");
scanf("%f", &n1);
printf("Digite o segundo numero:...");
scanf("%f", &n2);
printf("_______________________________\n");
printf("Selecione uma das opÃ§Ãµes abaixo:\n\n");
printf("1- O primeiro nÃºmero elevado ao segundo nÃºmero\n");
printf("2- Raiz quadrada de cada um dos nÃºmeros.\n");
printf("3- Raiz cÃºbica de cada um dos nÃºmeros.\n\n");
printf("Digite a opÃ§Ã£o desejada: ");
scanf("%d", &opcao);
printf("_______________________________\n");
if (opcao == 1)
{resultado = pow(n1,n2);
printf("O nÃºmero %.2f elevado a %.2f resulta em %.2f", n1, n2, resultado);}
else if (opcao == 2)
{resultado = sqrt(n1);
printf("A raiz quadrada de %.2f Ã© %.2f\n", n1, resultado);
resultado = sqrt(n2);
printf("A raiz quadrada de %.2f Ã© %.2f\n", n2, resultado);}
else if (opcao == 3)
{resultado = pow(n1, 1.0/3.0);
printf("A raiz cÃºbica de %.2f Ã© %.2f\n", n1, resultado);
resultado = pow(n2, 1.0/3.0);
printf("A raiz cÃºbica de %.2f Ã© %.2f\n", n2, resultado);}
else
{printf("A opÃ§Ã£o %d nÃ£o Ã© um valor aceito!", opcao);}
return 0;

}
16) No slide 2 foi sugerido o vídeo “Por que todos deveriam aprender a programar”, hospedado no endereço: https://www.youtube.com/watch?v=mHW1Hsqlp6A, após assistir o mesmo cite dois momentos que você achou mais importante e qual a sua visão em relação ao tema?

Achei muito interessantes as pessoa de peso na programação que contribuíram no mundo e estão estimulando novos programadores com suas historia de programas simples e (bobos) no inícios de suas jornadas.

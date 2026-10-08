import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])

except (ValueError, IndexError):
    print('Escolha número inteiros')
    sys.exit(1)
# Os sys.arv's no código possibilitam a seleção dos valores de a e b por meio da linha de comando,
# o int garante que o valor seja um número inteiro possibilitando a realização dos cálculos. As 
# funções "try" e "except" garantem que apenas números inteiros serão considerados, interrompendo
# o código caso essas condições não sejam respeitadas.

if a < 500 and b < 500:
    hip_quad = (b**2) + (a**2)
else:
    print("Escolha um número menor que quinhentos")

# A função if foi utilizada nessa situação para garantir que os valores de a e b sejam menores que 500

print('O quadrado da hipotenusa para o triangulo retângulo com lados a=',a, "e b=",b,', é', hip_quad)


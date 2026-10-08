import sys

try:
    dna_seq = sys.argv[1]
    n1 = int(sys.argv[2])
    n2 = int(sys.argv[3])
    n3 = int(sys.argv[4])
    n4 = int(sys.argv[5])
    n5 = int(sys.argv[6])
    n6 = int(sys.argv[7])

except (IndexError, ValueError):
    print("Utilizar a seguinte sequência no terminal: python script_CDS.py <sequência de DNA> <n1> <n2> <n3> <n4> <n5> <n6>")
    sys.exit(1)

# Esse bloco de código verifica se os valores colocados no terminal são correspondentes com o esperado, caso não sejam, o programa é encerrado.

if len(dna_seq) <n6:
    print("A sequência de DNA é menor que o valor de n6")
    sys.exit(1)
else:
    CDS_1 = dna_seq[n1:n2]
    CDS_2 = dna_seq[n3:n4]
    CDS_3 = dna_seq[n5:n6]


# Esse bloco do código é responsável por extrair as informações das regiões codificantes (CDS) e verificar se o número colocado no terminal comporta a sequência de DNA


if CDS_1[0:3] == 'ATG' and CDS_3[-3:] in ['TAA', 'TAG', 'TGA']:
    print(CDS_1 + CDS_2 + CDS_3)
else:
    print("Os valores dos pontos 3 e 5 são falsos")
# Caso todas as condições sejam verdadeiras, o programa printa a concatenação das CDS, caso contrário, printa um aviso.

seq = input('Digite uma sequência de DNA: ').upper()
#Recebe a sequência de DNA do usuário por meio de um input e garante que independente se a lista estiver em letras maiúsculas ou minúsculas contínua funcionando.

# A sequência só é válida se todas as letras forem A, T, C ou G.
# set(seq) tem as letras distintas; <= verifica se são subconjunto de "ATCG"
if seq and set(seq) <= set("ATCG"):
    # str.count() conta quantas vezes cada base aparece na sequência inteira
    print('A:', seq.count("A"))
    print('T:', seq.count("T"))
    print('C:', seq.count("C"))
    print('G:', seq.count("G"))
else:
    print("Coloque uma sequência de DNA válida, incluindo apenas A, T, C ou G")
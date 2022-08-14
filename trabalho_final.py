#abrir e ler o arquivo txt
file = open('text.txt','r' )

#função para conjunto união
def uniao(A, B):
    
    result = []

    final_result = ', '

    for i in A:
        result.append(i)
    for i in B:
        if i not in A:
            result.append(i)
            
    return(final_result.join(result))

#função para o conjunto interseção
def inter(A, B):

    result = []
    
    final_result = ', '

    for i in A:
        if i in B:
            result.append(i)

    return(final_result.join(result))

#função para o conjunto diferença
def dif(A, B):

    result = []

    final_result = ', '
    
    for i in A:
        result.append(i)
        if i in B:
            result.remove(i)

    return(final_result.join(result))

#função para o conjunto produto cartesiano
def cart(A, B):

    result = [(x, y) for x in A for y in B]

    final_result = ', '
    
    return(result)


#Depois de ler o arquivo faz um for nas linhas e verifica a operação do conjunto e puxa para a devida função
for value in file:

    if "U" in value[0]:
        
        
        A = file.readline().rstrip("\n").replace(" ", "").split(",")
        B = file.readline().rstrip("\n").replace(" ", "").split(",")
        a = ', '
        b = ', '
        print(f"União: conjunto 1 = {{{a.join(A)}}} conjunto 2 = {{{b.join(B)}}} Resultado: {{{uniao(A, B)}}}")

    elif "I" in value[0]:
        A = file.readline().rstrip("\n").replace(" ", "").split(",")
        B = file.readline().rstrip("\n").replace(" ", "").split(",")
        a = ', '
        b = ', '
        print(f"Interseção: conjunto 1 = {{{a.join(A)}}} conjunto 2 = {{{b.join(B)}}} Resultado: {{{inter(A, B)}}}")
    elif "D" in value[0]:
        A = file.readline().rstrip("\n").replace(" ", "").split(",")
        B = file.readline().rstrip("\n").replace(" ", "").split(",")
        a = ', '
        b = ', '
        print(f"Diferença: conjunto 1 = {{{a.join(A)}}} conjunto 2 = {{{b.join(B)}}} Resultado: {{{dif(A, B)}}}")

    elif "C" in value[0]:
        A = file.readline().rstrip("\n").replace(" ", "").split(",")
        B = file.readline().rstrip("\n").replace(" ", "").split(",")
        a = ', '
        b = ', '
        c = ', '
        print(f"""Produto Cartesiano: conjunto 1 = {{{a.join(A)}}} conjunto 2 = {{{b.join(B)}}} Resultado: {{{c.join(map(str, cart(A, B))).replace(")(", "), (").replace("('", "(").replace("')", ")").replace("', ", " ").replace(" '", ", ")}}}""")
        #print(f"""{{{c.join(map(str, cart(A, B))).replace(")(", "), (").replace("('", "(").replace("')", ")").replace("', ", " ").replace(" '", ", ")}}}""")
        #Resultado: {{{cart(A, B)}}}
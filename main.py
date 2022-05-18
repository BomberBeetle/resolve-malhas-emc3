# 18/05/2022
# Código por André Luiz Ferrari de Arruda e Letícia... esqueci o nome inteiro dela

#Esse script assume que todas malhas estão assinaladas uma direção horária

import numpy as np
print("Resolutor de Circuitos de Malha.\nImportante: considere todas as malhas como estando em direção horária.")
n = int(input("Digite o número de malhas: "))

tabela_coef= np.zeros(shape=(n, n), dtype=np.float_)
#Inicializar a tabela de coeficientes (i1, i2, i3...) das equações do sistema

tabela_ord = np.zeros(shape=(n), dtype=np.float_)
#Inicializar a tabela de ordenadas (tensões) das equações do sistema

for i in range(n):
    #Pra cada malha...

    tabela_ord[i] = -float(input("Digite a tensão total da malha {}: ".format(i+1)))
    #Insere o inverso da tensão total da malha na tabela de ordenadas, partindo das equações LKT: V -(i1a, i2b) -> -(i1a, i2b) = -V

    tabela_coef[i][i] -= float(input("Digite a resistência total (não compartilhada com outras malhas) da malha {}: ".format(i+1)))
    #Lê e se adiciona ao coeficiente da corrente da malha na equação LKT dessa malha.

    for j in range(n-i-1):
    #Este "for" nos deixa passar por cada resistência compartilhada sem repeti-las entre leituras de malhas individuais.

        nres = float(input("Digite a resistência compartilhada entre as malhas {} e {}: ".format(i+1, j+2+i)))

        tabela_coef[i][i] -= nres
        tabela_coef[i][j+1+i] += nres
        tabela_coef[j+1+i][i] += nres
        tabela_coef[j+1+i][j+1+i] -= nres
        #As resistências compartilhadas usam do fato que consideramos todas as malhas como tendo a mesma direção horária. Logo, nós sempre consideramos a tensão nesse resistor como (imalhaDaEquação*r - ioutraMalha*r), e fazemos isso nas duas malhas. 
        

res = np.linalg.solve(tabela_coef, tabela_ord)
#Resolve o nosso sistema de equações LKT usando a função "linalg.solve" da biblioteca NumPy, que resolve sistemas lineares em geral usando uma tabela de coeficientes e uma tabela de ordenadas. Essa função, em turno, usa internamente da função _gesv da biblioteca LAPACK, que providencia implementações eficientes de baixo nível para operações simples de álgebra linear.

for idx, val in enumerate(res, start=1):
    print("Corrente da malha {}: {}A".format(idx, val))
import numpy as np
# importa o sys para pegar o argumento instância passado pelo usuário através do terminal
import sys

def criaMatriz(inst):
    # cria uma variável caminho que irá acessar a pasta contendo as instâncias. Em seguida,, abre o arquivo com rb para que não o arquivo não seja corrompido independente de seu formato. Como é um txt, é usado o loadtxt do numpy para que os dados sejam lidos e guardados na variável matriz
    caminho = rf'C:\Users\hanna\OneDrive\Ambiente de Trabalho\Faculdade\05SEM\005_GRAFOS\atividades\instancias\{inst}.txt'
    with open(caminho, 'rb') as f:
        matriz = np.loadtxt(f)
    return matriz

def recebeResultado(matriz):
    #cria uma variável resultado que armazenará a instância (que é o nome do arquivo) e as dimensões da matriz (que são transformadas em string para que não haja problema na hora de printar) com o shape do numpy.
    resultado = str(inst)+ '\n' + str(matriz.shape)
    return resultado

def salvaResultado(resultado):
    #cria uma variável que irá acessar uma pasta criada para receber os resultados gerados pelo programa. Nesse open, já usamos o w para que o arquivo seja aberto no modo escrita. Após escrever o resultado, o arquivo é fechado.
    arq = open(rf'c:\Users\hanna\OneDrive\Ambiente de Trabalho\Faculdade\05SEM\005_GRAFOS\atividades\resultados\res{inst}.txt', 'w')
    arq.write(resultado + '\n')
    arq.close()


if __name__ == '__main__':
    #A variável inst é recebida do usuário pelo terminal. Depois, as funcções são chamadas para que a matriz seja criada, para que o resultado receba o nome e as dimensões dela e para que o resultado seja salvo num novo arquivo.
    inst = sys.argv[1]
    mat = criaMatriz(inst)
    res = recebeResultado(mat)
    salvaResultado(res)
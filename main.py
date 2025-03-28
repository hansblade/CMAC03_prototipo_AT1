import numpy as np
# importa o sys para pegar o argumento instância passado pelo usuário através do terminal
import sys

def criaMatriz(inst):
    # cria uma variável caminho que irá acessar a pasta contendo as instâncias. Em seguida,, abre o arquivo 
    caminho = rf'C:\Users\hanna\OneDrive\Ambiente de Trabalho\Faculdade\05SEM\005_GRAFOS\atividades\instancias\{inst}.txt'
    with open(caminho, 'rb') as f:
        matriz = np.loadtxt(f)
    return matriz

def recebeResultado(matriz):
    resultado = str(inst)+ '\n' + str(matriz.shape)
    return resultado

def salvaResultado(resultado):
    arq = open(rf'c:\Users\hanna\OneDrive\Ambiente de Trabalho\Faculdade\05SEM\005_GRAFOS\atividades\resultados\res{inst}.txt', 'w')
    arq.writelines(resultado + '\n')
    arq.close()


if __name__ == '__main__':
    inst = sys.argv[1]
    mat = criaMatriz(inst)
    res = recebeResultado(mat)
    salvaResultado(res)
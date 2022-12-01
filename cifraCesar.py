import sys

MODO_CRIPTOGRAF = 1
MODO_DESCRIPTOGRAF = 0
CHAVE = 12

def cifra(texto, chave, modo): #Desenvolvimento da Cifra de Cesar
    alfabeto= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_txt = ''
    for c in texto: #Passa por cada caracter dentro do texto
        index = alfabeto.find(c) #Procura a posição desse caracter dentro da string alfabeto
        if index == -1:
            new_txt += c
        else:
            new_index = index + chave if modo == MODO_CRIPTOGRAF else index - chave
            new_index = new_index % len(alfabeto)
            new_txt += alfabeto[new_index:new_index+1]
    return new_txt

def verificaArquivo(): #Verifica se há um arquivo com esse nome, caso não tenha ele cria
    try:
        f = open('arquivo_de_entrada.txt')
        f.close()
    except:
        print("Criando arquivo para receber seu texto de entrada!")
        f = open('arquivo_de_entrada.txt', 'w')
        f.close()
        sys.exit()
    
def getInfo(nome, op):
    with open(nome, op) as f:
        arquivo = f.readlines()

    f.close()
    return arquivo

def descriptografar():
    nome = 'arquivo_criptografado.txt'
    op = 'r'
    arquivo = getInfo(nome, op)

    f = open('arquivo_descriptografado.txt', 'a')

    for frase in arquivo:
        descriptografado = cifra(frase, CHAVE, MODO_DESCRIPTOGRAF)
        f.write(descriptografado)
    f.close()

def criptografar():
    nome = 'arquivo_de_entrada.txt'
    op = 'r'
    arquivo = getInfo(nome, op)

    f = open('arquivo_criptografado.txt', 'a') #Cria o arquivo caso não exista com a possibilidade de acrescentar

    for frase in arquivo:
        criptografado = cifra(frase, CHAVE, MODO_CRIPTOGRAF)
        f.write(criptografado)
    f.close()

def main():
    verificaArquivo()
    criptografar()
    descriptografar()

if __name__ == "__main__":
    main()
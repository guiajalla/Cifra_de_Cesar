MODO_CRIPTOGRAF = 1
MODO_DESCRIPTOGRAF = 0

def cifra(texto, chave, modo): #Desenvolvimento da Cifra de Cesar
    alfabeto= "abcdefghijklmnopqrstuvwxyz"
    texto = texto.lower() #Mantém o texto em minusculo, visto que o alfabeto utilizado, apenas trabalha com letras minusculas
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
        f = open('arquivo_criptografado.txt', 'a')
        f.close()
    except:
        print('Erro ao abrir arquivo!')
    
def interface():
    print('----- Escolha o que deseja fazer -----')
    print('1 - Criptografar')
    print('2 - Descriptografar')
    print('--------------------------------------')
    op = input('Opcao: ')
    match op:
        case '1':
            print('você escolheu criptografar')
        case '2':
            print('Você escolheu descriptografar')


def main():
    interface()
    # Tests
    # chave = 24
    # original = 'A ligeira raposa marrom saltou sobre o cachorro cansado'
    # print('  Original:', original)
    # ciphered = cifra(original, chave, MODO_CRIPTOGRAF)
    # print('Encriptada:', ciphered)
    # plain = cifra(ciphered, chave, MODO_DESCRIPTOGRAF)
    # print('Decriptada:', plain)
    #verificaArquivo()

if __name__ == "__main__":
    main()
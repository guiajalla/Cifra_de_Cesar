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
        f = open('arquivo_criptografado.txt')
        f.close()
        return True
    except:
        return False
    
def getInfo():
    print('entrou')

def setInfo():
    info = []
    f = open('arquivo_criptografado.txt', 'w')
    texto = input('\nDigite o que deseja criptografar: \n')
    chave = int(input('\nDigite o número da chave para criptografar(1~26): \n'))

    txt_cifrado = cifra(texto, chave, MODO_CRIPTOGRAF)
    info.append(txt_cifrado)
    info.append(chave)

    for conteudo in info:
        f.write(str(conteudo) + ';')
    f.close()

def interface():
    print('----- Escolha o que deseja fazer -----')
    print('1 - Criptografar')
    print('2 - Descriptografar')
    print('--------------------------------------')
    op = input('Opcao: ')
    match op:
        case '1':
            setInfo()
        case '2':
            if verificaArquivo() ==  False:
                print('Você não possui um arquivo para descriptografar!\n')
                return interface()
            else:
                print('Descriptografando arquivo')
                getInfo()
            


def main():
    interface()

if __name__ == "__main__":
    main()
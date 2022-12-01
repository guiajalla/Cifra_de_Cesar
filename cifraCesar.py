def verificaArquivo():
    try:
        f = open('arquivo_criptografado.txt', 'a')
        f.close()
    except:
        print('Erro ao abrir arquivo!')
    

def main():
    # alphabet = "abcdefghijklmnopqrstuvwxyz"
    verificaArquivo()

if __name__ == "__main__":
    main()
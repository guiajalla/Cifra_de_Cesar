<div stye="display:flex; flex-direction: row">
  <img src="https://img.shields.io/badge/guiajalla-Caesar_Cipher-green" />
  <img src="https://img.shields.io/badge/-Cifra_de_César-grey" />
  <a href="https://www.linkedin.com/in/guilherme-ajalla/">
    <img src="https://img.shields.io/badge/-Linkedin-blue" />
  </a>
</div>

# Cifra de Cesar

## Sobre:
<p>Trata-se de um tipo de cifra de substituição, na qual cada letra de um texto a ser criptografado é substituída por outra letra, presente no alfabeto porém deslocada um certo número de posições à esquerda ou à direita.</p>

## Inicio do código:
<p>Inicialmente meu código inicia com a importação da biblioteca sys, que será responsável por encessar o programa posteriormente. Em seguida eu defino os valores para o modo de Criptografar e descrioptografar, assim como a definição da chave para realizar o processo.<br><br><b>Como mostra na imagem abaixo!</b></p>

![image](https://user-images.githubusercontent.com/55240778/205143002-9a7ff2de-8a86-4296-8931-778902bd5475.png)

<p>Código inicia-se chamando o método main(), <i>-como mostra a imagem abaixo-</i> dentro dela irei fazer a chamada dos métodos verificaArquivo(), criptografar() e descriptografar().</p>

![image](https://user-images.githubusercontent.com/55240778/205144225-e1a49a8a-d995-49f8-87b1-5ff2290e2c9b.png)

## Método verificaArquivo():

<p>Esse método é responsável por verificar se há um arquivo com o nome "arquivo_de_entrada.txt" caso o arquivo exista ele irá fechar o arquivo e seguirá para criptografia dele, caso contrário ele irá criar esse arquivo para o usuário e encerrará o programa, deixando o usuário livre para colocar as informações dentro do arquivo .txt que ele deseja criptografar.</p>

![image](https://user-images.githubusercontent.com/55240778/205145286-7a2f35cf-e28a-4e3d-b9c1-abf80a1bdb08.png)

## Método criptografar():
<p>
Como o próprio nome já informa, ele será responsável por criptografar as informações que foram inseridas no documento "arquivo_de_entrada.txt".
<br>
<br>
Inicialmente eu defino o nome deste arquivo na variavel <i>"nome"</i> e o método de manipulação de arquivo na variável <i>"op"</i>, em seguida faço a criação de num novo arquivo, chamado "arquivo_criptografado.txt", com a possibilidade de escrever/acrescentar coisas a ele. Em um <i>for</i> eu coleto cada frase escrita no documento "arquivo_de_entrada.txt", chamo o método em que a Cifra de César está implementada junto da frase (que está sendo processada no momento), a chave de criptografia definida e o modo que refere-se ao de criptografar as informações; logo após esse procedimento, escrevo as frases no arquivo "arquivo_criptografado.txt".
</p>

![image](https://user-images.githubusercontent.com/55240778/205146224-e01e9aad-5ef7-49cd-9a87-cbeadef1c7b5.png)

Obs: Após rodar algumas vezes, percebi que com o método de manipulação de arquivos <i>"a"</i> a criptografia é sempre adicionada ao documento, havendo contatenações ao conteúdo que já havia dentro do arquivo("arquivo_criptografado.txt").

<img src="https://img.shields.io/badge/-Caso_queira_rodar_novamente_o_programa_é_necessário_limpar_o_conteúdo_do_arquivo_de_nome_arquivo_criptografado-red" />

## Método descriptografar():
<p>
Responsável por descriptografar o arquivo que foi criptografado anteriormente, ele abre o "arquivo_criptografado.txt" pega o que tem dentro com getInfo() e começa o tratamento de descriptografar, semelhante ao processo de criptografia, porém, realizando ele de forma contrária. Logo após o tratamento de descriptografia, utilizando a Cifra de César, ele criar um novo arquivo cujo o nome é "arquivo_descriptografado.txt" com as informações descriptografadas.
</p>

![image](https://user-images.githubusercontent.com/55240778/205149159-8c0a040a-ebb0-4084-b0a5-f98abeb75644.png)

Obs²: Assim como no método de criptografia, caso o programa seja rodado novamente ele irá concatenar com o que já havia dentro do arquivo(arquivo_descriptografado.txt)

<img src="https://img.shields.io/badge/-Caso_queira_rodar_novamente_o_programa_é_necessário_limpar_o_conteúdo_do_arquivo_de_nome_arquivo_descriptografado-red" />

## Método getInfo(nome, op):
<p>
Esse método apenas pega as informações contidas dentro do arquivo que está sendo solicitado para ele. ele é chamado dentro do método descriptografar() e criptografar().
</p>

![image](https://user-images.githubusercontent.com/55240778/205151767-2042bcdf-8029-405c-b190-f50bf57a0bee.png)

## Método cifra(texto, chave, modo):
<p>
É aqui onde a magia acontece!
<br><br>
O método recebe um texto, a chave e o método que será realizado. Inicialmente, eu defino uma string com o alfabeto (que será utilizado para fazer as comparações para realizar a criptografia ou descriptografia). Defino uma lista vazia, para que seja atribuido o novo texto que ela irá formar.
<br><br>
Inicio um <i>for</i> que irá percorrer os caracteres (c) dentro da string com a frase passada (texto), em que irá procurar o index em relação ao alfabeto, caso passe do tamanho da string ele irá começar a pegar os valores a partir do inicio da string. Após essas atribuições ele irá começar o processo de criptografar ou descriptografar a frase de acordo com modo escolhido. No fim do seu processo, o método retorna o novo texto criado para que possa ser tratado dentro de descriptografar() ou criptografar().
</p>

![image](https://user-images.githubusercontent.com/55240778/205152229-9209d0c6-1c0f-4eaf-ac40-c8818d7f6fe3.png)



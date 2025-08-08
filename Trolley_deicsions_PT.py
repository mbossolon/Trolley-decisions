import random
import sys
import time

cenario = 1

#Definir função para texto ser exibido lentamente
def digitar(texto, velocidade=0.05):
    for letra in texto:
        sys.stdout.write(letra) #escreve uma letra por vez
        sys.stdout.flush() #Atualizar a tela imediatamente
        time.sleep(velocidade) #Serve para pausar entre cada letra
    print() #pula linha no final


def trem6():
    global cenario
    digitar("033[32m\nUm trem transportando um carregamento de vacinas contra uma doença mortal", 0.05)
    digitar("está indo e direção a uma ponte prestes a desabar.", 0.05)
    digitar("Você pode desviá-lo para outro trilho, mas vai atropelar dez crianças", 0.05)
    print("O que você faz?\033[0m")
    print("1 - Puxa a alavanca, deixando o trem atropelar as crianças")
    print("2- Mantém o curso, perdendo todas as vacinas e condenando milhares de pessoas")

    while True:
        escolha = input("Digite o número escolhido: ")
        if escolha == "1":
            digitar("\033[0m\n Você puxou a alavanca e o trem atropelou dez crianças", 0.05)
            digitar("As vacinas chegaram a tempo na cidade e com isso, milhares de vidas foram salvas\033[0m", 0.05)
            break

        elif escolha == "2":
            digitar("\033[32m\nVocê manteve o trem no percurso. As crianças foram poupadas", 0.05)
            digitar("No entanto, milhares de pessoas morreram da doença\033[0m", 0.05)
            break

        else:
            print("Você precisa tomar uma decisão!")
    
    cenario += 1
    proximo_cenario()


def trem5():
    global cenario
    digitar("\033[34m\nUm trem está andando normalmente. Não há nenhum problema aqui", 0.05)
    digitar("Mesmo assim você pode puxar a alavanca só por diversão", 0.05)
    digitar("Isso mudará a rota do trem para outra cidade\033[0m", 0.05)
    print("O que você faz?")
    print("1 - Puxa a alavanca e muda a rota do trem sem motivo algum")
    print("2 - Mantém o trem na rota original")

    while True:
        escolha = input("Digite o número escolhido: ")
        if escolha == "1":
            sorteio1 = random.randint(1, 100)
            if sorteio1 <= 10:
                digitar("\033[32m\nVocê desviou o trem. Por sorte havia um sequestrador no trem!", 0.05)
                digitar("A cidade para onde você o enviou haviam muitas autoridades e o sequestrador foi preso", 0.05)
                digitar("Você foi condecorado como herói e apareceu no jornal! Todos te amam!\033[0m", 0.05)
            
            elif 11 <= sorteio1 <=55:
                digitar("\033[32m\nVocê puxou a alavanca e desviou o trem para outra cidade", 0.05)
                digitar("Havia uma mulher grávida no trem e não deu tempo de ela chegar na maternidade", 0.05)
                digitar("Ela deu a luz dentro do trem e o bebê ganhou passagens gratis pela vida toda\033[0m", 0.05)
                digitar("\033[31m\nInfelizmente isso será descontado do seu pagamento e você assumiu uma divida eterna\033[0m", 0.05)
            
            elif 56 <= sorteio1 <= 100:
                digitar("\033[31m\nVocê puxou a alavanca e desviou o trem", 0.05)
                digitar("Todos os passageiros ficaram furiosos e processaram a companhia", 0.05)
                digitar("Você foi demitido. Sem emprego sua famílai te abandonou", 0.05)
                digitar("Agora você vive na rua sem ninguém. Ninguém te ama!\033[0m", 0.05)
            
            break
        elif escolha == "2":
            digitar("\033[33m\nVocê decidiu manter o trem na rota original. Nada de especial aconteceu\033[0m", 0.05)
            break

        else:
            print("Você precisa fazer uma escolha!")
    cenario += 1
    proximo_cenario()

def trem4():
    global cenario
    digitar("\033[34m\nUm trem desgovernado está indo em direção À 5 pessoas amarradas nos trilhos", 0.05)
    digitar("Você pode puxar a alavanca, mas vai redirecionar o trem e ele vai atropelar a sua MÃE\033[0m", 0.05)
    print("O que você faz?")
    print("1 - Puxa a alavanca e o trem atropela sua mãe")
    print("2 - Não faz nada e deixa o trem atropelar 5 pessoas")

    while True:
        escolha = input("digite o número da sua decisão: ")
        if escolha == "1":
            digitar("\033[31m\nVocê puxou a alavanca e o trem atropelou sua mãe", 0.05)
            digitar("No velório estavam todos tristes. Sua irmã não fala mais com você", 0.05)
            digitar("Ela te culpa pela morte da mãe. E agora te chama de assassinos", 0.05)
            digitar("O seu pai entende sua decisão, mas entrou em depressão e não come direito\033[0m", 0.05)
            break
        elif escolha == "2":
            digitar("\033[31m\nVocê ama demais a sua mãe e não puxou a alavanca", 0.05)
            digitar("5 pessoas morreram, mas sua mãe está viva!", 0.05)
            digitar("Você abraça sua mãe. E ela agradece seu amor", 0.05)
            digitar("\nOs familiares daquelas 5 pessoas nunca poderão abraçá-las", 0.05)
            digitar("Eles te culpam pela morte de seus familiares. A vida da sua mãe vale mais do que a de 5 pessoas.\033[0m", 0.05)
            break
        else:
            print("VOcê precisa tomar uma decisão!")
    
    cenario += 1
    proximo_cenario()

def trem2():
    global cenario
    digitar("\033[34m\nUm trem desgovernado está indo em direção a 1 pessoa", 0.05)
    digitar("Se você puxar a alavanca, o trem desvia, mas atropela um cachorrinho\033[0m", 0.05)
    print("O que você faz?")
    print("1 - Puxar a alavanca")
    print("2 - Não fazer nada")

    while True:
        escolha = input("Digite o número da sua decisão: ")
        if escolha == "1":
            digitar("\033[31m\nVocê puxou a alavanca e o trem atropelou um cachorrinho\033[0m", 0.05)
            digitar("\033[34m\nLogo depois, você está andando e vê uma criança chorando por seu cachorrinho morto\033[0m", 0.05)
            digitar("1 - Contar a verdade e pedir desculpas", 0.05)
            digitar("2 - Ignorar e seguir seu caminho", 0.05)
            
            while True:
                escolha2 = input("Você decide: ")
                if escolha2 == "1":
                    digitar("\033[32m\nA criança entendeu, e te agradeceu por ser honesto\033[0m", 0.05)
                    break  # Sai do loop interno
                elif escolha2 == "2":
                    digitar("\033[33m\nVocê ignorou a criança e seguiu seu caminho", 0.05)
                    digitar("Nossa, como você é babaca!\033[0m", 0.05)
                    break  # Sai do loop interno
                else:
                    print("Você deve tomar uma decisão válida!")  # Mantém o jogador no loop

            cenario += 1
            proximo_cenario()  # Chama o próximo cenário apenas após uma escolha válida
            break  # Sai do loop principal
        
        elif escolha == "2":
            digitar("\033[31mVocê não puxou a alavanca e o trem atropelou 1 pessoa\033[0m", 0.05)
            cenario += 1
            proximo_cenario()
            break
        
        else:
            print("Você deve tomar uma decisão válida!")  # Mantém o jogador no loop até escolher "1" ou "2"

def trem3():
    global cenario
    digitar("\033[34m\nUm trem desgovernado está prestes a atropelar 5 pessoas", 0.05)
    digitar("não há alavanca, mas você pode empurrar Douglas, um homem de 50 anos com obesidade, nos trilhos e parar o trem\033[0m", 0.05)
    print("1 - empurrar Douglas nos trilho")
    print("2 - não empurrar o Douglas")
    while True:
        escolha = input("Você decide: ")
        if escolha == "1":
            digitar("\033[31m\nVocê empurrou Douglas nos trilhos", 0.05)
            digitar("Douglas olhou para você desesperado", 0.05)
            digitar("Ele tentou desesperadamente correr, mas foi em vão", 0.05)
            digitar("O trem atropelou Douglas. os corpos dele voaram por toda a parte\033[0m", 0.05)
            digitar("\033[32m\nMas você parou o trem e salvou 5 pessoas\033[0m", 0.05)
            break

        elif escolha == "2":
            digitar("\033[31m\nVocê não fez nada e o trem atropelou 5 pessoas", 0.05)
            digitar("Você e Douglas ficaram olhando horrorizados", 0.05)
            digitar("Douglas ficou traumatizado com aquilo e teve que ir a um psicólogo\033[0m", 0.05)
            digitar("\033[32m\nVocê e Douglas se tornaram proximos depois disso e hoje ele é seu melhor amigo\033[0m", 0.05)
            break

        else:
            print("Você deve tomar uma decisão!")
    cenario += 1
    proximo_cenario()


def trem1():
    global cenario
    digitar("\033[34mBem vindo ao trolley decisions.", 0.05)
    digitar("Aqui você deve tomar decisões e aceitar os resultados", 0.05)
    print("\nCenário 1:")
    digitar("Um trem desgovernado está indo em direção a cinco pessoas amarradas nos trilhos.", 0.05)
    digitar("Você pode puxar uma alavanca para desviar o trem para outro trilho, mas há uma pessoa amarrada lá.\033[0m", 0.05)
    print("Qual é sua decisão?")
    print("1 - Puxar a alavanca")
    print("2 - Não fazer nada")
    while True:
        escolha = input("Digite o número da sua decisão: ")
        if escolha == "1":
            digitar("\033[31m\nVocê puxou a alavanca e o trem atropelou uma pessoa\033[0m", 0.05)
            break
        
        elif escolha == "2":
            digitar("\033[31m\nVocê não puxou a alavanca e o trem matou 5 pessoas.\033[0m", 0.05)
            break
        
        else:
            print("Você deve tomar uma decisão!")

    cenario += 1
    proximo_cenario()

cenarios = {
    2: trem2,
    3: trem3,
    4: trem4,
    5: trem5,
    6: trem6
}

def proximo_cenario():
    global cenario
    print("\nir para o príxmo cenário?")
    print("1 - sim / 2 - sair")
    while True:
        escolha = input("digite o numero da sua decisão: ")
        if escolha == "1":
            sorteio = random.randint(2, 6)
            print(f"\nCenário {sorteio}:")
            cenarios[sorteio]()
            break

        elif escolha == "2":
            print(f"\nVocê jogou {cenario} cenários! Obrigado por jogar!")
            break

        else:
            print("Opção inválida. Escolha 1 ou 2!")



trem1()
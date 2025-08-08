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
    digitar("033[32m\nA train carrying a shipment of vaccines against a deadly disease", 0.05)
    digitar("is heading towards a bridge that is about to collapse.", 0.05)
    digitar("You can pull a lever and divert it to another track", 0.05)
    digitar("but the train will run over ten children", 0.05)
    print("What will you do?\033[0m")
    print("1 - Pull the lever and let the train run over the children")
    print("2- Don't pull the lever, losing all the vaccines and condemning thousands of people")

    while True:
        escolha = input("Type the number of your choice: ")
        if escolha == "1":
            digitar("\033[0m\n You pulled the lever and the train ran  over ten children", 0.05)
            digitar("The vaccine arrived in the city on time and thousands of lives were saved\033[0m", 0.05)
            break

        elif escolha == "2":
            digitar("\033[32m\nYou kept the train on track. The children were spared", 0.05)
            digitar("However thousands of people died with the deseace\033[0m", 0.05)
            break

        else:
            print("You must make a decision!")
    
    cenario += 1
    proximo_cenario()


def trem5():
    global cenario
    digitar("\033[34m\nA train is running normally; There is no problem here", 0.05)
    digitar("You can still pull the lever just for fun", 0.05)
    digitar("This will change the train route to another city\033[0m", 0.05)
    print("What will you do?")
    print("1 - Pull the lever and change the train route ust for fun")
    print("2 - Keep the train on the original route")

    while True:
        escolha = input("Type the number of your choice: ")
        if escolha == "1":
            sorteio1 = random.randint(1, 100)
            if sorteio1 <= 10:
                digitar("\033[32m\nYou diverted the train from its route. Luckily there was a hijacker on the train!", 0.05)
                digitar("The city where you send him was full of cops and the hijacker was busted!", 0.05)
                digitar("You've been crowed a hero and made the newspaper! Everyone loves you!\033[0m", 0.05)
            
            elif 11 <= sorteio1 <=55:
                digitar("\033[32m\nYou pulled the lever and diverted the train to another city", 0.05)
                digitar("There was a pregnant woman on the train and she didn't make it to the maternity hospital", 0.05)
                digitar("She gave birth inside the train and the baby won free tickets ride for life\033[0m", 0.05)
                digitar("\033[31m\nUnfortunately this will be deducted from your payment and you got a lifetime debt\033[0m", 0.05)
            
            elif 56 <= sorteio1 <= 100:
                digitar("\033[31m\nYou pulled the lever and diverted the train to another city", 0.05)
                digitar("All the passengers were furious and sued the company", 0.05)
                digitar("You were fired. With no job your family left you", 0.05)
                digitar("Now you live in the streets with nobody. Nobody loves you!\033[0m", 0.05)
            
            break
        elif escolha == "2":
            digitar("\033[33m\nYou chose to keep the train on it's original route. Nothing special happened\033[0m", 0.05)
            break

        else:
            print("You must make a decision!")
    cenario += 1
    proximo_cenario()

def trem4():
    global cenario
    digitar("\033[34m\nA runaway train is going towards 5 people tied on the tracks", 0.05)
    digitar("You can pull the lever, but that wil divert the train and it will run over your MOTHER!\033[0m", 0.05)
    print("What will you do?")
    print("1 - Pull the lever and let the train run over your mom")
    print("2 - Don't pull the lever and let the train run over 5 people")

    while True:
        escolha = input("Type the number of your choice: ")
        if escolha == "1":
            digitar("\033[31m\nYou pulled the lever and the train ran over your mother", 0.05)
            digitar("Everyone is sad at the wake. YOur sister doesn't talk to you anymore.", 0.05)
            digitar("She blames you for your mother death. NOw she calls you murderer", 0.05)
            digitar("Your father understand your decision, but he is depressed and doesn't eat anymore.\033[0m", 0.05)
            break
        elif escolha == "2":
            digitar("\033[31m\nYou love your mother too much and didn't pull the lever.", 0.05)
            digitar("5 people died, but your mother is alive!", 0.05)
            digitar("You hug your mom and she thank you for your love.", 0.05)
            digitar("\nThe relatives of those 5 people will never be able to hugh them", 0.05)
            digitar("They blame you for their families death. YOur mother's life worth more than the lives of those 5 people.\033[0m", 0.05)
            break
        else:
            print("You must make a decision!")
    
    cenario += 1
    proximo_cenario()

def trem2():
    global cenario
    digitar("\033[34m\nA runaway train is going towards 1 person", 0.05)
    digitar("If you pull the lever, the train swerves, but it will run over a puppy\033[0m", 0.05)
    print("What will you do?")
    print("1 - Pull the lever")
    print("2 - Do nothing")

    while True:
        escolha = input("Type the number of your choice: ")
        if escolha == "1":
            digitar("\033[31m\nYou pulled the lever and the train ran over the puppy\033[0m", 0.05)
            digitar("\033[34m\nSoon after that, you are going home when you see a child crying over her dead puppy\033[0m", 0.05)
            digitar("1 - Tell the truth and apoligize", 0.05)
            digitar("2 - Ignore and go home", 0.05)
            
            while True:
                escolha2 = input("You decide: ")
                if escolha2 == "1":
                    digitar("\033[32m\nThe child understood and thank you for being honest\033[0m", 0.05)
                    break  # Sai do loop interno
                elif escolha2 == "2":
                    digitar("\033[33m\nYou ignored the child and went home", 0.05)
                    digitar("Geez, you are such an asshole!\033[0m", 0.05)
                    break  # Sai do loop interno
                else:
                    print("You must make a decision!")  # Mantém o jogador no loop

            cenario += 1
            proximo_cenario()  # Chama o próximo cenário apenas após uma escolha válida
            break  # Sai do loop principal
        
        elif escolha == "2":
            digitar("\033[31mYou didn't pull the lever and the train ran over 1 person.\033[0m", 0.05)
            cenario += 1
            proximo_cenario()
            break
        
        else:
            print("You must make a decision!")  # Mantém o jogador no loop até escolher "1" ou "2"

def trem3():
    global cenario
    digitar("\033[34m\nA runaway train is about to run over 5 people", 0.05)
    digitar("There is no lever, but you can push Doug, a 50 years old man with obesity, on the tracks and stop the train\033[0m", 0.05)
    print("1 - Push Doug")
    print("2 - Don't push Doug")
    while True:
        escolha = input("You decide: ")
        if escolha == "1":
            digitar("\033[31m\nYou pushed Doug on the tracks", 0.05)
            digitar("Doug look at you disapointed and betrayed.", 0.05)
            digitar("He tried to run desperately, but it was in vain.", 0.05)
            digitar("The train ran over Doug. His bodies parts flew everywhere.\033[0m", 0.05)
            digitar("\033[32m\nBut you stopped the train and saved 5 people\033[0m", 0.05)
            break

        elif escolha == "2":
            digitar("\033[31m\nYou did nothing and the train ran over 5 people", 0.05)
            digitar("You and Doug stared in horror", 0.05)
            digitar("Doug got traumatized with that and had to go to a therapist\033[0m", 0.05)
            digitar("\033[32m\nYou and Doug became good friends after that and today he is your best friend\033[0m", 0.05)
            break

        else:
            print("You must make a decision!")
    cenario += 1
    proximo_cenario()


def trem1():
    global cenario
    digitar("\033[34mWelcome to trolley decisions.", 0.05)
    digitar("Here you must make decisions and accept the results", 0.05)
    print("\nScenario 1:")
    digitar("A runaway trolley is heading towards 5 people tied up on the tracks.", 0.05)
    digitar("You can pull a lever to divert the trolley to another track, but there is a person tied up there.\033[0m", 0.05)
    print("What is your decision?")
    print("1 - Pull the lever")
    print("2 - Do nothing")
    while True:
        escolha = input("Type the number of your answer: ")
        if escolha == "1":
            digitar("\033[31m\nYou pulled the lever and the trolley ran over one person\033[0m", 0.05)
            break
        
        elif escolha == "2":
            digitar("\033[31m\nYou didn't pull the lever and the trolley ran over five people.\033[0m", 0.05)
            break
        
        else:
            print("You must make a decision!")

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
    print("\nNext scenario?")
    print("1 - yes / 2 - quit")
    while True:
        escolha = input("Type the number of your answer: ")
        if escolha == "1":
            sorteio = random.randint(2, 6)
            print(f"\nCenário {sorteio}:")
            cenarios[sorteio]()
            break

        elif escolha == "2":
            print(f"\nYou played {cenario} scenarios! Thanks for playing!")
            break

        else:
            print("Invalid option. Choose 1 or 2!")



trem1()
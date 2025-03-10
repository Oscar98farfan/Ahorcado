import random, os
import pyfiglet


maximum_attempts = 8
header = pyfiglet.figlet_format("HANGED   : D !!")
msglost = pyfiglet.figlet_format("YOU LOST : ( ")
msgwin = pyfiglet.figlet_format("YOU WON : ) ")
words = ['oso', 'castor', 'ballena', 'carro', 'autobus', 'mesa', 'cuaderno', 'cartelera', 'serpiente', 'elefante', 'profesor', 'estudiante']

drawings = [""" 

       +----+                         
       |    |                           
            |                           
            |                           
            |                           
    ============""", """
    
       +----+
       |    |
       0    |
            |
            |
    ============""", """
    
       +----+
       |    |
       0    |
       |    |
            |
    ============""", """ 
    
       +----+
       |    |
       0    |
       |\   |
            |
    ============""", """
    
       +----+
       |    |
       0    |
      /|\   |
            |
    ============""", """
    
       +----+
       |    |
       0    |
      /|\   |
        \   |
    ============""", """
    
       +----+
       |    |
       0    |
      /|\   |
      / \   |
    ============""", """
    
       +----+
       |    |
    ___0___ |
      /|\   |
      / \   |
    ============""","""
    
       +----+
       |    |
            |
            |
     O-|--< |
    ============""","""
    
       \O/    
        |
      _/ \_
    ============"""]
   

def word_secret():
    secret = random.choice(words)
    numberWords = len(secret)
    empty_space = "_" * len(secret)
    return secret, empty_space, numberWords

def succes(secreto, empty_space, letra):   # Simbolo: es la letra que yo coloco, original: Palabra secreta, empty_space: guiones 
    cant = secreto.count(letra)
    begin = 0
    for i in range(cant):
        pos = secreto.find(letra, begin)
        empty_space = empty_space[:pos] + letra + empty_space[pos+1:]
        begin = pos + 1
    return empty_space

def run():
    secreto, empty_space, numberWords = word_secret()
    print(header)
    
    jugador = input("Dime tu nombre: ")
    print(f"Bienvenido {jugador}")
    print(f"Hoy jugaremos el Ahorcado, tu palabra secreta esta entre {len(words)} palabras")
    print(f"Y tiene {numberWords} caracteres. Tienes unicamnente {maximum_attempts} intentos antes de que mueras ajajajaja")
    print() #Espacico
    print(f"Suerte")
    print() #Espacico
    input("Presiona enter para empezar:...")
    print() #Espacico

    # original, empty_space = word_secret()
    fallos = 0
    while empty_space != secreto and fallos < maximum_attempts:
        # os.system('cls')
        print() #Espacico
        print(f"Palabra secreta es: {empty_space}")
        print() #Espacico
        #print(original) # Esta es para revisar la orginal
        s = input("Cual letra quieres intentar?: ")
        print() #Espacico
        if s in secreto:
            empty_space = succes(secreto, empty_space, s)
            print(f"Bien Hecho {jugador}, la letra {s} esta {secreto.count(s)} veces. Sigue asi")
        # elif fallos == 7:
            # print(f"{jugador} te queda solo una oportunidad para fallar. Si no aciertas Tony Morira")
        else:
            print(f"Lo siento la letra {s} no esta en la palabra secreta")
            print(f"Sigue intentanto {jugador}")
            print() #Espacico
            fallos += 1
            print(f"Este es tu fallo numero {fallos}, te quedan {(maximum_attempts - fallos)}")
            print() #Espacico
            print(drawings[fallos])
        
        if empty_space == secreto and fallos < maximum_attempts:
            print() # Espacio
            print(msgwin)
            print() # Espacio
            print(f"Bien hecho {jugador} ganaste y evitaste que Tony muriera")
            print() # Espacio
            print(drawings[9])
        elif fallos == maximum_attempts:
            print(msglost)
            print()
            print(f"{jugador} quieres volver a jugar")
            print()
        else:
            print()



if __name__ == '__main__':
    run()
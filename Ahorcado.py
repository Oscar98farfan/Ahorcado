import random, pyfiglet, os

maximum_attempts = 9
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

def succes(original, empty_space, simbolo):   # Simbolo: es la letra que yo coloco, original: Palabra secreta, empty_space: guiones 
    cant = original.count(simbolo)
    begin = 0
    for i in range(cant):
        pos = original.find(simbolo, begin)
        empty_space = empty_space[:pos] + simbolo + empty_space[pos+1:]
        begin = pos + 1
    return empty_space

def run():
    original, empty_space, numberWords = word_secret()
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
    fallos = -1
    while empty_space != original and fallos < maximum_attempts:
        # os.system('cls')
        print() #Espacico
        print(f"Palabra secreta es: {empty_space}")
        print() #Espacico
        print(original) # Esta es para revisar la orginal
        s = input("Cual letra quieres intentar?: ")
        print() #Espacico
        if s in original:
            empty_space = succes(original, empty_space, s)
            print(f"Bien Hecho {jugador}, la letra {s} esta {original.count(s)} veces. Sigue asi")
        # elif fallos == 7:
            # print(f"{jugador} te queda solo una oportunidad para fallar. Si no aciertas Tony Morira")
        else:
            print(f"Lo siento esa letra {s} no esta en la palabra")
            print() #Espacico
            fallos += 1
            print(f"Este es tu fallo numero {fallos}, te quedan {(maximum_attempts - fallos)}")
            print() #Espacico
            print(drawings[fallos])
        
        if empty_space == original and fallos < maximum_attempts:
            print() # Espacio
            print(msgwin)
            print() # Espacio
            print(f"Bien hecho {jugador} ganaste y evitaste que Tony muriera")
            print() # Espacio
            print(drawings[10])
        elif fallos == maximum_attempts:
            print(msglost)
        else:
            print("G")




            



if __name__ == '__main__':
    run()
#JUEGO DE AVENTURA V2

#Nivel 1

nombre = input("Hola bienvenido al mundo de los pokemon, soy el profesor oak ¿Cómo te llamas? ")

print(f"Profesor Oak: ¿{nombre}? Es un buen nombre.")

rival = input("Profesor Oak: Te presento a mi nieto, ustedes han sido rivales desde pequeños ¿Cómo se llama? ")

print(f"Profesor Oak: Ahh {rival}, claro que sí. Ahora ve a buscarme en el laboratorio.")

dentrodelab = False

laboratorio = input(f"Vas a entrar al laboratorio?").lower().strip()

if (laboratorio == "si" or laboratorio == "s") or (laboratorio == "yes" or laboratorio == "y"): 
     print("Entraste al laboratorio") 
     dentrodelab = True
elif (laboratorio == "no" or laboratorio == "n"):
     hierba =input (f"Entonces quieres ir a la Hierba alta?").lower()
     if (hierba == "si" or hierba == "s") or (hierba == "yes" or hierba == "y"): print("Hay muchos pokemon salvajes, es peligroso. Necesitas un pokemon")

     elif (hierba == "no" or hierba == "n"): print ("JAJA no. Ya entraste al laboratorio")
else:
    print("vrga responde Si o No.")

print("\nProfesor Oak: Listo, ya están ustedes dos. Ahora agarren uno de los pokémon que están en la mesa.")

pkmn1 = "Charmander"
Charmander = {
        "nivelCharmander": 5,
        "saludCharmander": 80,
        "ataqueCharmander": 12,
        "Ascuas": 20,
        "Gruñido": 1.25
}
pkmn2 = "Squirtle"
Squirtle = {
        "nivelSquirtle": 5,
        "saludSquirtle": 120,
        "ataqueSquirtle": 8,
        "Pistola Agua": 20,
        "Refugio": 1.25
}
pkmn3 = "Bulbasaur"
Bulbasaur = {
        "nivelBulbasaur": 5,
        "saludBulbasaur": 100,
        "ataqueBulbasaur": 10,
        "Látigo Cepa": 20,
        "Malicioso": 1.25
}


print(f"1. El pokémon tipo fuego: {pkmn1}")
print(f"2. El pokémon tipo agua: {pkmn2}")
print(f"3. El pokémon tipo planta: {pkmn3}")

eleccion = True


eleccion = input("Elige (1, 2, 3): ").strip()

if eleccion == "1":
        print(f"\n{nombre} ha elegido a {pkmn1}.")
        print(f"{rival}: ¿Ah sí? Entonces voy a elegir a {pkmn2}.")
        print("Profesor Oak: Buena decisión de ambos. ¡Vayan a hacer su recorrido para ser los mejores entrenadores!")
        
elif eleccion == "2":
        print(f"\n{nombre} ha elegido a {pkmn2}.")
        print(f"{rival}: ¿Ah sí? Entonces voy a elegir a {pkmn3}.")
        print("Profesor Oak: Buena decisión de ambos. ¡Vayan a hacer su recorrido para ser los mejores entrenadores!")
        
elif eleccion == "3":
        print(f"\n{nombre} ha elegido a {pkmn3}.")
        print(f"{rival}: ¿Ah sí? Entonces voy a elegir a {pkmn1}.")
        print("Profesor Oak: Buena decisión de ambos. ¡Vayan a hacer su recorrido para ser los mejores entrenadores!")
        
else:
        print("Opción inválida. Por favor elige 1, 2 o 3.")

#nivel 2 
pkmnSalvaje1 = "Pidgey"
Pidgey = {
    "nivelPidgey": 3,
    "saludPidgey": 60,
    "ataquePidgey": 6,
    "Placaje": 10,
}

if eleccion == "1":
       print(f"{nombre} ha salido a la ruta 1 con {pkmn1}. y entrando a la hierba alta se encuentra con un {pkmnSalvaje1} salvaje.")
       print(f"{nombre} quieres luchar o huir de {pkmnSalvaje1}?.")
       luchar = input("¿Qué deseas hacer? ").lower().strip()
       if (luchar == "luchar" or luchar == "l") or (luchar == "fight" or luchar == "f"):
        print(f"{nombre} ha decidido luchar contra {pkmnSalvaje1}.")
        #mecanica de batalla-------------------------------------------------------------------------------------
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn1} ----------------- Nivel: {Charmander['nivelCharmander']}//////// HP: {Charmander['saludCharmander']}")
        ataque = input(f"1. Ascuas ///daño: {Charmander['Ascuas']} \n2. Gruñido ///Baja el ataque del oponente \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Charmander["ataqueCharmander"] += Charmander["Ascuas"]
                print(f"{pkmn1} ha usado Ascuas y le ha hecho {Charmander['Ascuas']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Charmander['Ascuas']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn1} ha usado Gruñido y ha bajado el ataque de {pkmnSalvaje1}.")
                Pidgey['ataquePidgey'] /= Charmander['Gruñido']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['ataquePidgey']} de ataque.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.") 
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn1}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn1}.")
              Charmander['saludCharmander'] -= Pidgey['Placaje']
              print(f"{pkmn1} ahora tiene {Charmander['saludCharmander']} de HP.")
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn1} ----------------- Nivel: {Charmander['nivelCharmander']}//////// HP: {Charmander['saludCharmander']}")
        ataque = input(f"1. Ascuas ///daño: {Charmander['Ascuas']} \n2. Gruñido ///Baja el ataque del oponente \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Charmander["ataqueCharmander"] += Charmander["Ascuas"]
                print(f"{pkmn1} ha usado Ascuas y le ha hecho {Charmander['Ascuas']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Charmander['Ascuas']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn1} ha usado Gruñido y ha bajado el ataque de {pkmnSalvaje1}.")
                Pidgey['ataquePidgey'] /= Charmander['Gruñido']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['ataquePidgey']} de ataque.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.") 
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn1}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn1}.")
              Charmander['saludCharmander'] -= Pidgey['Placaje']
              print(f"{pkmn1} ahora tiene {Charmander['saludCharmander']} de HP.")
              #bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn1} ----------------- Nivel: {Charmander['nivelCharmander']}//////// HP: {Charmander['saludCharmander']}")
        ataque = input(f"1. Ascuas ///daño: {Charmander['Ascuas']} \n2. Gruñido ///Baja el ataque del oponente \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Charmander["ataqueCharmander"] += Charmander["Ascuas"]
                print(f"{pkmn1} ha usado Ascuas y le ha hecho {Charmander['Ascuas']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Charmander['Ascuas']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn1} ha usado Gruñido y ha bajado el ataque de {pkmnSalvaje1}.")
                Pidgey['ataquePidgey'] /= Charmander['Gruñido']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['ataquePidgey']} de ataque.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.") 
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn1}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn1}.")
              Charmander['saludCharmander'] -= Pidgey['Placaje']
              print(f"{pkmn1} ahora tiene {Charmander['saludCharmander']} de HP.")
              #bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn1} ----------------- Nivel: {Charmander['nivelCharmander']}//////// HP: {Charmander['saludCharmander']}")
        ataque = input(f"1. Ascuas ///daño: {Charmander['Ascuas']} \n2. Gruñido ///Baja el ataque del oponente \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Charmander["ataqueCharmander"] += Charmander["Ascuas"]
                print(f"{pkmn1} ha usado Ascuas y le ha hecho {Charmander['Ascuas']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Charmander['Ascuas']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn1} ha usado Gruñido y ha bajado el ataque de {pkmnSalvaje1}.")
                Pidgey['ataquePidgey'] /= Charmander['Gruñido']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['ataquePidgey']} de ataque.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.") 
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn1}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn1}.")
              Charmander['saludCharmander'] -= Pidgey['Placaje']
              print(f"{pkmn1} ahora tiene {Charmander['saludCharmander']} de HP.")
              #bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn1} ----------------- Nivel: {Charmander['nivelCharmander']}//////// HP: {Charmander['saludCharmander']}")
        ataque = input(f"1. Ascuas ///daño: {Charmander['Ascuas']} \n2. Gruñido ///Baja el ataque del oponente \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Charmander["ataqueCharmander"] += Charmander["Ascuas"]
                print(f"{pkmn1} ha usado Ascuas y le ha hecho {Charmander['Ascuas']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Charmander['Ascuas']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn1} ha usado Gruñido y ha bajado el ataque de {pkmnSalvaje1}.")
                Pidgey['ataquePidgey'] /= Charmander['Gruñido']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['ataquePidgey']} de ataque.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.") 
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn1}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn1}.")
              Charmander['saludCharmander'] -= Pidgey['Placaje']
              print(f"{pkmn1} ahora tiene {Charmander['saludCharmander']} de HP.")
              #bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn1} ----------------- Nivel: {Charmander['nivelCharmander']}//////// HP: {Charmander['saludCharmander']}")
        ataque = input(f"1. Ascuas ///daño: {Charmander['Ascuas']} \n2. Gruñido ///Baja el ataque del oponente \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Charmander["ataqueCharmander"] += Charmander["Ascuas"]
                print(f"{pkmn1} ha usado Ascuas y le ha hecho {Charmander['Ascuas']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Charmander['Ascuas']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn1} ha usado Gruñido y ha bajado el ataque de {pkmnSalvaje1}.")
                Pidgey['ataquePidgey'] /= Charmander['Gruñido']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['ataquePidgey']} de ataque.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.") 
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn1}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn1}.")
              Charmander['saludCharmander'] -= Pidgey['Placaje']
              print(f"{pkmn1} ahora tiene {Charmander['saludCharmander']} de HP.")
              #bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn1} ----------------- Nivel: {Charmander['nivelCharmander']}//////// HP: {Charmander['saludCharmander']}")
        ataque = input(f"1. Ascuas ///daño: {Charmander['Ascuas']} \n2. Gruñido ///Baja el ataque del oponente \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Charmander["ataqueCharmander"] += Charmander["Ascuas"]
                print(f"{pkmn1} ha usado Ascuas y le ha hecho {Charmander['Ascuas']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Charmander['Ascuas']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn1} ha usado Gruñido y ha bajado el ataque de {pkmnSalvaje1}.")
                Pidgey['ataquePidgey'] /= Charmander['Gruñido']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['ataquePidgey']} de ataque.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.") 
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn1}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn1}.")
              Charmander['saludCharmander'] -= Pidgey['Placaje']
              print(f"{pkmn1} ahora tiene {Charmander['saludCharmander']} de HP.")
              #bucle
       elif (luchar == "huir" or luchar == "h") or (luchar == "run" or luchar == "r"):

        print(f"{nombre} ha decidido huir de {pkmnSalvaje1}.")
       else:
        print("Opción inválida. Por favor elige luchar o huir.")
        
        #--------------------------------------------------------------------------------------------------------

elif eleccion == "2":
       print(f"{nombre} ha salido a la ruta 1 con {pkmn2}. y entrando a la hierba alta se encuentra con un {pkmnSalvaje1} salvaje.")
       print(f"{nombre} quieres luchar o huir de {pkmnSalvaje1}?.")
       luchar = input("¿Qué deseas hacer? ").lower().strip()
       if (luchar == "luchar" or luchar == "l") or (luchar == "fight" or luchar == "f"):
        print(f"{nombre} ha decidido luchar contra {pkmnSalvaje1}.")
        #mecanica de batalla-------------------------------------------------------------------------------------
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn2} ----------------- Nivel: {Squirtle['nivelSquirtle']}//////// HP: {Squirtle['saludSquirtle']}")
        ataque = input(f"1. Pistola de Agua ///daño: {Squirtle['Pistola de Agua']} \n2. Refugio ///Sube la defensa del usuario \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Squirtle["ataqueSquirtle"] += Squirtle["Pistola de Agua"]
                print(f"{pkmn2} ha usado Pistola de Agua y le ha hecho {Squirtle['Pistola de Agua']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Squirtle['Pistola de Agua']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn2} ha usado Refugio y ha subido su defensa.")
                Squirtle['defensaSquirtle'] += Squirtle['Refugio']
                print(f"{pkmn2} ahora tiene {Squirtle['defensaSquirtle']} de defensa.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.") 
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn2}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn2}.")
              Squirtle['saludSquirtle'] -= Pidgey['Placaje']
              print(f"{pkmn2} ahora tiene {Squirtle['saludSquirtle']} de HP.")   
#bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn2} ----------------- Nivel: {Squirtle['nivelSquirtle']}//////// HP: {Squirtle['saludSquirtle']}")
        ataque = input(f"1. Pistola de Agua ///daño: {Squirtle['Pistola de Agua']} \n2. Refugio ///Sube la defensa del usuario \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Squirtle["ataqueSquirtle"] += Squirtle["Pistola de Agua"]
                print(f"{pkmn2} ha usado Pistola de Agua y le ha hecho {Squirtle['Pistola de Agua']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Squirtle['Pistola de Agua']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn2} ha usado Refugio y ha subido su defensa.")
                Squirtle['defensaSquirtle'] += Squirtle['Refugio']
                print(f"{pkmn2} ahora tiene {Squirtle['defensaSquirtle']} de defensa.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.") 
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn2}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn2}.")
              Squirtle['saludSquirtle'] -= Pidgey['Placaje']
              print(f"{pkmn2} ahora tiene {Squirtle['saludSquirtle']} de HP.")
#bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn2} ----------------- Nivel: {Squirtle['nivelSquirtle']}//////// HP: {Squirtle['saludSquirtle']}")
        ataque = input(f"1. Pistola de Agua ///daño: {Squirtle['Pistola de Agua']} \n2. Refugio ///Sube la defensa del usuario \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Squirtle["ataqueSquirtle"] += Squirtle["Pistola de Agua"]
                print(f"{pkmn2} ha usado Pistola de Agua y le ha hecho {Squirtle['Pistola de Agua']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Squirtle['Pistola de Agua']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn2} ha usado Refugio y ha subido su defensa.")
                Squirtle['defensaSquirtle'] += Squirtle['Refugio']
                print(f"{pkmn2} ahora tiene {Squirtle['defensaSquirtle']} de defensa.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.") 
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn2}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn2}.")
              Squirtle['saludSquirtle'] -= Pidgey['Placaje']
              print(f"{pkmn2} ahora tiene {Squirtle['saludSquirtle']} de HP.")
#bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn2} ----------------- Nivel: {Squirtle['nivelSquirtle']}//////// HP: {Squirtle['saludSquirtle']}")
        ataque = input(f"1. Pistola de Agua ///daño: {Squirtle['Pistola de Agua']} \n2. Refugio ///Sube la defensa del usuario \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Squirtle["ataqueSquirtle"] += Squirtle["Pistola de Agua"]
                print(f"{pkmn2} ha usado Pistola de Agua y le ha hecho {Squirtle['Pistola de Agua']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Squirtle['Pistola de Agua']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn2} ha usado Refugio y ha subido su defensa.")
                Squirtle['defensaSquirtle'] += Squirtle['Refugio']
                print(f"{pkmn2} ahora tiene {Squirtle['defensaSquirtle']} de defensa.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.") 
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn2}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn2}.")
              Squirtle['saludSquirtle'] -= Pidgey['Placaje']
              print(f"{pkmn2} ahora tiene {Squirtle['saludSquirtle']} de HP.")
#bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn2} ----------------- Nivel: {Squirtle['nivelSquirtle']}//////// HP: {Squirtle['saludSquirtle']}")
        ataque = input(f"1. Pistola de Agua ///daño: {Squirtle['Pistola de Agua']} \n2. Refugio ///Sube la defensa del usuario \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Squirtle["ataqueSquirtle"] += Squirtle["Pistola de Agua"]
                print(f"{pkmn2} ha usado Pistola de Agua y le ha hecho {Squirtle['Pistola de Agua']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Squirtle['Pistola de Agua']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn2} ha usado Refugio y ha subido su defensa.")
                Squirtle['defensaSquirtle'] += Squirtle['Refugio']
                print(f"{pkmn2} ahora tiene {Squirtle['defensaSquirtle']} de defensa.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.") 
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn2}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn2}.")
              Squirtle['saludSquirtle'] -= Pidgey['Placaje']
              print(f"{pkmn2} ahora tiene {Squirtle['saludSquirtle']} de HP.")
#bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn2} ----------------- Nivel: {Squirtle['nivelSquirtle']}//////// HP: {Squirtle['saludSquirtle']}")
        ataque = input(f"1. Pistola de Agua ///daño: {Squirtle['Pistola de Agua']} \n2. Refugio ///Sube la defensa del usuario \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Squirtle["ataqueSquirtle"] += Squirtle["Pistola de Agua"]
                print(f"{pkmn2} ha usado Pistola de Agua y le ha hecho {Squirtle['Pistola de Agua']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Squirtle['Pistola de Agua']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn2} ha usado Refugio y ha subido su defensa.")
                Squirtle['defensaSquirtle'] += Squirtle['Refugio']
                print(f"{pkmn2} ahora tiene {Squirtle['defensaSquirtle']} de defensa.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.") 
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn2}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn2}.")
              Squirtle['saludSquirtle'] -= Pidgey['Placaje']
              print(f"{pkmn2} ahora tiene {Squirtle['saludSquirtle']} de HP.")
#bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn2} ----------------- Nivel: {Squirtle['nivelSquirtle']}//////// HP: {Squirtle['saludSquirtle']}")
        ataque = input(f"1. Pistola de Agua ///daño: {Squirtle['Pistola de Agua']} \n2. Refugio ///Sube la defensa del usuario \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Squirtle["ataqueSquirtle"] += Squirtle["Pistola de Agua"]
                print(f"{pkmn2} ha usado Pistola de Agua y le ha hecho {Squirtle['Pistola de Agua']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Squirtle['Pistola de Agua']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn2} ha usado Refugio y ha subido su defensa.")
                Squirtle['defensaSquirtle'] += Squirtle['Refugio']
                print(f"{pkmn2} ahora tiene {Squirtle['defensaSquirtle']} de defensa.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.") 
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn2}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn2}.")
              Squirtle['saludSquirtle'] -= Pidgey['Placaje']
              print(f"{pkmn2} ahora tiene {Squirtle['saludSquirtle']} de HP.")
#bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn2} ----------------- Nivel: {Squirtle['nivelSquirtle']}//////// HP: {Squirtle['saludSquirtle']}")
        ataque = input(f"1. Pistola de Agua ///daño: {Squirtle['Pistola de Agua']} \n2. Refugio ///Sube la defensa del usuario \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Squirtle["ataqueSquirtle"] += Squirtle["Pistola de Agua"]
                print(f"{pkmn2} ha usado Pistola de Agua y le ha hecho {Squirtle['Pistola de Agua']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Squirtle['Pistola de Agua']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn2} ha usado Refugio y ha subido su defensa.")
                Squirtle['defensaSquirtle'] += Squirtle['Refugio']
                print(f"{pkmn2} ahora tiene {Squirtle['defensaSquirtle']} de defensa.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.") 
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn2}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn2}.")
              Squirtle['saludSquirtle'] -= Pidgey['Placaje']
              print(f"{pkmn2} ahora tiene {Squirtle['saludSquirtle']} de HP.")
#bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn2} ----------------- Nivel: {Squirtle['nivelSquirtle']}//////// HP: {Squirtle['saludSquirtle']}")
        ataque = input(f"1. Pistola de Agua ///daño: {Squirtle['Pistola de Agua']} \n2. Refugio ///Sube la defensa del usuario \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Squirtle["ataqueSquirtle"] += Squirtle["Pistola de Agua"]
                print(f"{pkmn2} ha usado Pistola de Agua y le ha hecho {Squirtle['Pistola de Agua']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Squirtle['Pistola de Agua']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn2} ha usado Refugio y ha subido su defensa.")
                Squirtle['defensaSquirtle'] += Squirtle['Refugio']
                print(f"{pkmn2} ahora tiene {Squirtle['defensaSquirtle']} de defensa.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.") 
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn2}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn2}.")
              Squirtle['saludSquirtle'] -= Pidgey['Placaje']
              print(f"{pkmn2} ahora tiene {Squirtle['saludSquirtle']} de HP.")
       elif (luchar == "huir" or luchar == "h") or (luchar == "run" or luchar == "r"):

        print(f"{nombre} ha decidido huir de {pkmnSalvaje1}.")
       else:
        print("Opción inválida. Por favor elige luchar o huir.")
        
        #--------------------------------------------------------------------------------------------------------

elif eleccion == "3":
       print(f"{nombre} ha salido a la ruta 1 con {pkmn3}. y entrando a la hierba alta se encuentra con un {pkmnSalvaje1} salvaje.")
       print(f"{nombre} quieres luchar o huir de {pkmnSalvaje1}?.")
       luchar = input("¿Qué deseas hacer? ").lower().strip()
       if (luchar == "luchar" or luchar == "l") or (luchar == "fight" or luchar == "f"):
        print(f"{nombre} ha decidido luchar contra {pkmnSalvaje1}.")
        #mecanica de batalla-------------------------------------------------------------------------------------
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn3} ----------------- Nivel: {Bulbasaur['nivelBulbasaur']}//////// HP: {Bulbasaur['saludBulbasaur']}")
        ataque = input(f"1. Látigo Cepa ///daño: {Bulbasaur['Látigo Cepa']} \n2. Malicioso ///Baja el ataque del oponente \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Bulbasaur["ataqueBulbasaur"] += Bulbasaur["Látigo Cepa"]
                print(f"{pkmn3} ha usado Látigo Cepa y le ha hecho {Bulbasaur['Látigo Cepa']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Bulbasaur['Látigo Cepa']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn3} ha usado Malicioso y ha bajado el ataque de {pkmnSalvaje1}.")
                Pidgey['ataquePidgey'] /= Bulbasaur['Malicioso']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['ataquePidgey']} de ataque.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.")
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn3}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn3}.")
              Bulbasaur['saludBulbasaur'] -= Pidgey['Placaje']
              print(f"{pkmn3} ahora tiene {Bulbasaur['saludBulbasaur']} de HP.")
#bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn3} ----------------- Nivel: {Bulbasaur['nivelBulbasaur']}//////// HP: {Bulbasaur['saludBulbasaur']}")
        ataque = input(f"1. Látigo Cepa ///daño: {Bulbasaur['Látigo Cepa']} \n2. Malicioso ///Baja el ataque del oponente \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Bulbasaur["ataqueBulbasaur"] += Bulbasaur["Látigo Cepa"]
                print(f"{pkmn3} ha usado Látigo Cepa y le ha hecho {Bulbasaur['Látigo Cepa']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Bulbasaur['Látigo Cepa']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn3} ha usado Malicioso y ha bajado el ataque de {pkmnSalvaje1}.")
                Pidgey['ataquePidgey'] /= Bulbasaur['Malicioso']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['ataquePidgey']} de ataque.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.")
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn3}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn3}.")
              Bulbasaur['saludBulbasaur'] -= Pidgey['Placaje']
              print(f"{pkmn3} ahora tiene {Bulbasaur['saludBulbasaur']} de HP.")
#bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn3} ----------------- Nivel: {Bulbasaur['nivelBulbasaur']}//////// HP: {Bulbasaur['saludBulbasaur']}")
        ataque = input(f"1. Látigo Cepa ///daño: {Bulbasaur['Látigo Cepa']} \n2. Malicioso ///Baja el ataque del oponente \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Bulbasaur["ataqueBulbasaur"] += Bulbasaur["Látigo Cepa"]
                print(f"{pkmn3} ha usado Látigo Cepa y le ha hecho {Bulbasaur['Látigo Cepa']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Bulbasaur['Látigo Cepa']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn3} ha usado Malicioso y ha bajado el ataque de {pkmnSalvaje1}.")
                Pidgey['ataquePidgey'] /= Bulbasaur['Malicioso']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['ataquePidgey']} de ataque.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.")
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn3}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn3}.")
              Bulbasaur['saludBulbasaur'] -= Pidgey['Placaje']
              print(f"{pkmn3} ahora tiene {Bulbasaur['saludBulbasaur']} de HP.")
#bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn3} ----------------- Nivel: {Bulbasaur['nivelBulbasaur']}//////// HP: {Bulbasaur['saludBulbasaur']}")
        ataque = input(f"1. Látigo Cepa ///daño: {Bulbasaur['Látigo Cepa']} \n2. Malicioso ///Baja el ataque del oponente \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Bulbasaur["ataqueBulbasaur"] += Bulbasaur["Látigo Cepa"]
                print(f"{pkmn3} ha usado Látigo Cepa y le ha hecho {Bulbasaur['Látigo Cepa']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Bulbasaur['Látigo Cepa']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn3} ha usado Malicioso y ha bajado el ataque de {pkmnSalvaje1}.")
                Pidgey['ataquePidgey'] /= Bulbasaur['Malicioso']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['ataquePidgey']} de ataque.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.")
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn3}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn3}.")
              Bulbasaur['saludBulbasaur'] -= Pidgey['Placaje']
              print(f"{pkmn3} ahora tiene {Bulbasaur['saludBulbasaur']} de HP.")
#bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn3} ----------------- Nivel: {Bulbasaur['nivelBulbasaur']}//////// HP: {Bulbasaur['saludBulbasaur']}")
        ataque = input(f"1. Látigo Cepa ///daño: {Bulbasaur['Látigo Cepa']} \n2. Malicioso ///Baja el ataque del oponente \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Bulbasaur["ataqueBulbasaur"] += Bulbasaur["Látigo Cepa"]
                print(f"{pkmn3} ha usado Látigo Cepa y le ha hecho {Bulbasaur['Látigo Cepa']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Bulbasaur['Látigo Cepa']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn3} ha usado Malicioso y ha bajado el ataque de {pkmnSalvaje1}.")
                Pidgey['ataquePidgey'] /= Bulbasaur['Malicioso']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['ataquePidgey']} de ataque.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.")
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn3}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn3}.")
              Bulbasaur['saludBulbasaur'] -= Pidgey['Placaje']
              print(f"{pkmn3} ahora tiene {Bulbasaur['saludBulbasaur']} de HP.")
#bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn3} ----------------- Nivel: {Bulbasaur['nivelBulbasaur']}//////// HP: {Bulbasaur['saludBulbasaur']}")
        ataque = input(f"1. Látigo Cepa ///daño: {Bulbasaur['Látigo Cepa']} \n2. Malicioso ///Baja el ataque del oponente \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Bulbasaur["ataqueBulbasaur"] += Bulbasaur["Látigo Cepa"]
                print(f"{pkmn3} ha usado Látigo Cepa y le ha hecho {Bulbasaur['Látigo Cepa']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Bulbasaur['Látigo Cepa']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn3} ha usado Malicioso y ha bajado el ataque de {pkmnSalvaje1}.")
                Pidgey['ataquePidgey'] /= Bulbasaur['Malicioso']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['ataquePidgey']} de ataque.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.")
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn3}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn3}.")
              Bulbasaur['saludBulbasaur'] -= Pidgey['Placaje']
              print(f"{pkmn3} ahora tiene {Bulbasaur['saludBulbasaur']} de HP.")
#bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn3} ----------------- Nivel: {Bulbasaur['nivelBulbasaur']}//////// HP: {Bulbasaur['saludBulbasaur']}")
        ataque = input(f"1. Látigo Cepa ///daño: {Bulbasaur['Látigo Cepa']} \n2. Malicioso ///Baja el ataque del oponente \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Bulbasaur["ataqueBulbasaur"] += Bulbasaur["Látigo Cepa"]
                print(f"{pkmn3} ha usado Látigo Cepa y le ha hecho {Bulbasaur['Látigo Cepa']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Bulbasaur['Látigo Cepa']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn3} ha usado Malicioso y ha bajado el ataque de {pkmnSalvaje1}.")
                Pidgey['ataquePidgey'] /= Bulbasaur['Malicioso']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['ataquePidgey']} de ataque.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.")
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn3}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn3}.")
              Bulbasaur['saludBulbasaur'] -= Pidgey['Placaje']
              print(f"{pkmn3} ahora tiene {Bulbasaur['saludBulbasaur']} de HP.")
#bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn3} ----------------- Nivel: {Bulbasaur['nivelBulbasaur']}//////// HP: {Bulbasaur['saludBulbasaur']}")
        ataque = input(f"1. Látigo Cepa ///daño: {Bulbasaur['Látigo Cepa']} \n2. Malicioso ///Baja el ataque del oponente \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Bulbasaur["ataqueBulbasaur"] += Bulbasaur["Látigo Cepa"]
                print(f"{pkmn3} ha usado Látigo Cepa y le ha hecho {Bulbasaur['Látigo Cepa']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Bulbasaur['Látigo Cepa']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn3} ha usado Malicioso y ha bajado el ataque de {pkmnSalvaje1}.")
                Pidgey['ataquePidgey'] /= Bulbasaur['Malicioso']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['ataquePidgey']} de ataque.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.")
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn3}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn3}.")
              Bulbasaur['saludBulbasaur'] -= Pidgey['Placaje']
              print(f"{pkmn3} ahora tiene {Bulbasaur['saludBulbasaur']} de HP.")
#bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn3} ----------------- Nivel: {Bulbasaur['nivelBulbasaur']}//////// HP: {Bulbasaur['saludBulbasaur']}")
        ataque = input(f"1. Látigo Cepa ///daño: {Bulbasaur['Látigo Cepa']} \n2. Malicioso ///Baja el ataque del oponente \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Bulbasaur["ataqueBulbasaur"] += Bulbasaur["Látigo Cepa"]
                print(f"{pkmn3} ha usado Látigo Cepa y le ha hecho {Bulbasaur['Látigo Cepa']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Bulbasaur['Látigo Cepa']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn3} ha usado Malicioso y ha bajado el ataque de {pkmnSalvaje1}.")
                Pidgey['ataquePidgey'] /= Bulbasaur['Malicioso']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['ataquePidgey']} de ataque.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.")
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn3}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn3}.")
              Bulbasaur['saludBulbasaur'] -= Pidgey['Placaje']
              print(f"{pkmn3} ahora tiene {Bulbasaur['saludBulbasaur']} de HP.")
#bucle
        print(f"{pkmnSalvaje1} ----------------- Nivel: {Pidgey['nivelPidgey']}//////// HP: {Pidgey['saludPidgey']}")
        print("----------------------------------------------------------------------")
        print("\n----------------------------------------------------------------------")
        print(f"{pkmn3} ----------------- Nivel: {Bulbasaur['nivelBulbasaur']}//////// HP: {Bulbasaur['saludBulbasaur']}")
        ataque = input(f"1. Látigo Cepa ///daño: {Bulbasaur['Látigo Cepa']} \n2. Malicioso ///Baja el ataque del oponente \nElige un ataque (1 o 2): ")
        print("----------------------------------------------------------------------")
        if ataque == "1":
                Bulbasaur["ataqueBulbasaur"] += Bulbasaur["Látigo Cepa"]
                print(f"{pkmn3} ha usado Látigo Cepa y le ha hecho {Bulbasaur['Látigo Cepa']} de daño a {pkmnSalvaje1}.")
                Pidgey['saludPidgey'] -= Bulbasaur['Látigo Cepa']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['saludPidgey']} de HP.")
        elif ataque == "2":
                print(f"{pkmn3} ha usado Malicioso y ha bajado el ataque de {pkmnSalvaje1}.")
                Pidgey['ataquePidgey'] /= Bulbasaur['Malicioso']
                print(f"{pkmnSalvaje1} ahora tiene {Pidgey['ataquePidgey']} de ataque.")
        else:
                print("Opción inválida. Por favor elige 1 o 2.")
        if Pidgey['saludPidgey'] <= 0:
                print(f"{pkmnSalvaje1} ha sido derrotado por {pkmn3}.")
        elif Pidgey['saludPidgey'] > 0:
              Pidgey["ataquePidgey"] += Pidgey["Placaje"]
              print(f"{pkmnSalvaje1} ha usado Placaje y le ha hecho {Pidgey['Placaje']} de daño a {pkmn3}.")
              Bulbasaur['saludBulbasaur'] -= Pidgey['Placaje']
              print(f"{pkmn3} ahora tiene {Bulbasaur['saludBulbasaur']} de HP.")
       elif (luchar == "huir" or luchar == "h") or (luchar == "run" or luchar == "r"):

        print(f"{nombre} ha decidido huir de {pkmnSalvaje1}.")
       else:
        print("Opción inválida. Por favor elige luchar o huir.")
        
        #--------------------------------------------------------------------------------------------------------
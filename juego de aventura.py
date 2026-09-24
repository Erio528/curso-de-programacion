nombre = input("Hola bienvenido al mundo de los pokemon, soy el profesor oak ¿Cómo te llamas? ")

print(f"Profesor Oak: ¿{nombre}? Es un buen nombre.")

rival = input("Profesor Oak: Te presento a mi nieto, ustedes han sido rivales desde pequeños ¿Cómo se llama? ")

print(f"Profesor Oak: Ahh {rival}, claro que sí. Ahora ve a buscarme en el laboratorio.")

dentrodelab = False

laboratorio = input("¿Vas a entrar al laboratorio? ").lower().strip()

if laboratorio in ["si", "s", "yes", "y"]:
    print("Entraste al laboratorio.")
    dentrodelab = True
elif laboratorio in ["no", "n"]:
    hierba = input("¿Entonces quieres ir a la Hierba alta? ").lower().strip()
    if hierba in ["si", "s", "yes", "y"]:
        print("Hay muchos pokémon salvajes, es peligroso. Necesitas un pokémon. Vas al laboratorio.")
        dentrodelab = True
    elif hierba in ["no", "n"]:
        print("JAJA no. Terminas entrando al laboratorio de todos modos.")
        dentrodelab = True
    else:
        print("Responde Si o No.")
else:
    print("Responde Si o No.")

print("\nProfesor Oak: Listo, ya están ustedes dos. Ahora agarren uno de los pokémon que están en la mesa.")

pkmn1 = "Charmander"
pkmn2 = "Squirtle"
pkmn3 = "Bulbasaur"

print(f"1. El pokémon tipo fuego: {pkmn1}")
print(f"2. El pokémon tipo agua: {pkmn2}")
print(f"3. El pokémon tipo planta: {pkmn3}")

while True:
    eleccion = input("Elige (1, 2, 3): ").strip()

    if eleccion == "1":
        print(f"\n{nombre} ha elegido a {pkmn1}.")
        print(f"{rival}: ¿Ah sí? Entonces voy a elegir a {pkmn2}.")
        print("Profesor Oak: Buena decisión de ambos. ¡Vayan a hacer su recorrido para ser los mejores entrenadores!")
        break
    elif eleccion == "2":
        print(f"\n{nombre} ha elegido a {pkmn2}.")
        print(f"{rival}: ¿Ah sí? Entonces voy a elegir a {pkmn3}.")
        print("Profesor Oak: Buena decisión de ambos. ¡Vayan a hacer su recorrido para ser los mejores entrenadores!")
        break
    elif eleccion == "3":
        print(f"\n{nombre} ha elegido a {pkmn3}.")
        print(f"{rival}: ¿Ah sí? Entonces voy a elegir a {pkmn1}.")
        print("Profesor Oak: Buena decisión de ambos. ¡Vayan a hacer su recorrido para ser los mejores entrenadores!")
        break
    else:
        print("Opción inválida. Por favor elige 1, 2 o 3.")
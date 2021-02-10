#!/usr/bin/python3

# imports always go at the top of your code
import requests
import json

def obtain_pokemon_image(spriteUrl):
    # Download Front Default Sprite Image
    mySpriteUrl = requests.get(spriteUrl)

    print("Image has been downloaded to current directory as: favoritePokemon.png")

    with open("/home/student/mycode/favoritePokemon.png", 'wb') as f:
        f.write(mySpriteUrl.content)

    return

def obtain_pokemon_info(whosThatPokemon,challengePart):
    #
    pokeapi = requests.get('https://pokeapi.co/api/v2/pokemon/' + whosThatPokemon).json()

    if challengePart == 0:
        print(pokeapi)

    if challengePart == 1:
        print("")
        print(f"This is the URL for Front Default Sprite: {pokeapi['sprites']['front_default']}")
        frontDefaultSpriteUrl = pokeapi['sprites']['front_default']
        obtain_pokemon_image(frontDefaultSpriteUrl)

    if challengePart == 2:
        pokemonIndexCount = len(pokeapi['game_indices'])
        print("\nPokemon : " + whosThatPokemon + " has been in " + str(pokemonIndexCount) + " indices")

    if challengePart == 3:
        print("")
        print("These are the given moves for this Pokemon: ")

        pokemonMoveCount = len(pokeapi['moves'])
       
        i = 0
        while i < pokemonMoveCount:
            print(f"   {pokeapi['moves'][i]['move']['name']}")
            i += 1

    return

def main():
    # Part 0 : Change Pokemon to Celebi
    print("<<< Going Through Part 0 >>>")

    pokemonName = "celebi"
    obtain_pokemon_info(pokemonName,0)
    print("\n\n\n")

    # Part 0 : BONUS : Send Pokemon of Choice 
    print("<<< Going Through Part 0 : BONUS ROUND >>>")

    pokemonName = input("Please enter name of your favs Pokemans: ")
    obtain_pokemon_info(pokemonName,0)
    print("\n\n\n")

    # Part 1 : Obtain front_default sprite and print to screen and obtain file
    print("<<< Going Through Part 1 including BONUS ROUND >>>")
    obtain_pokemon_info(pokemonName,1)
    print("\n\n\n")

    # Part 2 : Obtain Game Indices Count
    print("<<< Going Through Part 2 >>>")
    obtain_pokemon_info(pokemonName,2)
    print("\n\n\n")

    # Part 3 : Print the name of all the related Pokemon Moves
    print("<<< Going Through Part 2 >>>")
    obtain_pokemon_info(pokemonName,3)
    print("\n\n\n")


if __name__ == "__main__":
    main()

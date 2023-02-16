import eel
import pokebase as pb


@eel.expose
def show_pokemon(id):
    pokemon = pb.SpriteResource('pokemon', int(id))
    print(pokemon.url)
    eel.showPokemon(pokemon.url)

if __name__ == '__main__':
    eel.init('./web')
    eel.start('index.html', size=(300, 300), port=300)

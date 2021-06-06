from flask import Flask, jsonify
from GetPokemonData import GetPokemon

app = Flask(__name__)

@app.route("/")
def main():
    return ("It's working")

@app.route('/<string:pokemon>')
def getPokemon(pokemon):
    pokemon = GetPokemon(pokemon)
    return jsonify(pokemon)

if __name__ == "__main__":
    app.run(debug=True)
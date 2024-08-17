from flask import Flask, render_template, request, jsonify, abort
import keyboard
import json
import os

app = Flask(__name__)

# Carrega os dados dos jogadores do arquivo JSON
with open('jogadores.json', 'r') as f:
    jogadores = json.load(f)

# Rota dinâmica para os jogadores
@app.route('/jogador/<nome>')
def jogador(nome):
    if nome in jogadores:
        teclas = jogadores[nome]
        return render_template('jogador.html', nome=nome, teclas=teclas)
    else:
        return abort(404, description="Jogador não encontrado")

# Rota para capturar as teclas pressionadas
@app.route('/key', methods=['POST'])
def key():
    data = request.json
    key = data.get('key')
    
    # Simula a entrada da tecla no computador
    if key:
        keyboard.press_and_release(key)
        return jsonify(success=True), 200
    return jsonify(success=False), 400

if __name__ == '__main__':
    app.run(debug=True)

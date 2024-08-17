from flask import Flask, render_template, request
import keyboard

app = Flask(__name__)

# Rota para a página do jogador 1
@app.route('/jogador/1')
def jogador1():
    return render_template('jogador1.html')

# Rota para a página do jogador 2
@app.route('/jogador/2')
def jogador2():
    return render_template('jogador2.html')

# Rota para capturar as teclas pressionadas
@app.route('/key', methods=['POST'])
def key():
    data = request.json
    key = data.get('key')
    
    # Simula a entrada da tecla no computador
    if key:
        keyboard.press_and_release(key)
        return f'Key {key} pressed', 200
    return 'No key', 400

if __name__ == '__main__':
    app.run(debug=True)

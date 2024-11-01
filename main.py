from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco e obter os livros
def obter_pib_db():
    conn = sqlite3.connect('database.db')  # Conectar ao banco de dados
    cursor = conn.cursor()
    cursor.execute("SELECT id, periodo, valor FROM PIB")  # Selecionar todos os livros
    rows = cursor.fetchall()  # Obter todos os resultados
    conn.close()  # Fechar a conexão
    
    # Transformar os dados
    pibBrasil = [{'id': row[0], 'periodo': row[1], 'valor': row[2]} for row in rows]
    return pibBrasil

@app.route('/pib', methods=['GET'])
def obterPib():
    pib = obter_pib_db()  # Chamar a função que busca os dados no banco
    return jsonify(pib)

if __name__ == '__main__':
    app.run(debug=True)

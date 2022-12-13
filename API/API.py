from flask import Flask, jsonify, request
app = Flask(__name__)
pecas = [
    
    {
        'nome': 'Monitor Philco Gaming 24 165Hz',
        'cod': 7891,
        'fornecedor' : 'Amazon'
    },


    {
        'nome': 'Placa de video 3070',
        'cod': 7892,
        'fornecedor' : 'Kabum'
    },


    {
        'nome': 'Gabinete Mancer Warg',
        'cod': 7893,
        'fornecedor' : 'Pichau'
    },


    {
        'nome' : 'Processador R5 5600',
        'cod' : 7894,
        'fornecedor' : 'Aliexpress'
    },


    {
        'nome' : 'Placa Mae B450M Steel Legends',
        'cod' : 7895,
        'fornecedor' : 'Americanas'
    }


]


# Consulta Completa
@app.route('/pecas',methods=['GET'])
def mostrar_pecas():
    return jsonify(pecas)


# Consulta Por Codico
@app.route('/pecas/<int:cod>',methods=['GET'])
def cod_pecas(cod):
    for peca in pecas:
        if peca.get('cod') == cod:
            return jsonify(peca)


# Adicionar Peça
@app.route('/pecas',methods=['POST'])
def add_peca():
    nova_peca = request.get_json()
    pecas.append(nova_peca)
    return jsonify(pecas)


# Excluir Peça
@app.route('/pecas/<int:cod>',methods=['DELETE'])
def del_peca(cod):
    for indice, peca in enumerate(pecas):
        if peca.get('cod') == cod:
            del pecas[indice]
    return jsonify(pecas)


# Modificar Informações
@app.route('/pecas/<int:cod>',methods=['PUT'])
def editar_pecas(cod):
    peca_modificada = request.get_json()
    
    for indice,peca in enumerate(pecas):
        if peca.get('cod') == cod:
            pecas[indice].update(peca_modificada)
            
            return jsonify(pecas[indice])

app.run(port=7788,host='localhost',debug=True)

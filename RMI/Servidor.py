# Python Remote Objects(Biblioteca python para criação de aplicações que se comuniquem pela rede)
import Pyro4
import os.path
import json
import requests

# Decorator  que permite com que as classes/metódos abaixo sejam expostos para um acesso remoto.
@Pyro4.expose
# Criação de uma classe qualquer
class SD:
    
    def Broadcast(self, texto):
        return texto
    def Agencia(self, moeda, orcamento):
        base_real = 4.43
        #link muito util inclusive caso queira usar em tempo real o valor de qualquer moeda
        link = requests.get('http://data.fixer.io/api/latest?access_key=ad9f98211c08ae5983b119065722bbcd&symbols=' + moeda)
        if link.status_code == 200:
            dados = json.loads(link.content)
            taxa = dados['rates'][moeda]
            calculo = orcamento/base_real
            resultado = taxa * calculo
            return resultado



# SERVIDOR instancia OBJETO remoto
objeto = Pyro4.Daemon()

# SERVIDOR registra OBJETO e faz um vinculo dele em uma porta.
vinculo = objeto.register(SD)


ns = Pyro4.locateNS()
ns.register('obj',vinculo)

# Vinculo que será usado no programa CLIENTE é apresentado na tela
print('Rodando...')

# OBJETO  espera por clientes que invoquem seus metódos.
objeto.requestLoop()


import Pyro4

ns = Pyro4.locateNS()

uri = ns.lookup('obj')

#CLIENTE acessa remotamente SERVIDOR
acesso = Pyro4.Proxy(uri)

#CLIENTE referencia remotamente um ou mais métodos do OBJETO que está no SERVIDOR


print('CLIENTE 0')

print('\nEnvia mensagem para o servidor')
#Chamada do metodo
resultado_broadcast = acesso.Broadcast('Sou Cliente 0')
print(resultado_broadcast)



print('\nCotacao de moeda')
moeda = 'USD'
orcamento = 200
resultado_agencia = acesso.Agencia(moeda,orcamento)
print(moeda,resultado_agencia)

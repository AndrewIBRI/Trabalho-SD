import Pyro4

ns = Pyro4.locateNS()

uri = ns.lookup('obj')

#CLIENTE acessa remotamente SERVIDOR
acesso = Pyro4.Proxy(uri)

#CLIENTE referencia remotamente um ou mais métodos do OBJETO que está no SERVIDOR


print('CLIENTE 0')


print('\n-----------------Exercicio 1--------------------')
#Chamada do metodo
resultado_arquivo = acesso.Arquivo('arquivo.txt')

#Apresentando resultados
if (resultado_arquivo == False):
    print('Arquivo nao encontrado')
else:
    print('Arquivo encontrado')



print('\n-----------------Exercicio 2--------------------')
#Chamada do metodo
resultado_broadcast = acesso.Broadcast('Quero enviar esta mensagem para todos os clientes - Cliente 0')
print(resultado_broadcast)



print('\n-----------------Exercicio 3--------------------')
destino = 'USD'
orcamento = 200
resultado_agencia = acesso.Agencia(destino,orcamento)
print(destino,resultado_agencia)

import Pyro4

#CLIENTE acessa remotamente SERVIDOR
acesso = Pyro4.Proxy("PYRO:obj_044e4c14b87a48e4bd84eadc87adb6e2@localhost:49501")


print('CLIENTE 1')

print('-----------------Exercicio 3--------------------')
#Chamada do metodo
resultado_broadcast = acesso.Broadcast('Quero enviar esta mensagem para todos os clientes - Cliente 1')
print(resultado_broadcast)



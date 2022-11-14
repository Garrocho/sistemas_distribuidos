import rpyc

proxy = rpyc.connect('localhost', 18861, config={'allow_public_attrs': True})

objeto_arquivo = open('arquivo_teste.txt')

n_linhas = proxy.root.contador_linha(objeto_arquivo)
print('Numero de linhas no arquivo: ', n_linhas)

import rpyc

class MeuServico(rpyc.Service):
    def exposed_contador_linha(self, objeto_arquivo):
        n_linhas = len(objeto_arquivo.readlines())
        return n_linhas

from rpyc.utils.server import ThreadedServer
t = ThreadedServer(MeuServico, port=18861)
t.start()

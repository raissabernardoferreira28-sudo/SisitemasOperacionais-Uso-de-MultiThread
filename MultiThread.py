import threading
import time

# Recurso compartilhado: uma lista para armazenar resultados parciais
resultados_parciais = []

def soma_parcial(sublista):
    """
    Cada thread executará esta função sobre uma fatia dos dados.
    """
    parcial = sum(sublista)
    # Compartilhamento de recursos: adicionando à lista global
    resultados_parciais.append(parcial)

def processamento_multi_thread(dados):
    meio = len(dados) // 2
    
    # Divisão da tarefa em duas partes (fatiamento)
    parte1 = dados[:meio]
    parte2 = dados[meio:]

    # Criação de Threads: instanciando os objetos da classe Thread
    t1 = threading.Thread(target=soma_parcial, args=(parte1,))
    t2 = threading.Thread(target=soma_parcial, args=(parte2,))

    # Iniciando a execução simultânea
    t1.start()
    t2.start()

    # Sincronização: o método join() faz com que o programa principal 
    # espere as threads terminarem antes de prosseguir.
    t1.join()
    t2.join()

    return sum(resultados_parciais)

if __name__ == "__main__":
    numeros = list(range(10_000_000))
    resultados_parciais = [] # Resetando para garantir limpeza
    
    inicio = time.time()
    resultado = processamento_multi_thread(numeros)
    fim = time.time()
    
    print(f"--- Versão Multithread ---")
    print(f"Resultado: {resultado}")
    print(f"Tempo de execução: {fim - inicio:.4f} segundos")
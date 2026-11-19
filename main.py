import sys

from bfs import executar_bfs
from dfs import executar_dfs
from grafo import ler_grafo
from kruskal import executar_kruskal
from topologica import executar_topologica


def main():
    # Explica o funcionamento do programa e os argumentos esperados.
    if len(sys.argv) != 3:
        print("Uso: python main.py algoritmo arquivo.txt")
        print("Algoritmos: bfs, dfs, topologica, mst")
        return 1

    # Recebe os argumentos da linha de comando. O primerio argumento indica o algoritmo escolhido 
    # e o segundo indica o nome do arquivo contendo as arestas do grafo.
    algoritmo = sys.argv[1].lower()
    arquivo = sys.argv[2]

    # Verifica se o algoritmo escolhido está dentro das opções possíveis.
    # Se não estiver, exibe uma mensagem de erro e encerra o programa.
    if algoritmo not in ("bfs", "dfs", "topologica", "mst"):
        print("Algoritmo inválido. Escolha: bfs, dfs, topologica ou mst.")
        return 1

    # Tenta executar o algoritmo escolhido. Se ocorrer algum erro, captura a exceção e exibe uma mensagem de erro.
    try:
        if algoritmo == "bfs":
            grafo = ler_grafo(arquivo)
            if not grafo:
                raise ValueError("O arquivo do grafo está vazio.")

            executar_bfs(grafo)

        if algoritmo == "dfs":
            grafo = ler_grafo(arquivo)
            if not grafo:
                raise ValueError("O arquivo do grafo está vazio.")

            executar_dfs(grafo)

        if algoritmo == "topologica":
            grafo = ler_grafo(arquivo, orientado=True)
            if not grafo:
                raise ValueError("O arquivo do grafo está vazio.")
            
            executar_topologica(grafo)

        if algoritmo == "mst":
            executar_kruskal(arquivo)

    except (OSError, ValueError) as erro:
        print(f"Erro: {erro}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

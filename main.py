import sys

from bfs import executar_bfs
from grafo import ler_grafo
from kruskal import executar_kruskal


def main():
    if len(sys.argv) != 3:
        print("Uso: python main.py algoritmo arquivo.txt")
        print("Algoritmos: bfs, dfs, topologica, mst")
        return 1

    algoritmo = sys.argv[1].lower()
    arquivo = sys.argv[2]

    if algoritmo not in ("bfs", "dfs", "topologica", "mst"):
        print("Algoritmo inválido. Escolha: bfs, dfs, topologica ou mst.")
        return 1

    try:
        if algoritmo == "bfs":
            grafo = ler_grafo(arquivo)
            if not grafo:
                raise ValueError("O arquivo do grafo está vazio.")

            executar_bfs(grafo)

        if algoritmo == "dfs":
            print("DFS ainda não implementado.")

        if algoritmo == "topologica":
            print("Ordenação topológica ainda não implementada.")

        if algoritmo == "mst":
            executar_kruskal(arquivo)

    except (OSError, ValueError) as erro:
        print(f"Erro: {erro}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

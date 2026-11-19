
"""Algoritmo de Kruskal para árvore geradora mínima."""

from grafo import ler_grafo


def kruskal(grafo):
    """Calcula a árvore ou floresta geradora mínima."""

    pai = {vertice: vertice for vertice in grafo}
    tamanho = {vertice: 1 for vertice in grafo}

    def encontrar(vertice):
        """Encontra o representante do conjunto de um vértice."""
        if pai[vertice] != vertice:
            pai[vertice] = encontrar(pai[vertice])
        return pai[vertice]

    def unir(u, v):
        """Une dois conjuntos, se forem diferentes."""
        raiz_u = encontrar(u)
        raiz_v = encontrar(v)

        if raiz_u == raiz_v:
            return False

        if tamanho[raiz_u] < tamanho[raiz_v]:
            raiz_u, raiz_v = raiz_v, raiz_u

        pai[raiz_v] = raiz_u
        tamanho[raiz_u] += tamanho[raiz_v]
        return True

    arestas = []

    for origem, vizinhos in grafo.items():
        for destino, peso in vizinhos.items():
            if origem < destino:
                arestas.append((peso, origem, destino))

    arestas.sort()

    selecionadas = []
    peso_total = 0.0

    for peso, origem, destino in arestas:
        if unir(origem, destino):
            selecionadas.append((origem, destino, peso))
            peso_total += peso

    componentes = len({encontrar(v) for v in grafo})

    return selecionadas, peso_total, componentes


def executar_kruskal(arquivo):
    """Lê o arquivo e apresenta o resultado."""
    grafo = ler_grafo(arquivo)

    selecionadas, peso_total, componentes = kruskal(grafo)

    print("\n=== ALGORITMO DE KRUSKAL ===")
    print(f"Vértices: {len(grafo)}")
    print(f"Arestas selecionadas: {len(selecionadas)}")

    print("\nArestas da árvore/floresta geradora mínima:")
    for origem, destino, peso in selecionadas:
        print(f"{origem} -- {destino} | peso: {peso:.2f}")

    print(f"\nPeso total: {peso_total:.2f}")
    print(f"Componentes conexos: {componentes}")

    if componentes == 1 and grafo:
        print("Resultado: árvore geradora mínima.")
    elif componentes > 1:
        print("Resultado: floresta geradora mínima.")
    else:
        print("Resultado: grafo vazio.")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Uso: py kruskal.py dados/teste_pequeno.txt")
        sys.exit(1)

    executar_kruskal(sys.argv[1])

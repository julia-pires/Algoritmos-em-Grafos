"""Leitura e representações de grafos não orientados e ponderados."""


def ler_grafo(arquivo, orientado=False):
    
    """Lê arestas 'origem destino peso' e retorna lista de adjacência por nome."""
    
    # Inicializa o grafo como um dicionário de dicionários. 
    # "grafo" é o dicionário externo. Possui como chaves os nomes dos vértices e como valores os dicionários internos.
    # Cada dicionário interno representa a lista de adjascência do vértice, possuindo como chaves os nomes dos vértices 
    # vizinhos e como valores os pesos das arestas.
    grafo = {}
    with open(arquivo, encoding="utf-8-sig") as entrada:
        for numero, linha in enumerate(entrada, start=1):
            campos = linha.split("#", 1)[0].split()
            if not campos:
                continue
            if len(campos) == 1:
                grafo.setdefault(campos[0], {})
                continue
            if len(campos) != 3:
                raise ValueError(f"Linha {numero}: use o padrão origem destino peso.")
            origem, destino, texto_peso = campos
            try:
                peso = float(texto_peso.replace(",", "."))
            except ValueError as erro:
                raise ValueError(f"Linha {numero}: peso inválido.") from erro
            grafo.setdefault(origem, {})[destino] = peso
            grafo.setdefault(destino, {})
            if not orientado:
                grafo[destino][origem] = peso
    return grafo


def mapear_vertices(grafo):
    """Cria dicionários nome->índice e índice->nome, em ordem alfabética."""
    nomes = sorted(grafo)
    nome_para_indice = {nome: indice for indice, nome in enumerate(nomes)}
    indice_para_nome = {indice: nome for indice, nome in enumerate(nomes)}
    return nome_para_indice, indice_para_nome


def lista_adjacencia_indices(grafo, nome_para_indice):
    """Converte a lista por nomes para uma lista indexada por inteiros."""
    lista = [[] for _ in range(len(nome_para_indice))]
    for origem, vizinhos in grafo.items():
        i = nome_para_indice[origem]
        lista[i] = sorted(
            ((nome_para_indice[destino], peso) for destino, peso in vizinhos.items()),
            key=lambda par: par[0],
        )
    return lista


def matriz_adjacencia(lista):
    """Gera matriz ponderada: None = sem aresta; número = peso da aresta."""
    n = len(lista)
    matriz = [[None for _ in range(n)] for _ in range(n)]
    for origem, vizinhos in enumerate(lista):
        for destino, peso in vizinhos:
            matriz[origem][destino] = peso
    return matriz


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: python grafo.py arquivo.txt")
        sys.exit(1)
    grafo = ler_grafo(sys.argv[1])
    nomes_indices, indices_nomes = mapear_vertices(grafo)
    lista = lista_adjacencia_indices(grafo, nomes_indices)
    matriz = matriz_adjacencia(lista)
    print("Mapeamento nome -> índice:")
    for nome, indice in nomes_indices.items():
        print(f"  {nome} -> {indice}")
    print("\nLista de adjacência (índice: [(vizinho, peso), ...]):")
    for i, vizinhos in enumerate(lista):
        print(f"  {i} ({indices_nomes[i]}): {vizinhos}")
    print("\nMatriz de adjacência (None = sem aresta):")
    for linha in matriz:
        print("  ", linha)

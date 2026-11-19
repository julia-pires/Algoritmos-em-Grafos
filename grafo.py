def ler_grafo(arquivo, orientado=False):
    """Lê arestas 'origem destino peso' e retorna lista de
    adjacência por nome."""

    # cada vértice aponta para um dicionário de vizinhos e pesos.
    grafo = {}

    with open(arquivo, encoding="utf-8") as entrada:
        for numero, linha in enumerate(entrada, start=1):
            # ignora comentários e linhas vazias.
            campos = linha.split("#", 1)[0].split()
            if not campos:
                continue

            # um único campo cadastra um vértice sem declarar arestas.
            if len(campos) == 1:
                grafo.setdefault(campos[0], {})
                continue

            # valida origem, destino e peso antes de cadastrar a aresta.
            if len(campos) != 3:
                raise ValueError(f"Linha {numero}: use o padrão origem destino peso.")
            origem, destino, texto_peso = campos

            try:
                peso = float(texto_peso)
            except ValueError as erro:
                raise ValueError(f"Linha {numero}: peso inválido.") from erro

            # cadastra os dois vértices e, se o grafo for não orientado,
            # registra a aresta também no sentido inverso.
            grafo.setdefault(origem, {})[destino] = peso
            grafo.setdefault(destino, {})

            if not orientado:
                grafo[destino][origem] = peso

    return grafo


def mapear_vertices(grafo):
    """Cria dicionários nome->índice e índice->nome, em ordem alfabética."""

    # atribui índices a partir de zero na ordem dos identificadores.
    nomes = sorted(grafo)
    nome_para_indice = {}
    indice_para_nome = {}

    for indice, nome in enumerate(nomes):
        nome_para_indice[nome] = indice
        indice_para_nome[indice] = nome

    return nome_para_indice, indice_para_nome


def lista_adjacencia_indices(grafo, nome_para_indice):
    """Converte a lista por nomes para uma lista indexada por inteiros."""

    # cria uma lista de vizinhos independente para cada vértice.
    lista = []
    for _ in range(len(nome_para_indice)):
        lista.append([])
    # para cada origem, guarda os pares (índice do vizinho, peso) em ordem de índice.
    for origem, vizinhos in grafo.items():

        i = nome_para_indice[origem]
        vizinhos_indexados = []
        for destino, peso in vizinhos.items():
            indice_destino = nome_para_indice[destino]
            vizinhos_indexados.append((indice_destino, peso))

        lista[i] = sorted(vizinhos_indexados, key=lambda par: par[0])

    return lista


def matriz_adjacencia(lista):
    """Gera matriz ponderada: None = sem aresta; número = peso da aresta."""

    n = len(lista)
    matriz = []
    for _ in range(n):
        linha = []
        for _ in range(n):
            linha.append(None)
        matriz.append(linha)

    # cada linha representa uma origem e cada coluna, um destino.
    for origem, vizinhos in enumerate(lista):
        for destino, peso in vizinhos:
            matriz[origem][destino] = peso

    return matriz


# mostra as representações do grafo quando o arquivo é executado diretamente.
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
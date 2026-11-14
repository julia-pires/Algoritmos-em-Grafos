"""Leitura e representação do grafo."""

def ler_grafo(arquivo):
    """Lê linhas 'origem destino peso' de um grafo não orientado.

    Uma linha com apenas um nome declara um vértice isolado.
    Os pesos são preservados, mas não são usados pelo BFS.
    """
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
                raise ValueError(f"Linha {numero}: use origem destino peso.")
            origem, destino, texto_peso = campos
            try:
                peso = float(texto_peso.replace(",", "."))
            except ValueError as erro:
                raise ValueError(f"Linha {numero}: peso inválido.") from erro
            grafo.setdefault(origem, {})[destino] = peso
            grafo.setdefault(destino, {})[origem] = peso
    return grafo

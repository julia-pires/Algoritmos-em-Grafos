"""Busca em largura em um grafo representado por lista de adjacência."""

def bfs(grafo, origem):
    """Retorna distância em arestas e predecessor para cada vértice.

    None indica um vértice inalcançável ou a ausência de predecessor.
    Os vizinhos são examinados em ordem crescente de identificador.
    """
    if origem not in grafo:
        raise ValueError(f"Vértice de origem inexistente: {origem}")

    distancia = {vertice: None for vertice in grafo}
    predecessor = {vertice: None for vertice in grafo}
    distancia[origem] = 0
    fila = [origem]
    inicio = 0

    while inicio < len(fila):
        atual = fila[inicio]
        inicio += 1
        for vizinho in sorted(grafo[atual]):
            if distancia[vizinho] is None:
                # Marcar na entrada da fila evita visitar novamente um ciclo.
                distancia[vizinho] = distancia[atual] + 1
                predecessor[vizinho] = atual
                fila.append(vizinho)

    return distancia, predecessor


def reconstruir_caminho(predecessor, origem, destino):
    """Retorna o caminho da origem ao destino, ou [] se não houver caminho.

    Use o mapa de predecessores produzido pelo BFS a partir dessa origem.
    """
    if origem not in predecessor or destino not in predecessor:
        raise ValueError("Origem ou destino inexistente no resultado do BFS.")

    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        if atual == origem:
            caminho.reverse()
            return caminho
        atual = predecessor[atual]
    return []


def executar_bfs(grafo):
    """Executa o BFS no grafo conectado a partir do menor identificador."""
    origem = min(grafo)
    distancia, predecessor = bfs(grafo, origem)

    print(f"\nOrigem: {origem}")
    exibir_tabela(distancia, predecessor)
    for destino in sorted(grafo):
        caminho = reconstruir_caminho(predecessor, origem, destino)
        exibir_caminho(caminho)


def exibir_tabela(distancia, predecessor):
    """Mostra a distância e o predecessor de cada vértice."""
    print(f"{'Vértice':<12}{'Distância':<12}Predecessor")
    for vertice in sorted(distancia):
        valor = distancia[vertice]
        texto = str(valor) if valor is not None else "INF"
        print(f"{vertice:<12}{texto:<12}{predecessor[vertice] or 'NIL'}")


def exibir_caminho(caminho):
    """Mostra o caminho reconstruído e sua quantidade de arestas."""
    if not caminho:
        print("\nNão existe caminho entre a origem e o destino.")
        return

    print("\nCaminho: " + " -> ".join(caminho))
    print(f"Distância: {len(caminho) - 1} arestas")

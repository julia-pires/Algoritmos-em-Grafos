def bfs(grafo, origem):
    """Retorna distância em arestas e predecessor para cada vértice.
    None indica um vértice inalcançável ou a ausência de predecessor.
    Os vizinhos são examinados em ordem crescente de identificador.
    """

    # verifica se a origem informada pertence ao grafo.
    if origem not in grafo:
        # interrompe a busca se a origem n for valida
        raise ValueError(f"Vértice de origem inexistente: {origem}")

    # inicializa as distâncias com none 
    # para indicar vértices ainda não descobertos.
    distancia = {vertice: None for vertice in grafo}
    
    # inicializa os predecessores com none 
    # até que a busca descubra como chegar a cada vértice.
    predecessor = {vertice: None for vertice in grafo}
    
    distancia[origem] = 0
    fila = [origem] # origem como primeiro vértice a processar
    inicio = 0 # aponta para o primeiro item da fila ainda não processado.

    # continua enquanto houver vértices aguardando processamento na fila.
    while inicio < len(fila):
        # Obtém o próximo vértice na ordem em que entrou na fila.
        atual = fila[inicio]
        inicio += 1

        # percorre os vizinhos em ordem crescente 
        # de identificador para fixar o desempate.
        for vizinho in sorted(grafo[atual]):

            # usa a distância None para identificar 
            # um vizinho ainda não descoberto.
            if distancia[vizinho] is None:
                # marca o vizinho antes de enfileirá-lo 
                # e soma uma aresta à distância do atual.
                distancia[vizinho] = distancia[atual] + 1
                # registra o vértice atual como o 
                # primeiro pelo qual o vizinho foi descoberto.
                predecessor[vizinho] = atual
                # adiciona o vizinho ao fim da fila 
                # para explorar suas arestas depois.
                fila.append(vizinho)

    return distancia, predecessor


def reconstruir_caminho(predecessor, origem, destino):
    """Retorna o caminho da origem ao destino,
    ou [] se não houver caminho.
    Use o mapa de predecessores produzido pelo BFS
    a partir dessa origem.
    """

    # confere se a origem e o destino constam no resultado da busca.
    if origem not in predecessor or destino not in predecessor:
        raise ValueError("Origem ou destino inexistente no resultado do BFS.")

    caminho = []
    atual = destino
    # Começa pelo destino e segue os predecessores 
    # em sentido contrário ao caminho.

    # continua enquanto houver um vértice na cadeia de predecessores.
    while atual is not None:
        # adiciona o vértice atual na seq percorrida.
        caminho.append(atual)
        # verifica se a cadeia chegou na origem desejada.
        if atual == origem:
            # inverte a lista para colocar a origem antes do destino.
            caminho.reverse()
            # devolve o caminho completo em ordem de percurso.
            return caminho
        # volta para o vértice pelo qual o atual foi descoberto.
        atual = predecessor[atual]

    # eevolve uma lista vazia se a cadeia terminou sem chegar à origem.
    return []


def executar_bfs(grafo):
    """Executa o BFS no grafo conectado a partir do menor identificador."""

    # escolhe como origem o vértice de menor identificador.
    origem = min(grafo)
    distancia, predecessor = bfs(grafo, origem)

    print(f"\nOrigem: {origem}")
    exibir_tabela(distancia, predecessor)

    # percorre os possíveis destinos em ordem crescente de identificador.
    for destino in sorted(grafo):
        # recupera o caminho da origem ao destino atual.
        caminho = reconstruir_caminho(predecessor, origem, destino)
        # mostra o caminho recuperado ou informa que ele não existe.
        exibir_caminho(caminho)


def exibir_tabela(distancia, predecessor):
    """Mostra a distância e o predecessor de cada vértice."""

    print(f"{'Vértice':<12}{'Distância':<12}Predecessor")

    # percorre os vértices em ordem crescente de identificador.
    for vertice in sorted(distancia):
        # dist. registrada para o vértice atual.
        valor = distancia[vertice]
        # converte a distância para texto ou usa INF se o vértice é inalcançável.
        texto = str(valor) if valor is not None else "INF"
        # exibe o vértice, a distância e o predecessor, usando NIL quando ele está ausente.
        print(f"{vertice:<12}{texto:<12}{predecessor[vertice] or 'NIL'}")


def exibir_caminho(caminho):
    """Mostra o caminho reconstruído e sua quantidade de arestas."""

    # verifica se a reconstrução devolveu uma lista vazia.
    if not caminho:
        print("\nNão existe caminho entre a origem e o destino.")
        return

    # mostra a sequência de vértices separados por setas.
    print("\nCaminho: " + " -> ".join(caminho))
    # conta as arestas do caminho subtraindo um da quantidade de vértices.
    print(f"Distância: {len(caminho) - 1} arestas")

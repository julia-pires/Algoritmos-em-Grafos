from dataclasses import dataclass, field
from typing import Dict, List

# Define a estrutura de uma aresta. Contém o vértice de origem, o vértice de destino e peso da aresta.
@dataclass
class Aresta:
  origem: str
  destino: str
  peso: float

# Define a estrutura de um vértice. Contém o ID do vértice, cor, pai, tempos de descoberta e finalização, e suas arestas.
@dataclass
class Vertice:
  id: str
  cor: str = "Branco"
  pai: str = None
  descoberto: int = 0
  finalizado: int = 0
  arestas: List[Aresta] = field(default_factory=list)

# Converte o grafo lido em um dicionário de Vertice.
def construir_vertices(grafo: Dict[str, Dict[str, float]]) -> Dict[str, Vertice]:
    vertices = {id: Vertice(id=id) for id in sorted(grafo)}
    
    # Cria uma aresta para cada vizinho de cada vértice, em ordem crescente.
    for origem, vizinhos in grafo.items():
        for destino, peso in sorted(vizinhos.items()):
            vertices[origem].arestas.append(Aresta(origem=origem, destino=destino, peso=peso))
    return vertices

# Inicializa a ordenação topológica
def ordenacao_topologica(grafo: Dict[str, Vertice]):

    # Define a cor de todos os vértices como "Branco" e o pai como None, indicando que ainda não foram visitados.
    for u in grafo.values():
        u.cor = "Branco"
        u.pai = None

    # Inicializa o temporizador, a lista de vértices finalizados e a lista de ciclos encontrados.
    tempo = [0]
    finalizados = []
    ciclos = []

    # Percorre todos os vértices do grafo. Cada vértice branco inicia uma nova árvore de busca em profundidade.
    for u in grafo.values():
        if u.cor == "Branco":
            topologica_visita(grafo, u, tempo, finalizados, ciclos)

    # Os vértices foram guardados na ordem em que terminaram. A ordem topológica é a ordem inversa de finalização.
    finalizados.reverse()

    return finalizados, ciclos

#Iniciando a visita DFS a partir de um vértice 'u'.
def topologica_visita(grafo: Dict[str, Vertice], u: Vertice, tempo: List[int], finalizados: List[str], ciclos: List[str]) -> None:
    tempo[0] += 1
    u.descoberto = tempo[0]
    u.cor = "Cinza"

    # Explora cada vizinho conectado pelas arestas do vértice 'u'
    for aresta in u.arestas:
        v = grafo[aresta.destino]
        if v.cor == "Branco":
            v.pai = u.id
            topologica_visita(grafo, v, tempo, finalizados, ciclos)

        # Se o vizinho já está em exploração (Cinza), encontramos uma aresta de retorno. Como o grafo é orientado,
        # não existe exceção para o pai de 'u': qualquer aresta para um vértice Cinza forma um ciclo.
        elif v.cor == "Cinza":
            ciclos.append(f"{u.id} -> {v.id}")

    # Marca o vértice 'u' como finalizado. Todos os seus vizinhos já foram explorados, então 'u' deve vir antes deles na ordem.
    u.cor = "Preto"
    tempo[0] += 1
    u.finalizado = tempo[0]
    finalizados.append(u.id)


# Executa a ordenação topológica no grafo orientado lido por ler_grafo e imprime os resultados.
def executar_topologica(grafo_lido: Dict[str, Dict[str, float]]) -> None:
    grafo = construir_vertices(grafo_lido)
    ordem, ciclos = ordenacao_topologica(grafo)

    for v_id, v in grafo.items():
        print(
            f"Vértice: {v_id} | Cor: {v.cor} | Pai: {v.pai} | "
            f"Descoberto: {v.descoberto} | Finalizado: {v.finalizado}"
        )

    # Se houver ciclo, o grafo não é um DAG e não existe ordenação topológica.
    if ciclos:
        print("\nO grafo possui ciclo(s). Não existe ordenação topológica. Arestas de retorno:")
        for c in ciclos:
            print(f"  {c}")
    else:
        print("\nOrdenação topológica:")
        print("  " + " -> ".join(ordem))
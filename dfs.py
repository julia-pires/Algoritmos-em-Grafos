from dataclasses import dataclass, field
from typing import Dict, List

# Define a estrutura de uma aresta. Contém o vértice de origem, o vértice de destino e peso da aresta.
@dataclass
class Aresta:
  origem: str
  destino: str
  peso: float

# Define a estrutura de um vértice. Contém o ID do vértice, cor, pai, tempos de descoberta e finalização, e componente.
@dataclass
class Vertice:
  id: str
  cor: str = "Branco"
  pai: str = None
  descoberto: int = 0
  finalizado: int = 0
  componente: int = 0
  arestas: List[Aresta] = field(default_factory=list)

# Converte o grafo lido por ler_grafo (dicionário de dicionários) em um dicionário de Vertice.
def construir_vertices(grafo: Dict[str, Dict[str, float]]) -> Dict[str, Vertice]:
    vertices = {id: Vertice(id=id) for id in sorted(grafo)}
    
    # Cria uma aresta para cada vizinho de cada vértice, em ordem crescente.
    for origem, vizinhos in grafo.items():
        for destino, peso in sorted(vizinhos.items()):
            vertices[origem].arestas.append(Aresta(origem=origem, destino=destino, peso=peso))
    return vertices

# Inicializa o DFS
def dfs(grafo: Dict[str, Vertice]):

    # Define a cor de todos os vértices como "Branco" e o pai como None, indicando que ainda não foram visitados.
    for u in grafo.values():
        u.cor = "Branco"
        u.pai = None

    # Inicializa o temporizador, o contador de componentes e a lista de ciclos encontrados.
    tempo = [0]
    componentes = 0
    ciclos = []

    # Percorre todos os vértices do grafo. Cada vértice branco inicia um novo componente conexo.
    for u in grafo.values():
        if u.cor == "Branco":
            componentes += 1
            dfs_visita(grafo, u, tempo, componentes, ciclos)

    return componentes, ciclos

#Iniciando a visita DFS a partir de um vértice 'u'.
def dfs_visita(grafo: Dict[str, Vertice], u: Vertice, tempo: List[int], componente: int, ciclos: List[str]) -> None:
    tempo[0] += 1
    u.descoberto = tempo[0]
    u.cor = "Cinza"
    u.componente = componente

    # Explora cada vizinho conectado pelas arestas do vértice 'u'
    for aresta in u.arestas:
        v = grafo[aresta.destino]
        if v.cor == "Branco":
            v.pai = u.id
            dfs_visita(grafo, v, tempo, componente, ciclos)

        # Se o vizinho já está em exploração (Cinza) e não é o pai de 'u', encontramos um ciclo.
        elif v.cor == "Cinza" and v.id != u.pai:
            ciclos.append(f"{u.id} -> {v.id}")

    # Marca o vértice 'u' como finalizado. Todos os seus vizinhos já foram explorados.
    u.cor = "Preto"
    tempo[0] += 1
    u.finalizado = tempo[0]


# Executa o algoritmo DFS no grafo lido por ler_grafo e imprime os resultados.
def executar_dfs(grafo_lido: Dict[str, Dict[str, float]]) -> None:
    grafo = construir_vertices(grafo_lido)
    componentes, ciclos = dfs(grafo)

    for v_id, v in grafo.items():
        print(
            f"Vértice: {v_id} | Cor: {v.cor} | Pai: {v.pai} | "
            f"Descoberto: {v.descoberto} | Finalizado: {v.finalizado} | "
            f"Componente: {v.componente}"
        )

    print(f"\nComponentes conexos: {componentes}")

    if ciclos:
        print("O grafo possui ciclo(s). Arestas de retorno:")
        for c in ciclos:
            print(f"  {c}")
    else:
        print("O grafo não possui ciclos.")
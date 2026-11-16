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

# Define um dicionário de vértices, cujo conjunto chave: valor é é o ID do vértice e o Vertice correspondente.
grafo: Dict[str, Vertice] = {}

# Realiza a leitura do arquivo "arestas.txt" e insere os vértices e arestas no dicionário "grafo".
with open("arestas.txt", "r") as arquivo:
  
    # Inicializa a leitura do arquivo, pulando a primeira linha.
    next(arquivo)
    for linha in arquivo:
        origem, destino, peso_str = linha.strip().split()
        peso = float(peso_str)

        # Verifica se os vértices de origem e destino já existem no dicionário "grafo". Se não, insere novos vértices no dicionário.
        if origem not in grafo:
            grafo[origem] = Vertice(id=origem)
        if destino not in grafo:
            grafo[destino] = Vertice(id=destino)

        # Verifica se as arestas já existem para os vértices de origem e destino. Se não, insere novas arestas para cada um desses vértices.
        # Considera-se que o grafo é não direcionado, então adiciona-se a aresta em ambos os vértices.
        if not any(aresta.destino == destino for aresta in grafo[origem].arestas):
            grafo[origem].arestas.append(
            Aresta(origem=origem, destino=destino, peso=peso)
        )
        if not any(aresta.destino == origem for aresta in grafo[destino].arestas):
            grafo[destino].arestas.append(
            Aresta(origem=destino, destino=origem, peso=peso)
        )

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
    u.cor = "Cinza"  # Vértice descoberto e em exploração
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


# Executa o algoritmo DFS no grafo e imprime os resultados.
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
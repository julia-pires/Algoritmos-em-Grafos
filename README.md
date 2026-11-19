# Algoritmos-em-Grafos

Trabalho de Algoritmos em Grafos — Ciência da Computação, UEM.


```console
python main.py bfs dados/teste_pequeno.txt
python main.py topologica dados/teste_topologica.txt
```

Formato: `python main.py algoritmo arquivo.txt`.
O BFS escolhe o menor identificador como origem e mostra a tabela e os caminhos
para todos os vértices. Consideramos que o grafo é conectado; uma única busca
alcança todos os vértices. As distâncias e os caminhos partem da mesma origem.

Algoritmos aceitos: `bfs`, `dfs`, `topologica` e `mst`.

### Arquivos

- `main.py`: entrada do programa, com um `if` para cada algoritmo.
- `grafo.py`: leitura do grafo, compartilhada pelos algoritmos.
- `bfs.py`: busca em largura, reconstrução e exibição dos resultados.
- `topologica.py`: ordenação topológica, feita com uma busca em profundidade.
- `dados/`: grafos de teste e gabaritos.
- `test_bfs.py`: testes automáticos do BFS.

### Entrada

Grafo não orientado, com uma aresta por linha no formato `origem destino peso`:

```text
M057 M058 1.00
M058 M059 0.75
```

Os pesos aceitam ponto ou vírgula. Uma linha com apenas um identificador
representa um vértice isolado. Linhas vazias e comentários com `#` são ignorados.
A representação é uma lista de adjacência: `grafo[origem][destino] = peso`.

Na ordenação topológica o grafo é orientado: a linha `origem destino peso` vale
só para a aresta `origem -> destino`, e o grafo precisa ser acíclico.
Nos outros algoritmos ele continua não orientado.

### Funções

- `ler_grafo`: lê o arquivo e monta a lista de adjacência. Com `orientado=True`,
  guarda cada aresta só no sentido origem -> destino.
- `bfs`: calcula as distâncias e os predecessores usando uma fila.
- `executar_bfs`: escolhe a origem, chama o BFS e mostra os resultados.
- `reconstruir_caminho`: segue os predecessores e inverte a sequência.
- `exibir_tabela`: imprime as distâncias e os predecessores.
- `exibir_caminho`: imprime o caminho e seu tamanho.
- `ordenacao_topologica`: faz o DFS em todos os vértices e devolve a ordem e os ciclos.
- `topologica_visita`: visita um vértice, marca os tempos e o guarda ao finalizar.
- `executar_topologica`: lê o grafo como orientado, chama a ordenação e mostra os resultados.
- `main` (em `main.py`): recebe as escolhas e coordena a execução.

O BFS visita os vizinhos pelo menor identificador. A distância conta arestas,
sem somar pesos. `None` indica distância indefinida ou ausência de predecessor;
na tabela, esses valores aparecem como `INF` e `NIL`, respectivamente.

A fila usa uma lista e um índice que avança a cada vértice processado.
O arquivo `bfs.py` não usa imports.

A reconstrução deve receber os predecessores da busca feita com a mesma origem.
Retorna `[]` quando não existe caminho e `[origem]` quando origem e destino são iguais.

A ordem topológica é a ordem inversa de finalização do DFS: quem termina por
último vem primeiro. Os vértices e os vizinhos são visitados pelo menor
identificador, então o resultado é sempre o mesmo. Se uma aresta aponta para um
vértice que ainda está sendo explorado (`Cinza`), existe um ciclo e não há
ordenação possível. Nesse caso o programa mostra as arestas de retorno.
No `teste_pequeno.txt`, a aresta `M057 M068` está nesse sentido para o grafo
não ter ciclo.

### Verificação

```console
python -m unittest -v
```

O teste compara as distâncias e os predecessores com `dados/gabarito_bfs.txt`,
que contém o gabarito da planilha com as colunas separadas por espaços.
Também verifica desempate, ciclos, vértices desconectados e vértices inexistentes.
Para M086, o resultado esperado é:

```text
M057 -> M058 -> M059 -> M069 -> M083 -> M084 -> M085 -> M086
Distância: 7 arestas
```

Os arquivos `gabarito_dfs.txt`, `gabarito_topologica.txt` e `gabarito_mst.txt`
trazem o resultado esperado para `dados/teste_pequeno.txt`. Na árvore geradora
mínima o peso total é sempre 9.50, mas as arestas podem mudar em caso de empate.
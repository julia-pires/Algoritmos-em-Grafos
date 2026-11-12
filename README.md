# Algoritmos-em-Grafos

Trabalho de Algoritmos em Grafos — Ciência da Computação, UEM.

## BFS — passo 6

Requer Python 3, sem bibliotecas adicionais. Execute na pasta do repositório:

```console
python main.py bfs dados/teste_pequeno.txt
```

Formato: `python main.py algoritmo arquivo.txt`.
O BFS escolhe o menor identificador como origem e mostra a tabela e os caminhos
para todos os vértices. Consideramos que o grafo é conectado; uma única busca
alcança todos os vértices. As distâncias e os caminhos partem da mesma origem.

Algoritmos aceitos: `bfs`, `dfs`, `topologica` e `mst`.
DFS, ordenação topológica e MST ainda não estão implementados.
A ordenação topológica exigirá adaptar a leitura para grafos orientados.
O programa recebe tudo pela linha de comando, sem perguntas interativas.
`main.py` usa apenas `sys` da biblioteca padrão para acessar esses argumentos.

### Arquivos

- `main.py`: entrada do programa, com um `if` para cada algoritmo.
- `grafo.py`: leitura do grafo, compartilhada pelos algoritmos.
- `bfs.py`: busca em largura, reconstrução e exibição dos resultados.
- `dados/`: grafo de teste e gabarito.
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

### Funções

- `ler_grafo`: lê o arquivo e monta a lista de adjacência.
- `bfs`: calcula as distâncias e os predecessores usando uma fila.
- `executar_bfs`: escolhe a origem, chama o BFS e mostra os resultados.
- `reconstruir_caminho`: segue os predecessores e inverte a sequência.
- `exibir_tabela`: imprime as distâncias e os predecessores.
- `exibir_caminho`: imprime o caminho e seu tamanho.
- `main` (em `main.py`): recebe as escolhas e coordena a execução.

O BFS visita os vizinhos pelo menor identificador. A distância conta arestas,
sem somar pesos. `None` indica distância indefinida ou ausência de predecessor;
na tabela, esses valores aparecem como `INF` e `NIL`, respectivamente.

A fila usa uma lista e um índice que avança a cada vértice processado.
O arquivo `bfs.py` não usa imports.

A reconstrução deve receber os predecessores da busca feita com a mesma origem.
Retorna `[]` quando não existe caminho e `[origem]` quando origem e destino são iguais.

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

# Algoritmos-em-Grafos

Trabalho de Algoritmos em Grafos — Ciência da Computação, UEM.

```console
python main.py bfs dados/teste_pequeno.txt
python main.py dfs dados/teste_pequeno.txt
python main.py topologica dados/teste_topologica.txt
python main.py mst dados/teste_pequeno.txt
```

Formato: `python main.py algoritmo arquivo.txt`.

Algoritmos aceitos: `bfs`, `dfs`, `topologica` e `mst`.

- `bfs`: escolhe o menor identificador como origem e mostra a tabela e os caminhos
  para todos os vértices. Consideramos que o grafo é conectado; uma única busca
  alcança todos os vértices.
- `dfs`: mostra cor, pai, tempos de descoberta e finalização e componente de cada
  vértice, além do número de componentes e das arestas de retorno (ciclos).
- `topologica`: lê o grafo como orientado e mostra a ordem topológica, ou as
  arestas de retorno se houver ciclo.
- `mst`: roda o Kruskal e mostra as arestas da árvore geradora mínima e o peso total.

### Arquivos

- `main.py`: entrada do programa, com um `if` para cada algoritmo.
- `grafo.py`: leitura do grafo, compartilhada pelos algoritmos. Também tem funções
  para converter para índices e montar a matriz de adjacência.
- `bfs.py`: busca em largura, reconstrução e exibição dos resultados.
- `dfs.py`: busca em profundidade, com detecção de ciclos e de componentes.
- `topologica.py`: ordenação topológica, feita com uma busca em profundidade.
- `kruskal.py`: árvore geradora mínima, com união por tamanho e compressão de caminho.
- `dados/`: grafos de teste e gabaritos.

### Entrada

Grafo não orientado, com uma aresta por linha no formato `origem destino peso`:

```text
M057 M058 1.00
M058 M059 0.75
```

Use ponto como separador decimal nos pesos (ex.: `0.75`).
Uma linha com apenas um identificador representa um vértice isolado. Linhas vazias e comentários com `#` são ignorados.
A representação é uma lista de adjacência: `grafo[origem][destino] = peso`.

Na ordenação topológica o grafo é orientado: a linha `origem destino peso` vale
só para a aresta `origem -> destino`, e o grafo precisa ser acíclico.
Nos outros algoritmos ele continua não orientado.

### Arquivos de dados

- `teste_pequeno.txt`: grafo não orientado com 12 vértices e um ciclo. Serve para
  `bfs`, `dfs` e `mst`.
- `teste_topologica.txt`: o mesmo grafo, mas com a aresta `M057 M068` no lugar de
  `M068 M057`. Assim, lido como orientado, ele não tem ciclo.
- `arestas_shroom_city.txt`: grafo grande, com 394 linhas.
- `gabarito_*.txt`: resultado esperado de cada algoritmo. Os de `bfs`, `dfs` e `mst` valem
  para o `teste_pequeno.txt`; o de `topologica` vale para o `teste_topologica.txt`.

Se rodar `topologica` com o `teste_pequeno.txt`, o programa avisa que existe ciclo
(`M068 -> M057`) e não mostra ordem. É o comportamento esperado.

### Funções

- `ler_grafo`: lê o arquivo e monta a lista de adjacência. Com `orientado=True`,
  guarda cada aresta só no sentido origem -> destino, mas o destino entra no
  grafo mesmo que nenhuma aresta saia dele.
- `bfs`: calcula as distâncias e os predecessores usando uma fila.
- `executar_bfs`: escolhe a origem, chama o BFS e mostra os resultados.
- `reconstruir_caminho`: segue os predecessores e inverte a sequência.
- `exibir_tabela`: imprime as distâncias e os predecessores.
- `exibir_caminho`: imprime o caminho e seu tamanho.
- `mapear_vertices`, `lista_adjacencia_indices` e `matriz_adjacencia` (em `grafo.py`): convertem
  o grafo para índices e montam a matriz de adjacência. Só o `python grafo.py arquivo.txt` usa.
- `construir_vertices` (em `dfs.py` e `topologica.py`): transforma a lista de adjacência em
  objetos `Vertice`, com as arestas em ordem crescente de identificador.
- `dfs`: faz a busca em todos os vértices e devolve o número de componentes e os ciclos.
- `dfs_visita`: visita um vértice, marca os tempos e procura arestas de retorno.
- `executar_dfs`: monta os vértices, chama o DFS e mostra os resultados.
- `ordenacao_topologica`: faz o DFS em todos os vértices e devolve a ordem e os ciclos.
- `topologica_visita`: visita um vértice, marca os tempos e o guarda ao finalizar.
- `executar_topologica`: recebe o grafo orientado, chama a ordenação e mostra os resultados.
- `kruskal`: ordena as arestas por peso e junta as que não formam ciclo.
- `executar_kruskal`: lê o grafo, chama o Kruskal e mostra os resultados.
- `main` (em `main.py`): recebe as escolhas, lê o grafo (orientado só na topológica),
  confere se ele não está vazio e chama o algoritmo. O `mst` é a exceção: recebe o
  nome do arquivo e lê o grafo por conta própria.

### BFS

O BFS visita os vizinhos pelo menor identificador. A distância conta arestas,
sem somar pesos. `None` indica distância indefinida ou ausência de predecessor;
na tabela, esses valores aparecem como `INF` e `NIL`, respectivamente.

A fila usa uma lista e um índice que avança a cada vértice processado.
O arquivo `bfs.py` não usa imports.

A reconstrução deve receber os predecessores da busca feita com a mesma origem.
Retorna `[]` quando não existe caminho e `[origem]` quando origem e destino são iguais.

### DFS

Os vértices e os vizinhos são visitados pelo menor identificador (comparação de
texto, não de número), então o resultado é sempre o mesmo. Cada vértice branco que sobra no laço principal
começa um novo componente. Se um vizinho está `Cinza` e não é o pai, existe um
ciclo, e a aresta é guardada como aresta de retorno.

### Ordenação topológica

A ordem topológica é a ordem inversa de finalização do DFS: quem termina por
último vem primeiro. Se uma aresta aponta para um vértice que ainda está sendo
explorado (`Cinza`), existe um ciclo e não há ordenação possível. Nesse caso o
programa mostra as arestas de retorno. Como o grafo é orientado, aqui não há
exceção para o pai.

Uma aresta para um vértice já finalizado (`Preto`) é ignorada: o vértice não é
visitado de novo e o pai dele continua sendo quem o descobriu primeiro. No
`teste_topologica.txt`, o M068 tem pai M081 porque chega por ali antes de o M057
olhar a aresta `M057 M068`. A ordem continua certa, pois o M068 termina antes do M057.

### Kruskal

Cada aresta aparece uma vez (a com origem menor que o destino) e todas são
ordenadas por peso. Uma aresta só entra se ligar dois conjuntos diferentes.
Se o grafo for desconexo, o resultado é uma floresta geradora mínima.

No `teste_pequeno.txt` o peso total é sempre 9.50, mas as arestas podem mudar em
caso de empate. O gabarito foi feito com desempate por identificador.

### Verificação

Rode cada algoritmo e compare com o gabarito correspondente em `dados/`:

```console
python main.py bfs dados/teste_pequeno.txt
python main.py dfs dados/teste_pequeno.txt
python main.py topologica dados/teste_topologica.txt
python main.py mst dados/teste_pequeno.txt
python main.py bfs dados/arestas_shroom_city.txt
python main.py dfs dados/arestas_shroom_city.txt
python main.py mst dados/arestas_shroom_city.txt
python main.py topologica dados/teste_pequeno.txt
```

Para o BFS, o caminho esperado até M086 é:

```text
M057 -> M058 -> M059 -> M069 -> M083 -> M084 -> M085 -> M086
Distância: 7 arestas
```

No DFS, o gabarito tem 1 componente e a aresta de retorno `M068 -> M057`.
Na topológica, os tempos de descoberta e finalização são os mesmos do DFS, e a
ordem esperada é:

```text
M057 -> M058 -> M059 -> M069 -> M083 -> M084 -> M085 -> M086 -> M070 -> M082 -> M081 -> M068
```

Nos erros (arquivo inexistente, linha mal formatada, peso inválido), o programa
mostra `Erro: ...` e termina com código 1. Um arquivo vazio dá erro no `bfs`, no
`dfs` e na `topologica`; no `mst` ele apenas mostra "grafo vazio".

Não há testes automáticos: `python -m unittest` não encontra nenhum teste.

### Resultados

Para salvar a saída do terminal em um arquivo, execute na raiz do repositório:

```console
python main.py bfs dados/teste_pequeno.txt > resultados/bfs_pequeno.txt
```

O operador `>` cria o arquivo de saída ou sobrescreve seu conteúdo se ele já existir.

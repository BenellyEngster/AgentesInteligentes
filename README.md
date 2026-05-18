# Agentes Inteligentes: Algoritmos de Busca com Heurísticas 

## Sobre o Projeto
Este repositório contém a implementação e comparação de algoritmos clássicos de Inteligência Artificial para a resolução de problemas de *pathfinding* (busca de caminhos). O objetivo do sistema é permitir que um agente autônomo navegue em um labirinto gerado dinamicamente a partir de um ponto inicial 'A' até um ponto final 'B', desviando de obstáculos e calculando o menor custo de deslocamento.

O foco principal deste projeto é a aplicação e comparação prática entre algoritmos de **busca cega** e algoritmos baseados em **heurísticas**, avaliando o desempenho de cada um.

## Algoritmos Implementados
* **Busca em Largura (BFS - Breadth-First Search):** Explora o labirinto nível a nível de forma não informada (busca cega).
* **Busca em Profundidade (DFS - Depth-First Search):** Explora os caminhos possíveis até o limite antes de retroceder (busca cega).
* **Busca Gulosa (Greedy Search):** Algoritmo informado que utiliza uma **heurística de distância** para avaliar e escolher o vizinho que aparenta estar mais próximo do objetivo, reduzindo drasticamente o esforço computacional.
* **Busca A* (A-Star):** Algoritmo ótimo e completo que toma decisões combinando o custo real acumulado (peso do terreno) com a heurística de distância até o destino.

## Regras do Ambiente (Labirinto)
O labirinto é gerado em formato de matriz. Os custos de movimentação variam de acordo com o tipo de terreno simulado:
* **Grama:** Custo de movimento = `2`
* **Lama:** Custo de movimento = `5`
* **Paredes (Obstáculos):** Intransponíveis (Representadas por `■`)

## Problema do Caixeiro Viajante (PCV)

### Autor

Phillip da Silva Cardoso

---

## Descrição do Trabalho

Este trabalho implementa e analisa empiricamente dois algoritmos para o **Problema do Caixeiro Viajante (PCV)**:

1. **Algoritmo Exato — Held-Karp**

   * Baseado em programação dinâmica.
   * Retorna a solução ótima.
   * Possui complexidade exponencial.

2. **Algoritmo Aproximado — 2-PCV**

   * Baseado na construção de uma Árvore Geradora Mínima (AGM).
   * Utiliza percurso em pré-ordem.
   * Garante solução com custo no máximo duas vezes o ótimo.
   * Possui complexidade polinomial.

O objetivo do trabalho é **comparar empiricamente** o comportamento dos dois algoritmos em termos de **tempo de execução**, confirmando suas complexidades teóricas.

---

## Metodologia

* As instâncias do PCV são **métricas**, geradas a partir de pontos aleatórios no plano cartesiano.
* As distâncias entre cidades são calculadas utilizando a **distância euclidiana**, garantindo a desigualdade triangular.
* Para cada valor de `n` (número de cidades):

  * Uma instância é gerada.
  * O algoritmo é executado.
  * O tempo de execução é medido com `time.perf_counter()`.

---

## Tecnologias Utilizadas

* **Python 3.14.0**
* Bibliotecas padrão:

  * `random`
  * `math`
  * `time`
  * `itertools`
  * `sys`
* Biblioteca externa:

  * `matplotlib`

---

## Como Executar

1. Certifique-se de ter o Python instalado:

   ```bash
   python --version
   ```

2. Instale o matplotlib (caso não esteja instalado):

   ```bash
   pip install matplotlib
   ```

3. Execute o programa:

   ```bash
   python main.py
   ```

---

## Resultados Gerados

Após a execução, o programa gera automaticamente dois arquivos de imagem:

* `held_karp.png`

  * Gráfico do tempo de execução do algoritmo exato.
  * Demonstra crescimento exponencial.

* `aproximado.png`

  * Gráfico do tempo de execução do algoritmo aproximado.
  * Demonstra crescimento polinomial.

Esses arquivos são salvos no mesmo diretório do script.

> ⚠️ Observação: os gráficos não são exibidos na tela, apenas salvos em arquivo, garantindo compatibilidade com macOS.

---

## Parâmetros Utilizados

### Held-Karp

* Número de cidades: de **4 até 16**
* Valores maiores tornam o tempo de execução impraticável devido à complexidade exponencial.

### Algoritmo Aproximado

* Número de cidades: **10, 50, 100, 200 e 400**
* Permite observar escalabilidade e desempenho em instâncias maiores.

---

## Estrutura do Código

* `gerar_cidades`: gera instâncias do PCV
* `calcular_distancias`: cria a matriz de distâncias
* `held_karp`: implementação do algoritmo exato
* `prim`: construção da Árvore Geradora Mínima
* `pcv_aproximado`: implementação do algoritmo aproximado
* `testar_held_karp`: mede o tempo do algoritmo exato
* `testar_aproximado`: mede o tempo do algoritmo aproximado
* `plotar_grafico`: gera e salva os gráficos

---

## ✅ Conclusão

Os resultados obtidos confirmam o comportamento esperado:

* O algoritmo **Held-Karp** apresenta crescimento exponencial e se torna inviável para instâncias maiores.
* O algoritmo **aproximado 2-PCV** apresenta crescimento polinomial, sendo escalável para um número maior de cidades, embora não garanta a solução ótima.
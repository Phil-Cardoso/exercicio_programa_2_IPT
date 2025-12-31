import random
import math
import time
import matplotlib.pyplot as plt
from itertools import combinations
import sys

# GERAÇÃO DAS INSTÂNCIAS DO PCV (MÉTRICO)

def gerar_cidades(n, limite=100):
    """
    Gera n cidades como pontos no plano cartesiano.
    """
    return [(random.uniform(0, limite), random.uniform(0, limite)) for _ in range(n)]


def calcular_distancias(cidades):
    """
    Calcula a matriz de distâncias euclidianas entre as cidades.
    """
    n = len(cidades)
    dist = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = math.dist(cidades[i], cidades[j])
    return dist


# ALGORITMO EXATO — HELD-KARP

def held_karp(dist):
    """
    Resolve o Problema do Caixeiro Viajante usando
    programação dinâmica (Held-Karp).
    Retorna o custo mínimo do ciclo Hamiltoniano.
    """
    n = len(dist)
    dp = {}

    # Casos base: subconjuntos de tamanho 1
    for k in range(1, n):
        dp[(1 << k, k)] = dist[0][k]

    # Subconjuntos de tamanho crescente
    for tamanho in range(2, n):
        for subconjunto in combinations(range(1, n), tamanho):
            bits = sum(1 << i for i in subconjunto)
            for k in subconjunto:
                prev_bits = bits & ~(1 << k)
                dp[(bits, k)] = min(
                    dp[(prev_bits, m)] + dist[m][k]
                    for m in subconjunto if m != k
                )

    # Fecha o ciclo retornando à cidade 0
    bits_finais = (1 << n) - 2
    return min(dp[(bits_finais, k)] + dist[k][0] for k in range(1, n))


# ALGORITMO APROXIMADO — 2-PCV (AGM + PRÉ-ORDEM)

def prim(dist):
    """
    Constrói uma Árvore Geradora Mínima usando o algoritmo de Prim.
    Retorna o vetor de pais.
    """
    n = len(dist)
    visitado = [False] * n
    chave = [float("inf")] * n
    pai = [-1] * n

    chave[0] = 0

    for _ in range(n):
        u = min((i for i in range(n) if not visitado[i]), key=lambda i: chave[i])
        visitado[u] = True

        for v in range(n):
            if not visitado[v] and dist[u][v] < chave[v]:
                chave[v] = dist[u][v]
                pai[v] = u

    return pai

def percurso_pre_ordem(pai):
    """
    Realiza percurso em pré-ordem na AGM gerada.
    """
    n = len(pai)
    arvore = {i: [] for i in range(n)}

    for i in range(1, n):
        arvore[pai[i]].append(i)

    caminho = []

    def dfs(u):
        caminho.append(u)
        for v in arvore[u]:
            dfs(v)

    dfs(0)
    caminho.append(0)
    return caminho


def custo_caminho(caminho, dist):
    """
    Calcula o custo total de um caminho.
    """
    return sum(dist[caminho[i]][caminho[i + 1]] for i in range(len(caminho) - 1))


def pcv_aproximado(dist):
    """
    Algoritmo aproximado 2-PCV.
    """
    pai = prim(dist)
    caminho = percurso_pre_ordem(pai)
    return custo_caminho(caminho, dist)

# EXPERIMENTOS E MEDIÇÃO DE TEMPO

def testar_held_karp(valores_n):
    tempos = []
    for n in valores_n:
        cidades = gerar_cidades(n)
        dist = calcular_distancias(cidades)

        inicio = time.perf_counter()
        held_karp(dist)
        fim = time.perf_counter()

        tempos.append(fim - inicio)
        print(f"Held-Karp | n={n} | tempo={tempos[-1]:.4f}s")

    return tempos

def testar_aproximado(valores_n):
    tempos = []
    for n in valores_n:
        cidades = gerar_cidades(n)
        dist = calcular_distancias(cidades)

        inicio = time.perf_counter()
        pcv_aproximado(dist)
        fim = time.perf_counter()

        tempos.append(fim - inicio)
        print(f"Aproximado | n={n} | tempo={tempos[-1]:.4f}s")

    return tempos

# GRÁFICOS

def plotar_grafico(valores_n, tempos, titulo, nome_arquivo):
    plt.figure()
    plt.plot(valores_n, tempos, marker="o")
    plt.xlabel("Número de cidades")
    plt.ylabel("Tempo de execução (s)")
    plt.title(titulo)
    plt.grid()
    plt.savefig(nome_arquivo)
    plt.close()


# PROGRAMA PRINCIPAL

def main():
    sys.setrecursionlimit(10**7)

    # Valores de n para cada algoritmo
    valores_hk = list(range(4, 17))      # Exato (limitado)
    valores_ap = [10, 50, 100, 200, 400]  # Aproximado

    print("\n=== Testando Held-Karp ===")
    tempos_hk = testar_held_karp(valores_hk)

    print("\n=== Testando Algoritmo Aproximado ===")
    tempos_ap = testar_aproximado(valores_ap)

    plotar_grafico(valores_hk, tempos_hk, 
                "Held-Karp — Crescimento Exponencial",
                "held_karp.png")

    plotar_grafico(valores_ap, tempos_ap, 
                "Aproximado 2-PCV — Crescimento Polinomial",
                "aproximado.png")


if __name__ == "__main__":
    main()

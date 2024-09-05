from collections import deque

# Função para verificar se um número pode ser colocado na posição
def e_valido(matriz, linha, coluna, num):
    for i in range(9):
        if matriz[linha][i] == num or matriz[i][coluna] == num:
            return False
    
    inicio_linha, inicio_coluna = 3 * (linha // 3), 3 * (coluna // 3)
    for i in range(inicio_linha, inicio_linha + 3):
        for j in range(inicio_coluna, inicio_coluna + 3):
            if matriz[i][j] == num:
                return False
    return True

# Função para encontrar a próxima célula vazia
def encontrar_local_vazio(matriz):
    for i in range(9):
        for j in range(9):
            if matriz[i][j] == 0:
                return i, j
    return -1, -1

# Função para verificar se o Sudoku foi resolvido
def esta_resolvido(matriz):
    return all(all(celula != 0 for celula in linha) for linha in matriz)

# Função principal que usa BFS para resolver o Sudoku
def resolver_sudoku_bfs(matriz):
    fila = deque([matriz])
    while fila:
        tabuleiro_atual = fila.popleft()
        
        if esta_resolvido(tabuleiro_atual):
            return tabuleiro_atual
        
        linha, coluna = encontrar_local_vazio(tabuleiro_atual)
        
        if linha == -1:
            continue
        
        for num in range(1, 10):
            if e_valido(tabuleiro_atual, linha, coluna, num):
                novo_tabuleiro = [linha[:] for linha in tabuleiro_atual]
                novo_tabuleiro[linha][coluna] = num
                fila.append(novo_tabuleiro)
    
    return None

# Exemplo de uso
if __name__ == "__main__":

    sudoku = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    solucao = resolver_sudoku_bfs(sudoku)
    if solucao:
        for linha in solucao:
            print(linha)
    else:
        print("Nenhuma solução encontrada")

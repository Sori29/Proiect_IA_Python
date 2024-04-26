def is_valid(board, row, col, n):
    # Verifică dacă se poate plasa o regină în poziția curentă
    for i in range(n):
        if board[row][i] == 1 or board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n, 1)):
        if board[i][j] == 1:
            return False
    return True

def solve(board, col, n):
    # Caz de bază: am plasat toate reginele
    if col == n:
        return True
    # Încercăm să plasăm o regină pe fiecare rând pentru coloana curentă
    for i in range(n):
        if is_valid(board, i, col, n):
            board[i][col] = 1
            if solve(board, col+1, n):
                return True
            # Dacă nu s-a găsit soluția, înlăturăm regina din poziția curentă
            board[i][col] = 0
    # Dacă nu s-a putut plasa regina în nicio poziție de pe coloana curentă, nu există soluție
    return False

def n_queens_backtracking(n):
    # Inițializăm tabla de șah cu valori de 0
    board = [[0 for x in range(n)] for y in range(n)]
    # Apelăm funcția solve pentru a găsi soluția
    if not solve(board, 0, n):
        print("Nu există soluție pentru o tablă de %d x %d." % (n, n))
        return
    # Afisăm soluția
    print("Soluția pentru o tablă de %d x %d:" % (n, n))
    for row in board:
        print(row)


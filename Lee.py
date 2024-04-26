from collections import deque

def lee_algorithm(matrix, start, end):
    """
    Lee algorithm implementation to find the shortest path in a matrix.
    Args:
        matrix (list of lists): The input matrix, represented as a 2D list.
        start (tuple): The starting point in the matrix, represented as a tuple (row, col).
        end (tuple): The ending point in the matrix, represented as a tuple (row, col).
    Returns:
        list: The shortest path from start to end, represented as a list of tuples [(row, col), ...].
    """
    rows = len(matrix)
    cols = len(matrix[0])

    # Define possible moves: up, down, left, right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Create a visited matrix to keep track of visited cells
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[start[0]][start[1]] = True

    # Create a queue for BFS
    queue = deque([(start[0], start[1], [])])

    # Perform BFS
    while queue:
        row, col, path = queue.popleft()

        # Check if we reached the end point
        if (row, col) == end:
            return path + [[row, col]]

        # Generate next possible moves
        for move in moves:
            new_row = row + move[0]
            new_col = col + move[1]

            # Check if the new position is within the matrix and is not visited
            if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col] and matrix[new_row][new_col] != -1:
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, path + [[row, col]]))

    # If no path is found, return an empty list
    return []

def citire_fisier_Lee(numeFisier):
    myMatrix=[[]]
    try:
        with open(numeFisier,'r') as f:
            if f.read().strip() == "":
                    print("Fișierul este gol.")
                    return
            f.seek(0)
            # Citim liniile din fișier și ignorăm liniile goale
            linii = [line.strip() for line in f.readlines() if line.strip() != ""]
            if not linii:
                print("Nu există date valide în fișier.")
                return
            myMatrix = [list(map(int, line.split(","))) for line in linii[0:]]
    except FileNotFoundError:
        print(f"Fișierul {numeFisier} nu a fost găsit.")
    for i in range(len(myMatrix)):
        for j in range(len(myMatrix[0])):
            if myMatrix[i][j] == -2:
                end = (i,j)
                print("Punctul destinatie:["+str(i)+ ", "+str(j)+"]")
            if myMatrix[i][j] == -3:    
                start = (i,j)
                print("Punctul sursa:["+str(i)+ ", "+str(j)+"]")   
    return myMatrix,start,end

def afisare_fisier_Lee(path,numeFisier):
    with open(numeFisier,"w") as f:
        for linie in path:
            linie_str = "["+",".join(str(element) for element in linie)+"]"
            f.write(linie_str + ", ")           
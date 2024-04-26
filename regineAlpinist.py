import random

def generate_random_board(n):
    """Generates a random NxN chess board with N queens"""
    state = [random.randint(0, n-1) for i in range(n)]
    return state

def count_attacking_pairs(state):
    n = len(state)
    attacking_pairs = 0

    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacking_pairs += 1

    return attacking_pairs

def hill_climbing(n):
    inital_state = generate_random_board(n)
    current_state = inital_state
    current_attacks = count_attacking_pairs(current_state)

    while True:
        neighbors = []
        for i in range(n):
            for j in range(n):
                if current_state[i] != j:
                    neighbor = list(current_state)
                    neighbor[i] = j
                    neighbors.append(neighbor)

        best_neighbor = current_state
        best_attacks = current_attacks

        for neighbor in neighbors:
            attacks = count_attacking_pairs(neighbor)
            if attacks < best_attacks:
                best_neighbor = neighbor
                best_attacks = attacks

        if best_attacks == 0:
            # Solution found
            return best_neighbor

        if best_attacks >= current_attacks:
            # Local minimum reached, restart with a new random state
            current_state = generate_random_board(n)
            current_attacks = count_attacking_pairs(current_state)
        else:
            current_state = best_neighbor
            current_attacks = best_attacks


def print_board(board):
    """Prints the board in a matrix format"""
    n = len(board)
    for i in range(n):
        row = ["Q" if j == board[i] else "-" for j in range(n)]
        print(" ".join(row))

def afisare_fisier(solution,numeFisier):
    with open(numeFisier,"w") as f:
        f.write("["+",".join(str(element) for element in solution)+"]")
             
# Example usage
#solution = hill_climbing(8)
#print(solution)
#print_board(solution)


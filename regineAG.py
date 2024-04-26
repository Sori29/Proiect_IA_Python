import random

class GAChess:
    def __init__(self, n, population_size=100, mutation_rate=0.1):
        self.n = n
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = []
        self.initial_board = None

    def generate_random_board(self):
        board = list(range(self.n))
        random.shuffle(board)
        return board

    def initialize_population(self):
        self.population = [self.generate_random_board() for _ in range(self.population_size)]

    def fitness(self, board):
        clashes = 0
        for i in range(self.n):
            for j in range(i+1, self.n):
                if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                    clashes += 1
        return self.n - clashes

    def crossover(self, parent1, parent2):
        split_point = random.randint(1, self.n-1)
        child1 = parent1[:split_point] + parent2[split_point:]
        child2 = parent2[:split_point] + parent1[split_point:]
        return child1, child2

    def mutate(self, board):
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(self.n), 2)
            board[i], board[j] = board[j], board[i]

    def evolve(self, num_generations):
        self.initialize_population()
        self.initial_board = self.population[0]  # Store the initial board

        for _ in range(num_generations):
            # Evaluate fitness
            fitness_scores = [self.fitness(board) for board in self.population]

            # Select parents
            parents = random.choices(self.population, weights=fitness_scores, k=self.population_size)

            # Create next generation
            next_generation = []
            for i in range(0, self.population_size, 2):
                parent1, parent2 = parents[i], parents[i+1]
                child1, child2 = self.crossover(parent1, parent2)
                self.mutate(child1)
                self.mutate(child2)
                next_generation.extend([child1, child2])

            self.population = next_generation

        # Find the best solution
        best_board = max(self.population, key=self.fitness)
        return self.initial_board, best_board




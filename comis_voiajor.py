import time

def read_input_file(filename):
    cities = []
    distances = []
    start_city = None
    
    with open(filename, 'r') as f:
        n = int(f.readline())
        for i in range(n):
            city_name = f.readline().strip()
            cities.append(city_name)
        for i in range(n):
            row = list(map(int, f.readline().split()))
            if len(row) != n:
                print("Matricea nu este simetrica!")
                return None, None, None
            distances.append(row)
            
        start_city = int(f.readline())-1
        start_city_distances = distances[start_city]
        
        if n < 4:
            print("Numarul minim de orase este 4!")
            return None, None, None
        
    return cities, distances, start_city_distances, start_city

def nearest_neighbor(cities, distances, start_city):
    start_time = time.perf_counter()
    
    n = len(cities)
    visited = [False] * n
    visited[start_city] = True
    path = [cities[start_city]]
    total_distance = 0
    current_city = start_city
    
    while False in visited:
        nearest_city = None
        nearest_distance = float('inf')
        for i in range(n):
            if not visited[i] and distances[current_city][i] < nearest_distance:
                nearest_city = i
                nearest_distance = distances[current_city][i]
        visited[nearest_city] = True
        path.append(cities[nearest_city])
        total_distance += nearest_distance
        current_city = nearest_city
    
    total_distance += distances[current_city][start_city]
    path.append(cities[start_city])
    
    end_time = time.perf_counter()
    execution_time = (end_time - start_time)*1000
    
    print("Solutia pentru problema comis-voiajorului cu nearest neighbor:")
    print("Orase:", path)
    print("Distanta totala:", total_distance)
    print(f"Timpul de executie: {execution_time:.3f} ms")
    
    return path, total_distance, execution_time

def afisare_fisier(path,total_distance,numeFisier):
    with open(numeFisier, "w") as f:
        f.write(",".join(str(oras) for oras in path)+"\n"+str(total_distance)+"\n")

# Exemplu de utilizare
if __name__ == '__main__':
    cities, distances, start_city_distances, start_city = read_input_file('comis_voiajor_input1.txt')
    if cities is not None:
        print("Orase:", cities)
        print("Distante:", distances)
        print("Oras de start:", cities[start_city])
        path, total_distance, execution_time = nearest_neighbor(cities, distances, start_city)
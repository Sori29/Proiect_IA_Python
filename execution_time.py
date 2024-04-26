import time
from regineBacktracking import n_queens_backtracking
from regineLee import queens_lee
from regineAlpinist import hill_climbing
import regineAG
import comis_voiajor
import Lee
import matplotlib.pyplot as plt

def measure_time(n, runs):
    times = []
    
    # Măsurăm timpul de execuție pentru algoritmul de backtracking
    total_time = 0
    for i in range(runs):
        start_time = time.time()
        n_queens_backtracking(n)
        end_time = time.time()
        total_time += end_time - start_time
    times.append(('Backtracking', total_time / runs))
    
    # Măsurăm timpul de execuție pentru algoritmul lui Lee
    total_time = 0
    for i in range(runs):
        start_time = time.time()
        queens_lee(n)
        end_time = time.time()
        total_time += end_time - start_time
    times.append(('Lee', total_time / runs))
    
    # Măsurăm timpul de execuție pentru algoritmul alpinistului
    total_time = 0
    for i in range(runs):
        start_time = time.time()
        hill_climbing(n)
        end_time = time.time()
        total_time += end_time - start_time
    times.append(('Hill Climbing', total_time / runs))
    
    # Măsurăm timpul de execuție pentru algoritmul AG
    total_time = 0
    for i in range(runs):
       start_time = time.time()
       chess = regineAG.GAChess(n)
       chess.evolve(num_generations=1000)
       end_time = time.time()
       total_time += end_time - start_time
    times.append(('AG', total_time / runs)) 
    return times

def exemplu_regine():
    # Măsurăm timpul de execuție pentru dimensiunile de 4x4, 8x8, 12x12
    n_values = [4, 6, 8, 10, 12, 14]
    runs = 6
    results = []
    for n in n_values:
        results.append(measure_time(n, runs))
    print(results)
    # Datele pentru fiecare algoritm
    backtracking_times = [result[0][1] for result in results]
    lee_times = [result[1][1] for result in results]
    hill_climbing_times = [result[2][1] for result in results]
    AG_times = [result[3][1] for result in results]

    # Dimensiunile tablei de șah
    n_values = [4, 6, 8, 10, 12, 14]

    # Creăm diagrama
    plt.plot(n_values, backtracking_times, label='Backtracking')
    plt.plot(n_values, lee_times, label='Lee')
    plt.plot(n_values, hill_climbing_times, label='Hill Climbing')
    plt.plot(n_values, AG_times, label='AG')

    # Adăugăm titlul și etichetele pentru axele diagramelor
    plt.title('Timpul de execuție pentru problema reginelor')
    plt.xlabel('Dimensiunea tablei de șah (N)')
    plt.ylabel('Timpul de execuție (secunde)')

    # Adăugăm legenda
    plt.legend()

    # Afișăm diagrama
    plt.show()

def exemplu_comis_voiajor():
     times = []
     runs = 20
     #Pentru 4 orase
     total_time = 0
     for i in range(runs):
        cities, distances, start_city_distances, start_city = comis_voiajor.read_input_file("I&O\\comis_voiajor_input1.txt")
        path, total_distance, execution_time = comis_voiajor.nearest_neighbor(cities, distances, start_city)
        total_time += execution_time
     times.append((str(len(cities)),total_time/runs))
     
     #Pentru 8 orase
     total_time = 0
     for i in range(runs):
        cities, distances, start_city_distances, start_city = comis_voiajor.read_input_file("I&O\\comis_voiajor_input2.txt")
        path, total_distance, execution_time = comis_voiajor.nearest_neighbor(cities, distances, start_city)
        total_time += execution_time
     times.append((str(len(cities)),total_time/runs))
     
     #Pentru 12 orase
     total_time = 0
     for i in range(runs):
        cities, distances, start_city_distances, start_city = comis_voiajor.read_input_file("I&O\\comis_voiajor_input3.txt")
        path, total_distance, execution_time = comis_voiajor.nearest_neighbor(cities, distances, start_city)
        total_time += execution_time
     times.append((str(len(cities)),total_time/runs))
     
     print(times)
     n_values = [4, 8, 12]
     timp_executie = [timp[1] for timp in times]
     plt.plot(n_values, timp_executie, label='Comis Voiajor')
     
     plt.title('Timpul de execuție pentru problema comis voiajor')
     plt.xlabel('Numarul de orase')
     plt.ylabel('Timpul de execuție (ms)')
     
     plt.legend()

     plt.show()

def exemplu_Lee():
    times = []
    runs = 20
    
    # Pentru labirint 9x9
    total_time = 0
    for i in range(runs):
        start_time = time.perf_counter()
        myMatrix, start, end = Lee.citire_fisier_Lee("I&O\\Lee_input1.txt")
        Lee.lee_algorithm(myMatrix, start, end)
        end_time = time.perf_counter()
        total_time += end_time - start_time
    times.append(('9x9', total_time * 1000/runs))
    
    # Pentru labirint 12x12
    total_time = 0
    for i in range(runs):
        start_time = time.perf_counter()
        myMatrix, start, end = Lee.citire_fisier_Lee("I&O\\Lee_input2.txt")
        Lee.lee_algorithm(myMatrix, start, end)
        end_time = time.perf_counter()
        total_time += end_time - start_time
    times.append(('12x12', total_time * 1000/runs))
    
    # Pentru labirint 14x14
    total_time = 0
    for i in range(runs):
        start_time = time.perf_counter()
        myMatrix, start, end = Lee.citire_fisier_Lee("I&O\\Lee_input3.txt")
        Lee.lee_algorithm(myMatrix, start, end)
        end_time = time.perf_counter()
        total_time += end_time - start_time
    times.append(('14x14', total_time * 1000/runs))
    
    print(times)
    
    n_values = [9, 12, 14]
    timp_executie = [timp[1] for timp in times]
    plt.plot(n_values, timp_executie, label='Algoritmul lui Lee')
    
    plt.title('Timpul de execuție pentru algoritmul lui Lee')
    plt.xlabel('Dimensiune labirint')
    plt.ylabel('Timpul de execuție (ms)')
    
    plt.legend()
    plt.show()


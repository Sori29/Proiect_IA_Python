import Lee #Lab1

import regineAlpinist #Lab6

import comis_voiajor #Lab7

import calirea_simulata #Lab8

import regineAG  #Lab9

import execution_time

import msvcrt
import os

def wait_for_keypress():
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for keypress
    os.system('cls')

while True:
    print("Alegeti o optiune:\n"
          "1. Algoritmul lui Lee\n"
          "2. N Regine cu alpinist\n"
          "3. Comis voiajor\n"
          "4. N regine cu calire simulata\n"
          "5. N regine cu AG\n"
          "6. Grafice\n"
          "7. Info autor\n"
          "8. iesire\n")
    optiune = int(input("Selecteaza o optiune: "))
    
    if optiune == 1:
        print("Algoritmul lui Lee a fost selectat\n")
        myMatrix,start,end=Lee.citire_fisier_Lee("I&O\\Lee_input1.txt")
        shortest_path=Lee.lee_algorithm(myMatrix,start,end)
        print("Calea cea mai scurta:", shortest_path)
        Lee.afisare_fisier_Lee(shortest_path,"I&O\\Lee_output.txt")
        wait_for_keypress()
        
    elif optiune == 2:
        print("N regine cu alpinist a fost selectat\n")
        solution = regineAlpinist.hill_climbing(8)
        regineAlpinist.afisare_fisier(solution,"I&O\\Regine_Alpinist_output.txt")
        print(solution)
        regineAlpinist.print_board(solution)
        wait_for_keypress()
        
    elif optiune == 3:
        print("Comis voiajor a fost selectat\n")
        cities, distances, start_city_distances, start_city = comis_voiajor.read_input_file("I&O\\comis_voiajor_input1.txt")
        if cities is not None:
            print("Orase:", cities)
            print("Distante:", distances)
            print("Oras de start:", cities[start_city])
            path, total_distance, execution_time = comis_voiajor.nearest_neighbor(cities, distances, start_city)
            comis_voiajor.afisare_fisier(path,total_distance,"I&O\\comis_voiajor_output.txt")
            wait_for_keypress()
            
    elif optiune == 4:
        print("N regine cu calire simulata a fost selectat\n")
        stare_finala = calirea_simulata.cautare_simulata(8)
        print("Starea finală: ", stare_finala)
        print("Numărul de conflicte: ", calirea_simulata.numar_conflicte(stare_finala))
        calirea_simulata.afisare_fisier(stare_finala,"I&O\\calire_simulata_output.txt")
        wait_for_keypress()
        
    elif optiune == 5:
        print("N regine cu AG a fost selectat\n")
        n=5
        chess = regineAG.GAChess(n)
        initial_board, best_solution = chess.evolve(num_generations=1000)
        print("Initial Board:")
        print(initial_board)
        print("Best Solution (GA):")
        print(best_solution)
        with open("I&O\\Regine_AG_output.txt","w") as f:
            f.write(",".join(str(element) for element in best_solution))
        wait_for_keypress()
        
    elif optiune == 6:
        os.system('cls')
        print("Alegeti o optiune\n"
              "1. Problema Reginelor (toti algoritmii disponibili)\n"
              "2. Problema comis voiajor\n"
              "3. Algoritmul lui Lee")
        option = int(input("Selecteaza o optiune: "))
        if option == 1:
            execution_time.exemplu_regine()
        elif option == 2:
            execution_time.exemplu_comis_voiajor()
        elif option == 3:
            execution_time.exemplu_Lee()
        else:
            print("Opțiune invalidă")
        wait_for_keypress()
    elif optiune == 7:
        print("Lungu Sorin, gr.3131b\n")
        wait_for_keypress()
    elif optiune == 8:
        exit()
    else:
        os.system('cls')
        print("Opțiune invalidă. Te rog selectează o opțiune validă.")
    
        



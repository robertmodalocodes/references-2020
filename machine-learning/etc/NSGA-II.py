'''
Tugas Kecerdasan Komputasional
Non-dominated Sorting Genetic Algorithm II
Oleh:
Nama    :   Robert John Modalo
NIM     :   G651190331
'''

# Import paket library
import math
import random
import matplotlib.pyplot as plt
# %matplotlib inline

'''
Non-dominated Sorting Genetic Algorithm II merupakan
pengembangan dari NSGA. Algoritma ini pada dasarnya mirip dengan
NSGA tetapi dikembangkan untuk menangani masalah optimisasi
dengan fungsi objektif yang banyak.

Dalam suatu masalah optimisasi dengan satu fungsi objektif, 
cukup mudah untuk mengidentifikasi kualitas solusinya. Sebagai contoh,
semakin besar nilainya maka dapat dikatakan itu solusi terbaiknya.
Tetapi jika fungsi objektifnya banyak, kualitas solusinya tidak mudah untuk ditemukan.
Di sinilah konsep “non-dominated” digunakan. Ketika dalam banyak fungsi 
objektif ditemukan banyak solusi, kita dapat menggunakan konsep “dominasi” ini
untuk menilai solusi mana yang terbaik.

NSGA-II menghasilkan generasi (offspring) menggunakan suatu tipe 
penyilangan (crossover) dan mutase (mutation) yang spesifik dan
kemudian menyeleksi generasi berikutnya menurut perbandingan
jarak kerumunan (crowding distance)

Berikut implementasinya dengan bahasa pemrograman python
'''

# fungsi objektif untuk dioptimisasi
# misalkan diberikan fungsi objektif
# sebagai berikut

# fungsi objektif 1
def objective1(x):
    y = -x**3
    return y

# fungsi objektif 2
def objective2(x):
    y = -(x-2)**2
    return y


# input/inisialisasi parameter
population = 30
max_gen = 501
min_value = -100
max_value = 100

# metode helper
# fungsi pencari index
def index_locator(a, list):
    for i in range(0, len(list)):
        if list[i] == a:
            return i
    return -1

# fungsi penyortir berdasarkan nilai/value
def sort_by_values(list1, values):
    sorted_list = []
    while(len(sorted_list) != len(list1)):
        if index_locator(min(values), values) in list1:
            sorted_list.append(index_locator(min(values), values))
        values[index_locator(min(values), values)] = math.inf
    return sorted_list

# fungsi crowding distance
def crowding_distance(values1, values2, front):
    distance = [0 for i in range(0, len(front))]
    sorted1 = sort_by_values(front, values1[:])
    sorted2 = sort_by_values(front, values2[:])
    distance[0] = 9999999999999999
    distance[len(front) - 1] = 9999999999999999
    for k in range(1, len(front)-1):
        distance[k] = distance[k] + (values1[sorted1[k+1]] -
                                     values2[sorted1[k-1]])/(max(values1)-min(values1))
    for k in range(1, len(front)-1):
        distance[k] = distance[k] + (values1[sorted2[k+1]] -
                                     values2[sorted2[k-1]])/(max(values2)-min(values2))
    return distance

# fungsi-fungsi operator genetik
# fungsi crossover
def crossover(a, b):
    r = random.random()
    if r > 0.5:
        return mutation((a+b)/2)
    else:
        return mutation((a-b)/2)

# fungsi mutasi
def mutation(solution):
    mutation_prob = random.random()
    if mutation_prob < 1:
        solution = min_value+(max_value-min_value)*random.random()
    return solution

# algoritma non-dominated sorting
def non_dominated_sorting_algorithm(values1, values2):
    S = [[] for i in range(0, len(values1))]
    front = [[]]
    n = [0 for i in range(0, len(values1))]
    rank = [0 for i in range(0, len(values1))]

    for p in range(0, len(values1)):
        S[p] = []
        n[p] = 0
        for q in range(0, len(values1)):
            if (values1[p] > values1[q] and values2[p] > values2[q]) or (values1[p] >= values1[q] and values2[p] > values2[q]) or (values1[p] > values1[q] and values2[p] >= values2[q]):
                if q not in S[p]:
                    S[p].append(q)
            elif (values1[q] > values1[p] and values2[q] > values2[p]) or (values1[q] >= values1[p] and values2[q] > values2[p]) or (values1[q] > values1[p] and values2[q] >= values2[p]):
                n[p] = n[p] + 1
        if n[p] == 0:
            rank[p] = 0
            if p not in front[0]:
                front[0].append(p)
    i = 0
    while(front[i] != []):
        Q = []
        for p in front[i]:
            for q in S[p]:
                n[q] = n[q] - 1
                if(n[q] == 0):
                    rank[q] = i+1
                    if q not in Q:
                        Q.append(q)
        i = i+1
        front.append(Q)
    del front[len(front)-1]
    return front


# fungsi implementasi akhir
# fungsi implementasi NSGA-II
def nsga2(population, max_gen, min_value, max_value):

    gen_no = 0
    solution = [min_value+(max_value-min_value)*random.random()
                for i in range(0, population)]

    while(gen_no < max_gen):
        objective1_values = [objective1(solution[i])
                             for i in range(0, population)]
        objective2_values = [objective2(solution[i])
                             for i in range(0, population)]
        non_dominated_sorted_solution = non_dominated_sorting_algorithm(
            objective1_values[:], objective2_values[:])
        print('Front terbaik untuk generasi:', gen_no)
        for values in non_dominated_sorted_solution[0]:
            print(round(solution[values], 3), end=" ")
        print("\n")
        crowding_distance_values = []
        for i in range(0, len(non_dominated_sorted_solution)):
            crowding_distance_values.append(crowding_distance(
                objective1_values[:], objective2_values[:], non_dominated_sorted_solution[i][:]))
        solution2 = solution[:]

        while(len(solution2) != 2*population):
            a1 = random.randint(0, population-1)
            b1 = random.randint(0, population-1)
            solution2.append(crossover(solution[a1], solution[b1]))
        objective1_values2 = [objective1(solution2[i])
                              for i in range(0, 2*population)]
        objective2_values2 = [objective2(solution2[i])
                              for i in range(0, 2*population)]
        non_dominated_sorted_solution2 = non_dominated_sorting_algorithm(
            objective1_values2[:], objective2_values2[:])
        crowding_distance_values2 = []
        for i in range(0, len(non_dominated_sorted_solution2)):
            crowding_distance_values2.append(crowding_distance(
                objective1_values2[:], objective2_values2[:], non_dominated_sorted_solution2[i][:]))
        new_solution = []
        for i in range(0, len(non_dominated_sorted_solution2)):
            non_dominated_sorted_solution2_1 = [index_locator(
                non_dominated_sorted_solution2[i][j], non_dominated_sorted_solution2[i]) for j in range(0, len(non_dominated_sorted_solution2[i]))]
            front22 = sort_by_values(
                non_dominated_sorted_solution2_1[:], crowding_distance_values2[i][:])
            front = [non_dominated_sorted_solution2[i][front22[j]]
                     for j in range(0, len(non_dominated_sorted_solution2[i]))]
            front.reverse()
            for value in front:
                new_solution.append(value)
                if(len(new_solution) == population):
                    break
            if (len(new_solution) == population):
                break
        solution = [solution2[i] for i in new_solution]
        gen_no = gen_no + 1
    return [objective1_values, objective2_values]

# plot kurva
def non_dominating_curve_plotter(objective1_values, objective2_values):
    plt.figure(figsize=(15, 8))
    objective1 = [i * -1 for i in objective1_values]
    objective2 = [j * -1 for j in objective2_values]
    plt.xlabel('Fungsi Objektif 1', fontsize=15)
    plt.ylabel('Fungsi Objektif 2', fontsize=15)
    plt.scatter(objective1, objective2, c='red', s=25)
    plt.show()


# output operasi
# input dimasukkan ke fungsi NSGA-II
objective1_values, objective2_values = nsga2(
    population, max_gen, min_value, max_value)
print('nilai objektif 1:\n', objective1_values)
print('')
print('nilai objektif 2:\n', objective2_values)
print('')

# kurva non-dominasi
non_dominating_curve_plotter(objective1_values, objective2_values)

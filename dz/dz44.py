# Задача 1. Пересечение множеств
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
intersection = A & B
print("Пересечение A и B:", intersection)

# Задача 2. Объединение множеств
X = {'a', 'b', 'c'}
Y = {'b', 'd', 'e'}
union = X | Y
print("Объединение X и Y:", union)

# Задача 3. Разность множеств
P = {10, 20, 30, 40}
Q = {30, 50}
difference = P - Q
print("Разность P \ Q:", difference)

# Задача 4. Подмножество
M = {1, 2, 3, 4}
N = {2, 3}
is_subset = N.issubset(M)
print("N является подмножеством M:", is_subset)

# Задача 5. Количество подмножеств
Z = {'x', 'y', 'z'}
num_subsets = 2 ** len(Z)
print("Количество подмножеств множества Z:", num_subsets)

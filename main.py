from parse import *

COUNT = 0

def recursive_search(A, depth, cost_max, action_max, ALPHA):
    global COUNT
    COUNT += 1
    if depth == len(A) or cost_max == 0:
        return (contrib(A, D, 1, ALPHA), contrib(A, D, 2, ALPHA), contrib(A, D, 3, ALPHA)), action_max
    else:
        A1 = A[:depth] + [[1,0,0]] + A[depth+1:]
        A2 = A[:depth] + [[0,1,0]] + A[depth+1:]
        A3 = A[:depth] + [[0,0,1]] + A[depth+1:]

        v1, a1 = (0,0,0), A1
        v2, a2 = (0,0,0), A2
        v3, a3 = (0,0,0), A3
        v4, a4 = (0,0,0), A

        if C[depth][0] <= cost_max:
            v1, a1 = recursive_search(A1, depth+1, cost_max - C[depth][0], A1, ALPHA)
        if C[depth][1] <= cost_max:
            v2, a2 = recursive_search(A2, depth+1, cost_max - C[depth][1], A2, ALPHA)
        if C[depth][2] <= cost_max:
            v3, a3 = recursive_search(A3, depth+1, cost_max - C[depth][2], A3, ALPHA)
        v4, a4 = recursive_search(A, depth+1, cost_max, A, ALPHA)

        # max = lexmax([v1, v2, v3, v4])
        # if max == v1:
        #     action_max = a1
        # elif max == v2:
        #     action_max = a2
        # elif max == v3:
        #     action_max = a3
        # elif max == v4:
        #     action_max = a4
        
        # Computing lexmax locally for more efficiency
        m = v1
        argmax = a1
        for (a,v) in zip([a1, a2, a3, a4], [v1, v2, v3, v4]):
            if lex_ord(m, v): # m < v
                m = v
                argmax = a
        action_max = argmax

        return lexmax([v1, v2, v3, v4]), action_max
    
ALPHA = 1
COSTMAX = 7
A = [
    [0, 0, 0] for i in range(14)
]

contributions, actions = recursive_search(A, 0, COSTMAX, A, ALPHA)
print('Critères: ', contributions)
print('Coût: ', cost(actions, C))
print('Actions: ')
for a in get_actions(actions, FULLDATA):
    print('    '+a)
print('Number of recursive calls: ', COUNT)

# Answer:
# Critères:  (0.79, 0.05, 0.02)
# Coût:  10.0
# Actions:
# Barrage écrêteur 8m
# Murets de protection centre ville
# Puits infiltration dans le Nord de la ville et la basse ville
# Revêtements de sol perméables dans toute la ville
# Délocaliser les 12 bâtiments les plus critiques
# Extension zone Naturelle dans la ville nouvelle
# Number of recursive calls:  11540078
# python3.11 main.py  187,75s user 0,77s system 101% cpu 3:06,41 total
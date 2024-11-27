from itertools import combinations

def all_variants(text):
    for i in range(1, len(text) + 1):
        for comb in combinations(text, i):
            yield ''.join(comb)

a = all_variants("abc")
for i in a:
    print(i)
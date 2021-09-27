"""udregn alle kombinationsmuligheder ved altid at prøve at
    regne det næste tal ud"""

seq = [1, 2, 3, 4]
past_permutations = []
this_permutation = []
for i in range(10):

    is_num_added = False

    print(this_permutation, "this_permutation")

    for val in [num for num in seq if num not in this_permutation]:
        print(this_permutation + [val], "compare", this_permutation + [val] in past_permutations)
        if not this_permutation + [val] in past_permutations:
            this_permutation.append(val)
            is_num_added = True
            break

    if not is_num_added:
        print(this_permutation, "not popped")
        past_permutations.append(this_permutation)
        print(past_permutations, "past permutations")
        this_permutation.pop(-1)
        print(this_permutation, "popped")

    """if len(this_permutation) == len(seq):
        pass
        past_permutations.append(this_permutation)
        print(past_permutations, "past_permutations")
"""
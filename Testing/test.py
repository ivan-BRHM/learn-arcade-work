sequence = [1, 2, 3]
for inc in range(6):

    k = 0
    i = 0

    for n in sequence[:-1]:
        if n < sequence[sequence.index(n) + 1]:
            k = n - 1

    for n in sequence:
        if n > k:
            i = n - 1

    print(f"{sequence[:k]}, {sequence[i]}, {sequence[k + 1:i]}, {sequence[k]}, {sequence[i+1:]}")

    print(k, i)
    print(sequence)
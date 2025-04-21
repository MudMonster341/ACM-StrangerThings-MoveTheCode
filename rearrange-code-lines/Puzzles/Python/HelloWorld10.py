def take(gen, n):
    result = []
    for _ in range(n):
        result.append(next(gen))
    return result

evens = (x for x in range(20) if x % 2 == 0)
print(take(evens, 5))

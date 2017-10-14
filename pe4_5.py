def kwadraten_som(grondgetallen):
    som = 0
    for i in grondgetallen:
        if i >= 0:
            i = i**2
            som = som + i
    return som


lijst = [4, 5, 3, -81]
print(kwadraten_som(lijst))

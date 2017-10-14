def standaardprijs(afstandKM):
    k = 0.80 * afstandKM
    if afstandKM > 50.0:
        k = 15.0 + ((afstandKM - 50.0) * 0.60)
        return k
    elif afstandKM <= 0.0:
        k = 0.0 * afstandKM
        return k
    else:
        return k


def ritprijs(leeftijd, weekendrit, afstandKM):
    p = standaardprijs(afstandKM)
    if weekendrit == "nee" and (leeftijd < 12 or leeftijd >= 65):
        p = p * 0.7
        return p
    elif weekendrit == "ja" and (leeftijd < 12 or leeftijd >= 65):
        p = p * 0.65
        return p
    elif weekendrit == "nee" and 12 <= leeftijd < 65:
        return p
    elif weekendrit == "ja" and 12 <= leeftijd < 65:
        p = p * 0.6
        return p


lt = eval(input("Leeftijd: "))
wk = input("Weekendrit: ")
km = eval(input("Afstand: "))
p = ritprijs(lt, wk, km)
print("Je betaalt:", p)

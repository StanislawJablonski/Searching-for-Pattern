import time

def RK(text, pattern):
    q = 397

    #usowanie spacji, nowych lini, tabow
    temp = pattern.split()
    pattern = "".join(temp)
    temp = text.split()
    text = "".join(temp)

    found = []

    #czy  pattern jest none albo empty
    if pattern is None or not pattern:
        print("Wzor ma dlugosc 0")
        return

    # text jest None, albo dl text jest mniejsza niz dl pattern
    if text is None or len(pattern) > len(text):
        print("Nie znaleziono wzoru")
        return

    m = len(pattern)
    n = len(text)

    h = 1
    for i in range(m-1):
        h = (h*10) % q

    p = 0
    t = 0
    # Haszowanie
    for i in range(m):
        p = (10*p + ord(pattern[i])) % q    # ord() zwraca wartosc znaku  w ASCII
        t = (10*t + ord(text[i])) % q

    j = 0
    # Szukanie wzorca
    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break

            j += 1
            if j == m:
                #print("Wzor znaleziony na pozycji: " + str(i))
                found.append(int(i))

        if i < n-m:
            t = (10*(t-ord(text[i])*h) + ord(text[i+m])) % q

            if t < 0:
                t = t+q
    return found


def KMP(text, pattern):

    #usowanie spacji, nowych lini, tabow
    temp = pattern.split()
    pattern = "".join(temp)
    temp = text.split()
    text = "".join(temp)

    found = []

    #czy  pattern jest none albo empty
    if pattern is None or not pattern:
        print("Wzor ma dlugosc 0")
        return

    # text jest None, albo dl text jest mniejsza niz dl pattern
    if text is None or len(pattern) > len(text):
        print("Nie znaleziono wzoru")
        return

    m = len(pattern)
    n = len(text)

    #lp[] tablica najdlozszych prefixow
    lp = [0] * m
    j = 0  # index w pattern[]

    # Uzupelnianie tablicy
    LPTab(pattern, m, lp)

    i = 0  # index w txt[]
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            #print("Wzor znaleziony na pozycji " + str(i - j))
            found.append(int(i - j))
            j = lp[j - 1]

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lp[j - 1]
            else:
                i += 1
    return found


def LPTab(pattern, m, lp):
    len = 0  # dl prefixu

    for i in range(1,m):
        if pattern[i] == pattern[len]:
            len += 1
            lp[i] = len
            i += 1
        else:
            if len != 0:
                len = lp[len - 1]
            else:
                lp[i] = 0
                i += 1


if __name__ == '__main__':
    with open("tekst2.txt", 'r') as t, open("wzorzec2.txt", 'r') as p:

        pattern = p.readlines()
        text = t.readlines()
        t = text
        pattern = "".join(pattern)
        text = "".join(text)

        startRK = time.time()
        rkFound = RK(text,pattern)
        endRK = time.time()
        startKMP = time.time()
        kmpFound = KMP(text,pattern)
        endKMP = time.time()

        print("RK _______________________________________")
        counter2 = 0
        for x in range(0,len(t)):
            counter = 0
            for y in t[x]:
                counter += 1
                if counter2 in rkFound:
                    print("Wzor znaleziono w linii nr: " + str(x+1) + " na pozycji nr: " + str(counter))
                counter2 += 1

        print("KMP _______________________________________")
        counter2 = 0
        for x in range(0,len(t)):
            counter = 0
            for y in t[x]:
                counter += 1
                if counter2 in kmpFound:
                    print("Wzor znaleziono w linii nr: " + str(x+1) + " na pozycji nr: " + str(counter))
                counter2 += 1

        print("__________________________________________")
        print("Czas wykonywania wyszukiwania RK: ", (endRK - startRK))
        print("Czas wykonywania wyszukiwania KMP: ", (endKMP - startKMP))




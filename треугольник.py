P1 = [1, 0]
P2 = [2, 0]
P3 = [2, 4]
Ptest = [1.5, 1]

def dist(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

a = dist(P2, P3)
b = dist(P1, P3)
c = dist(P1, P2)



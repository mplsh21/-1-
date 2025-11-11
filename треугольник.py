P1 = [1, 0]
P2 = [2, 0]
P3 = [2, 4]
Ptest = [1.5, 1]

def dist(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

a = dist(P2, P3)
b = dist(P1, P3)
c = dist(P1, P2)

d1 = dist(P1, Ptest)
d2 = dist(P2, Ptest)
d3 = dist(P3, Ptest)

s_main = (a + b + c) / 2
s1 = (c + d1 + d2) / 2
s2 = (b + d1 + d3) / 2
s3 = (a + d2 + d3) / 2

def heron(p, x, y, z):
    return np.sqrt(p * (p - x) * (p - y) * (p - z))

S_main = heron(s_main, a, b, c)
S1 = heron(s1, c, d1, d2)
S2 = heron(s2, b, d1, d3)
S3 = heron(s3, a, d2, d3)
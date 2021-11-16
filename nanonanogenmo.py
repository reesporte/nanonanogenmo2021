from random import choice as x

t = open("i", "r").read().split()
n = {}
for i in range(len(t) - 1):
    w = t[i]
    if n.get(w, None):
        n[w].append(t[i + 1])
    else:
        n[w] = [t[i + 1]]
o = open("o", "w")
c = "a"
for i in range(50000):
    o.write(c + " ")
    c = x(n[c])
o.close()

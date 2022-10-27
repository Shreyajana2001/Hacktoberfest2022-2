def has_descendants(m, Z):
    for des in G[m]:
        if des in Z:
            return True
    return False

def marked_parent(n):
    s = ['A']
    while len(s)!=0:
        print(s)
        cur = s[0]
        s.remove(cur)
        print(s)
        if len(G[cur]) != 0:
            for ch in G[cur]:
                print(ch)
                if ch == n and edg[tuple({cur, ch})] == 1:
                    print(cur)
                    return cur
            s.append(ch)
    return ''

def cost_revise(n):
    Z = [n]
    while True:
        print(Z)
        if len(Z) == 0:
            return
        for m in Z:
            initial_cost = f[m]
            if has_descendants(m, Z):
                Z.pop()
                break
            if m in AND_NODES:
                sol = True
                for r in G[m]:
                    f[m] += f[r] + 1
                    edg.update({tuple({m, r}): 1})
                    if solved[r] == 0:
                        sol = False
                if sol == True:
                    solved[m] = 1
            else:
                sol = True
                for r in G[m]:
                    f[m] = min(f[r] + 1, f[m])
                min_cost = 10000
                for r in G[m]:
                    if f[r] < min_cost:
                        min_cost = f[r]
                        best_successor = r
                edg.update({tuple({m, best_successor}): 1})
                if solved[best_successor] == 1:
                    solved[m] = 1
            if initial_cost != f[m]:
                print(f)
                mp = marked_parent(m)
                print(m, mp)
                if mp != '':
                    Z.append(mp)
            print(f)

def ao_star(G, s,T):
    g_star = [s]
    f[s] = h[s]
    while True:
        print(s)
        if s in T:
            solved[s] = 1
            return
        for n in G[s]:
            if len(G[n]) == 0:
                continue
            for m in G[s]:
                f[m] = h[m]
                if m in T:
                    solved[m] = 1
            cost_revise(n)
            
        

h = {'A': 50, 'B': 6, 'C':2, 'D' : 12, 'E': 2,'F':3, 'G': 5, 'H': 7, 'I': 7, 'J': 1}
f = {'A': 0, 'B': 0, 'C':0, 'D' : 0, 'E': 0,'F':0, 'G': 0, 'H': 0, 'I': 0, 'J': 0}
edg = {tuple({'A', 'B'}) : 0, tuple({'A', 'C'}) : 0, tuple({'A', 'D'}) : 0, tuple({'B', 'G'}) : 0,
       tuple({'B', 'H'}) : 0, tuple({'C', 'J'}) : 0, tuple({'D', 'E'}) : 0, tuple({'D', 'F'}) : 0,
       tuple({'G', 'I'}) : 0}
solved = {'A': 0, 'B': 0, 'C':0, 'D' : 0, 'E': 0,'F':0, 'G': 0, 'H': 0, 'I': 0, 'J': 0}
G = {'A' :['B', 'C', 'D'],
     'B' :['G', 'H'],
     'C' :['J'],
     'D': ['E', 'F'],
     'E': [],
     'F': [],
     'G': ['I'],
     'H': [],
     'I': []
     }
AND_NODES = ['A', 'D']
T = ['I', 'H', 'J', 'E', 'F' ]
s = 'A'
print(G[s])
ao_star(G, s, T)
print(f)

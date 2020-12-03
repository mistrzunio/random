with open('input3.txt') as f:
    c = f.readlines()

def trav(c, hor=1, ver=1):
    x = 0 if ver==1 else 1
    y = 1
    line = 1
    sc = { '.': 0, '#': 0 }
    for l in c:
        if line == 1 and ver > 1:
            True # skipping
        else:
            if y<ver:
                # skipping
                y+=1
            else:
                y = 1
                length = len(l)-1
                sc[l[x]] += 1

                x = x + hor if x + hor < length else (x + hor) % length
        line += 1
    return sc

t1 = trav(c,1)
t3 = trav(c,3)
t5 = trav(c,5)
t7 = trav(c,7)
t12 = trav(c,1,2)

print (t3)
print(t1['#']*t3['#']*t5['#']*t7['#']*t12['#'])

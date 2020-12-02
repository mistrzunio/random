def proc(line):
    el = line.split()
    ran = el[0].split('-')
    return [int(ran[0]),int(ran[1]),el[1][0],el[2]]

with open('input.txt') as f:
    pwd = f.readlines()\

res = map(proc, pwd)
num = 0
num2 = 0
for case in list(res):
    occ = case[3].count(case[2])
    if occ >= case[0] and occ <= case[1]:
        # print(case)
        num += 1
    fm = case[3][case[0]-1] == case[2]
    sm = case[3][case[1]-1] == case[2]
    if fm  ^ sm:
        # rint(case)
        num2 += 1
print(num)
print(num2)

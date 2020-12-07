import re

with open('input4.txt') as f:
    c = f.readlines()

vld = {
    'byr': lambda y: 1920 <= int(y) <= 2002,
    'iyr': lambda y: 2010 <= int(y) <= 2020,
    'eyr': lambda y: 2020 <= int(y) <= 2030,
    'hgt': lambda n: True if (
                                     n[-2:] == 'cm' and 150 <= int(n[0:-2]) <= 193
                             ) or (
                                     n[-2:] == 'in' and 59 <= int(n[0:-2]) <= 76
    ) else False,
    'hcl': lambda n: True if re.search('^#[0-9a-f]{6}$',n) else False,
    'ecl': lambda c: True if c in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] else False,
    'pid': lambda n: True if re.match('^[0-9]{9}$',n) else False,
    'cid': lambda x: True
}

new = {'byr': False, 'iyr': False, 'eyr': False, 'hgt': False, 'hcl': False, 'ecl': False, 'pid': False, 'cid': False }
curr = dict(new)
valids1 = 0
valids2 = 0
vald2cond = True
while len(c):
    l = c.pop(0)
    li = l.split()
    if li:
        for el in li:
            prop = el.split(':')
            curr[prop[0]] = True
            if not vld[prop[0]](prop[1]):
                vald2cond = False
    else:
        if curr['byr'] and curr['iyr'] and curr['eyr'] and curr['hgt'] and curr['hcl'] and curr['ecl'] and curr['pid']:
            valids1 += 1
            if vald2cond:
                valids2 += 1
        curr = dict(new)
        vald2cond = True

print (valids1, valids2)

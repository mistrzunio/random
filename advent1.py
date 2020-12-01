with open('input.txt') as f:
    content = f.readlines()

numbers = [int(i) for i in content]

numbers.sort()

pivot = 0
beg = 1
end = -1
tries = 0
giveup = False

while numbers[pivot]+numbers[beg]+numbers[end] != 2020 and not giveup:
    tries += 1
    if numbers[pivot]+numbers[beg]+numbers[end] > 2020:
        end -=1
    if numbers[pivot]+numbers[beg]+numbers[end] < 2020:
        beg +=1
    if tries == len(numbers):
        pivot += 1
        beg = 0
        end = -1
    if pivot > len(numbers):
        giveup = True

print(giveup)

print(numbers[pivot])
print(numbers[beg])
print(numbers[end])

print(numbers[pivot]*numbers[beg]*numbers[end])

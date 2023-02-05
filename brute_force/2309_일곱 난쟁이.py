# 9명 중에 난쟁이가 아닌 2명을 고르면 된다. -> 경우의 수 : 9C2 = 36 이므로 모든 경우의 수를 사용해서 해결

dwarf = []
twiceBreak = False
for i in range(9):
    height = int(input())
    dwarf.append(height)
dwarf.sort()
all_dwarf = sum(dwarf)
for i in range(9):
    for j in range(i+1, 9):
        if all_dwarf - (dwarf[i]+dwarf[j]) == 100:
            dwarf.remove(dwarf[i])
            dwarf.remove(dwarf[j-1])
            twiceBreak = True
            break
    if twiceBreak == True:
        break

print(*dwarf, sep='\n')
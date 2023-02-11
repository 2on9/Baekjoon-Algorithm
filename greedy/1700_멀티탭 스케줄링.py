#동일한 제품이 멀티탭에 꽂혀있을 경우는 그냥 넘어가고, 멀티탭에 빈자리가 있다면 빈자리에 그냥 꽂아주고 빈자리가 없다면 우선순위(이후에 또 나오는지, 나온다면 얼마나 빨리 나오는지)를 정해서 우선순위가 낮은 제품을 빼고 꽂아주면 된다.
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
appliance = list(map(int, input().split()))
multitap = [0] * N
cnt = 0
change = maximum = 0

while appliance:
    product = appliance[0]
    if product in multitap: # 동일한 제품이 멀티탭에 꽂혀있을 경우는 패스
        appliance.remove(product)
        continue
    elif 0 in multitap: # 멀티탭에 빈자리가 있다면 빈자리에 꽂아준다.
        multitap[multitap.index(0)] = product
        appliance.remove(product)
    else: # 멀티탭에 빈자리가 없다면
        for mt in multitap: # 멀티탭에 꽂혀있는 제품 중에서
            if mt not in appliance: # 이후에 또 나오는지 -> 안 나온다면 우선순위가 젤 낮으므로 먼저 빼버린다.
                change = mt
                break
            else: # 이후에 또 나온다면 
                if appliance.index(mt) > maximum: # 더 늦게 사용되는 제품을 빼준다.
                    change = mt
                    maximum = appliance.index(mt)
        multitap[multitap.index(change)] = product
        appliance.remove(product)
        cnt += 1
        maximum = 0 

print(cnt)
time=int(input())
entry=[int(x) for x in input().split()]
exit=[int(x) for x in input().split()]
count=0
guests=[]
for i in range(len(entry)):
count=count+entry[i]-exit[i]
guests.append(count)
print(max(guests))

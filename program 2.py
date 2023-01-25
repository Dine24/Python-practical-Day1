def sumsquare(numbers):
    return [
        sum(map(lambda x: x**2, [i for i in numbers if i%2==1])),
        sum(map(lambda x: x**2, [i for i in numbers if i%2==0]))
    ]
results = sumsquare([2,4,5,6,7,11,12,13])
print(results)

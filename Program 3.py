def is_Happy_num(n):
  x = set()
  while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in x:
            return False
        x.add(n)
  return True
n=int(input("enter a n: "));
print(is_Happy_num(n))



nums = [10, 20, 30]

for n in nums:
   print(n)


nums = [10, 20, 30]

it = iter(nums)
print(next(it))
print(next(it))
print(next(it))



def test():
   return 5
print(test())

def numbers():
   yield 1
   yield 2
   yield 3

gen = numbers()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


nums = list(range(1000000))
def nums():
   for i in nums:
      yield i
      

# bubble sort a list
# (See lab1.pdf for requirements.)

def bubblesort(alist):
   for i in range(len(alist)):
      for n in range(len(alist) - 1):
         if alist[n] > alist[n+1]:
            alist[n], alist[n+1] = alist[n+1], alist[n] 
if __name__ == "__main__":
    a = [1,3,5,2,9,6,7,5]
    b = [42]       # special singleton case 
    c = []         # special empty list case 
    bubblesort(a)
    bubblesort(b)
    bubblesort(c)
    print(a)       # => [1,2,3,5,5,6,7,9]
    print(b)       # => [42]
    print(c)       # => [] 

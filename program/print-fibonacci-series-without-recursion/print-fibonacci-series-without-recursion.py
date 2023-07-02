terms = int(input("Enter the number of terms:"))
f, s = 0, 1
print("Fibonacci series are:")
print(f, s, end=" ")
for i in range(2,terms):
    t = f + s
    f = s
    s = t
    print(t, end=" ")
    terms = terms - 1

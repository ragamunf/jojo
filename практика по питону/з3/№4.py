def lace(a, b, l, N):
    return 2*l + 2*b*(N-1) + a*(2*N-1)
a, b, l, N = int(input()), int(input()), int(input()), int(input())
print(lace(a, b, l, N))
    

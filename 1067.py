import math
import sys
input = sys.stdin.readline

def fft(x):
    N = len(x)
    if N <= 1: return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [math.e**(-2j * math.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

def ifft(x):
    N = len(x)
    if N <= 1: return x
    even = ifft(x[0::2])
    odd = ifft(x[1::2])
    T = [math.e**(2j * math.pi * k / N) * odd[k] for k in range(N // 2)]
    return [(even[k] + T[k]) / 2 for k in range(N // 2)] + [(even[k] - T[k]) / 2 for k in range(N // 2)]

def convolve_fft(a, b):
    N = len(a) + len(b) - 1
    n = 1
    while n < N: n *= 2  # n을 N보다 크거나 같은 최소의 2의 거듭제곱으로 설정
    a += [0] * (n - len(a))
    b += [0] * (n - len(b))
    
    fft_a = fft(a)
    fft_b = fft(b)
    fft_product = [x*y for x, y in zip(fft_a, fft_b)]
    convolution = ifft(fft_product)
    
    return [x.real for x in convolution][:N]

def find_max_convolution(a, b):
    conv_result = convolve_fft(a, b)
    max_value = max(conv_result)
    return max_value, conv_result.index(max_value)



N = int(input())
x = list(map(int,input().strip().split()))
y = list(map(int,input().strip().split()))*2

max_value, index = find_max_convolution(y, x) #근데 max val이 정확하지 않음

index = (index - 1)%N
new_y = y[index:index+N]
ans = 0
for j in range(N):
    ans += x[j] * new_y[j]

print(ans)
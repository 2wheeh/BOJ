import sys
sys.stdin = open('1074.txt', 'r')
input = sys.stdin.readline

N, r, c = map(int, input().rstrip().split())
step = 0
# N : 1 ~ 15

def get_quadrant(n, c, r):
    global step
    if n == 0:
        return
    else:
        x = c // 2**(n-1)
        y = r // 2**(n-1)

        if [x, y] == [0, 0]:
            k = 0
        elif [x, y] == [1, 0]:
            k = 1
        elif [x, y] == [0, 1]:
            k = 2
        else:
            k = 3

        step += k*4**(n-1)

        c %= 2**(n-1)
        r %= 2**(n-1)
        get_quadrant(n-1, c, r)
    
get_quadrant(N, c, r)
print(step)


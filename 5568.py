import sys
from itertools import permutations
sys.stdin = open('5568.txt', 'r')
input = sys.stdin.readline
nPk = permutations

n = int(input())
k = int(input())

card_list = [input().rstrip() for _ in range(n)]
numbers = list(nPk(card_list, k))
numbers = set(map(''.join, numbers))
print(len(numbers))



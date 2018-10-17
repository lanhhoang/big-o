# https://www.hackerrank.com/challenges/find-the-median/problem

n = int(input())
ar = list(map(int, input().split()))

ar.sort()
print(ar[n//2])
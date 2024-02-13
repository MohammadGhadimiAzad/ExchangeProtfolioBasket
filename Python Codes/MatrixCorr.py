from random import random

def corrTitle(a, b):
  return a + '-' + b + '-'

def corr(a, b):
  return a + b

def GetData(usd):
  return random()

arr = ["BTC", "ETH", "USDT", "BNB", "USDC", "BUSD"]
n = len(arr)
matrix = [([0]*n) for i in range(n)]
arr_data = [([0]*n)][0]


for i in range(n):
  arr_data[i] = GetData(arr[i])


for i in range(n):
  for j in range(n):
      if (i == j):
        matrix[i][j] = 1
      elif (matrix[i][j] == 0):
        matrix[i][j] = matrix[j][i] = corrTitle(arr[i], arr[j]) + str( corr(arr_data[i], arr_data[j]) )


print(matrix)

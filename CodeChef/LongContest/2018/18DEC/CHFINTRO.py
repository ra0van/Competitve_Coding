def main():
  n,r = map(int,input().split())
  good = "Good boi"
  bad = "Bad boi"
  for _ in range(n):
    R = int(input())
    if R < r:
      print(bad)
    else:
      print(good)

if __name__ == '__main__':
  main()
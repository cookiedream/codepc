def f(a):
  if a==0 or a==1:
    return a+1
  else:
    return f(a-1)+f(a//2)
while True:
  try:
    k =int(input())
    print(f(k))
  except:
    break
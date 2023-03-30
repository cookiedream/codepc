while True:
  try:
    a = [float(j) for j in input().split()]
    max = a[0]
    min = a[9]
    for i in range(10):
      if a[i]>max:
        max = a[i]
      elif a[i]<min:
        min = a[i]
    print("maximum:"+format(max,'.2f'))
    print("minimum:"+format(min,'.2f'))
  except:
    break
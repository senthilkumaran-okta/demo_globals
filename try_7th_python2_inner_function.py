def outer():
  x = 1
  def inner():
    x += 1
    print("inner:", x)
  inner()
  print("outer:", x)

if __name__ == '__main__':
  outer()


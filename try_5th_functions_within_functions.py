MODULE_GLOBAL = 10

def function2():
  MODULE_GLOBAL = 20

  def inner_function3():
    print MODULE_GLOBAL

  def inner_function4():
    global MODULE_GLOBAL
    MODULE_GLOBAL = 40
    # This mutates the global scope.

  inner_function3()
  inner_function4()

def function3():
  print MODULE_GLOBAL

if __name__ == '__main__':
    function2()
    function3()

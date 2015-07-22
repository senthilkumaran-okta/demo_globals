MAIN_GLOBAL = None

print MAIN_GLOBAL



def function1():
  try:
    print MAIN_GLOBAL
  except UnboundLocalError as e:
    # If you define a local variable by the same name in the module's function scope
    # (i.e in the line number 14 below), you wont be able to access the global as the
    # local scope over-shadows it.
    print "Caught Exception:", e

  MAIN_GLOBAL = 42
  # This is a local variable to function1
  print MAIN_GLOBAL

# This will again print None
print MAIN_GLOBAL

def function2():
  print MAIN_GLOBAL
  print "Look ma. NO Unbound Local Error!"


def function3():
  print "I am going to override the MAIN_GLOBAL"
  global MAIN_GLOBAL

  MAIN_GLOBAL = "overriden."


def function4():
  print "If function3 is called ahead of me, I will be:"
  print MAIN_GLOBAL

if __name__ == '__main__':
  function1()
  function2()
  function3()
  function4()

from pkg1.module1 import GLOBAL_MODULE_VARIABLE1, function1
from pkg2.module2 import GLOBAL_MODULE_VARIABLE2, function2


# Try to override values.

GLOBAL_MODULE_VARIABLE1 = "overridden_global_module_variable1"
GLOBAL_MODULE_VARIABLE2 = "overridden_global_module_variable2"


def main():
  print GLOBAL_MODULE_VARIABLE1
  print GLOBAL_MODULE_VARIABLE2

  # What are they in those functions?
  function1()
  function2()

  # They remain unchanged.
  # These GLOBAL_MODULE_VARIABLE1, and GLOBAL_MODULE_VARIABLE2 are in this modules scope
  # shadowing the imports and can treated similar variables in try_1st_access_within_funtion.py

if __name__ == '__main__':
  main()

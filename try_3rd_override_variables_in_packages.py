from pkg1 import module1
from pkg1.module1 import function1


def explicit_override_function():
  module1.GLOBAL_MODULE_VARIABLE1 = "explictly_overriding_global_module_variable1"
  function1()

if __name__ == '__main__':
  explicit_override_function()


if(EXISTS "C:/Users/dimac/OneDrive/Рабочий стол/ООП/Dev/CPP/LR-2/out/build/x64-Debug/tests/number_tests[1]_tests.cmake")
  include("C:/Users/dimac/OneDrive/Рабочий стол/ООП/Dev/CPP/LR-2/out/build/x64-Debug/tests/number_tests[1]_tests.cmake")
else()
  add_test(number_tests_NOT_BUILT number_tests_NOT_BUILT)
endif()

cmake_minimum_required (VERSION 2.6)

add_executable(Test main.cpp)

INSTALL(TARGETS Test DESTINATION bin)

add_subdirectory(python)
add_subdirectory(ui)

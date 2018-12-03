cmake_minimum_required (VERSION 2.6)

file(GLOB UI_FILES "*.ui")
foreach(UI_FILE ${UI_FILES})
  # Create the auto-gen file
  #message("${UI_FILE}")
  execute_process(COMMAND pyuic4 "${UI_FILE}"
                  WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
                  RESULT_VARIABLE RESULT
                  OUTPUT_VARIABLE AUTO_GEN_FILE_TEXT)
  # Write the generated file
  get_filename_component(FILE_NAME ${UI_FILE} NAME)
  file(WRITE ${CMAKE_CURRENT_BINARY_DIR}/${FILE_NAME}.py ${AUTO_GEN_FILE_TEXT})
  install(FILES ${CMAKE_CURRENT_BINARY_DIR}/${FILE_NAME}.py DESTINATION ${CMAKE_INSTALL_PREFIX}/python)
endforeach()



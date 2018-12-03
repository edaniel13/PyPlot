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
  get_filename_component(FILE_NAME ${UI_FILE} NAME_WE)
  file(WRITE ${CMAKE_CURRENT_BINARY_DIR}/${FILE_NAME}_ui.py ${AUTO_GEN_FILE_TEXT})
  install(FILES ${CMAKE_CURRENT_BINARY_DIR}/${FILE_NAME}_ui.py DESTINATION ${CMAKE_INSTALL_PREFIX}/python PERMISSIONS OWNER_EXECUTE OWNER_READ OWNER_WRITE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE)
endforeach()



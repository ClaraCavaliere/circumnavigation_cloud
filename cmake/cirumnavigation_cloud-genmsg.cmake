# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "cirumnavigation_cloud: 0 messages, 2 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg;-Igeomtwo:/home/smladmin/catkin_ws/src/geomtwo/msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(cirumnavigation_cloud_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/smladmin/catkin_ws/src/circumnavigation_cloud/srv/SensorService.srv" NAME_WE)
add_custom_target(_cirumnavigation_cloud_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "cirumnavigation_cloud" "/home/smladmin/catkin_ws/src/circumnavigation_cloud/srv/SensorService.srv" "geomtwo/Vector"
)

get_filename_component(_filename "/home/smladmin/catkin_ws/src/circumnavigation_cloud/srv/CloudService.srv" NAME_WE)
add_custom_target(_cirumnavigation_cloud_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "cirumnavigation_cloud" "/home/smladmin/catkin_ws/src/circumnavigation_cloud/srv/CloudService.srv" "geomtwo/Vector"
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(cirumnavigation_cloud
  "/home/smladmin/catkin_ws/src/circumnavigation_cloud/srv/SensorService.srv"
  "${MSG_I_FLAGS}"
  "/home/smladmin/catkin_ws/src/geomtwo/msg/Vector.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cirumnavigation_cloud
)
_generate_srv_cpp(cirumnavigation_cloud
  "/home/smladmin/catkin_ws/src/circumnavigation_cloud/srv/CloudService.srv"
  "${MSG_I_FLAGS}"
  "/home/smladmin/catkin_ws/src/geomtwo/msg/Vector.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cirumnavigation_cloud
)

### Generating Module File
_generate_module_cpp(cirumnavigation_cloud
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cirumnavigation_cloud
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(cirumnavigation_cloud_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(cirumnavigation_cloud_generate_messages cirumnavigation_cloud_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/smladmin/catkin_ws/src/circumnavigation_cloud/srv/SensorService.srv" NAME_WE)
add_dependencies(cirumnavigation_cloud_generate_messages_cpp _cirumnavigation_cloud_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/smladmin/catkin_ws/src/circumnavigation_cloud/srv/CloudService.srv" NAME_WE)
add_dependencies(cirumnavigation_cloud_generate_messages_cpp _cirumnavigation_cloud_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(cirumnavigation_cloud_gencpp)
add_dependencies(cirumnavigation_cloud_gencpp cirumnavigation_cloud_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cirumnavigation_cloud_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(cirumnavigation_cloud
  "/home/smladmin/catkin_ws/src/circumnavigation_cloud/srv/SensorService.srv"
  "${MSG_I_FLAGS}"
  "/home/smladmin/catkin_ws/src/geomtwo/msg/Vector.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cirumnavigation_cloud
)
_generate_srv_lisp(cirumnavigation_cloud
  "/home/smladmin/catkin_ws/src/circumnavigation_cloud/srv/CloudService.srv"
  "${MSG_I_FLAGS}"
  "/home/smladmin/catkin_ws/src/geomtwo/msg/Vector.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cirumnavigation_cloud
)

### Generating Module File
_generate_module_lisp(cirumnavigation_cloud
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cirumnavigation_cloud
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(cirumnavigation_cloud_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(cirumnavigation_cloud_generate_messages cirumnavigation_cloud_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/smladmin/catkin_ws/src/circumnavigation_cloud/srv/SensorService.srv" NAME_WE)
add_dependencies(cirumnavigation_cloud_generate_messages_lisp _cirumnavigation_cloud_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/smladmin/catkin_ws/src/circumnavigation_cloud/srv/CloudService.srv" NAME_WE)
add_dependencies(cirumnavigation_cloud_generate_messages_lisp _cirumnavigation_cloud_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(cirumnavigation_cloud_genlisp)
add_dependencies(cirumnavigation_cloud_genlisp cirumnavigation_cloud_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cirumnavigation_cloud_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(cirumnavigation_cloud
  "/home/smladmin/catkin_ws/src/circumnavigation_cloud/srv/SensorService.srv"
  "${MSG_I_FLAGS}"
  "/home/smladmin/catkin_ws/src/geomtwo/msg/Vector.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cirumnavigation_cloud
)
_generate_srv_py(cirumnavigation_cloud
  "/home/smladmin/catkin_ws/src/circumnavigation_cloud/srv/CloudService.srv"
  "${MSG_I_FLAGS}"
  "/home/smladmin/catkin_ws/src/geomtwo/msg/Vector.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cirumnavigation_cloud
)

### Generating Module File
_generate_module_py(cirumnavigation_cloud
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cirumnavigation_cloud
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(cirumnavigation_cloud_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(cirumnavigation_cloud_generate_messages cirumnavigation_cloud_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/smladmin/catkin_ws/src/circumnavigation_cloud/srv/SensorService.srv" NAME_WE)
add_dependencies(cirumnavigation_cloud_generate_messages_py _cirumnavigation_cloud_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/smladmin/catkin_ws/src/circumnavigation_cloud/srv/CloudService.srv" NAME_WE)
add_dependencies(cirumnavigation_cloud_generate_messages_py _cirumnavigation_cloud_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(cirumnavigation_cloud_genpy)
add_dependencies(cirumnavigation_cloud_genpy cirumnavigation_cloud_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS cirumnavigation_cloud_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cirumnavigation_cloud)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/cirumnavigation_cloud
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(cirumnavigation_cloud_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET geomtwo_generate_messages_cpp)
  add_dependencies(cirumnavigation_cloud_generate_messages_cpp geomtwo_generate_messages_cpp)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cirumnavigation_cloud)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/cirumnavigation_cloud
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(cirumnavigation_cloud_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET geomtwo_generate_messages_lisp)
  add_dependencies(cirumnavigation_cloud_generate_messages_lisp geomtwo_generate_messages_lisp)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cirumnavigation_cloud)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cirumnavigation_cloud\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/cirumnavigation_cloud
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(cirumnavigation_cloud_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET geomtwo_generate_messages_py)
  add_dependencies(cirumnavigation_cloud_generate_messages_py geomtwo_generate_messages_py)
endif()

cmake_minimum_required(VERSION 3.18)

project(IMGUI_GLFW)

add_library(imgui_impl_glfw
    backends/imgui_impl_glfw.cpp
)

target_include_directories(imgui_impl_glfw PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/backends ${IMGUI_INCLUDE_DIR} ${GLFW_INCLUDE_DIR})

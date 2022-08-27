cmake_minimum_required(VERSION 3.18)

project(IMGUI)

add_library(imgui_impl_opengl3
    backends/imgui_impl_opengl3.cpp
)

target_include_directories(imgui_impl_opengl3 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/backends ${IMGUI_INCLUDE_DIR})

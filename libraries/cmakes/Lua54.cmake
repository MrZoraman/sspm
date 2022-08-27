cmake_minimum_required(VERSION 3.18)

project(Lua54)

add_library(lua54 SHARED
    lapi.c
    lauxlib.c
    lbaselib.c
    lcode.c
    lcorolib.c
    lctype.c
    ldblib.c
    ldebug.c
    ldo.c
    ldump.c
    lfunc.c
    lgc.c
    linit.c
    liolib.c
    llex.c
    lmathlib.c
    lmem.c
    loadlib.c
    lobject.c
    lopcodes.c
    loslib.c
    lparser.c
    lstate.c
    lstring.c
    lstrlib.c
    ltable.c
    ltablib.c
    ltm.c
    lua.c
    lundump.c
    lutf8lib.c
    lvm.c
    lzio.c
)

target_include_directories(lua54 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

set_property(TARGET lua54 PROPERTY C_STANDARD 17)
set_property(TARGET lua54 PROPERTY C_STANDARD_REQUIRED ON)

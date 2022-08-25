from setup.libs.utf8 import Utf8
from setup.libs.sdl2 import Sdl2
from setup.libs.uv import Uv
from setup.libs.lua import Lua
from setup.libs.enet import Enet

def collect_dependencies(is_verbose):
    return [
        Utf8(is_verbose),
        Sdl2(is_verbose),
        Uv(is_verbose),
        Lua(is_verbose),
        Enet(is_verbose)
    ]
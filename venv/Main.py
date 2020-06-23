from Generate import *
from DrawSavedMap import *
from CreateMap import *

create_map = CreateMap()
generate("maps/pre_maps/cache.json")
drawSavedMap("maps/final_maps/cache.json")



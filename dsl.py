
import json

# class JsonSerializable(object):
#     def toJson(self):
#         return json.dumps(self.__dict__)
#
#     def __repr__(self):
#         return self.toJson()

class Tile(object):
    """Tile representation"""

    def __init__(self, tile_id, map_x, map_y, tile_x = 1, tile_y = 1):
        super(Tile, self).__init__()
        self.tile_id = tile_id
        self.map_x = map_x
        self.map_y = map_y
        self.tile_x = tile_x
        self.tile_y = tile_y

t = Tile("green", 1, 1)

print(t.__dict__)

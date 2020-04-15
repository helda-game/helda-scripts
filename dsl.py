
import json

# class JsonSerializable(object):
#     def toJson(self):
#         return json.dumps(self.__dict__)
#
#     def __repr__(self):
#         return self.toJson()

# (s/defschema Msg
#   {
#     :msg_id s/Int ;should be unique on WorldUpdate entity.
#     :msg_body s/Str})

class Msg(object):
    """Msg representation"""

    seq_num = 0

    def __init__(self, msg_body):
        super(Msg, self).__init__()
        Msg.seq_num += 1
        self.msg_id = Msg.seq_num
        self.msg_body = msg_body

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
m = Msg("HELLO")
m2 = Msg("WORLD")

print(t.__dict__)
print(m.__dict__)
print(m2.__dict__)


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

class WorldUpdateBuilder(object):
    """WorldUpdateBuilder"""

    def __init__(self,
        seq_num = 1,
        drawing = {'background_tiles' : [], 'foreground_tiles' : [], 'sprites': []}
        ):

        super(WorldUpdateBuilder, self).__init__()
        self.seq_num = seq_num
        self.drawing = drawing
        self.msgs = []

    def draw_bg_tile(self, tile):
        self.remove_bg_tile(tile.map_x, tile.map_y)
        self.drawing['background_tiles'].append(tile.__dict__)

    def remove_bg_tile(self, map_x, map_y):
        self.drawing['background_tiles'] = [
            tile for tile in self.drawing['background_tiles']
            if (tile.map_x == map_x) and (tile.map_y == map_y) ]

    def draw_fg_tile(self, tile):
        self.drawing['foreground_tiles'].append(tile.__dict__)

    def draw_sprite(self, tile):
        self.drawing['sprite'].append(tile.__dict__)

    def print_msg(self, msg):
        self.msgs.append(msg.__dict__)

    def new_update(self):
        self.seq_num += 1
        self.msgs = []

t = Tile("green", 1, 1)
m = Msg("HELLO")
m2 = Msg("WORLD")

w = WorldUpdateBuilder()
w.draw_bg_tile(t)
w.print_msg(m)
w.print_msg(m2)
print(w.__dict__)

import dsl
import worker

def process_iteration(i, ctx):
    if not ctx:
        t = dsl.Tile("green", 1, 1)
        m = dsl.Msg("HELLO")
        m2 = dsl.Msg("WORLD")

        ctx = dsl.WorldUpdateBuilder()
        ctx.draw_bg_tile(t)
        ctx.print_msg(m)
        ctx.print_msg(m2)
        ctx.send_update()
        return ctx
    else:
        ctx.new_update()
        ctx.print_msg(dsl.Msg("HELLO!!!"))
        ctx.send_update()
        return ctx

worker.start_worker(process_iteration)

# import arcade library
import arcade

# open a window function
arcade.open_window(500, 300, "drawing example")

# set background color
arcade.set_background_color(arcade.color.LIGHT_APRICOT)

# get ready to draw
arcade.start_render()

# draw eyes
arcade.draw_circle_filled(200, 150, 40, arcade.color.WHITE)
arcade.draw_circle_filled(300, 150, 40, arcade.color.WHITE)
arcade.draw_circle_filled(200, 140, 15, arcade.color.BLACK)
arcade.draw_circle_filled(300, 140, 15, arcade.color.BLACK)

# draw eyebrows
arcade.draw_rectangle_filled(250, 200, 200, 40, arcade.color.DARK_BROWN)

# draw nose
arcade.draw_triangle_filled(220, 100, 250, 130, 270, 100, arcade.color.RUBY_RED)

# draw mouth
arcade.draw_circle_outline(250, 50, 30, arcade.color.ONYX)

# finish drawing
arcade.finish_render()

# keep window open
arcade.run()

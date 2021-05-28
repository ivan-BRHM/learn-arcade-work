# import arcade library
import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500


# define functions
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "drawing example")
    arcade.set_background_color(arcade.color.LIGHT_APRICOT)
    arcade.start_render()


def draw_eye_left(x, y):
    """"draw an eye at the input coordinate, looking to the left"""
    arcade.draw_circle_filled(x, y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x - 15, y - 10, 15, arcade.color.BLACK)


def draw_eye_right(x, y):
    """"draw an eye at the input coordinate, looking to the right"""
    arcade.draw_circle_filled(x, y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 15, y - 10, 15, arcade.color.BLACK)


def draw_eyes(x, y, dist_between_eyes):
    draw_eye_left(x + dist_between_eyes / 2, y)
    draw_eye_right(x - dist_between_eyes / 2, y)


def on_draw(delta_time):
    """"draw everything"""
    arcade.start_render()

    draw_eye_left(on_draw.left_eye1_x, 500)
    draw_eye_right(200, 400)
    draw_eyes(250, 150, 100)
    on_draw.left_eye1_x += 1


# create "left_eye1_x" so we can use it to define on_draw
on_draw.left_eye1_x = 300

# call main
main()

# call on_draw every 1/60 of a second
arcade.schedule(on_draw, 1/60)

# keep window open
arcade.run()

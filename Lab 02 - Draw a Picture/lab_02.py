import arcade

arcade.open_window(800, 600, "Drawing Example")
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 799, 300, 0, arcade.csscolor.GREEN)
# A road
arcade.draw_lrtb_rectangle_filled(300, 499, 300, 0, arcade.csscolor.BEIGE)
arcade.draw_lrtb_rectangle_filled(394, 404, 295, 275, arcade.csscolor.DARK_GRAY)
arcade.draw_lrtb_rectangle_filled(394, 404, 255, 235, arcade.csscolor.DARK_GRAY)
arcade.draw_lrtb_rectangle_filled(394, 404, 215, 195, arcade.csscolor.DARK_GRAY)
arcade.draw_lrtb_rectangle_filled(394, 404, 175, 155, arcade.csscolor.DARK_GRAY)
arcade.draw_lrtb_rectangle_filled(394, 404, 135, 115, arcade.csscolor.DARK_GRAY)
arcade.draw_lrtb_rectangle_filled(394, 404, 95, 75, arcade.csscolor.DARK_GRAY)
arcade.draw_lrtb_rectangle_filled(394, 404, 55, 35, arcade.csscolor.DARK_GRAY)
arcade.draw_lrtb_rectangle_filled(394, 404, 15, 0, arcade.csscolor.DARK_GRAY)

# Draw a sun
arcade.draw_circle_filled(750, 550, 40, arcade.color.YELLOW)

# Rays to the left, right, up, and down
arcade.draw_line(750, 550, 650, 550, arcade.color.YELLOW, 3)
arcade.draw_line(750, 550, 850, 550, arcade.color.YELLOW, 3)
arcade.draw_line(750, 550, 750, 450, arcade.color.YELLOW, 3)
arcade.draw_line(750, 550, 750, 650, arcade.color.YELLOW, 3)

# Diagonal rays
arcade.draw_line(750, 550, 800, 600, arcade.color.YELLOW, 3)
arcade.draw_line(750, 550, 800, 500, arcade.color.YELLOW, 3)
arcade.draw_line(750, 550, 700, 600, arcade.color.YELLOW, 3)
arcade.draw_line(750, 550, 700, 500, arcade.color.YELLOW, 3)

# House
arcade.draw_lrtb_rectangle_filled(550, 750, 350, 150, arcade.csscolor.FIREBRICK)
arcade.draw_triangle_filled(550, 350, 750, 350, 650, 470, arcade.csscolor.DARK_RED)
arcade.draw_lrtb_rectangle_filled(675, 725, 300, 250, arcade.csscolor.CHOCOLATE)
arcade.draw_lrtb_rectangle_filled(575, 625, 250, 150, arcade.csscolor.BLACK)
arcade.draw_circle_filled(585, 200, 5, arcade.csscolor.WHITE)

# Tree trunk
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.SEA_GREEN)

arcade.draw_rectangle_filled(180, 170, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(180, 200, 30, arcade.csscolor.DARK_GREEN)

arcade.draw_rectangle_filled(50, 20, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(50, 50, 30, arcade.csscolor.DARK_OLIVE_GREEN)

# Another tree, with a trunk and ellipse for top
arcade.draw_rectangle_filled(40, 220, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(40, 270, 60, 80, arcade.csscolor.DARK_GREEN)

arcade.draw_rectangle_filled(200, 20, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 70, 60, 80, arcade.csscolor.SEA_GREEN)

arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_OLIVE_GREEN)

arcade.finish_render()
arcade.run()


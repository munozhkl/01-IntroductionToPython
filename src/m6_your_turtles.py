"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Kathi Munoz-Hofmann.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
marlow = rg.SimpleTurtle('turtle')
cindy = rg.SimpleTurtle('turtle')
marlow.pen = rg.Pen('green', 5)
cindy.pen = rg.Pen('midnight blue', 10)
marlow.speed = 20
cindy.speed = 20
size = 300
for k in range(8):
    marlow.draw_circle(size)
    marlow.pen_up()
    marlow.right(45)
    marlow.forward(10)
    marlow.pen_down()
    cindy.draw_regular_polygon(8,100)
    cindy.pen_up()
    cindy.left(45)
    cindy.backward(10)
    cindy.pen_down()
window.close_on_mouse_click()





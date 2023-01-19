"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics_extension import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    vx = graphics.get_vx()
    vy = graphics.get_vy()
    bricks = graphics.bricks_total
    # upper_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
    # upper_right = graphics.window.get_object_at(graphics.ball.x + graphics.radius * 2,
    #                                             graphics.ball.y)
    # lower_left = graphics.window.get_object_at(graphics.ball.x,
    #                                            graphics.ball.y + graphics.radius * 2)
    # lower_right = graphics.window.get_object_at(graphics.ball.x + graphics.radius * 2,
    #                                             graphics.ball.y + graphics.radius * 2)
    
    # Add the animation loop here!
    # 3 times to play the game
    while lives > 0:
        pause(FRAME_RATE)
        # switch the game start
        while graphics.play:
            graphics.ball.move(vx, vy)
            # make ball rebounding in the window except for the bottom
            if graphics.ball.x < 0:
                vx = -vx
            if graphics.ball.x + graphics.ball.width > graphics.window.width:
                vx = -vx
            if graphics.ball.y < 0:
                vy = -vy
            # when ball hit the bottom, lives minus one
            if graphics.ball.y > graphics.window.height:
                lives -= 1
                #  close the switch and restart, waiting for the click to start it again
                graphics.play = False
                graphics.window.add(graphics.ball, x=(graphics.window.width-graphics.ball.width) / 2,
                                    y=(graphics.window.height - graphics.ball.height) / 2)
            pause(FRAME_RATE)
            #  check the four corners touch the paddle or bricks
            if graphics.window.get_object_at(graphics.ball.x, graphics.ball.y) is not None:
                # rebounding when hit the paddle
                if graphics.window.get_object_at(graphics.ball.x, graphics.ball.y) is graphics.paddle:
                    #  make ball don't shock on the paddle
                    if vy > 0:
                        vy = -vy
                #  remove the bricks if this corner touch it
                else:
                    vy = - vy
                    graphics.window.remove(graphics.window.get_object_at(graphics.ball.x, graphics.ball.y))
                    bricks -= 1
            #  check the others corner
            elif graphics.window.get_object_at(graphics.ball.x + graphics.radius * 2,
                                                graphics.ball.y) is not None:
                if graphics.window.get_object_at(graphics.ball.x + graphics.radius * 2,
                                                graphics.ball.y) is graphics.paddle:
                    if vy > 0:
                        vy = -vy
                else:
                    vy = -vy
                    graphics.window.remove(graphics.window.get_object_at(graphics.ball.x + graphics.radius * 2,
                                                graphics.ball.y))
                    bricks -= 1
            elif graphics.window.get_object_at(graphics.ball.x,
                                               graphics.ball.y + graphics.radius * 2) is not None:
                if graphics.window.get_object_at(graphics.ball.x,
                                                 graphics.ball.y + graphics.radius * 2) is graphics.paddle:
                    if vy > 0:
                        vy = -vy
                else:
                    vy = -vy
                    graphics.window.remove(graphics.window.get_object_at(graphics.ball.x,
                                                                         graphics.ball.y + graphics.radius * 2))
                    bricks -= 1
            elif graphics.window.get_object_at(graphics.ball.x + graphics.radius * 2,
                                               graphics.ball.y + graphics.radius * 2) is not None:
                if graphics.window.get_object_at(graphics.ball.x + graphics.radius * 2,
                                                 graphics.ball.y + graphics.radius * 2) is graphics.paddle:
                    if vy > 0:
                        vy = -vy
                else:
                    vy = - vy
                    graphics.window.remove(graphics.window.get_object_at(graphics.ball.x + graphics.radius * 2,
                                                                         graphics.ball.y + graphics.radius * 2))
                    bricks -= 1
            if bricks == 0:
                graphics.window.remove(graphics.ball)
                graphics.window.add(graphics.success, x=100, y=300)
    if bricks > 0:

        graphics.window.add(graphics.fail, x=100, y=300)




if __name__ == '__main__':
    main()

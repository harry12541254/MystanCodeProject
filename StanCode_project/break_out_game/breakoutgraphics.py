"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.gui.events.timer import pause
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 6    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
FRAME_RATE = 10        # 100 frames per second


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height,
                            x=(self.window.width-paddle_width)/2,
                            y=self.window.height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2,
                          x=(self.window.width-ball_radius*2)/2,
                          y=(self.window.height-ball_radius*2)/2)
        self.ball.filled = True
        self.window.add(self.ball)
        self.radius = ball_radius

        # Default initial velocity for the ball
        # do not let ball drop vertically
        self._dx = random.randint(1, MAX_X_SPEED)
        self._dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        self.play = False
        onmousemoved(self.paddle_move)
        onmouseclicked(self.start_game)

        # Success ending
        self.success = GLabel('Success!!!!')
        self.success.font = '-40'

        # Draw bricks
        for i in range(brick_rows):
            row_position = 0
            row_position += (brick_width + brick_spacing) * i
            # use nest for loop two built a plane image
            for j in range(brick_cols):
                col_position = brick_offset
                col_position += (brick_height + brick_spacing) * j
                self.bricks = GRect(brick_width, brick_height)
                self.bricks.filled = True
                # draw different colors
                if j == 0 or j == 1:
                    self.bricks.fill_color = 'maroon'
                elif j == 2 or j == 3:
                    self.bricks.fill_color = 'orange'
                elif j == 4 or j == 5:
                    self.bricks.fill_color = 'lightyellow'
                elif j == 6 or j == 7:
                    self.bricks.fill_color = 'lightgreen'
                elif j == 8 or j == 9:
                    self.bricks.fill_color = 'steelblue'
                self.window.add(self.bricks, x=row_position, y=col_position)
        self.bricks_total = brick_rows * brick_cols

    def start_game(self, mouse):
        # turn on the game
        self.play = True

    def paddle_move(self, mouse):
        # make the mouse is at the center of paddle
        self.paddle.x = mouse.x - self.paddle.width / 2
        # make paddle move horizontally
        self.paddle.y = self.paddle.y
        # make paddle won't excess the windows
        if self.paddle.x + self.paddle.width >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        elif self.paddle.x <= 0:
            self.paddle.x = 0

    def get_vx(self):
        if self._dx > 0.5:
            self._dx = -self._dx
        return self._dx

    def get_vy(self):
        return self._dy




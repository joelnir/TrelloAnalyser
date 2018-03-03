from graphics import *

SIDE_MARGIN = 40

WIN_WIDTH = 360
WIN_HEIGHT = 550

DAY_SPACE = 40
HOUR_SPACE = 20

WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Colors are given as a list of three elements, on rgb format
def show_week(data, start_color, stop_color):
    max = max_action(data)

    win = GraphWin('Week', WIN_WIDTH, WIN_HEIGHT)

    # Background
    bg = Rectangle(Point(0, 0), Point(WIN_WIDTH, WIN_HEIGHT))
    bg.setFill("white")
    bg.draw(win)

    # Headers
    for i in range(7):
        txt = Text(Point((SIDE_MARGIN * 2 + DAY_SPACE * i), SIDE_MARGIN), WEEKDAYS[i])
        txt.draw(win)

    for i in range(24):
        txt = Text(Point(SIDE_MARGIN, SIDE_MARGIN + HOUR_SPACE * (i + 1)), str(i))
        txt.draw(win)

    # Draw color map
    for i in range(7):
        for j in range(24):
            relative = float(data[i][j])/max
            col = [int(start_color[col_i] + relative * (stop_color[col_i] - start_color[col_i])) for col_i in range(3)]

            x = SIDE_MARGIN + (DAY_SPACE * i) + (DAY_SPACE/2)
            y = SIDE_MARGIN + (HOUR_SPACE * j) + (HOUR_SPACE/2)

            rec = Rectangle(Point(x, y), Point(x + DAY_SPACE, y + HOUR_SPACE))
            rec.setFill(color_rgb(col[0], col[1], col[2]))
            rec.draw(win)

    # Wait for any key to be pressed
    win.getKey()

def max_action(data):
    return max([max(day) for day in data]);

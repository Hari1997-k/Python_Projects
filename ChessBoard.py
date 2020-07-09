import turtle


def draw_box(tur, x, y, size, fill_color):
    tur.penup()
    tur.goto(x, y)
    tur.pendown()

    tur.fillcolor(fill_color)
    tur.begin_fill()
    tur.begin_fill()
    tur.speed(50)
    for i in range(0, 4):
        board.forward(size)
        board.right(90)

    tur.end_fill()
    tur.position


def draw_chess_board():
    square_color = "black"
    start_x = 0
    start_y = 0
    box_size = 43
    for i in range(0, 8):
        for j in range(0, 8):
            draw_box(board, start_x + j * box_size, start_y + i * box_size, box_size, square_color)
            square_color = 'black' if square_color == 'white' else 'white'
        square_color = 'black' if square_color == 'white' else 'white'


board = turtle.Turtle()
draw_chess_board()
turtle.done()

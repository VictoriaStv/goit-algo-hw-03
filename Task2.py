import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0
        koch_curve(t, order-1, size)
        t.left(60)
        koch_curve(t, order-1, size)
        t.right(120)
        koch_curve(t, order-1, size)
        t.left(60)
        koch_curve(t, order-1, size)

def snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def main():
    while True:
        try:
            order = int(input("Введіть рівень рекурсії (від 1 до 6): "))
            if 1 <= order <= 6:
                break
            else:
                print("Рівень рекурсії повинен бути від 1 до 6, бо вийде не дуже. Спробуйте ще раз.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")

    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    size = 300
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()
    snowflake(t, order, size)
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()

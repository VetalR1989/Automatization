# # Квадрат в цикле

# from turtle import *

# my_turtle = Turtle()
# my_turtle.speed(0)
# my_turtle.screen.setup(1200, 800)

# # Нарисовать квадрат
# def draw_rect(t):
#     for x in range(0, 4):
#         t.right(90)
#         t.forward(200)

# # Рисует квадраты в цикле
# for x in range(0, 360):
#     draw_rect(my_turtle)
#     my_turtle.right(5)

# # Необходимо, чтобы окно не закрывалось само, а только по клику
# my_turtle.screen.exitonclick()
# my_turtle.screen.mainloop()


from turtle import *
rabbit = Turtle()
rabbit.screen.setup(1200, 800)
rabbit.screen.bgcolor("yellow")
rabbit.pensize(3)
rabbit.up()
rabbit.goto(0, -100)
rabbit.down()
# передние лапы
rabbit.goto(-200, -100)
rabbit.left(180)
rabbit.circle(-20, 180)
rabbit.goto(-170, -70)
# холка
rabbit.circle(20, 130)
rabbit.circle(-130, 40)
rabbit.circle(20, 90)
rabbit.goto(-270, 65)
# морда
rabbit.circle(-40, 80)
rabbit.circle(-20, 60)
rabbit.goto(-195, 190)
# уши
rabbit.left(45)
rabbit.circle(-200, 60)
rabbit.circle(-5, 150)
rabbit.goto(-120, 255)
rabbit.left(190)
rabbit.circle(-220, 40)
rabbit.circle(-5, 110)
rabbit.circle(-230, 60)
# спинка
rabbit.left(180)
rabbit.circle(-280, 40)
rabbit.circle(-130, 80)
# хвост
rabbit.circle(20, 360)
# задние лапы
rabbit.left(20)
rabbit.circle(-130, 180)
rabbit.circle(-90, 80)
rabbit.up()
# глаза
rabbit.goto(-190, 130)
rabbit.down()
rabbit.begin_fill()
rabbit.circle(10, 360)
rabbit.end_fill()
rabbit.up()
# подпись
rabbit.goto(0, -200)
rabbit.down()
rabbit.write("Зайчик-побегайчик", True, "right", font = ("arial", 20, "bold"))

rabbit.screen.exitonclick()
rabbit.screen.mainloop()
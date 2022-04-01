import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from lines import Line1, Line2, Line3, Line4

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


user = Player()
cars = CarManager()
score = Scoreboard()
line1 = Line1()
line2 = Line2()
line3 = Line3()
line4 = Line4()

screen.listen()
screen.onkey(user.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move_cars()

    # Detect the Collision with Car
    for car in cars.all_cars:
        if car.distance(user) < 23:
            game_is_on = False
            user.write("GAME OVER", align='center', font=('Courier', 24, 'normal'))

    # Detect the Crossing of the Road
    if user.is_finish():
        user.reset()
        cars.level_up()
        score.main_score()


screen.exitonclick()

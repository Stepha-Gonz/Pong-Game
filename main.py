import time
import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

POS_PADDLE1=(350,0)
POS_PADDLE2=(-350,0)
screen=t.Screen()
screen.bgcolor("black")
screen.title("Pong-StephaGonz")
screen.setup(800,600)
screen.tracer(0)



r_paddle=Paddle(POS_PADDLE1)
l_paddle=Paddle(POS_PADDLE2)
pong_ball=Ball()
scoreboard=Scoreboard()
scoreboard.score()
screen.listen()
screen.onkey(r_paddle.move_up_paddle,"Up")
screen.onkey(r_paddle.move_down_paddle,"Down")
screen.onkey(l_paddle.move_up_paddle,"w")
screen.onkey(l_paddle.move_down_paddle,"s")

is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(pong_ball.move_speed)
    pong_ball.ball_movement()
    
    if pong_ball.ycor()>280 or pong_ball.ycor()<-280:
        pong_ball.bounce()
        
    if pong_ball.xcor()>380: 
        scoreboard.lpaddle_increment()
        pong_ball.reset()
        
    if pong_ball.xcor()<-380:
        scoreboard.rpaddle_increment()
        pong_ball.reset()
        
    if scoreboard.scorer==4 or scoreboard.scorel==4:
        is_game_on=False
        scoreboard.game_over()
    if pong_ball.distance(r_paddle)<50 and pong_ball.xcor()>320 or pong_ball.distance(l_paddle)<50 and pong_ball.xcor()<-320:
        pong_ball.paddle_bounce()
    
        
screen.exitonclick()

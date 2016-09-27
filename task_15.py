#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
   if wall_is_above():
       if wall_is_on_the_left():
           while not wall_is_beneath() and not wall_is_on_the_right():
               move_down()
               move_right()
       elif wall_is_on_the_right():
           while not wall_is_beneath() and not wall_is_on_the_left():
               move_down()
               move_left()
   elif wall_is_beneath():
       if wall_is_on_the_left():
           while not wall_is_above() and not wall_is_on_the_right():
               move_up()
               move_right()
       elif wall_is_on_the_right():
           while not wall_is_above() and not wall_is_on_the_left():
               move_up()
               move_left()
   pass


if __name__ == '__main__':
    run_tasks()

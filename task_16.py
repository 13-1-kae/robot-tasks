#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
   while wall_is_on_the_left() and  wall_is_on_the_right() and not wall_is_above():
       move_up()
   if wall_is_on_the_right():
       while not wall_is_on_the_left():
           move_left()
   else:
       while not wall_is_on_the_right():
           move_right()

   pass


if __name__ == '__main__':
    run_tasks()

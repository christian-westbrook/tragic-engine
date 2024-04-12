"""
This module contains a single class called GameServer that serves a persistent 
virtual world of tiles and sprites to connected players.
"""

# Standard library imports
import time

TICKS_PER_SECOND = 1
NANOSECONDS_PER_SECOND = 1e9

class GameServer:
    """
    This class represents a game server responsible for serving a persistent 
    virtual world of tiles and sprites to connected players.
    """
    def __init__(self):
    
        time_per_tick = NANOSECONDS_PER_SECOND / TICKS_PER_SECOND

        last_time = time.time_ns()
        
        delta = 0
        timer = 0
        ticks = 0
        self.actual_ticks_per_second = 0

        while True:

            now = time.time_ns()
            delta = delta + (now - last_time) / time_per_tick
            timer = timer + (now - last_time)
            last_time = now

            if timer > NANOSECONDS_PER_SECOND:
                self.actual_ticks_per_second = ticks
                ticks = 0
                timer = timer - NANOSECONDS_PER_SECOND

            if delta >= 1:
                self.tick()
                ticks = ticks + 1
                delta = delta - 1
    
    def tick(self):
        """
        This method represents one game server tick.
        """

        print('ticks per second: ' + str(self.actual_ticks_per_second))

import curses

class Window:
   '''This is the base window object.
      Every view I create will be based off
      properties below.
   '''
   def __init__(self, h, w, start_y, start_x):
        self._h = h
        self._w = w
        self._start_y = start_y
        self._start_x = start_x

   def draw(self):
       raise NotImplementedError

   def update(self):
       raise NotImplementedError


class StatWindow(Window):
   def __init__(self, stats):
       super().__init__(14, 16, 0, 194)
       self._stats = stats
       self._win = curses.newwin(self._h, self._w, self._start_y, self._start_x)
       self._win.border(0,0,0,0,0,0,0,0)
        
   def draw(self):
       #This needs work....It's the length of the stat names 
       p = 2
       self._win.addstr(1,1, "STATS")
       self._win.addstr(2,1, "-----")
       for key in self._stats:
           p += 1
           self._win.addstr(p, 1, "{}: {}".format(key, self._stats[key]))
       self._win.refresh()

   def update(self):
       pass


if __name__ == '__main__':
    from curses import wrapper
    from Characters.Characters import STATS
    
    def main(stdscr):
        SW = StatWindow(STATS)
        SW.draw()
        curses.napms(2000)
    
    wrapper(main)


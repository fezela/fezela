from Settings import SETTINGS
from Characters import PartyMember
from GUI import StatWindow

class Game:
    '''This is the Game object.  It's basically 
    the skelton of a game engine at this time.
    All the other classes and modules of the game 
    will eventually 
    merge into this file.'''

    def __init__(self):
        ''' 
        I'm unsure of what values need to be passed to start
        this game.  I hate giving everything a generic property
        of 'name'.  It just seems like I don't know what else to 
        do.
        '''
        self.name = "WTF, I'm a nigger."
        self.statWin = None
        self.player = PartyMember('Jafaar')
        
    def initialize(self):
        '''
        The initialize method is to used to load necessary assets
        for the game. I.E. sound files, images, databases, and etc.
        It should load assets and then verify they are ready before
        moving forward to other parts of the program
        '''
        self.statWin = StatWindow(self.player.stats)

    def draw(self):
        '''
        The draw method is used to create the visual representation
        of the game for the user.  It takes the modeled data and 
        puts it into position in the GUI window
        '''
        self.statWin.draw()

    def update(self):
        '''
        The update method is used to alter the data that has happended
        since the user, or program has made changes to environmental, 
        positional, or etc information.
        '''
        #self.mainWindow.refresh()
        pass
    def mainLoop(self):
        '''
        Encompasses the main loop of the program.
        EX.

        self.canvas.clear()
        self.update()
        self.draw()
        '''
        #stdscr.clear()
        self.draw()
        self.update()
            
    
    def start(self):
        '''
        The start method is what will eventually be passed to the 
        main() function.  Everything needs to work here before it
        goes into main.py.
        EX.

        self.initialize()
        self.mainLoop()
        '''
        while True:
            self.initialize()
            self.mainLoop()

if __name__ == '__main__':
    from curses import wrapper
     
    def main(stdscr):
        G = Game()
        G.start()

    if SETTINGS['selected_win_manager'] == 'NCURSES':
        print("Congratulations you are a nigger 4 life")
        
        wrapper(main)
    
    else:
        print("lets build another gui example folder")

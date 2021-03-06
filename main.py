import gtk,pygtk,pygame,os
from static import config,tools
from console import PythonConsole
from games import Game1
import os, sys
kill=None
da=object
class GUI(gtk.Window):
    def __init__(self):
        window = gtk.Window()
        window.set_title ("Hello World")
        #Register the self.destroy function to the 'destroy' event of window.
        window.connect_after('destroy', self.destroy)
        window.set_resizable(False)
        #split the window
        self.box=gtk.VBox(False,2)
        window.add (self.box)
        self.createPygameWindow()

        #interpreter
        pc=PythonConsole() #the user can use the self.send(x) function with "send(x)"
        pc.set_size_request(config.WINX,config.InterpreterY)
        self.box.pack_start(pc,False,False,0)
        tools.interpreter=pc
        window.show_all()

    def createPygameWindow(self):
        area = gtk.DrawingArea()
        area.set_app_paintable(True)
        area.set_size_request(config.WINX, config.WINY)
        self.box.pack_start(area,False,False,0)
        ##################################
        #The three following lines link the pygame to the area:
        area.realize()
        os.putenv('SDL_WINDOWID', str(area.window.handle))
        gtk.gdk.flush()
        #################################
        pygame.init()
        tools.screen=pygame.display.set_mode((config.WINX, config.WINY), 0, 0)


    def destroy(self, window):
        gtk.main_quit()

    def send(self,a):
        if a==0:
            print ('T')
        else:
            print('F')

def main():
    app = GUI()
    Game1()
    gtk.main()

if __name__ == "__main__":
    main()

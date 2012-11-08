import pygame

class Game:
    

    def __init__(self, width=800, height=600,fps=60):
        pygame.init()
        self.screen = pygame.display.set_mode([width, height])
        self.fps=fps
        self.load_content()
        self.update_loop()

    def update_loop(self):
        done = False;
        clock = pygame.time.Clock()
        while not done:
            quitEvent = pygame.event.get(pygame.QUIT);
            if (quitEvent):
                break;
            self.screen.fill((0, 0, 0))    
            self.update(pygame.event.get())
            pygame.display.flip()
            clock.tick(self.fps)

        pygame.quit()

    def load_content(self):
        return

    def update(self, events):
        return
        

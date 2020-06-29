from Pygame_setup import *
from Main import main, browse
from CreateMapFromFile import chooseFileToCreate
import multiprocessing as mp

class Button:
    def __init__(self, name, y, height, return_func):
        self.name = name
        self.y = y
        self.height = height
        self.return_func = return_func

    def draw(self, selected=False):
        button_text = myfont.render(self.name, 1, (0, 0, 0))
        text_pos = [int(i) for i in [(WIDTH - button_text.get_rect().width)/2, self.y + (self.height - button_text.get_rect().height)/2]]
        if not selected:
            pg.draw.rect(screen, (200, 200, 200), [int(i) for i in (0, self.y, WIDTH, self.height)])
            pg.draw.rect(screen, (20, 20, 20), [int(i) for i in (0, self.y, WIDTH, self.height)], 5)

        else:
            pg.draw.rect(screen, (164, 231, 141), [int(i) for i in (0, self.y, WIDTH, self.height)])
            pg.draw.rect(screen, (255, 255, 255), [int(i) for i in (0, self.y, WIDTH, self.height)], 5)

        screen.blit(button_text, text_pos)

name_func = [("Draw graph-map for tile map creating", main), ("Browse saved previously created maps", browse),
             ("Create tile map from GeoJSON file", chooseFileToCreate)]
buttons = [Button(name_func[i][0], HEIGHT*(i/3), HEIGHT/3, name_func[i][1]) for i in range(3)]

def loadingScreen():
    loading_text = myfont.render("Loading...", 1, (0, 0, 0))
    pg.draw.rect(screen, (255, 255, 255), (0,0,WIDTH,HEIGHT))
    screen.blit(loading_text, (10, 10))
    pg.display.flip()


def mainGUI():
    selected_index = 0
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running=False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    selected_index = (selected_index + 1) % len(buttons)
                elif event.key == pg.K_UP:
                    selected_index = (selected_index - 1) % len(buttons)
                elif event.key == pg.K_RETURN:
                    loadingScreen()
                    if buttons[selected_index].return_func() == "escape":
                        mainGUI()
                    return None

        y = 0
        for i in range(3):
            buttons[i].draw(selected=(i==selected_index))
            y += HEIGHT/5

        pg.display.flip()

mainGUI()
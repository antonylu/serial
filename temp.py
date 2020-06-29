import serial
import pygame

BG_IMG          = "bg.jpg"
class Temp():
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self._surface = pygame.display.get_surface()
        self.bg = pygame.image.load(BG_IMG)
        self.s = serial.Serial('COM10')
        self._running = True if self.s else False
        self.font = pygame.font.SysFont('arialms', 512)
        self.w, self.h = self._surface.get_size()

    def run(self):
        while self._running:
            self._handle_events()
            self._get_temperature()
            self._redraw()
        pygame.quit()

    def _get_temperature(self) -> None:
        self.temp  = self.s.readline().decode('ascii').strip()
        print(self.temp)

    def _redraw(self) -> None:
        tt = float(self.temp)
        if tt > 37.5:
            text = self.font.render(self.temp, 1, (255, 0, 0))
        else:
            text = self.font.render(self.temp, 1, (255, 255, 255))

        text_rect = text.get_rect(center=(self.w/2, self.h/2))
        self._surface.blit(self.bg, (0,0))
        self._surface.blit(text, text_rect)
        #self._surface.fill(pygame.Color(41,36,33))
        pygame.display.update()
    def _handle_events(self) -> None:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    self._running = False

if __name__ == '__main__':
    sn = Temp().run()

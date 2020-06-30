import serial
import pygame
import json

BG_L_IMG    = "bg.jpg"
BG_P_IMG    = "bgp.jpg"
OPTION_JSON = "options.json"

class Temp():
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self._surface = pygame.display.get_surface()
        options = json.load(open(OPTION_JSON))
        self.s = serial.Serial(options['COM_PORT'])
        self.high_temp = float(options['HIGH_TEMP'])
        self._running = True if self.s else False
        self.w, self.h = self._surface.get_size()
        self.portrait_mode = True if self.w < self.h else False
        if self.portrait_mode:
            self.bg = pygame.image.load(BG_P_IMG)
            self.text_center = (int(self.w/2), 590)
            self.font = pygame.font.SysFont('consolas', 360)
        else: # landscape mode
            self.bg = pygame.image.load(BG_L_IMG)
            self.text_center = (int(self.w/2), int(self.h/2)+50)
            self.font = pygame.font.SysFont('consolas', 512)
        pygame.mouse.set_visible(False)
        self.alarm = pygame.mixer.Sound('balarm.wav')

    def run(self):
        while self._running:
            self._handle_events()
            self._get_temperature()
            self._redraw()
        pygame.quit()

    def _get_temperature(self) -> None:
        self.temp  = self.s.readline().decode('ascii').strip()
        #print(self.temp)

    def _redraw(self) -> None:
        tt = float(self.temp)
        if tt > self.high_temp:
            self.alarm.play()
            text = self.font.render(self.temp, 1, (255, 0, 0))
        else:
            text = self.font.render(self.temp, 1, (255, 255, 255))
            self.alarm.stop()

        text_rect = text.get_rect(center=self.text_center)
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

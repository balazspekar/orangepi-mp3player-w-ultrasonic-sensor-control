import pygame
import threading

class Player:

    def __init__(self):
        self.file = '/zene.mp3'
        pygame.init()
        pygame.mixer.init()

    def play(self):
        threading.Thread(target=self._play).start()
        print("PLAYER: play()")

    
    def _play(self):
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)            
   

    def pause(self):
        pass


    def stop(self):
        pygame.mixer.music.stop()
        return "PLAYER: stop()"


    def next(self):
        pass


    def prev(self):
        pass    


    def volume_up(self):
        pygame.mixer.music.set_volume(self.get_current_volume() + 0.5)        


    def volume_down(self):
        pygame.mixer.music.set_volume(self.get_current_volume() - 0.5)


    def load_file(self):
        pygame.mixer.music.load(self.file)


    def reload_music_library(self):
        pass

    
    def get_current_volume(self):
        return pygame.mixer.music.get_volume()



#c = 100
#    if c >= 0:
#        print("currvol " + str(currvol))
#        pygame.mixer.music.set_volume(currvol - 0.005)   
#    else:
#        pygame.mixer.music.stop()
#    pygame.time.Clock().tick(10)
#    c -= 1


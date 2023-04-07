import pygame 
import os

pygame.init()

screen = pygame.display.set_mode((800, 200))
pygame.display.set_caption("Music Player")

myfont = pygame.font.SysFont(None, 30)
music_dir = r"C:\Users\Dauir\All_Labs\sounds"
songs = os.listdir(music_dir)
current_song = 0

pygame.mixer.music.load(os.path.join(music_dir, songs[current_song]))

'''
play_key = pygame.K_SPACE
stop_key = pygame.K_ESCAPE
next_key = pygame.K_RIGHT
prev_key = pygame.K_LEFT
'''


pygame.mixer.music.play()

while True:
    screen.fill((10, 10, 10))
    songname = myfont.render(songs[current_song], True, "Yellow")
    screen.blit(songname,(10, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()            
            quit()
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.unpause()  
            elif event.key == pygame.K_ESCAPE:
                pygame.mixer.music.pause()
            elif event.key == pygame.K_RIGHT:
                current_song = (current_song + 1) % len(songs)
                pygame.mixer.music.load(os.path.join(music_dir, songs[current_song]))
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_song = (current_song - 1) % len(songs)
                pygame.mixer.music.load(os.path.join(music_dir, songs[current_song]))
                pygame.mixer.music.play()
    text = myfont.render('Press Space to Play, Esc to Stop, Left/Right to Change your Song', True, "white")
    screen.blit(text, (10, 50))
    pygame.display.update()
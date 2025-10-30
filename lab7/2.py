import pygame 
import os
from pygame import mixer

pygame.init()
mixer.init()

screen = pygame.display.set_mode((500,200))

BG=(255,192,203)
TXT=(255,80,155)

font= pygame.font.SysFont("Arial",24)

music_folder="/Users/zansaa/Documents/pp2/lab7/music"

playlist=[]
for f in os.listdir(music_folder):
    if f.endswith(".mp3"):
        full_path=os.path.join(music_folder,f)
        playlist.append(full_path)
        
current=0
playing= False

def play_music():
    global playing
    
    mixer.music.load(playlist[current])
    mixer.music.play()
    playing=True
    
def next_music():
    global current
    if playlist:
        current = (current + 1) % len(playlist)
        play_music()
        
def stop_music():
    global playing
    mixer.music.stop()
    playing = False
    print("Music stopped.")

def prev_music():
    global current
    if playlist:
        current = (current - 1) % len(playlist)
        play_music()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_music()
            elif event.key == pygame.K_b:
                prev_music()
            elif event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(BG)

    lines = [
    "Press P - Play, S - Stop",
    "Press N - Next, B - Back"
    ]   

    y = 20
    for line in lines:
      text = font.render(line, True, TXT)
      screen.blit(text, (20, y))
      y += 30  
      
    if playing and playlist:
     song_name = os.path.basename(playlist[current])
     now_playing = font.render(f"Now playing: {song_name}", True, TXT)
     screen.blit(now_playing, (20, y + 10))


    pygame.display.flip()

pygame.quit()

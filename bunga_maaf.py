import pygame
import time

pygame.init()
pygame.mixer.init()

width = 1000
height = 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bunga Maaf - The Lantis")

audio_file = "The Lantis - Bunga Maaf (Visualizer).mp3" 
pygame.mixer.music.load(audio_file)
pygame.mixer.music.play()

font = pygame.font.Font(None, 42)
text_color = (255, 255, 255)
bg_color = (0, 0, 0)

def display_text(text, duration):
    screen.fill(bg_color)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(width/2, height/2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    time.sleep(duration)

lyrics = [
    ("♪ .......", 4.0),
    ("♪ .......", 4.0),
    ("♪ .......", 4.0),
    ("♪ Hai", 1.5),
    ("♪ Masihkah Luka itu Ada di sana", 9.0),
    ("♪ Yang ku Tinggalkan", 5.5),
    ("♪ Saat kita Masih bersama", 6.5),
    ("♪ Kini waktu terasa berbeda", 6.5),
    ("♪ Tanpa hadirmu", 5.5),
    ("♪ Keras hati yang dulu bicara", 7.0),
    ("♪ Berujung pilu", 6.0),
    ("♪ .......", 1.0),
    ("♪ Andai Angin mengulang", 4.5),
    ("♪ Sebuah masa yang t'lah usang", 5.0),
    ("♪ Kan ku telan isi bumi hanya untukmu", 6.0),
    ("♪ Terima bunga maafku", 3.5),
    ("♪ Layu termakan egoku", 3.5),
    ("♪ Meski ku tahu", 3.0),
    ("♪ Tak bisa", 4.0),
    ("♪ .......", 4.0),
    ("♪ .......", 4.0),
    ("♪ .......", 4.0),
    ("♪ Oh Mungkinkah", 6.5),
    ("♪ Ada rindu", 3.0),
    ("♪ Dibalik benci itu", 6.0),
    ("♪ Yang perlahan Menghilang", 5.0),
    ("♪ Saat nyamanku tak lagi kau butuh", 5.5),
    # Verse 2
    ("♪ Kini waktu terasa berbeda", 6.5),
    ("♪ Tanpa hadirmu", 5.5),
    ("♪ Keras hati yang dulu bicara", 6.5),
    ("♪ Berujung pilu", 6.0),
    ("♪ .......", 1.0),
    # Bridge
    ("♪ Andai Angin mengulang", 3.5),
    ("♪ Sebuah masa yang t'lah usang", 4.0),
    ("♪ Kan ku telan isi bumi hanya untukmu", 5.0),
    # Chorus
    ("♪ Terima bunga maafku", 3.5),
    ("♪ Layu termakan egoku", 3.5),
    ("♪ Meski ku tahu", 3.0),
    ("♪ Tak bisa", 4.0),
    # Final
    ("♪ Andai Angin mengulang", 4.0),
    ("♪ Sebuah masa yang t'lah usang", 4.0),
    ("♪ Kan ku telan isi bumi hanya untukmu", 6.0),
    ("♪ Terima bunga maafku", 3.5),
    ("♪ Layu termakan egoku", 3.5),
    ("♪ Meski ku tahu", 3.0),
    ("♪ .......", 1.0),
    ("♪ Meski ku tahu", 3.0),
    ("♪ Tak bisa", 4.0),
    ("♪ .......", 4.0),
    ("♪ .......", 4.0),
    ("♪ .......", 4.0),
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for lyric, duration in lyrics:
        display_text(lyric, duration)
        
    if not pygame.mixer.music.get_busy():
        running = False
            
pygame.quit()
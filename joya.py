from mutagen.mp3 import MP3 as mp3
import pygame
import time
import datetime
import schedule


num_of_bonnou=108
num_of_HNY=1000000

file_bell = 'teranokane.mp3' #再生したいmp3ファイル
file_HNY_sound='happytime.mp3'

pygame.mixer.init()
pygame.mixer.music.load(file_bell) #音源を読み込み
mp3_length = mp3(file_bell).info.length -12#音源の長さ取得

def joya():
    print("煩悩の数：",num_of_bonnou)
    for i in range(num_of_bonnou):
        pygame.mixer.music.play(1) #再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)
        time.sleep(mp3_length) 
        remains_bonnou=num_of_bonnou-i-1
        print("煩悩の数：",remains_bonnou)

    time.sleep(5)
    pygame.mixer.music.stop() #音源の長さ待ったら再生停止
    pygame.mixer.init()
    pygame.mixer.music.load(file_HNY_sound) #音源を読み込み
    mp3_length_2 = mp3(file_HNY_sound).info.length #音源の長さ取得
    j=1
    pygame.mixer.music.play(j) #再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)


    for n in range(num_of_HNY):
        print("HAPPY NEW YEAR!!!!!  HAPPY NEW YEAR!!!!!  HAPPY NEW YEAR!!!!!  HAPPY NEW YEAR!!!!!  HAPPY NEW YEAR!!!!!  HAPPY NEW YEAR!!!!!  HAPPY NEW YEAR!!!!!")
        if n%10==0:
            print("あけおめーー!!!!!  あけおめーー!!!!!  あけおめーー!!!!!  あけおめーー!!!!!  あけおめーー!!!!!  あけおめーー!!!!!  あけおめーー!!!!!")
    print("\n今年もよろしくお願いいたします。")
    pygame.mixer.music.stop() #音源の長さ待ったら再生停止

joya()
# schedule.every().day.at("23:55").do(joya)
  
# while True:
#   schedule.run_pending()
#   time.sleep(60)

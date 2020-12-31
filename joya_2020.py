from mutagen.mp3 import MP3 as mp3
import pygame
import time
import datetime
import schedule
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--num_of_bonnou',  type=int, default=108,
                    help='the number of your bonnou (generally, this is 108)')
parser.add_argument('--speed',  default='fast', help='speed of ringing the kane, select fast or slow')

args = parser.parse_args()


num_of_bonnou=args.num_of_bonnou
num_of_HNY=1000000

if args.speed=='fast':
    file_bell='kane_fast.mp3'
elif args.speed=='slow':
    file_bell = 'teranokane.mp3' #再生したいmp3ファイル
else:
    raise Exception('Error!')

file_HNY_sound='happytime.mp3'

pygame.mixer.init()
pygame.mixer.music.load(file_bell) #音源を読み込み
mp3_length = mp3(file_bell).info.length #音源の長さ取得

# pygame.mixer.init()
# pygame.mixer.music.load(file_bell) #音源を読み込み
# mp3_length = mp3(file_bell).info.length -13#音源の長さ取得

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
    print("\n今年もよろしくお願いします。")
    pygame.mixer.music.stop() #音源の長さ待ったら再生停止

joya()

#start at 23:55
# schedule.every().day.at("23:55").do(joya)
  
# while True:
#   schedule.run_pending()
#   time.sleep(60)

import time
import pygame

# 音乐路径
filePath = r"D:\PythonCode\StudyCode\004_自动化办公\Kalimba.mp3"

pygame.mixer.init()

track = pygame.mixer.music.load(filePath)
pygame.mixer.music.play()
time.sleep(5)
pygame.mixer.music.pause()
time.sleep(5)
pygame.mixer.music.unpause()
time.sleep(5)
pygame.mixer.music.stop()
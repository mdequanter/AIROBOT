import urllib3
import time
import pygame

http = urllib3.PoolManager()

class Robot:
    def __init__(self,name, demo):
        self.ip = '127.0.0.1'
        self.name = name
        self.demo = demo
        self.color =  (255,0,0) # red
        self.x = 300
        self.y = 300
        self.size=50
        self.direction = 0


    def setcolor(self,color):
        self.color = color

    def forward(self,move,screen):
        # open a connection to a URL using urllib2
        if (self.demo == False) :
            webUrl = http.request('GET','http://'+self.ip+'/?left=70&right=100')
            time=move
            time.sleep(time)
        if (screen != False) :
            # Draw a solid blue circle in the center
            self.y = self.y+move
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
            # Flip the display
            pygame.display.flip()
        return True

    def left(self,move,screen):
        # open a connection to a URL using urllib2
        if (self.demo == False) :
            webUrl = http.request('GET','http://'+self.ip+'/?left=70&right=100')
            time=move
            time.sleep(time)
        if (screen != False) :
            # Draw a solid blue circle in the center
            self.x = self.x-move
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
            # Flip the display
            pygame.display.flip()
        return True

    def right(self,move,screen):
        # open a connection to a URL using urllib2
        if (self.demo == False) :
            webUrl = http.request('GET','http://'+self.ip+'/?left=70&right=100')
            time=move
            time.sleep(time)
        if (screen != False) :
            # Draw a solid blue circle in the center
            self.x = self.x+move
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
            # Flip the display
            pygame.display.flip()
        return True



    def backward(self,move,screen):
        # open a connection to a URL using urllib2
        if (self.demo == False) :
            webUrl = http.request('GET','http://'+self.ip+'/?left=100&right=70')
            time=move
            time.sleep(time)
        if (screen != False) :
            # Draw a solid blue circle in the center
            self.y = self.y-move
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
            # Flip the display
            pygame.display.flip()
        return True

    def stop(self):
        if (self.demo == False) :
            # open a connection to a URL using urllib2
            webUrl = http.request('GET','http://'+self.ip+'/?left=90&right=90')
        return True

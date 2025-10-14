import pygame
import time
from djitellopy import Tello
def main():
    tello = Tello()
    tello.connect()
    print("Connected")
    

    pygame.init()
    # Initializing surface
    surface = pygame.display.set_mode((780,880))
    
    # Initializing frame counter
    frame_number = 0
    # Initializing Color
    default_color = (128,128,128)
    r = (255, 0, 0)
    b = (0, 0, 255)
    p = (255, 0, 255)
    display = ['0']*64
    # Creating a dictionary to track the color of each rectangle
    rect_colors = {(i, j): default_color for i in range(8) for j in range(8)}
    
    # Next Frame Button setup
    button_color = (0, 255, 0)
    button_text_color = (255, 255, 255)
    button_rect = pygame.Rect(320, 810, 140, 50)

    font = pygame.font.SysFont('Arial', 24)
    button_text = font.render("Next Frame", True, button_text_color)

    pygame.display.flip()
    running = True
    while running:
        surface.fill((255, 255, 255))

        # Draw the grid
        for i in range(8):
            for j in range(8):
                x, y = pygame.mouse.get_pos()
                left = i*100
                right = left +80
                top = j*100
                bottom = top +80
                width = 80
                height = 80
                color = rect_colors[(i, j)]
                pygame.draw.rect(surface, color, pygame.Rect(top, left, width, height))
        
        # Draw the "Next Frame" button
        pygame.draw.rect(surface, button_color, button_rect)
        surface.blit(button_text, (button_rect.x + 10, button_rect.y + 10))
                
        pygame.display.flip()
                
        for event in pygame.event.get():
            # check if quit
            if event.type == pygame.QUIT:
                running = False
            # checks if a mouse is clicked 
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                counter = 0
                for i in range(8):
                    for j in range(8):
                        left = j * 100
                        top = i * 100
                        right = left + 80
                        bottom = top + 80
                        
                        if (left <= x <= right) and (top <= y <= bottom):
                            if(rect_colors[(i, j)] == default_color):
                                rect_colors[(i, j)] = r 
                                display[counter] = 'r'
                            elif(rect_colors[(i, j)] == r):
                                rect_colors[(i, j)] = b
                                display[counter] = 'b'  
                            elif(rect_colors[(i, j)] == b):
                                rect_colors[(i, j)] = p 
                                display[counter] = 'p'
                            elif(rect_colors[(i, j)] == p):
                                rect_colors[(i, j)] = default_color  
                                display[counter] = '0'
                        counter += 1

                # Check if the click is on the "Next Frame" button
                if button_rect.collidepoint(x, y):
                    frame_number += 1
                    print("Frame number " + str(frame_number) + ":" + "".join(display))
                    tello.send_expansion_command("mled g " + "".join(display))
                    time.sleep(0.5)
                               
    pygame.quit()
    # print("".join(display))
    # tello.send_expansion_command("mled g " + "".join(display))
    # time.sleep(2)
    
if __name__=="__main__":
    main()
    

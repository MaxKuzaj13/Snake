#first version
import os
import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
res_x = 1000
res_y = 800
game_speed_value = 1


def insert_name():
    name_player = input('Enter player name: ')
    if name_player == '':
        name_player = 'player1'
    return name_player


def print_hello_message(name_player):
    print(f'Welcome {name_player} to the best game ever!! Python - Snake')


def game_loading():
    print('Game are loading')
    clock.tick(1)


def create_screan():
    pygame.init()
    screen = pygame.display.set_mode((res_x, res_y))
    # pygame.display.update()
    # pygame.quit()
    # quit()
    return screen

def main():
    os.system('clear')
    # add new player and print welcome information
    name_player = insert_name()
    print_hello_message(name_player)
    # start a game
    game_loading()
    os.system('clear')
    screan = create_screan()
    box = pygame.Rect(10, 10, 10, 10)
    while True:
        clock.tick(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        # Input
        box.x += 1

        # Drawing
        pygame.draw.rect(screan, (100, 150, 160), box)
        pygame.display.flip()



if __name__ == "__main__":
    main()


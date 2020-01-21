#first version
import os
import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
res_x = 1000
res_y = 800
game_speed_value = 10
black = (0, 0, 0)
size_snake = (20, 20, 20, 20)
count = 0


def insert_name():
    player_name = input('Enter player name: ')
    if player_name == '':
        player_name = 'player1'
    return player_name


def print_hello_message(player_name):
    print(f'Welcome {player_name} to the best game ever! Python - Snake')


def game_loading():
    print('The game is loading...')
    clock.tick(1)


def create_screen():
    pygame.init()
    screen = pygame.display.set_mode((res_x, res_y))
    return screen


def clear_screen(count, screen):
    count += 1
    # print(count)
    # clear screen every 4 moves
    if count == 5:
        screen.fill(black)
        count = 0
    else:
        pass
    return count


def player_coordinates(box):
    coordinates = [box[0], box[1]]
    return coordinates

def is_snake_in_wall(player_position, res_x, res_y):
    if player_position[1] < 0 or player_position[1] > res_y:
        return True
    elif player_position[0] < 0 or player_position[0] > res_x:
        return True
    else:
        return False

def is_snake_bitten_tail():
    return False

def is_snake_dead(player_position, res_x, res_y):
    if is_snake_in_wall(player_position, res_x, res_y):
        return True
    elif is_snake_bitten_tail():
        return True
    else:
        return False

def main():
    os.system('clear')
    # add new player and print welcome information
    player_name = insert_name()
    print_hello_message(player_name)
    # start a game
    game_loading()
    os.system('clear')
    screen = create_screen()
    box = pygame.Rect(size_snake)
    global count
    creep_direction = 90
    while True:
        clock.tick(game_speed_value)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and creep_direction != 180:
                    creep_direction = 0
                elif event.key == pygame.K_RIGHT and creep_direction != 270:
                    creep_direction = 90
                elif event.key == pygame.K_DOWN and creep_direction != 0:
                    creep_direction = 180
                elif event.key == pygame.K_LEFT and creep_direction != 90:
                    box.y += 10
                    creep_direction = 270
                else:
                    creep_direction

        # InputK
        keys = pygame.key.get_pressed()
        if creep_direction == 90:
            box.x += game_speed_value
        elif creep_direction == 180:
            box.y += game_speed_value
        elif creep_direction == 270:
            box.x -= game_speed_value
        elif creep_direction == 0:
            box.y -= game_speed_value

        # Drawing
        # Clear screen
        count = clear_screen(count, screen)
        pygame.draw.rect(screen, (255, 0, 0), box)
        player_position = player_coordinates(box)

        print(player_position)
        print(is_snake_dead(player_position, res_x, res_y))
        if is_snake_dead(player_position, res_x, res_y) == True:
            break
        pygame.display.flip()


if __name__ == "__main__":
    main()


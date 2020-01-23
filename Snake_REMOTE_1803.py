# first version
import os
import pygame
import sys
from random import randint

pygame.init()
clock = pygame.time.Clock()
res_x = 1000
res_y = 800
myfont = pygame.font.SysFont('monospace', 16)
bigfont = pygame.font.SysFont('monospace', 44)
game_speed_value = 10
black = (0, 0, 0)
pixel_size = 20
size_snake = (int(res_x/2), int(res_y/2), pixel_size, pixel_size)
count = 0
box_color = (0, 255, 0)
creep_direction = 90
score = 0


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


def text_and_score(screen, score, player_name):
    disclaimer_text = myfont.render('SNAKE', 0, (255, 255, 255))
    name_text = myfont.render(f'Player: {player_name}', 0, (255, 255, 255))
    score_text = myfont.render("Score: " + str(score), 0, (255, 255, 255))
    screen.blit(name_text, (10, 10))
    screen.blit(disclaimer_text, (475, 745))
    screen.blit(score_text, (10, 30))


def menu(screen):
    game = 0
    menu_text = bigfont.render('Snake — The Game', 0, (255, 255, 255))
    start_text = myfont.render('Press ENTER to start', 0, (255, 255, 255))
    screen.blit(menu_text, (310, 30))
    screen.blit(start_text, (410, 600))
    pygame.display.flip()
    temp_key = pygame.event.get()
    for event in temp_key:
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game = 1
    return game


def clear_screen(count, screen):
    count += 1
    # clear screen every 4 moves when we use worm not snake
    if count == 1:  # 5 jesli chemy pełcać
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


def spawn_apple(res_x, res_y):
    apple_x = (randint(0, res_x/10))*10
    apple_y = (randint(0, res_y/10))*10
    return apple_x, apple_y


# do sprawdzenia


def catch_apple(score):
    score += 1
    spawn_apple(res_x, res_y)
    return score



def is_snake_bitten_tail(player_move):
    temp_list_body_snake = player_move.copy()[1:]
    head_snake = player_move[0]
    if head_snake in temp_list_body_snake:
        bool_val = True
    else:
        bool_val = False
    return bool_val


def is_snake_dead(player_position, res_x, res_y, player_move):
    if is_snake_in_wall(player_position, res_x, res_y):
        return True
    elif is_snake_bitten_tail(player_move):
        return True
    else:
        return False


def list_of_move_player(player_position, player_move, score):
    player_move.append(player_position)
    lenght_snake = score + 4
    if len(player_move) > lenght_snake:
        player_move = player_move[1:]
    return player_move


def inputs_from_os(creep_direction):
    temp_key = pygame.event.get()
    if len(temp_key) == 0:
        return creep_direction
    else:
        for event in temp_key:
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
                    creep_direction = 270
            else:
                return creep_direction

            return creep_direction


def direction_control(box, game_speed_value, creep_direction):
    if creep_direction == 90:
        box.x += game_speed_value
    elif creep_direction == 180:
        box.y += game_speed_value
    elif creep_direction == 270:
        box.x -= game_speed_value
    elif creep_direction == 0:
        box.y -= game_speed_value

    return box


def draw_apple_and_score(screen, apple_x, apple_y, player_name, score):
    apple_img = pygame.image.load('apple.png')
    screen.blit(apple_img, (apple_x, apple_y))
    text_and_score(screen, score, player_name)
    # if we need make rectangle
    '''
    pygame.draw.rect(screen, box_color, (apple_x, apple_y, 20, 20))
    
    '''


def draw_the_worm(game_mode, player_move, screen, box, pixel_size):
    if game_mode == 0:
        # Drawing worm longer then 1
        for i in range(len(player_move)):
            if i == 0:
                pygame.draw.rect(screen, (255, 0, 0), box)
            else:
                pygame.draw.rect(screen, (255, 0, 0), (player_move[i][0], player_move[i][1], pixel_size, pixel_size))
    elif game_mode == 1:
        # Drowing worm lenght 1
        pygame.draw.rect(screen, (255, 0, 0), box)
    else:
        sys.exit(0)


def main():
    # initial parameters
    game_mode = 0
    score = 0
    game = 0
    player_move = []
    # add new player and print welcome information
    player_name = insert_name()
    print_hello_message(player_name)
    # start a game
    game_loading()
    os.system('clear')
    screen = create_screen()
    while game == 0:
        # zmienić na ardziej ituicyjne
        game = menu(screen)
    box = pygame.Rect(size_snake)
    global count
    creep_direction = 90
    apple_x, apple_y = spawn_apple(res_x, res_y)
    while True:
        clock.tick(game_speed_value)
        creep_direction = inputs_from_os(creep_direction)
        # Input control of direction creep
        box = direction_control(box, game_speed_value, creep_direction)
        # Clear screen
        count = clear_screen(count, screen)
        # Drawing worm
        draw_the_worm(game_mode, player_move, screen, box, pixel_size)
        player_position = player_coordinates(box)
        player_move = list_of_move_player(player_position, player_move, score)
        # print(player_position)
        # print(is_snake_dead(player_position, res_x, res_y))
        if is_snake_dead(player_position, res_x, res_y, player_move) == True:
            sys.exit(0)
        draw_apple_and_score(screen, apple_x, apple_y, player_name, score)


        # print(player_move)
        # Check is a player eat apple
        # is_a_player_eat_apple():
        if player_position == [apple_x, apple_y]:
            score = catch_apple(score)
            apple_x, apple_y = spawn_apple(res_x, res_y)
            # print(f'Score: {score}')

        pygame.display.flip()



if __name__ == "__main__":
    main()

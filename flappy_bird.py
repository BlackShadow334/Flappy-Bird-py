import pygame
from pygame.locals import *
import random
import time
import math
import re

# GLOBAL VARIABLES
SCREENWIDTH = 800
SCREENHEIGHT = 600
FPS = 32
PLAYER_X = int(SCREENWIDTH * 0.2)
BASE_Y = int(SCREENHEIGHT * 0.87)
Y_OFFSET = 168  # 128 # miin required gap for bird to pass
X_OFFSET = 168  # 128 # miin required gap for bird to pass
MAX_OBJECT_X_DIST = 400  # 200
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GAME_NAME = "Flappy Bird"
GAME_ICON = "assets/bird3.png"


PLAYER1_IMG = "assets/bird1.png"
PLAYER2_IMG = "assets/bird2.png"
PLAYER3_IMG = "assets/bird3.png"
PLAYER4_IMG = "assets/bird4.png"
PLAYER5_IMG = "assets/bird5.png"
PLAYER6_IMG = "assets/bird6.png"

BACKGROUND1_IMG = "assets/background1.jpg"
BACKGROUND2_IMG = "assets/background2.jpg"
BACKGROUND3_IMG = "assets/background3.jpg"
BACKGROUND4_IMG = "assets/background4.jpg"
BACKGROUND5_IMG = "assets/background5.jpg"
BACKGROUND6_IMG = "assets/background6.jpg"

BASE1_IMG = "assets/base1.png"
BASE2_IMG = "assets/base2.png"
BASE3_IMG = "assets/base3.png"
BASE4_IMG = "assets/base4.png"
BASE5_IMG = "assets/base5.png"
BASE6_IMG = "assets/base6.png"

OBJECT1_IMG = "assets/object1.png"
OBJECT2_IMG = "assets/object2.png"
OBJECT3_IMG = "assets/object3.png"
OBJECT4_IMG = "assets/object4.png"

BACKGROUND_MUSIC = "assets/music.ogg"
FLAP_SOUND = "assets/flap.ogg"
SCOREUP_SOUND = "assets/score_up.ogg"
HIT_SOUND = "assets/hit.ogg"
OVER_SOUND = "assets/game_over.ogg"
BUTTON_SOUND = "assets/button.ogg"

FONT_FILE1 = "assets/ToetheLineless.ttf"
FONT_FILE2 = "assets/zai_CourierPolski1941.ttf"

COLORS = {
    1: {
        "game_name": (72, 217, 113),
        "choose": (255, 222, 205),
        "abcd": (255, 222, 205),
        "space": (170, 255, 170),
        "controls": (255, 222, 205),
        "game_score": (49, 149, 242),
        "over": (255, 78, 0),
        "your_score": (200, 255, 255),
        "best_player": (255, 255, 130),
    },
    2: {
        "game_name": (0, 75, 180),
        "choose": (0, 100, 140),
        "abcd": (150, 215, 255),
        "space": (20, 80, 190),
        "controls": (150, 215, 255),
        "game_score": (80, 80, 150),
        "over": (0, 75, 180),
        "your_score": (0, 100, 140),
        "best_player": (20, 129, 245),
    },
    3: {
        "game_name": (72, 240, 113),
        "choose": (57, 180, 196),
        "abcd": (18, 100, 190),
        "space": (72, 250, 113),
        "controls": (57, 180, 196),
        "game_score": (57, 180, 196),
        "over": (57, 180, 196),
        "your_score": (20, 129, 245),
        "best_player": (22, 108, 212),
    },
    4: {
        "game_name": (72, 217, 113),
        "choose": (72, 217, 113),
        "abcd": (255, 255, 255),
        "space": (71, 44, 188),
        "controls": (218, 224, 231),
        "game_score": (49, 149, 242),
        "over": (255, 146, 31),
        "your_score": (63, 14, 50),
        "best_player": (67, 13, 86),
    },
    5: {
        "game_name": (72, 217, 113),
        "choose": (60, 202, 236),
        "abcd": (49, 149, 242),
        "space": (49, 149, 242),
        "controls": (49, 149, 242),
        "game_score": (217, 252, 201),
        "over": (49, 149, 242),
        "your_score": (34, 180, 117),
        "best_player": (12, 217, 253),
    },
    6: {
        "game_name": (72, 217, 113),
        "choose": (195, 214, 200),
        "abcd": (17, 21, 18),
        "space": (49, 149, 242),
        "controls": (49, 149, 242),
        "game_score": (49, 149, 242),
        "over": (249, 180, 70),
        "your_score": (181, 196, 24),
        "best_player": (181, 196, 24),
    },
}


PLAYERS = {}
BACKGROUNDS = {}
OBJECTS_DOWN = {}
OBJECTS_UP = {}
BASES = {}
SOUNDS = {}
FONTS = {}


if __name__ == "__main__":

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption(GAME_NAME)
    GAME_ICON = pygame.image.load("assets/bird3.png")
    pygame.display.set_icon(GAME_ICON)
    PLAYERS = {
        1: pygame.image.load(PLAYER1_IMG).convert_alpha(),
        2: pygame.image.load(PLAYER2_IMG).convert_alpha(),
        3: pygame.image.load(PLAYER3_IMG).convert_alpha(),
        4: pygame.image.load(PLAYER4_IMG).convert_alpha(),
        5: pygame.image.load(PLAYER5_IMG).convert_alpha(),
        6: pygame.image.load(PLAYER6_IMG).convert_alpha(),
    }
    BACKGROUNDS = {
        1: pygame.image.load(BACKGROUND1_IMG).convert(),
        2: pygame.image.load(BACKGROUND2_IMG).convert(),
        3: pygame.image.load(BACKGROUND3_IMG).convert(),
        4: pygame.image.load(BACKGROUND4_IMG).convert(),
        5: pygame.image.load(BACKGROUND5_IMG).convert(),
        6: pygame.image.load(BACKGROUND6_IMG).convert(),
    }
    BASES = {
        1: pygame.image.load(BASE1_IMG).convert_alpha(),
        2: pygame.image.load(BASE2_IMG).convert_alpha(),
        3: pygame.image.load(BASE3_IMG).convert_alpha(),
        4: pygame.image.load(BASE4_IMG).convert_alpha(),
        5: pygame.image.load(BASE5_IMG).convert_alpha(),
        6: pygame.image.load(BASE6_IMG).convert_alpha(),
    }
    OBJECTS_DOWN = {
        1: pygame.image.load(OBJECT1_IMG).convert_alpha(),
        2: pygame.image.load(OBJECT2_IMG).convert_alpha(),
        3: pygame.image.load(OBJECT3_IMG).convert_alpha(),
        4: pygame.image.load(OBJECT4_IMG).convert_alpha(),
    }
    OBJECTS_UP = {
        1: pygame.transform.flip(OBJECTS_DOWN[1], False, True),
        2: pygame.transform.flip(OBJECTS_DOWN[2], False, True),
        3: pygame.transform.flip(OBJECTS_DOWN[3], False, True),
        4: pygame.transform.flip(OBJECTS_DOWN[4], False, True),
    }
    SOUNDS = {
        "background": pygame.mixer.music.load(BACKGROUND_MUSIC),
        "flap": pygame.mixer.Sound(FLAP_SOUND),
        "scoreUp": pygame.mixer.Sound(SCOREUP_SOUND),
        "hit": pygame.mixer.Sound(HIT_SOUND),
        "over": pygame.mixer.Sound(OVER_SOUND),
        "button": pygame.mixer.Sound(BUTTON_SOUND),
    }
    FONTS = {
        1: pygame.font.Font(FONT_FILE1, 70),
        2: pygame.font.Font(FONT_FILE2, 70),
        3: pygame.font.Font(FONT_FILE2, 50),
        4: pygame.font.Font(FONT_FILE2, 40),
        5: pygame.font.Font(FONT_FILE2, 30),
        6: pygame.font.Font(FONT_FILE2, 25),
        7: pygame.font.Font(FONT_FILE2, 20),
        8: pygame.font.Font(FONT_FILE2, 16),
    }

    pygame.mixer.music.play(-1)
    # getting random index of BACKGROUNDS , BASES , OBJECTS
    random_background_i = random.randint(1, len(BACKGROUNDS))

    random_base_i = random.randint(1, len(BASES))
    random_objects_i = random.randint(1, len(OBJECTS_DOWN))
    # default index of PLAYERS
    players_i = 3

    # UTILITY FUNCTIONS
    def write_wrt_center(content, position, color, size):
        """("content", (position) , "color" , size)"""
        text = FONTS[size].render(content, True, color)
        rect = text.get_rect()
        rect.center = position
        SCREEN.blit(text, rect)

    # hrere oubiously objects means pipes
    def get_random_objects_pos(object_down, object_up):
        """it returns random position of objects as required"""
        x_down = SCREENWIDTH + random.randint(0, MAX_OBJECT_X_DIST)
        y_down = Y_OFFSET + (random.randint(0, (BASE_Y - Y_OFFSET)))
        x_up = SCREENWIDTH + random.randint(0, MAX_OBJECT_X_DIST)
        y_up = random.randint(0, (BASE_Y - Y_OFFSET)) - object_up.get_height()
        if math.fabs(x_down - x_up) <= X_OFFSET + object_down.get_width():
            while y_down - (y_up + object_up.get_height()) <= Y_OFFSET:
                y_down = Y_OFFSET + (random.randint(0, (BASE_Y - Y_OFFSET)))
                y_up = random.randint(0, (BASE_Y - Y_OFFSET)) - object_down.get_height()
        return {
            "x_down": x_down,
            "y_down": y_down,
            "x_up": x_up,
            "y_up": y_up,
        }

    # MAIN FUNCTIONS :
    # WELCOME SCREEN FUNCTION
    welcome_loop_running = True

    def show_welcomeScreen():
        """
        it shows welcome screen and do all the stufs whem main game is not running
        """
        global main_loop_running
        global welcome_loop_running
        global game_loop_running
        global over_loop_running
        global players_i

        while welcome_loop_running:
            # controls in case of welcomeScreen
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYUP and event.key == pygame.K_END
                ):
                    main_loop_running = False
                    welcome_loop_running = False
                    game_loop_running = False
                    over_loop_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        SOUNDS["button"].play()
                        welcome_loop_running = False
                        game_loop_running = True

                    i = 1
                    while i <= len(PLAYERS):
                        if event.key == (96 + i):
                            players_i = i
                            SOUNDS["button"].play()
                        i += 1
            # drawing display in case of  welcomeScreen
            SCREEN.blit(BACKGROUNDS[random_background_i], (0, 0))
            SCREEN.blit(PLAYERS[players_i], (PLAYER_X, int(SCREENHEIGHT * 0.35)))

            # fonts
            write_wrt_center(
                "Flappy birD",
                (int(SCREENWIDTH * 0.5), int(SCREENHEIGHT * 0.25)),
                COLORS[random_background_i]["game_name"],
                1,
            )
            # choose bird text
            write_wrt_center(
                "Choose your Bird",
                (int(SCREENWIDTH * 0.5), int(SCREENHEIGHT * 0.5)),
                COLORS[random_background_i]["choose"],
                6,
            )

            # player choosse display, here some calculation is done to keep it in center
            i = 1
            player_choose_x_start = (
                SCREENWIDTH / 2 - (len(PLAYERS) * (64 + 20) - 20) / 2
            )
            while i <= len(PLAYERS):
                SCREEN.blit(
                    PLAYERS[i], (int(player_choose_x_start), int(SCREENHEIGHT * 0.55))
                )
                choose_keyValue = 96 + i
                write_wrt_center(
                    f"{pygame.key.name(choose_keyValue)}",
                    (
                        int(player_choose_x_start + 32),
                        int(SCREENHEIGHT * 0.55 + 64 + 15),
                    ),
                    COLORS[random_background_i]["abcd"],
                    7,
                )
                i += 1
                player_choose_x_start += 64 + 20

            # text : press SPACE and other instructiona
            if time.time() % 1 > 0.2:
                write_wrt_center(
                    "Press Space",
                    (int(SCREENWIDTH * 0.5), int(SCREENHEIGHT * 0.75)),
                    COLORS[random_background_i]["space"],
                    5,
                )
            write_wrt_center(
                "TO Choose : press respective key",
                (int(SCREENWIDTH * 0.5), int(SCREENHEIGHT * 0.85)),
                COLORS[random_background_i]["controls"],
                8,
            )
            write_wrt_center(
                "To exit game : press delete key",
                (int(SCREENWIDTH * 0.5), int(SCREENHEIGHT * 0.89)),
                COLORS[random_background_i]["controls"],
                8,
            )
            pygame.display.update()
            FPSCLOCK.tick(FPS)

    # cheacking bird collision with base, floor(y=0 position) ,objects (pipes)
    def check_bird_collision(
        player_img, player_pos, base_y_pos, floor_y_pos, object_list, object_sample
    ):
        i = 0
        while i < len(object_list):
            player_left_x = player_pos[0] + player_img.get_width() * 0.1
            player_top_y = player_pos[1] + player_img.get_height() * 0.2
            player_right_x = player_pos[0] + player_img.get_width() * 0.9
            player_bottom_y = player_pos[1] + player_img.get_height() * 0.8

            object_down_left_x = (
                object_list[i]["x_down"] + object_sample.get_width() * 0.2
            )
            object_down_top_y = object_list[i]["y_down"]
            object_down_right_x = (
                object_list[i]["x_down"] + object_sample.get_width() * 0.8
            )

            object_up_left_x = object_list[i]["x_up"] + object_sample.get_width() * 0.2
            object_up_bottom_y = (
                object_list[i]["y_up"] + object_sample.get_height() * 0.98
            )
            object_up_right_x = object_list[i]["x_up"] + object_sample.get_width() * 0.8

            if player_bottom_y >= base_y_pos:
                return True
            if player_top_y <= 0:
                return True
            if (
                player_right_x >= object_down_left_x
                and player_left_x <= object_down_right_x
                and player_bottom_y >= object_down_top_y
            ):
                return True
            if (
                player_right_x >= object_up_left_x
                and player_left_x <= object_up_right_x
                and player_top_y <= object_up_bottom_y
            ):
                return True
            i += 1

    # MAIN GAME FUNCTION
    game_loop_running = True
    score = 3

    def run_game():
        """
        here actual game runs and it runs till player hit object.
        on pressing return key "welcome_loop_runing " become false
        due to which progam points towards this function.
        """
        global score
        score = 0
        score_inc_status = True
        player_x = int(PLAYER_X)
        player_y = int(SCREENHEIGHT * 0.35)
        obj_dx = -5
        player_dy = 1
        gravity = 0.8
        object_list = []

        # up and down both positiono installing objects
        objects_pos = get_random_objects_pos(
            OBJECTS_DOWN[random_objects_i], OBJECTS_UP[random_objects_i]
        )
        object_list.append(objects_pos)

        base1 = BASES[random_base_i]
        base2 = BASES[random_base_i]
        base1_pos = [0, BASE_Y]
        base2_pos = [SCREENWIDTH, BASE_Y]
        # print(object_list)
        global main_loop_running
        global welcome_loop_running
        global game_loop_running
        global over_loop_running
        while game_loop_running:

            SCREEN.blit(BACKGROUNDS[random_background_i], (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYUP and event.key == pygame.K_END
                ):
                    main_loop_running = False
                    welcome_loop_running = False
                    game_loop_running = False
                    over_loop_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player_dy = -10
                        SOUNDS["flap"].play()

            # for OBJECTS and some calculations
            # down here : objects moving , score increasing
            # drawing all objects (pipes)
            i = 0
            while i < len(object_list):
                SCREEN.blit(
                    OBJECTS_DOWN[random_objects_i],
                    (int(object_list[i]["x_down"]), int(object_list[i]["y_down"])),
                )
                SCREEN.blit(
                    OBJECTS_UP[random_objects_i],
                    (int(object_list[i]["x_up"]), int(object_list[i]["y_up"])),
                )
                # moving objects
                object_list[i]["x_down"] += obj_dx
                object_list[i]["x_up"] += obj_dx
                # appending pipe positions in list if required
                if object_list[len(object_list) - 1]["x_down"] < SCREENWIDTH - (
                    X_OFFSET + OBJECTS_DOWN[random_objects_i].get_width()
                ) and object_list[len(object_list) - 1]["x_up"] < SCREENWIDTH - (
                    X_OFFSET + OBJECTS_DOWN[random_objects_i].get_width()
                ):
                    newObject = get_random_objects_pos(
                        OBJECTS_DOWN[random_objects_i], OBJECTS_UP[random_objects_i],
                    )
                    if (
                        math.fabs(object_list[i]["x_down"] - newObject["x_up"])
                        <= X_OFFSET + OBJECTS_DOWN[random_objects_i].get_width()
                        or math.fabs(object_list[i]["x_up"] - newObject["x_down"])
                        <= X_OFFSET + OBJECTS_UP[random_objects_i].get_width()
                    ):
                        while (
                            object_list[i]["y_down"]
                            - (
                                newObject["y_up"]
                                + OBJECTS_DOWN[random_objects_i].get_height()
                            )
                            <= Y_OFFSET
                            or newObject["y_down"]
                            - (object_list[i]["y_up"] + OBJECTS_UP[random_objects_i])
                            <= Y_OFFSET
                        ):
                            newObject["y_down"] = Y_OFFSET + (
                                random.randint(0, (BASE_Y - Y_OFFSET))
                            )
                            newObject["y_up"] = (
                                random.randint(0, (BASE_Y - Y_OFFSET))
                                - OBJECTS_UP[random_objects_i].get_height()
                            )
                    object_list.append(newObject)
                    SOUNDS["scoreUp"].play()

                player_right_x = player_x + PLAYERS[players_i].get_width()
                player_left_x = player_x
                object_up_left_x = object_list[i]["x_up"]
                object_up_right_x = (
                    object_list[i]["x_up"] + OBJECTS_UP[random_objects_i].get_width()
                )
                object_down_left_x = object_list[i]["x_up"]
                object_down_right_x = (
                    object_list[i]["x_up"] + OBJECTS_DOWN[random_objects_i].get_width()
                )

                i += 1
            score = len(object_list)
            if score % 10 == 0:
                obj_dx = -int(score / 10 + 5)
            write_wrt_center(
                str(score),
                (int(SCREENWIDTH * 0.5), int(SCREENHEIGHT * 0.08)),
                COLORS[random_background_i]["game_score"],
                2,
            )
            # base blitting and moving
            SCREEN.blit(base1, base1_pos)
            SCREEN.blit(base2, base2_pos)
            base1_pos[0] += obj_dx
            base2_pos[0] += obj_dx
            if base1_pos[0] <= -SCREENWIDTH:
                base1_pos[0] = SCREENWIDTH
            if base2_pos[0] <= -SCREENWIDTH:
                base2_pos[0] = SCREENWIDTH
            # player blitting and moving (controls not here)
            if check_bird_collision(
                PLAYERS[players_i],
                (player_x, player_y),
                BASE_Y,
                0,
                object_list,
                OBJECTS_UP[random_objects_i],
            ):
                SOUNDS["hit"].play()

                game_loop_running = False
                over_loop_running = True
            SCREEN.blit(PLAYERS[players_i], (int(player_x), int(player_y)))
            player_y += player_dy
            player_dy += gravity

            pygame.display.update()
            FPSCLOCK.tick(FPS)

    # OVER SCREEN FUNCTION
    over_loop_running = True

    def show_overScreen():
        """after player hits object it become functional because,
        (game_loop_running) become false 
        """
        global main_loop_running
        global welcome_loop_running
        global game_loop_running
        global over_loop_running
        global random_background_i
        global random_base_i
        global random_objects_i
        global score
        time.sleep(0.5)
        SOUNDS["over"].play()
        abc_file_a = open("abc.bat", "a+")
        abc = abc_file_a.read()
        if len(abc) == 0:
            abc_file_a.write("Flappy Bird:0,")
        abc_file_a.close()
        new_player_text = ""
        file_ready = True
        while over_loop_running:
            SCREEN.blit(BACKGROUNDS[random_background_i], (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYUP and event.key == pygame.K_END
                ):
                    main_loop_running = False
                    welcome_loop_running = False
                    game_loop_running = False
                    over_loop_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        SOUNDS["button"].play()
                        if "highest_score" in locals():
                            if int(score) >= int(highest_score):
                                abc_file_a = open("abc.bat", "a+")
                                new_player = new_player_text
                                abc_file_a.write(f"{new_player}:{score},")
                                abc_file_a.close()
                                score = 0
                        over_loop_running = False
                        welcome_loop_running = True
                        # settting random index of BACKGROUNDS , BASES , OBJECTS again
                        random_background_i = random.randint(1, len(BACKGROUNDS))
                        random_base_i = random.randint(1, len(BASES))
                        random_objects_i = random.randint(1, len(OBJECTS_DOWN))

                    # new_player_text written if player makes new high score
                    if event.key == pygame.K_BACKSPACE:
                        if len(new_player_text) > 0:
                            SOUNDS["button"].play()
                            new_player_text = new_player_text[:-1]
                    else:
                        if re.match(r"[a-zA-Z0-9_\-\s]", event.unicode):
                            SOUNDS["button"].play()
                            new_player_text += event.unicode

            write_wrt_center(
                "Game Over",
                (int(SCREENWIDTH * 0.5), int(SCREENHEIGHT * 0.3)),
                COLORS[random_background_i]["over"],
                2,
            )
            if time.time() % 1 >= 0.2:
                write_wrt_center(
                    "Press Enter ",
                    (int(SCREENWIDTH * 0.5), int(SCREENHEIGHT * 0.75)),
                    COLORS[random_background_i]["space"],
                    5,
                )
            # file processing
            if file_ready == True:
                highest_score = 0
                abc_file_r = open("abc.bat", "r")
                abc = abc_file_r.read()
                abc_pattern = r"([a-zA-Z0-9_\-\s]+):([0-9]+),"
                abc_match = re.findall(abc_pattern, abc)
                abc_file_r.close()

                if abc_match:
                    for statement in abc_match:
                        each_player = statement[0]
                        each_score = statement[1]
                        if int(each_score) >= int(highest_score):
                            highest_score = each_score
                            best_player = each_player
                file_ready = False

            if int(score) >= int(highest_score):
                write_wrt_center(
                    f"new high score : {score}",
                    (int(SCREENWIDTH * 0.5), int(SCREENHEIGHT * 0.5)),
                    COLORS[random_background_i]["your_score"],
                    5,
                )

                text = FONTS[5].render(
                    f"Enter your name : {new_player_text}",
                    True,
                    COLORS[random_background_i]["best_player"],
                )
                text_rect = text.get_rect()
                text_rect.center = (int(SCREENWIDTH * 0.5), int(SCREENHEIGHT * 0.6))
                SCREEN.blit(text, text_rect)
                bar = FONTS[5].render(
                    "|", True, COLORS[random_background_i]["best_player"]
                )
                bar_rect = bar.get_rect()
                bar_rect.topleft = text_rect.topright
                if time.time() % 1 > 0.5:
                    SCREEN.blit(bar, bar_rect)

            else:
                write_wrt_center(
                    f"your score : {score}",
                    (int(SCREENWIDTH * 0.5), int(SCREENHEIGHT * 0.5)),
                    COLORS[random_background_i]["your_score"],
                    5,
                )
                write_wrt_center(
                    f"{best_player} : {highest_score}",
                    (int(SCREENWIDTH * 0.5), int(SCREENHEIGHT * 0.6)),
                    COLORS[random_background_i]["best_player"],
                    5,
                )

            pygame.display.update()
            FPSCLOCK.tick(FPS)

    main_loop_running = True
    while main_loop_running:
        show_welcomeScreen()
        run_game()
        show_overScreen()

    pygame.quit()
print()
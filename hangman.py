import os
import random
import unidecode #el mòdulo debe instalarse pip3 install unidecode

#https://asciiflow.com/#/
def read_words():
    with open("./archivos/data.txt","r",encoding="utf-8") as f:
        words = [unidecode.unidecode(word).strip() for word in f]
    return words

def clear_screen():
    os.system("clear")

def input_user():
    try:
        char = input("\n\nIngresa una letra: ")
        if len(char) != 1:
            raise ValueError("Has salido del juego")
        return char.lower()
    except ValueError as ve:
        print(ve)
        return False

def progress(count):
    ascii = """
        
        
        
        
        
        
        
        
        
        
      ─────────────────
        """
    if count == 1:
        ascii = """
        │
        │
        │
        │
        │
        │
        │
        │
        │
        │
      ──┴──────────────
        """
    elif count == 2:
        ascii ="""
        ┌─┬───────────
        │ │
        ├─┘
        │
        │
        │
        │
        │
        │
        │
      ──┴──────────────
        """
    elif count == 3:
        ascii = """
        ┌─┬───────────
        │ │
        ├─┘
        │
        │      xxx
        │     x   x
        │     x   x
        │      xxx
        │
        │
      ──┴──────────────
        """
    elif count == 4:
        ascii = """
        ┌─┬───────────
        │ │
        ├─┘
        │
        │      xxx
        │     x   x
        │     x   x
        │      xxx
        │      x x
        │     xx xx
      ──┴──────────────
        """
    elif count == 5:
        ascii = """
        ┌─┬───────────
        │ │
        ├─┘
        │
        │  x   xxx
        │   xxx   x
        │     x   x
        │      xxx
        │      x x
        │     xx xx
      ──┴──────────────
        """
    elif count == 6:
        ascii = """
        ┌─┬───────────
        │ │
        ├─┘
        │
        │  x   xxx   x
        │   xxx   xxx
        │     x   x
        │      xxx
        │      x x
        │     xx xx
      ──┴──────────────
        """
    elif count == 7:
        ascii = """
        ┌─┬───────────
        │ │    xx
        ├─┘   x  x
        │      xx
        │  x   xxx   x
        │   xxx   xxx
        │     x   x
        │      xxx
        │      x x
        │     xx xx
      ──┴──────────────
        """
    elif count == 8:
        ascii = """
        ┌─┬────────┬──
        │ │    xx  │
        ├─┘   x  x │
        │      xx──┘
        │  x   xxx   x
        │   xxx   xxx
        │     x   x
        │      xxx
        │      x x
        │     xx xx
      ──┴──────────────
        """
    return ascii



def print_result(user,dict):
    count = 0
    for k,v in dict.items():
        if k in user:
            print(f"{v.upper()}",end=" ")
        else:
            print("__",end=" ")
            count += 1

    if count == 0:
        word = list(dict.values())
        word = "".join(word).upper()
        print(f"\nHas ganado la palabra es: {word}")

    return count

def reset_game():
    clear_screen()
    user = []
    words = read_words()
    word = random.choice(words)
    word_dict = dict(enumerate(word))
    attempts = 0

    return user,word_dict,attempts



def run():
    menu = """
x   x xxxxx xxx x xxxxx xxxxxx xxxxx xxx x
x   x x   x x x x x     x xx x x   x x x x
xxxxx xxxxx x x x x xxx x xx x xxxxx x x x
x   x x   x x x x x   x x xx x x   x x x x
x   x x   x x xxx xxxxx x xx x x   x x xxx

Adivina la palabra
    """
    user,word_dict,attempts = reset_game()
    while True:
        clear_screen()
        print(menu)
        print(progress(attempts))
        if attempts >= 8:
            print("Has perdido :(")
            option = input("\n¿Quieres seguir jugando? \n[1] Si \n[2] No\n>>>")
            if option == '1':
                user,word_dict,attempts = reset_game()
            else:
                break
        gameover = print_result(user,word_dict)
        if gameover > 0:
            char = input_user()
            if char == False:
                break
            positions = [k for k,v in word_dict.items() if v == char]

            if len(positions) > 0:
                for pos in positions:
                    if pos not in user:
                        user.append(pos)
            else:
                attempts += 1
        else:
            option = input("\n¿Quieres seguir jugando? \n[1] Si \n[2] No\n>>>")
            if option == '1':
                user,word_dict,attempts = reset_game()
            else:
                break


if __name__ == "__main__":
    run()
from file_handler import *
from secret import *

if __name__ == '__main__':
    app_on = True
    while app_on:
        selected_menu = 0
        save_to_file = ''
        file_name = ''

        # print main menu
        print('=========[KEEP IT SECRET]=========')
        print('1. ENCRYPT')
        print('2. DECRYPT')
        print('3. EXIT')

        # get selected menu from user
        while not (0 < selected_menu < 4):
            selected_menu = input('\n> CHOOSE MENU: ')
            if not selected_menu.isnumeric():
                selected_menu = 0
                continue
            selected_menu = int(selected_menu)

        # exit when user select menu no 3
        if selected_menu == 3:
            app_on = False
            continue

        # get text from user
        text = input('\n> ENTER TEXT: ')
        if selected_menu == 1:
            text = Secret(text).encrypt()
        else:
            text = Secret(text).decrypt()
        print('\n> RESULT: "' + text + '"')

        # promp to ask if result want to save into file
        while not save_to_file:
            save_to_file = input('\n> SAVE TO FILE? (Y/n)').lower()
            if save_to_file != 'n' and save_to_file != 'y':
                save_to_file = ''

        # stop if user reject
        if save_to_file != 'y':
            continue
        
        # force user not fill an empty file name
        while not file_name:
            file_name = input('\n> FILE NAME: ')
            if not file_name:
                print('\n> PLEASE FILL FILE NAME!')

        # save into file
        file_handler = FileHandler(file_name)
        if not file_handler.is_exists():
            file_handler.create()

        file_handler.write(text)

import random
import tkinter as tk

choices = ['камень', 'ножницы', 'бумага']

def play_game(user_choice):
    computer_choice = random.choice(choices)

    result_message = f"Вы выбрали: {user_choice}\nКомпьютер выбрал: {computer_choice}\n"

    if user_choice == computer_choice:
        result_message += "Ничья!"
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
         (user_choice == 'ножницы' and computer_choice == 'бумага') or \
         (user_choice == 'бумага' and computer_choice == 'камень'):
        result_message += "Вы победили!"
    else:
        result_message += "Компьютер победил!"

    result_label.config(text=result_message)

def on_button_click(choice):
    play_game(choice)

root = tk.Tk()
root.title("Камень, ножницы, бумага")

result_label = tk.Label(root, text="Выберите: камень, ножницы или бумагу.")
result_label.pack(pady=10)

br = tk.Button(root, text="Камень", command=lambda: on_button_click('камень'))
br.pack(side=tk.LEFT, padx=10, pady=10)

bs = tk.Button(root, text="Ножницы", command=lambda: on_button_click('ножницы'))
bs.pack(side=tk.LEFT, padx=10, pady=10)

bp = tk.Button(root, text="Бумага", command=lambda: on_button_click('бумага'))
bp.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()
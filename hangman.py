import tkinter as tk
import os
from tkinter import messagebox

class HangmanGame:
    def __init__(self, root):
        self.word = input("Enter a word : ").lower()
        os.system("cls")
        print("Playing Hangman ...")

        self.root = root
        self.root.title("Hangman Game")
        self.guessed_letters = set()

        self.chances = len(self.word) + 2

        self.word_label = tk.Label(root, text=self.display_word(), font=("Arial", 20))
        self.word_label.pack(pady=10)

        self.chances_label = tk.Label(root, text=f"Chances left: {self.chances}", font=("Arial", 14))
        self.chances_label.pack()

        self.guess_entry = tk.Entry(root, font=("Arial", 16))
        self.guess_entry.pack(pady=10)
        self.guess_entry.bind("<Return>", lambda event: self.make_guess())  # Bind Enter key event
    

    def display_word(self):
        return ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])

    def make_guess(self):
        guess = self.guess_entry.get().lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in self.guessed_letters:
                messagebox.showinfo("Hangman", "You already guessed that letter. Try again.")
            else:
                self.guessed_letters.add(guess)

                if guess not in self.word:
                    self.chances -= 1

                self.word_label.config(text=self.display_word())
                self.chances_label.config(text=f"Chances left: {self.chances}")

                if self.display_word().replace(' ', '') == self.word:
                    messagebox.showinfo("Hangman", f"Congratulations, you won! The word is: {self.word}")
                    self.root.destroy()
                elif self.chances == 0:
                    messagebox.showinfo("Hangman", f"Sorry, you lose! The correct word was: {self.word}")
                    self.root.destroy()
        else:
            messagebox.showinfo("Hangman", "Invalid guess. Please enter a single letter.")
        self.guess_entry.delete(0,tk.END)
if __name__ == "__main__":
    root = tk.Tk()
    hangman_game = HangmanGame(root)
    root.mainloop()

import string
import random
import requests

class Game:
    def __init__(self):
        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)]

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        grid_copy = self.grid.copy()

        if not word:  # Return False if the word is empty
            return False

        for letter in word.upper():
            if letter in grid_copy:
                grid_copy.remove(letter)
            else:
                return False
        return self.__check_dictionary(word)

    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://dictionary.lewagon.com/{word}")
        json_response = response.json()
        return json_response['found']

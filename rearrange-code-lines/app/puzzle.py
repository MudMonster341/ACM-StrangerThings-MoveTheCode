''' Contains main puzzle generation code '''

import random
import os
from app.constants import *

class Puzzle:
    base_path = PUZZLES_DIR
    testing = False
    def __init__(self, lang: str, puzzle_name: str) -> None:
        self.lang = lang
        self.puzzle_name = puzzle_name
        self.puzzle_lines = self.shuffle_lines()

    @classmethod
    def get_lines(cls, lang: str, file_path: str) -> list[str]:
        file_path = Puzzle.base_path + lang + f'/{file_path}' if not Puzzle.testing else file_path
        with open(file_path) as f:
            lines = [line for line in f.read().splitlines() if line]
        return lines
    
    def shuffle_lines(self):
        lines = Puzzle.get_lines(self.lang, self.puzzle_name)
        random.shuffle(lines)
        return lines
    
    @classmethod   
    def get_puzzles(cls, lang: str):
        lang = lang.strip().title()
        base_path = Puzzle.base_path + lang if not Puzzle.testing else None
        files = [file for file in os.listdir(base_path) if file.endswith(SUPPORTED_LANGS[lang])]
        random.shuffle(files)

        puzzles = []
        for file in files[:MAX_PUZZLES]:
            puzzles.append(Puzzle(lang, file))
        
        return puzzles
    
    @classmethod
    def check_puzzle(cls, lang: str, puzzle_name: str, solution: list[str]):
        actual_solution = Puzzle.get_lines(lang, puzzle_name)
        if actual_solution == solution:
            return True
        return False
            
if __name__ == '__main__':
    Puzzle.testing = True
    Puzzle.get_puzzles('C')
    print(Puzzle.check_puzzle('C', 'helloworld2.c', ['#include <stdio.h>', 'int main() {', '    printf("Hello world 2!\\n");', '    return 0;', '}']))
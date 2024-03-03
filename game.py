import random
import numpy as np
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

class Game:
    def __init__(self, size=10):
        self.size = size
        self.board = np.zeros((size, size))
        self.player = (0, 0)
        self.score = 0
        self.ghosts = [(size-1, size-1)]
        self.points = []
        self.populate_points()

    def populate_points(self):
        for _ in range(self.size*2):  # Adjust as needed
            while True:
                point = (random.randint(0, self.size-1), random.randint(0, self.size-1))
                if point not in self.points and point != self.player and point not in self.ghosts:
                    self.points.append(point)
                    break

    def move_ghosts(self):
        for i, ghost in enumerate(self.ghosts):
            grid = Grid(matrix=self.board)
            start = grid.node(ghost[0], ghost[1])
            end = grid.node(self.player[0], self.player[1])
            finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
            path, _ = finder.find_path(start, end, grid)
            if len(path) > 1:
                self.ghosts[i] = (path[1][0], path[1][1])

    def move_player(self, direction):
        if direction == 'up':
            self.player = (max(0, self.player[0]-1), self.player[1])
        elif direction == 'down':
            self.player = (min(self.size-1, self.player[0]+1), self.player[1])
        elif direction == 'left':
            self.player = (self.player[0], max(0, self.player[1]-1))
        elif direction == 'right':
            self.player = (self.player[0], min(self.size-1, self.player[1]+1))
        if self.player in self.points:
            self.points.remove(self.player)
            self.score += 1

    def game_over(self):
        if self.score >= self.size*2 or not self.points:  # Adjust as needed
            return True, "You Win!"
        if self.player in self.ghosts:
            return True, "You Lose!"
        return False, ""

# Example usage
game = Game()
while True:
    game.move_player(input("Direction? "))  # Get user input
    game.move_ghosts()
    over, message = game.game_over()
    if over:
        print(message)
        break
# Create a tic-tac-toe board
import random
import pygame

# Function to draw grid lines
def draw_grid_lines(grid_size, screen_width, screen_height, screen):
        # Draw grid lines
        for i in range(1, grid_size):
                pygame.draw.line(screen, (0, 0, 0), (screen_width / grid_size * i, 0), (screen_width / grid_size * i, screen_height), 5)
                pygame.draw.line(screen, (0, 0, 0), (0, screen_height / grid_size * i), (screen_width, screen_height / grid_size * i), 5)

# Function for drawing X
def draw_x(x, y, size, screen):
        pygame.draw.line(screen, (0, 0, 0), (x, y), (x + size, y + size), 5)
        pygame.draw.line(screen, (0, 0, 0), (x + size, y), (x, y + size), 5)

# Function for drawing O
def draw_o(x, y, size, screen):
        pygame.draw.circle(screen, (0, 0, 0), (int(x + size / 2), int(y + size / 2)), int(size / 2), 5)

# Function for drawing squares
def draw_square(x, y, size, screen):
        reducer = 10
        size -= reducer
        x += reducer / 2
        y += reducer / 2
        pygame.draw.rect(screen, (0, 0, 0), (x, y, size, size), 5)

# Function for drawing triangles
def draw_triangle(x, y, size, screen):
        reducer = 15
        size -= reducer
        x += reducer / 2
        y += reducer / 2
        pygame.draw.polygon(screen, (0, 0, 0), ((x, y + size), (x + size, y + size), (x + size / 2, y)), 5)

# Function for drawing stars
def draw_star(x, y, size, screen):
        pygame.draw.polygon(screen, (0, 0, 0), ((x + size / 2, y), (x + size / 2 + size / 10, y + size / 2 - size / 10), (x + size, y + size / 2 - size / 10), (x + size / 2 + size / 5, y + size / 2 + size / 10), (x + size / 2 + size / 2.5, y + size), (x + size / 2, y + size / 2 + size / 3), (x + size / 2 - size / 2.5, y + size), (x + size / 2 - size / 5, y + size / 2 + size / 10), (x, y + size / 2 - size / 10), (x + size / 2 - size / 10, y + size / 2 - size / 10)), 5)

# Function for drawing shapes
def draw_shape(x, y, size, shape, screen):
        if shape == 1:
                draw_x(x, y, size, screen)
        elif shape == 2:
                draw_o(x, y, size, screen)
        elif shape == 3:
                draw_square(x, y, size, screen)
        elif shape == 4:
                draw_triangle(x, y, size, screen)
        elif shape == 5:
                draw_star(x, y, size, screen)

# Function for drawing numbers
def draw_number(x, y, size, number, screen):
        draw_text(str(number), x, y, size, screen)

# Function for displaying the board
def display_board(board, SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE, screen):
        # Draw players
        for i in range(len(board)):
                for j in range(len(board[i])):
                        if board[i][j] != 0:
                                draw_shape(SCREEN_WIDTH / GRID_SIZE * j, SCREEN_HEIGHT / GRID_SIZE * i, int(SCREEN_WIDTH / GRID_SIZE), board[i][j], screen)
                                # draw_number(SCREEN_WIDTH / GRID_SIZE * j, SCREEN_HEIGHT / GRID_SIZE * i, int(SCREEN_WIDTH / GRID_SIZE), board[i][j], screen)

# Function to get user move
def get_move(board, grid_size, screen_width, screen_height):
        """
        Waits for the user to make a move and returns the coordinates of the move.
        If the user does not make a move, returns None.
        """
        # Get user input
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        row = -1
        col = -1
        if mouse_click[0] == 1:
                # Check which row the user clicked
                for i in range(grid_size):
                        if mouse_pos[1] > screen_height / grid_size * i and mouse_pos[1] < screen_height / grid_size * (i + 1):
                                row = i
                # Check which column the user clicked
                for i in range(grid_size):
                        if mouse_pos[0] > screen_width / grid_size * i and mouse_pos[0] < screen_width / grid_size * (i + 1):
                                col = i

        # Return None if the user clicked outside the grid or the cell is already occupied
        if row == -1 or col == -1 or board[row][col] != 0:
                return None, None
        else:
                return row, col

def check_winner(board, WIN_AMOUNT):
        """
        Function for checking if there is a winner according to WIN_AMOUNT and NUM_PLAYERS.\n
        Returns None if there is no winner\n
        Returns 0 if there is a tie\n
        Returns n if player n won
        """
        # Check for a horizontal win
        for i in range(len(board)):
                for j in range(len(board[i]) - WIN_AMOUNT + 1):
                        if board[i][j] != 0:
                                win = True
                                for k in range(WIN_AMOUNT):
                                        if board[i][j + k] != board[i][j]:
                                                win = False
                                                break
                                if win:
                                        return board[i][j]

        # Check for a vertical win
        for i in range(len(board) - WIN_AMOUNT + 1):
                for j in range(len(board[i])):
                        if board[i][j] != 0:
                                win = True
                                for k in range(WIN_AMOUNT):
                                        if board[i + k][j] != board[i][j]:
                                                win = False
                                                break
                                if win:
                                        return board[i][j]

        # Check for a diagonal win
        for i in range(len(board) - WIN_AMOUNT + 1):
                for j in range(len(board[i]) - WIN_AMOUNT + 1):
                        if board[i][j] != 0:
                                win = True
                                for k in range(WIN_AMOUNT):
                                        if board[i + k][j + k] != board[i][j]:
                                                win = False
                                                break
                                if win:
                                        return board[i][j]
        
        # Check for a diagonal win (other direction)
        for i in range(WIN_AMOUNT - 1, len(board)):
                for j in range(len(board[i]) - WIN_AMOUNT + 1):
                        if board[i][j] != 0:
                                win = True
                                for k in range(WIN_AMOUNT):
                                        if board[i - k][j + k] != board[i][j]:
                                                win = False
                                                break
                                if win:
                                        return board[i][j]

        # Check for a tie
        tie = True
        for i in range(len(board)):
                for j in range(len(board[i])):
                        if board[i][j] == 0:
                                tie = False
        if tie:
                return 0

        return None

# Function for drawing text
def draw_text(text, x, y, size, screen):
        font = pygame.font.SysFont("comicsansms", size)
        text = font.render(text, True, (0, 0, 0))
        screen.blit(text, (x, y))

# Function for displaying the winner
def display_winner(winner, screen):
        size = screen.get_height() // 10
        x = screen.get_width() // 2 - size * 2
        y = screen.get_height() // 2 - size // 2

        # Display the winner
        if winner == 0:
                draw_text("Tie!", x, y, size, screen)
        else:
                draw_text("Player " + str(winner) + " wins!", x, y, size, screen)

# Main function
def main():
        # Height and width of the screen
        SCREEN_WIDTH = 500
        SCREEN_HEIGHT = 500
        # Grid size
        GRID_SIZE = 10
        # Amount needed in a row to win
        WIN_AMOUNT = 4
        # Number of players
        NUM_PLAYERS = 5
        # Store the board state as a 2D array
        board = [[0 for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
        # Store the number of turns
        turns = 0

        # Initialize pygame
        pygame.init()
        # Set up the drawing window
        screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        # Fill the background with white
        screen.fill((255, 255, 255))
        # Draw the grid lines
        draw_grid_lines(GRID_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, screen)

        # Run until the user asks to quit
        running = True
        while running:
                # Delay the game loop
                pygame.time.delay(100)

                # Did the user click the window close button?
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                running = False

                # Check for a winner
                winner = check_winner(board, WIN_AMOUNT)
                if winner != None:
                        display_winner(winner, screen)
                        display_board(board, SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE, screen)
                        pygame.display.flip()
                        pygame.time.delay(2000)

                        # Reset the board
                        board = [[0 for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
                        turns = 0
                        # Reset the screen
                        screen.fill((255, 255, 255))
                        draw_grid_lines(GRID_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, screen)
                        continue

                # Display the board
                display_board(board, SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE, screen)
                # Flip the display
                pygame.display.flip()

                # Get user input
                row, col = get_move(board, GRID_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT)
                if row == None or col == None:
                        continue

                # Place the move on the board
                board[row][col] = turns % NUM_PLAYERS + 1
                turns += 1

        # Done! Time to quit. 
        pygame.quit()

if __name__ == "__main__":
        main()
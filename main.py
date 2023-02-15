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

# Function for displaying the board
def display_board(board, SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE, screen):
        # Draw Xs and Os
        for i in range(len(board)):
                for j in range(len(board[i])):
                        if board[i][j] == 1:
                                draw_x(SCREEN_WIDTH / GRID_SIZE * j, SCREEN_HEIGHT / GRID_SIZE * i, SCREEN_WIDTH / GRID_SIZE, screen)
                        elif board[i][j] == 2:
                                draw_o(SCREEN_WIDTH / GRID_SIZE * j, SCREEN_HEIGHT / GRID_SIZE * i, SCREEN_WIDTH / GRID_SIZE, screen)

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
        Function for checking if there is a winner according to win_amount\n
        Returns 0 if there is no winner\n
        Returns 1 if X won\n
        Returns 2 if O won\n
        Returns 3 if there is a tie
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
        for i in range(len(board)):
                for j in range(len(board[i])):
                        if board[i][j] == 0:
                                return 0

        return 3

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
        NUM_PLAYERS = 2
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
                if winner != 0:
                        # Draw the winner
                        font = pygame.font.SysFont("comicsansms", 72)
                        if winner == 1:
                                text = font.render("X wins!", True, (0, 0, 0))
                        elif winner == 2:
                                text = font.render("O wins!", True, (0, 0, 0))
                        else:
                                text = font.render("It's a tie!", True, (0, 0, 0))
                        screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, SCREEN_HEIGHT / 2 - text.get_height() / 2))
                        
                        # Display the board
                        display_board(board, SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE, screen)
                        # Flip the display
                        pygame.display.flip()
                        # Delay the game loop
                        pygame.time.delay(2000)

                        # Reset the board
                        board = [[0 for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
                        # Reset the screen
                        screen.fill((255, 255, 255))
                        draw_grid_lines(GRID_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, screen)
                        turns = 0

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
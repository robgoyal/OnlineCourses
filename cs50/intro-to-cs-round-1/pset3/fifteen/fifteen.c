/**
 * fifteen.c
 *
 * Implements Game of Fifteen (generalized to d x d).
 *
 * Usage: fifteen d
 *
 * whereby the board's dimensions are to be d x d,
 * where d must be in [DIM_MIN,DIM_MAX]
 *
 * Note that usleep is obsolete, but it offers more granularity than
 * sleep and is simpler to use than nanosleep; `man usleep` for more.
 */
 
#define _XOPEN_SOURCE 500

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// constants
#define DIM_MIN 3
#define DIM_MAX 9

// board
int board[DIM_MAX][DIM_MAX];

// dimensions
int d;

// Blank tile location
int blankRow;
int blankColumn;

// prototypes
void clear(void);
void greet(void);
void init(void);
void draw(void);
bool move(int tile);
bool won(void);

int main(int argc, string argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        printf("Usage: fifteen d\n");
        return 1;
    }

    // ensure valid dimensions
    d = atoi(argv[1]);
    
    printf("Size of board is %i", d);
    if (d < DIM_MIN || d > DIM_MAX)
    {
        printf("Board must be between %i x %i and %i x %i, inclusive.\n",
            DIM_MIN, DIM_MIN, DIM_MAX, DIM_MAX);
        return 2;
    }

    // open log
    FILE *file = fopen("log.txt", "w");
    if (file == NULL)
    {
        return 3;
    }

    // greet user with instructions
    greet();

    // initialize the board
    init();

    // accept moves until game is won
    while (true)
    {
        // clear the screen
        clear();

        // draw the current state of the board
        draw();

        // log the current state of the board (for testing)
        for (int i = 0; i < d; i++)
        {
            for (int j = 0; j < d; j++)
            {
                fprintf(file, "%i", board[i][j]);
                if (j < d - 1)
                {
                    fprintf(file, "|");
                }
            }
            fprintf(file, "\n");
        }
        fflush(file);

        // check for win
        if (won())
        {
            printf("ftw!\n");
            break;
        }

        // prompt for move
        printf("Tile to move: ");
        int tile = get_int();
        
        // quit if user inputs 0 (for testing)
        if (tile == 0)
        {
            break;
        }

        // log move (for testing)
        fprintf(file, "%i\n", tile);
        fflush(file);

        // move if possible, else report illegality
        if (!move(tile))
        {
            printf("\nIllegal move.\n");
            usleep(500000);
        }

        // sleep thread for animation's sake
        usleep(100000);
    }
    
    // close log
    fclose(file);

    // success
    return 0;
}

/**
 * Clears screen using ANSI escape sequences.
 */
void clear(void)
{
    printf("\033[2J");
    printf("\033[%d;%dH", 0, 0);
}

/**
 * Greets player.
 */
void greet(void)
{
    clear();
    printf("WELCOME TO GAME OF FIFTEEN\n");
    usleep(200000);
}

/**
 * Initializes the game's board with tiles numbered 1 through d*d - 1
 * (i.e., fills 2D array with values but does not actually print them).  
 */
void init(void)
{
    // Initialize board values
    int iter = 1; 
    for (int i = 0; i < d; i++) {
        for (int j = 0; j < d; j++) {
            board[i][j] = d*d - iter;
            iter++;
        }
    }
    
    // Swap values of 1 and 2 in the case of even board dimensions
    if (d % 2 == 0) {
        board[d-1][d-2] = 2;
        board[d-1][d-3] = 1;
    }
    
    // Initialize blank space row and column to dimension values
    blankColumn = d-1;
    blankRow = d-1;
}

/**
 * Prints the board in its current state.
 */
void draw(void)
{
    
    // Iterate through board and print off values
    for (int i = 0; i < d; i++) {
        for (int j = 0; j < d; j++) {
            if (board[i][j] == 0) {
                printf("%3c", '_');
            }
            else {
                printf("%3i", board[i][j]);
            }
        }
        printf("\n");
    }
}

/**
 * If tile borders empty space, moves tile and returns true, else
 * returns false. 
 */
bool move(int tile)
{
    
    // Declare tile row and column variables to record location
    int tileRow;
    int tileColumn;
    
    // Temporary variable required for swap
    int tmp;
    
    // Find row and column location of tile
    for (int i = 0; i < d; i++) {
        for (int j = 0; j < d; j++) {
            if (board[i][j] == tile) {
                tileRow = i;
                tileColumn = j;
                break;
            }
            else {
                continue;
            }
            }
        }
     
    // Check if in same column but differing in row by 1 position
    if (abs(tileRow - blankRow) == 1 && (tileColumn - blankColumn) == 0) {
        
        // Perform a swap
        tmp = tile;
        board[tileRow][tileColumn] = board[blankRow][blankColumn];
        board[blankRow][blankColumn] = tmp;
        
        // Update blank space location
        blankRow = tileRow;
        
        return true;
    }
    
    // Check if in same row but differing in column by 1 position
    else if (abs(tileColumn - blankColumn) == 1 && (tileRow - blankRow) == 0) {
        
        // perform a swap
        tmp = tile;
        board[tileRow][tileColumn] = board[blankRow][blankColumn];
        board[blankRow][blankColumn] = tmp;
        
        // update blank space location
        blankColumn = tileColumn;
        
        return true;
    }
    
    else {
        return false;
    }
}

/**
 * Returns true if game is won (i.e., board is in winning configuration), 
 * else false.
 */
bool won(void)
{
    int iter = 1;
    
    // Loop through board to check if win configuration is met   
    for (int i = 0; i < d; i++) {
        for (int j = 0; j < d; j++) {
            
            // Check if board value is equal to required value
            if (board[i][j] == iter) {
                iter++;
                
                /*If next value is end of board, all previous board values 
                  met the required values. End of board value is 0 so we
                  return true at this point */
                
                if (iter == d*d) {
                    return true;
                }
            }
            
            // Return false if board value isn't equal to intended value
            else if (board[i][j] != iter) {
                return false;
            }
        }
    }
    
    return false;
}
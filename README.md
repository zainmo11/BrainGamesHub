# BrainGamesHub

# Django REST API README

This Django REST API provides several endpoints for various functionalities. Below is a list of available endpoints along with instructions on how to use them.

## Endpoints

### Admin Interface

- `/admin/`: Provides access to the Django admin interface for managing application data.

### Authentication

- `/api-auth/`: Endpoint for Django REST Framework authentication.

### Fetch Data by Model

- `/data/<str:model>/`: 
  - Method: GET
  - Description: Fetches data records based on the specified model.
  - Example: `/data/EasyLevel/` retrieves data for the `EasyLevel` model.

### Generate Sudoku Puzzle

- `/generate_sudoku/<int:N>/<int:K>/`: 
  - Method: GET
  - Description: Generates a Sudoku puzzle.
  - Parameters:
    - `N` (integer): Size of the Sudoku grid (e.g., 9 for a standard 9x9 grid).
    - `K` (integer): Number of digits to remove from the puzzle for gameplay.
  - Example: `/generate_sudoku/9/30/` generates a 9x9 Sudoku puzzle with 30 digits removed.

### Generate Math Equation

- `/generate_equation/<str:level>/<int:num_parameters>/<int:num_digits>/`: 
  - Method: GET
  - Description: Generates a math equation.
  - Parameters:
    - `level` (string): Difficulty level of the equation (e.g., "simple", "medium", "hard").
    - `num_parameters` (integer): Number of parameters in the equation.
    - `num_digits` (integer): Maximum number of digits in the parameters.
  - Example: `/generate_equation/simple/2/3/` generates a simple math equation with 2 parameters, each having up to 3 digits.

### Validate Answer

- `/validate_answer/`: 
  - Method: POST
  - Description: Validates a user's answer to a math equation.
  - Request Body (JSON):
    - `equation` (string): The math equation to validate.
    - `user_answer` (string/float): The user's answer to the equation.
  - Example JSON request:
    ```json
    {
      "equation": "2 + 3",
      "user_answer": 5
    }
    ```
  - Example response:
    ```json
    {
      "is_correct": true
    }
    ```

### Solve Sudoku Puzzle

- `/sudokuSolver/`: 
  - Method: POST
  - Description: Solves a Sudoku puzzle.
  - Request Body (JSON):
    - `N` (integer): Size of the Sudoku grid (e.g., 9 for a standard 9x9 grid).
    - `grid` (list of lists): The unsolved Sudoku grid.
  - Example JSON request:
    ```json
    {
      "N": 9,
      "grid": [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
      ]
    }
    ```
  - Example response:
    ```json
    {
      "solved_grid": [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
      ]
    }
    ```

## Conclusion

This Django REST API provides various endpoints for generating Sudoku puzzles, math equations, validating answers, and solving Sudoku puzzles. Use the provided examples and descriptions to interact with the API and leverage its functionalities.


# BrainGamesHub
# Django Sudoku Game and Database API

This Django project combines a Sudoku game generator, solver, and a database API for storing participant data across different game levels. It includes three database models: EasyLevel, MediumLevel, and HardLevel, each designed to store participant names, submission times, and scores for different levels of the game.

## Database Models

### EasyLevel Model
- `Participant_Name`: A character field to store the participant's name (max length 50).
- `Submission_Time`: A DateTime field to record the submission time.
- `Score`: An Integer field to store the participant's score.

### MediumLevel Model
- `Participant_Name`: A character field to store the participant's name (max length 50).
- `Submission_Time`: A DateTime field to record the submission time.
- `Score`: An Integer field to store the participant's score.

### HardLevel Model
- `Participant_Name`: A character field to store the participant's name (max length 50).
- `Submission_Time`: A DateTime field to record the submission time.
- `Score`: An Integer field to store the participant's score.

## Sudoku Game Generator and Solver

The project also includes a Sudoku game generator that creates Sudoku puzzles with varying levels of difficulty and a Sudoku solver that can find solutions to Sudoku puzzles.

## API Endpoints

- `/data/<str:model>/`: API endpoint to retrieve participant data for different game levels.
- `/generate_sudoku/<int:N>/<int:K>/`: API endpoint to generate a Sudoku puzzle of size N with K numbers removed.
- `/generate_equation/<str:level>/<int:num_parameters>/<int:num_digits>/`: API endpoint to generate mathematical equations based on the specified level, number of parameters, and number of digits.
- `/validate_answer/`: API endpoint to validate user-submitted answers to mathematical equations.
- `/sudokuSolver/`: API endpoint to solve Sudoku puzzles.

## Usage

- These models can be used to store and retrieve data about participants and their performance in different levels of a Sudoku game.
- You can create, update, and query these models using Django's database API.
- The Sudoku game generator and solver can be used to create and solve Sudoku puzzles programmatically.


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

This Django REST API provides various endpoints for generating Sudoku puzzles, math equations, validating answers, and solving Sudoku puzzles. Use the provided examples and descriptions to interact with the API 

## Installation

- This Django project assumes that you have Django installed. If not, you can install it using pip:

pip install django

vbnet
Copy code

- To use these models in your own project, you can add them to your Django app's `models.py` file and run database migrations.

python manage.py makemigrations
python manage.py migrate

less
Copy code

## Contributing

- Contributions are welcome! If you find any issues or have suggestions for improvements, please create a GitHub issue or submit a pull request.

## License

- This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- If you have any questions or need further assistance, you can contact me at [zyn6681@gmail.com].
- GitHub: ((https://github.com/zainmo11/))

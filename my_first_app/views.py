from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from my_first_app.models import EasyLevel, MediumLevel, HardLevel
import random
import math
from .serializer import EasyLevel_serializers, MediumLevel_serializers, HardLevel_serializers
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

class MathEquation:
    simple_operations = ['+', '-']
    medium_operations = ['*', '/'] + simple_operations
    hard_operations = ['**'] + medium_operations

    def __init__(self, levels, num_of_parameters, num_of_digits):
        self.levels = levels
        self.num_of_parameters = num_of_parameters
        self.num_of_digits = num_of_digits

    def EquGenerator(self):
        if self.levels == "EasyLevel":
            # Choose a simple operation (+, -)
            equation_operations = random.choices(self.simple_operations, k=self.num_of_parameters)
        elif self.levels == "MediumLevel":
            # Choose a medium operation (*, /)
            equation_operations = random.choices(self.medium_operations, k=self.num_of_parameters)
        elif self.levels == "HardLevel":
            # Choose a hard operation (**)
            equation_operations = random.choices(self.hard_operations, k=self.num_of_parameters)
        else:
            raise ValueError("Invalid level. Use 'simple' or 'complex'.")

        operands = [random.randint(1, 10 ** int(self.num_of_digits)) for _ in range(self.num_of_parameters )]

        # Ensure unique operands by shuffling
        random.shuffle(operands)

        equation = f"{operands[0]}"
        for i in range(1,self.num_of_parameters):
            equation += f" {equation_operations[i]} {operands[i]}"

        return equation

    @staticmethod
    def validate_result(equation, user_answer, decimal_places=2):
        try:
            # Evaluate the equation to calculate the correct result
            correct_result = eval(equation)

            # Format the correct_result to have a specific number of decimal places
            formatted_correct_result = "{:.{dp}f}".format(correct_result, dp=decimal_places)

            # Convert user_answer to a float for comparison
            user_answer = float(user_answer)

            # Format the user_answer to match the decimal places
            formatted_user_answer = "{:.{dp}f}".format(user_answer, dp=decimal_places)

            # Check if formatted_user_answer matches formatted_correct_result
            return formatted_user_answer == formatted_correct_result

        except (SyntaxError, ValueError):
            # Handle invalid equation or user_answer
            return False


class Sudoku:
    def __init__(self, N, K):
        self.N = N
        self.K = K

        # Compute square root of N
        SRNd = math.sqrt(N)
        self.SRN = int(SRNd)
        self.mat = [[0 for _ in range(N)] for _ in range(N)]

    def fillValues(self):
        # Fill the diagonal with SRN x SRN matrices
        self.fillDiagonal()

        # Fill remaining blocks
        self.fillRemaining(0, self.SRN)

        # Remove Randomly K digits to make game
        self.removeKDigits()

    def fillDiagonal(self):
        for i in range(0, self.N, self.SRN):
            self.fillBox(i, i)

    def unUsedInBox(self, rowStart, colStart, num):
        for i in range(self.SRN):
            for j in range(self.SRN):
                if self.mat[rowStart + i][colStart + j] == num:
                    return False
        return True

    def fillBox(self, row, col):
        num = 0
        for i in range(self.SRN):
            for j in range(self.SRN):
                while True:
                    num = self.randomGenerator(self.N)
                    if self.unUsedInBox(row, col, num):
                        break
                self.mat[row + i][col + j] = num

    def randomGenerator(self, num):
        return math.floor(random.random() * num + 1)

    def checkIfSafe(self, i, j, num):
        return (self.unUsedInRow(i, num) and self.unUsedInCol(j, num) and self.unUsedInBox(i - i % self.SRN,
                                                                                           j - j % self.SRN, num))

    def unUsedInRow(self, i, num):
        for j in range(self.N):
            if self.mat[i][j] == num:
                return False
        return True

    def unUsedInCol(self, j, num):
        for i in range(self.N):
            if self.mat[i][j] == num:
                return False
        return True

    def fillRemaining(self, i, j):
        # Check if we have reached the end of the matrix
        if i == self.N - 1 and j == self.N:
            return True

        # Move to the next row if we have reached the end of the current row
        if j == self.N:
            i += 1
            j = 0

        # Skip cells that are already filled
        if self.mat[i][j] != 0:
            return self.fillRemaining(i, j + 1)

        # Try filling the current cell with a valid value
        for num in range(1, self.N + 1):
            if self.checkIfSafe(i, j, num):
                self.mat[i][j] = num
                if self.fillRemaining(i, j + 1):
                    return True
                self.mat[i][j] = 0

        # No valid value was found, so backtrack
        return False

    def removeKDigits(self):
        count = self.K

        while count != 0:
            i = self.randomGenerator(self.N) - 1
            j = self.randomGenerator(self.N) - 1
            if (self.mat[i][j] != 0):
                count -= 1
                self.mat[i][j] = 0
        return


# def push_user(participant_Name, submission_Time, score, level):
#     try:
#         if level == "EasyLevel":
#             serializer =
#             EasyLevel.objects.create(Participant_Name=participant_Name, Submission_Time=submission_Time, Score=score)
#         elif level == "MediumLevel":
#             MediumLevel.objects.create(Participant_Name=participant_Name, Submission_Time=submission_Time, Score=score)
#         else:
#             HardLevel.objects.create(Participant_Name=participant_Name, Submission_Time=submission_Time, Score=score)
#     except IntegrityError as e:
#         # Handle the IntegrityError, e.g., log the error or return an error response.
#         print(f"Error: {e}")


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes((IsAuthenticated,))
def generate_sudoku(request, N, K):
    try:
        N = int(N)  # Size of the Sudoku grid (e.g., 9 for a 9x9 Sudoku)
        K = int(K)  # Number of digits to be removed
        sudoku = Sudoku(N, K)
        sudoku.fillValues()
        sudoku_prob = sudoku.mat

        response_data = {

            "sudoku_prob": sudoku_prob,
        }
        return Response(response_data)
    except ValueError:
        return Response({"error": "Invalid input"}, status=400)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes((IsAuthenticated,))
def FBA_LIST(request, model):
    try:
        if request.method == "GET":
            if model == "EasyLevel":
                users = EasyLevel.objects.all()
                serializer = EasyLevel_serializers(users, many=True)
            elif model == "MediumLevel":
                users = MediumLevel.objects.all()
                serializer = MediumLevel_serializers(users, many=True)
            elif model == "HardLevel":
                users = HardLevel.objects.all()
                serializer = HardLevel_serializers(users, many=True)
            return Response(serializer.data)
        elif request.method == "POST":
            participant = request.data.get("Participant_Name")
            Submission_Time = request.data.get("Submission_Time")
            Score = request.data.get("Score")
            level_params_digits = request.data.get("level_params_digits")

            if model == "EasyLevel":
                participant = EasyLevel(
                    Participant_Name=participant,
                    Submission_Time=Submission_Time,
                    Score=Score,
                    level_params_digits=level_params_digits,
                )
                participant.save()  # Save the object to the database

                # You can return a response indicating success
                return Response({"message": "Participant created successfully"}, status=201)
            elif model == "MediumLevel":
                participant = MediumLevel(
                    Participant_Name=participant,
                    Submission_Time=Submission_Time,
                    Score=Score,
                    level_params_digits=level_params_digits
                )
                participant.save()  # Save the object to the database

                # You can return a response indicating success
                return Response({"message": "Participant created successfully"}, status=201)
            elif model == "HardLevel":
                participant = HardLevel(
                    Participant_Name=participant,
                    Submission_Time=Submission_Time,
                    Score=Score,
                    level_params_digits=level_params_digits
                )
                participant.save()  # Save the object to the database

                # You can return a response indicating success
                return Response({"message": "Participant created successfully"}, status=201)
    except Exception as e:
        # Handle exceptions as needed (e.g., log the error)
        print(f"Error: {e}")
        return Response(e,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes((IsAuthenticated,))
def generate_equation(request, level, num_parameters, num_digits):
    try:
        # Create a MathEquation instance
        math_equation = MathEquation(level, num_parameters, num_digits)

        # Generate an equation using EquGenerator method
        equation = math_equation.EquGenerator()

        # Convert the equation to a JSON response
        response_data = {
            "equation": equation,
        }
        return Response(response_data)
    except ValueError:
        return Response({"error": "Invalid input"}, status=400)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes((IsAuthenticated,))
def validate_answer(request):
    try:
        equation = request.data.get('equation', '')
        user_answer = request.data.get('user_answer', '')

        is_correct = MathEquation.validate_result(equation, user_answer)

        # Return a JSON response indicating whether the answer is correct
        response_data = {
            "is_correct": is_correct,
        }
        return Response(response_data)
    except (ValueError, KeyError):
        return Response({"error": "Invalid input"}, status=400)

@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes((IsAuthenticated,))
def check_Participant_name(request):

    user_exists = False
    try:
        participant_name = request.data.get('participant_name')
        # Query the model to check if the participant_name exists
        if EasyLevel.objects.filter(Participant_Name=participant_name).exists() | MediumLevel.objects.filter(Participant_Name=participant_name).exists() | HardLevel.objects.filter(Participant_Name=participant_name).exists():
            user_exists = True
        response_data = {
            "user_exists": user_exists,
        }
        return Response(response_data)
    except (ValueError, KeyError):
        return Response({"error": "Invalid input"}, status=400)

def isSafe(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
    for x in range(9):
        if grid[x][col] == num:
            return False
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


def solver(N, grid, row, col):
    if row == N - 1 and col == N:
        return True
    if col == N:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return solver(N, grid, row, col + 1)
    for num in range(1, N + 1, 1):
        if isSafe(grid, row, col, num):
            grid[row][col] = num
            if solver(N, grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes((IsAuthenticated,))
def sudokuSolver(request):
    data = request.data
    N = data.get('N', 9)  # Default to a 9x9 Sudoku grid if N is not provided
    grid = data.get('grid', [])  # Sudoku grid as a list of lists
    solved = solver(N, grid, 0, 0)
    try:
        if solved:
            return Response({'solved_grid': grid})
        else:
            return Response({'error': 'No solution found'}, status=400)
    except Exception as e:
        return Response({'error': str(e)}, status=400)

def hello_user_view(request):
    return render(request, 'MyFirstApp/hello.html')

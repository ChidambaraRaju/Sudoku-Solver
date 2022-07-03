{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e48d7fbe",
   "metadata": {},
   "outputs": [],
   "source": [
    "from pprint import pprint"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9bb7bfda",
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_valid(puzzle, row, col, guess):\n",
    "    #used to check whether whether our guess is a valid one\n",
    "    #according to the rules of sudoku, the guessed value should not be in its row,column and its 3x3 matrix\n",
    "    row_values = puzzle[row] \n",
    "    if guess in row_values: #checking row\n",
    "        return False\n",
    "    col_values=[]\n",
    "    for i in range(9):\n",
    "        col_values.append(puzzle[i][col])\n",
    "    if guess in col_values: #checking column\n",
    "        return False\n",
    "    start_row=(row//3)*3\n",
    "    start_col=(col//3)*3\n",
    "    for row_value in range(start_row, start_row+3):\n",
    "        for col_value in range(start_col, start_col+3):\n",
    "            if(puzzle[row_value][col_value]==guess): #checking the 3x3 matrix\n",
    "                return False\n",
    "    return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "ceaafcfa",
   "metadata": {},
   "outputs": [],
   "source": [
    "def find_row_col(puzzle):\n",
    "    # used to find empty value in the puzzle which is represented as -1\n",
    "    for r in range(9):\n",
    "        for c in range(9):\n",
    "            if puzzle[r][c] == -1:\n",
    "                return r,c\n",
    "    return None,None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ad22b1f9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def solve_sudoku(puzzle):\n",
    "    row,col = find_row_col(puzzle)\n",
    "    if row is None:\n",
    "        return True\n",
    "        # if there is no more space in the puzzle,represents the completion of solving the puzzle hence returning the True\n",
    "    else:\n",
    "        for guess in range(0,10):# guesssing any value ranging from 1,2,...,9\n",
    "            if(check_valid(puzzle, row, col, guess)):\n",
    "                puzzle[row][col]=guess #if the guess is a valid one replacing -1 with our guess\n",
    "                if solve_sudoku(puzzle): #calling the function recursively to complete the puzzle\n",
    "                    return True\n",
    "            puzzle[row][col]=-1 # if the puzzle can't be solved by our guess again chaning the value to -1 and changing the guess\n",
    "    return False # returning False when the puzzle is UNSOLVABLE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "f34b955f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "[[3, 9, 0, 4, 5, 6, 1, 2, 7],\n",
      " [7, 1, 8, 2, 3, 0, 4, 6, 5],\n",
      " [4, 2, 5, 7, 1, 9, 0, 8, 3],\n",
      " [0, 5, 1, 9, 6, 8, 3, 7, 2],\n",
      " [2, 4, 6, 0, 7, 3, 5, 1, 8],\n",
      " [8, 3, 7, 5, 2, 1, 6, 0, 4],\n",
      " [5, 0, 2, 6, 8, 4, 7, 3, 1],\n",
      " [6, 7, 3, 1, 9, 5, 8, 4, 0],\n",
      " [1, 8, 9, 3, 0, 7, 2, 5, 6]]\n"
     ]
    }
   ],
   "source": [
    "example_board = [\n",
    "    [3, 9, -1, -1,  5, -1, -1, -1, -1],\n",
    "    [-1, -1, -1, 2, -1, -1, -1, -1, 5],\n",
    "    [-1, -1, -1, 7, 1, 9, -1, 8, -1],\n",
    "\n",
    "    [-1, 5, -1, -1, 6, 8, -1, -1, -1],\n",
    "    [2, -1, 6, -1, -1, 3, -1, -1, -1],\n",
    "    [-1, -1, -1, -1, -1, -1, -1, -1, 4],\n",
    "\n",
    "    [5, -1, -1, -1, -1, -1, -1, -1, -1],\n",
    "    [6, 7, -1, 1, -1, 5, -1, 4, -1],\n",
    "    [1, -1, 9, -1, -1, -1, 2, -1, -1]\n",
    "]\n",
    "print(solve_sudoku(example_board))\n",
    "pprint(example_board)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "010f5fb9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

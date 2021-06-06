# Canada Lottery Number Generator - Python

> ### [View all in one page(Jupyter Notebook)](https://github.com/brendensong/Canada-Lottery-Number-Generator/blob/main/Canada%20Lottery%20Number%20Generator.ipynb)
---
> ### [Ver.1](https://github.com/brendensong/Canada-Lottery-Number-Generator/blob/main/python_code_files/lottery_numbers.py)
- Very, very simple.
- Just creates all the numbers from the beginning and then compares them one by one and recreates them if they're the same number.

> ### [Ver.2](https://github.com/brendensong/Canada-Lottery-Number-Generator/blob/main/python_code_files/lottery_numbers_2.py)
- Generates only one number at the beginning.
- Then, using an infinite loop, generate next number and compare the numbers and break the loop when they're not the same number.

> ### [Ver.3](https://github.com/brendensong/Canada-Lottery-Number-Generator/blob/main/python_code_files/lottery_numbers_3.py)
- Added lottery type selection function.
- Generates 7 numbers when selecting 'Lotto Max' and 6 numbers when selecting 'Lotto 6/49'.
- Used `for` and `while` to reduce code lines for number generation and comparison.
- Added the result section(?).

> ### [Ver.4](https://github.com/brendensong/Canada-Lottery-Number-Generator/blob/main/python_code_files/Canada_lottery_number_generator.py)
- Used String Formatting to decorate the Input and Results sections to increase readability (and beauty a little).
- Added one more type of lottery. When selecting 'Daily Grand', generates five numbers between 1 and 49 and one grand number between 1 and 7.
- Added a lottery type tuple. Utilizes the objects in Tuple to generate the lottery numbers and shows the type of lottery selected in the Results section.
- Added a positive phrase for good luck.

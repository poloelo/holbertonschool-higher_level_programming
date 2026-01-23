# Python - Modules and Imports

This project is a collection of Python scripts that demonstrate different ways to use modules and imports in Python. It covers basic concepts of module importing, command-line argument handling, and variable usage across different files.

## Project Files

1. **0-add.py**
   - Imports the `add` function from the `add_0` module
   - Performs a simple addition and displays the result
   - Usage: `./0-add.py`

2. **1-calculation.py**
   - Imports `add`, `sub`, `mul`, and `div` functions from the `calculator_1` module
   - Performs and displays various mathematical operations
   - Usage: `./1-calculation.py`

3. **2-args.py**
   - Displays the number and list of command-line arguments
   - Handles singular/plural forms and no arguments case
   - Usage: `./2-args.py [arguments...]`

4. **3-infinite_add.py**
   - Adds an infinite number of integers passed as arguments
   - Handles both positive and negative integers
   - Usage: `./3-infinite_add.py 1 2 3 4 10 11`

5. **5-variable_load.py**
   - Imports and displays the value of variable `a` from the `variable_load_5` module
   - Demonstrates variable importing between modules
   - Usage: `./5-variable_load.py`

## Prerequisites

- Python 3.4+
- No external dependencies required

## How to Run

1. Make sure the files have execute permissions:
   ```bash
   chmod +x *.py
   ```

2. Run the scripts individually:
   ```bash
   ./0-add.py
   ./1-calculation.py
   ./2-args.py arg1 arg2
   ./3-infinite_add.py 1 2 3 4
   ./5-variable_load.py
   ```

## Author

[Your Name] - [Your Email]

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

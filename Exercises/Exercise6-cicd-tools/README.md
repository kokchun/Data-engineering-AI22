# Exercise  CI/CD Tools
The purpose of this exercise is to manually use some of the tools which are often run automatically in the Github CI/CD pipeline.

You will need to install some external Python packages for this exercise so it's advised to use a virtual environment e.g. pipenv.

## Intro
To practice coding, we will spend some time writing a program that generates random jokes and reactions to the jokes. We will later apply tools like Black and pytest to this program.

Switch to your own branch to avoid code conflicts with other students in the class.
1. Git clone this repository. If you've done this before the summer, do a git pull.
2. Create a branch `git branch olof-exercise-cicd`, but replace "olof" with your own name.
3. Switch to your new branch. `git checkout olof-exercise-cicd`.
4. Ask for help if you have any problems during this part before moving on.

Use Pyjokes https://pyjok.es/ to help you implement the program [print_joke.py](print_joke.py). Don't spend more than an hour on this step since it's just the first part of the exercise. Ask for help if you get stuck.

Once you've written the program, add it to git.
1. cd Exercises/Exercise6-cicd-tools/
2. git add print_joke.py
3. git commit -m "create joke file"

## Black
https://github.com/psf/black

Now you will use Black to format the code to the Black style.

1. Install Black by following the installation instructions on their website.
2. black print_joke.py
3. git diff print_joke.py
4. Take note of how it changed your code. Feel free to ask Google, ChatGPT, or the teacher if you don't understand why it changed it like it did.
5. git add print_joke.py
6. git commit -m "format joke file with Black"

## Isort
https://github.com/PyCQA/isort 

You will now use isort in the same fashion as Black.

1. Install isort by following the installation instructions on their website.
2. isort print_joke.py
3. git diff print_joke.py
4. Take note of how it changed your code. Feel free to ask Google, ChatGPT, or the teacher if you don't understand why it changed it like it did.
5. git add print_joke.py
6. git commit -m "sort imports in joke file with isort"

## Pytest
https://docs.pytest.org/ 

We will now create tests for our program that ensures that it's working as expected.
1. Install pytest by following the installation instructions on their website
2. Look at the test file [test_print_joke.py](test_print_joke.py)
3. Run the tests that are currently not working. `pytest -s test_print_joke.py`
4. Follow the instructions to fix/implement the tests in [test_print_joke.py](test_print_joke.py)

Once you're done you can commit your changes to git
1. git add print_joke.py
2. git add test_print_joke.py
3. git commit -m "add tests"


## Improve your solution (Optional)

If you finish the other tasks early, spend some time to study your solution. Look at another students solution to see how your solutions are different or ask chatGPT if it can come up with an improvement to your code.

If you have more time left, feel free to modify the code to your liking.

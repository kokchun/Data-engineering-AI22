# Exercise - CI/CD Tools

## Intro
To practice coding, we will spend some time to write a program that generates random jokes and reactions to the jokes. We will later apply tools like black and pytest on this program.

Switch to your own branch to avoid conflicts with others
1. Git clone this repository. If you've done this before the summer, do a git pull.
2. Create a branch `git branch olof-exercise-cicd` but replace olof with your own name.
3. Switch to your new branch. `git checkout olof-exercise-cicd`.


Use Pyjokes https://pyjok.es/ to help you implement the program [print_joke.py](print_joke.py). Feel free to modify the code to your liking, but try to not spend very much time on this step since it's just the first part of the exercise.

## Black
https://github.com/psf/black

Now you will use black to format the code to the black style. Before that, we want to create a commit so that we easily can see how the code changes.

1. cd Exercises/Exercise6-cicd-tools/
2. git add print_joke.py
3. git commit -m "create joke file"
4. black print_joke.py

## Isort

## Pytest

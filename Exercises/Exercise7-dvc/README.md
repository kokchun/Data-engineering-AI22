# Exercise Data Version Control with DVC 

## Intro
This will be a short exercise to get some hands on experience with DVC.

Switch to your own branch to avoid code conflicts with other students in the class.
1. Git clone this repository. If you've done this before the summer, do a git pull.
2. Create a branch `git branch olof-exercise-dvc`, but replace "olof" with your own name.
3. Switch to your new branch. `git checkout olof-exercise-dvc`.
4. Ask for help if you have any problems during this part before moving on.

## Setup DVC

1. Install the DVC Python package using pip. Look at their website https://dvc.org/doc/install.
2. Test that your installation was successful by executing the command `dvc --version`.

## Initialize DVC
The DVC commands are very similar to git commands. For example, instead of running git add, you will run dvc add. This makes it pretty easy to get started with dvc if you're familiar with git.

1. First you should change directory to this exercise folder. `cd path/to/Exercise7-dvc`.
2. Execute the command `dvc init --subdir` to initialize DVC.
3. Note that the command created a .dvc folder. It's hidden so you might not be able to see it by default. `ls -la` will list all files, even hidden ones. Open that folder and look what's inside of the folder. We will look at it again later in the exercise.

## Initialize remote storage
We will now create a backup of our data so that it won't get lost in case of an accident.

Typically one would create this backup in the cloud so that it's easily shared with teammates. We will create this backup in the Exercise7-dvc/fake_cloud_storage/ directory to avoid any costs and complexity of using a cloud solution.

1. `dvc remote add -d myremote /path/to/Exercise7-dvc/fake_cloud_storage/`.
2. Open the .dvc/config file to inspect what changed.

## Add data to DVC remote
1. Find your favorite cat image on the internet, download it and put it inside of the data/ directory with the name cat1.jpeg
2. Add the image of the cat by running the command `dvc add data/cat1.jpeg`. This will create a metadata file data/cat1.jpeg.dvc that describes the image and the file data/.gitignore which tells git to ignore the cat image since it's tracked by DVC instead.
3. Open the data/cat1.jpeg.dvc file and inspect what it contains. As long as you have this metadata file you will be able to download the data from the remote. Because of this, it's important to keep track of this metadata file.
4. To keep track of your metadata file you can add it to git. Note the difference of adding the metadata file to git vs the actual data. The metadata file is very small. `git add data/cat1.jpeg.dvc data/.gitignore`.
5. Upload this data to your remote by running `dvc push`. You should get the message "1 file pushed". This step is important and easy to forget in practice. I often use pre-commit to do it automatically :)
6. Open your Exercise7-dvc/fake_cloud_storage folder and inspect how dvc has stored your data in your remote. It's compressed data and is not something a human can read. 
7. Add your changes to git and create a commit. `git add .` and `git commit -m "track data with dvc"`.

## Add more data to DVC
Do the previous section's steps again to add a second cat image. Name it data/cat2.jpeg.

## Download data from DVC remote

We will now test that the data is stored in the remote correctly and that we can access it if our original data is lost.
1. Run `dvc status` to see if your dataset is up to date.
2. Remove the file data/cat1.jpeg.
3. Run `dvc status` again. It should now say that the cat image is missing.
4. Run the command `dvc pull` to download all missing data. Dvc will use your data/cat1.jpeg.dvc file to download the right data from the remote. 

## Learn about DVC
Explore your .dvc/ folder. What has changed since your started? What do these files and folders do?

Try to find answers on the website https://dvc.org

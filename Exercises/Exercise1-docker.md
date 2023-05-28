# Exercise 1 - Docker

Use bash a lot for exercise but you can use GUI tools such as a code editor to edit your code files.

---

## 0. warmup (\*)

a) Create this file structure

```bash
Exercise1
├── Dockerfile
└── src
    └── ex1_0_setup.py
    └── ex1_1_setup.py
```

b) Create a Dockerfile with base image Python 3.9 and with the following packages.

- matplotlib
- plotly_express
- pandas
- numpy
- dash
- sklearn

Make sure ex1_0_setup.py runs when the container starts. Also specify the working directory to /Exercise1 inside of the container.

c) Create a docker image with name ex1-image

d) Spin up your docker container and name it ex1-container.

e) Go into your container and make sure that these packages are installed.

f) Create a bash script that lists the installed packages.

g) Now create a Python script that prints out the installed packages and the version of Python.

h) Spin up the container in interactive mode. Here are some stuffs you can explore

- check your current directory
- list all files
- navigate to parents and list files
- list all files inside Exercise1
- count all files and folders inside Exercise1
- check your OS
- check the current date
- take a snapshot of the current python packages with corresponding versions and pipe them into requirements2.txt
- check the differences in requirements2.txt and requirements.txt

---

## 1. It's the final countdown (*)

Now you will create a Python script to keep track of time to different events. This is the list of events we would like to have a countdown to

| Event            | Date             |
| ---------------- | ---------------- |
| summer_break     | 2023-06-9 15:00  |
| lia_start        | 2023-09-25 8:00  |
| christmas        | 2023-12-24       |
| bellas_birthday  | 2023-12-07       |
| new_year         | 2024-01-01       |
| graduation_party | 2024-06-09 16:30 |

a) Make a script to get the following output to a file called countdown.log inside the folder logs. The logs directory is a sibling to the src directory.

<details>

<summary>check the output</summary>

<img src="../assets/countdown_a.png" width = 400>

</details>

b) Make a cron schedule inside of your docker container in interactive mode to run your script

Note that you might need to install

- crontab
- nano

Let it run for couple of minutes, the output should look something like this 

<details>

<summary>check the output</summary>

<img src="../assets/countdown_b.png" width = 400>

</details>

c) Stop your cron schedule and create another script that will output the events table to the beginning of countdown.log. Now schedule so that the script outputting to countdown.log happens once and then afterwards the countdown table should log every two minutes. (**)

<details>

<summary>check the output</summary>

<img src="../assets/countdown_c.png" width = 400>

</details>

---

## 2. Pokeiness (\*)-(\***)

Professor Oak is an expert in pokemons, and have developed a device for measuring a pokemons happiness level. He needs your help in performing a pokexperiment collecting data and visualizing them in a dashboard. As a poke professor he loves structure in his files, use this structure. Note that the pokemons in the pokebelt are example gotten from one run and observations are from transform_load after two runs. 

```bash
Exercise2
├── pokedata
│   ├── observations
│   │   ├── observation_23-05-18_17_34.csv
│   │   ├── observation_23-05-18_18_34.csv
│   ├── pokebelt
│   │   ├── fearow.json
│   │   ├── kabutops.json
│   │   ├── magneton.json
│   │   ├── poliwag.json
│   │   ├── vulpix.json
│   │   └── zapdos.json
│   └── pokelist.json
└── scripts
    ├── extract_data.py
    ├── poke_dashboard.py
    ├── release_pokemons.sh
    └── transform_load.py
```

Tasks a) and b) should be made in extract_data.py

a) Start by collecting a list of all pokemons from first generation (151 pokemons). Scrape this list from [wikipedia "Lista över Pokémon"](https://sv.wikipedia.org/wiki/Lista_%C3%B6ver_Pok%C3%A9mon) and save it as a json file in pokedata/pokelist.json. This json file should contain the poke index and the corresponding pokemon. Save this python script in 

```json
{"1":"Bulbasaur","2":"Ivysaur","3":"Venusaur","4":"Charmander","5":"Charmeleon","6":"Charizard","7":"Squirtle","8":"Wartortle","9":"Blastoise","10":"Caterpie", ...}
```

b) With the pokelist we can now randomly pick six numbers from 1-151 to catch and put in our pokebelt. Use this api to get the data [https://pokeapi.co/api/v2/pokemon-species/pikachu]("https://pokeapi.co/api/v2/pokemon-species/pikachu"), where you change pikachu to another pokemon name. Remember to add a pause for at least 2 seconds before each get request, you can use requests library to make a request. 

c) Now transform (clean) your data from the pokebelt and load (save) the observations in a csv file with timestamp in the name.  There should be a transform and a load function in your script. Example content of csv file.

```csv
pokemon,happiness
fearow,70
kabutops,50
magneton,50
poliwag,50
vulpix,50
zapdos,35
```

d) Create a bash script that cleans the pokebelt. 

e) Make a cron schedule inside of your container to clean the pokebelt, extracting new pokemons and load observations. 

f) Now make a dashboard showing the different pokemons and their happiness level. Choose a proper graph to show this.

g) As a non technical person professor Oak don't want to manage installations of softwares. Write clear detailed instructions for professor Oak how to use Docker to see the dashboard. This dashboard don't need to handle scheduling and updates. (**)

h) Make the dashboard have a dropdown to choose observations. Assume we catch new set of six pokemons every five minutes. We want it scheduled such that the dashboard is updated. (***)

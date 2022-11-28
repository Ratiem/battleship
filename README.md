# My Battleship Game

This is a simple python based game called Battleship where a user plays against a hidden user , which is the computer board. The aim of the user is to guess the ships by using their keyboard.

# Features 

## The Game Page

This battleship game has a board grid of 8 by 8. There are 10 turns and once you hit a ship te grid will show an "X" but if you miss a bit the grid will
display "-". 
Once the the welcome message is displayed the user will be asked to enter their name and commence game by selecting a row number between 1 and 8 as well as a column letter between A and H. For each turn the user makes, a message will be displayed to state whether the user has entered the details as required and any incorrectly completed information returns an error. The turns also decrease with each try. Once the game turns are complete the user will be asked if they wish to play again otherwise the game is terminated. 

![The Game](https://github.com/Ratiem/battleship/blob/main/assets/images/Game%20page.jpg)

# Technologies Used

Languages
- Python
- Gitpod
- Github
- Heroku

## Testing 

### Validator Testing 

- PEP 8
    - The Code institute Python linter was used for the python code and no errors were found

![PEP 8 Validator](https://github.com/Ratiem/battleship/blob/main/assets/images/CI%20Python%20linter.jpg)   

- Heroku
     - This was used for the deployed of the game to get the live version.

## Deployment

- The final code was pushed to GitHub.
- Next step was to log into Heroku.
- Create and add new app name.
- Connect to Github.
- Search for the repository you want to connect and connect it to Heroku.
- Add two buildpacks from the _settings _tab. The order is as follows:
    1. `heroku/python`
    2. `heroku/nodejs`
- Create a _configVar_ called `PORT`  and set it to `8000`
- In the deployment tab scroll to end of page to deploy main branch of connected repo.

### Bugs
The first time l ran the code in the terminal I ahd a lot of indentation errors and white spaces and there were some parts of the game 
that were not responding on the terminal hence l had to change around some parts of the code. I fixed this until l could run the code through
the `CI python linter` int he final check this was fixed and there were no further errors found.

## Credits 
- Code institute for the course material
- Slack community.
- Because l was in a remote area with very limited access to the internet during the time l was meant to work on my PP3 I decided to use the example as provided in the PP3 module to build a Battleships game.
I was limited on time hence l went with the idea to build a simple battleships game.
- Prior to commencing my project I watched a lot of Youtube tutorial on how to build a basic single users battleships game. 
- For some extra tutorials on understanding how to make sue of my python code I would especially like to thank my fellow student Dave Horrocks. 
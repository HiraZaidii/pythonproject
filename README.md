### The Battleship game

This is a simple CLI based Battleship game made by using basic Python code.
In this game the player has to search and hit ships by using his keyboard. 
![python](https://user-images.githubusercontent.com/98779723/191877713-6a9ff2d7-a380-4322-8334-96c33fa67508.png)

[The Game](https://battleshiphira.herokuapp.com/)

## Index

* Features
* Testing
* Technologies used
* Deployment
* Bugs
* Credits


## Features

A classic battleship game that has a board/grid of 5 by 5. The board is presented by the letter "O"
You can hit the ship by inserting a number from 0 to 4 for the row and for the column. The program will give you a reply in text everytime you take a turn. Once you do hit a spot the grid will show a "X" on that spot. You have 4 turns and then it's game over!

## Testing

* PEP 8
  * This was used for the python code and contained no errors.
* W3School 
  * This was used for solving issues regarding the commits.
* Heroku 
  * This was used to deploy the game in a live environment.
I had to test the app several times in Heroku, please read more about it in Bugs.


## Technology used

 * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
 * [Git](https://en.wikipedia.org/wiki/Git) 
 * [Github](https://en.wikipedia.org/wiki/GitHub) 
 * [Heroku](https://en.wikipedia.org/wiki/Heroku)


## Deployment

* Push the latest code to GitHub.
* Login on Heroku
* Create new app by adding app name and region
* Connect to GitHub.
* Search your repository and connect it to Heroku
* Add Python and Node.js in the buildpacks of the settings
* In the Deployement tab scroll down to deploy main branch of connected repo


## Bugs

The first time the code went through PEP8 validator I had a lot of wrong indentation and whitespaces. I fixed this until the code would pass through PEP8 validator.
After running in the terminalI came across a few errors. I fixed the code as much of the print statements did not have "()" I had to fix this and then tested again after deployment.

## Issue

I intially started this project by following a Python Battleship Tutorial by CS Student ( see credits section for more info ). I could not finish it due to lack of time. I really wanted to try to PyCharm as an IDE as per the tutorial but due to some licensing issues on my (work)laptop I was not able to download it hence I decided to go for a simpler version of the Battleship.

## Credits

* I was inspired by a lot of YouTube Tutorials for making this project but the main remains:
[CS Students ](https://www.youtube.com/watch?v=MgJBgnsDcF0&t=1165s) for the difficult one I couldn't finish
[Dylan Israel](https://www.youtube.com/watch?v=7Ki_2gr0rsE) for the one I am submitting
* Code Institute for the course material and overview of deployment
* Slack and Tutor support 
* I specially want to thank Student Care, due to some personal reasons I was on a leave of 3 months and they did the best they could during that period to support me. I have submitted this project just returning from the leave.

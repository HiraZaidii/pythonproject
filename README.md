### The Battleship game

This is a simple CLI based Battleship game made by using basic Python code.
In this game the player has to search and hit ships by using his keyboard. 

## Index

* Features
* Testing
* Technologies used
* Deployment
* Bugs
* Credits


## Features

A classic battleship game that has a board/grid of 5 by 5. The board is presented by the letter "O"
You can hit the ship by inserting a number for row and a number for column. The program will give you a reply in text everytime you take a turn. Once you do hit a spot the grid will show a "X" on that spot. You have limited turns.

## Testing

* PEP 8
  * This was used for the python code and contained no errors.
* W3School 
  * This was used for solving issues regarding the commits.
* Heroku 
  * This was used to deploy the game in a live environment.

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

I started off this project with a bit more complicated code that was not possible to timely debug and used PyCharm as an IDE of which I was unsure if it would be allowed as Pygame was prohibited. This project was inspired by the Youtube Tutorial of [CS Students ](https://www.youtube.com/watch?v=MgJBgnsDcF0&t=1165s)
Hence I created a simple version of the Battleship.
PEP8 was approving print entry without "()" but I got an error in Heroku while deploying so this was debugged by adding "()".


## Credits

* I was inspired by a lot of YouTube Tutorials for making this project but the main remains:
[CS Students ](https://www.youtube.com/watch?v=MgJBgnsDcF0&t=1165s)
* Code Institute for the course material and overview of deployment
* Slack and Tutor support 
* My loving family

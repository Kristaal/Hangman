# HANGMAN
(Developer: Kristina Orlichenko github: kristaal)

Hangman is a terminal based game, which runs in the Code Institute mock terminal Heroku.

Users try to guess a random word, by guessing the letters of the missing word. Each uncorrect guess takes one life. The game is over if the user guesses all the missing litters of the word or if he loses all his lives. Instructions are provided in the game to teach the user how to play.

![Start screen](docs/am-i-responsive.png)

[Live webpage](https://hangman99.herokuapp.com/)

## Table of Content

1. [How to play](#How-to-play)
2. [Project Goals](#projects-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
3. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
    4. [Site Owner Stories](#site-owner-stories)
4. [Technical Design](#technical-design)
    1. [Flowchart](#flowchart)
5. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks-&-tools)
6. [Features](#features)
7. [Testing](#testing)
    1. [Validation](#validation)
    2. [Testing user stories](#testing-user-stories)
8. [Bugs](#Bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
    1. [Code](#code)
11. [Acknowledgments](#acknowledgments)

## How to play

Hangman is a classic guessing game. You can read more about it on Wikipedia.
The length of the word is explicitly stated and is marked by underscores for each letter to be guessed.
The player attempts to build a missing word by guessing one letter at a time.
If the player puts an incorrect letter, he will lose a try. The user continues to guess until they run out of lives without guessing the word.

## Project Goals 
Hangman is a terminal game that outputs the word guessing game

### User Goals
You have the opportunity to play the classic game "Hangman" and guess the words

### Site Owner Goals
Allowing users to play and guess words

## User Experience

### Target Audience
- User, who wants to play the classic game "Hangman"
- User, who want to guess the word
- User, who likes terminal game

### User Requirements and Expectations
- Easy to play
- Easy setup
- Clear rules of the game

### User Stories
1. As a user, I want to read the rules of the game
2. As a user, I want to be able to choose different theme for words to guess
3. As a user, I want to start the game
4. As a user, I want to see which letters I guessed correctly. 
5. As a user, I want to see which letter 
 I guessed wrong
6. As user, I want to know what letter I already guessed
7. As a user, I want to get the result
8. As a user, I want to play again
### Site Owner Stories
9. As a site owner, I want the user to get feedback in case of wrong input

## Technical Design

### Flowchart
<details><summary>Flowchart</summary>
<img src="docs/flowchart.png">
</details>

## Technologies Used

### Languages
- Python

### Frameworks & Tools
- GitHub
- GitPod
- Smartdraw<span>.</span>com ( to create a flowchart)

## Features

### Welcome Screen
- The main screen displays title and menu with the option to choice start the game or read the rules of the game

<details><summary>Welcome screen</summary>
<img src="docs/features/welcome_screen.png">
</details>

### Rules Screen
- The user can select number 2 and read the rules of the game

<details><summary>Rules screen</summary>
<img src="docs/features/rules_screen.png">
</details>

### Theme Screen
- The user can also select number 1 and after will display the screen with option to choose the theme of words

<details><summary>Theme screen</summary>
<img src="docs/features/theme_screen.png">
</details>

### Game Screen
- After selecting the theme of words, the user can start the game
- Random word will be display
- A graphic hangman is displayed to show the user the lives remaining
- Underneath a '_' is shown for each letter in the word

<details><summary>Game screen</summary>
<img src="docs/features/game_screen.png">
</details>

### User input
- The user guesses a letter 
- If the entry is correct, the letter will apper in the word

<details><summary>User input 1</summary>
<img src="docs/features/user_input_1.png">
</details>

-  If the entry is wrong, the user will lose one life and will see the image of hangman

<details><summary>User input 2</summary>
<img src="docs/features/user_input_2.png">
</details>

- If the entry is invalid, the error messege will appear

<details><summary>User input 3</summary>
<img src="docs/features/user_input_3.png">
</details>

### Result Screen
- If the user guessed the word, the result screen will display and notice about this
<details><summary>Result screen 1</summary>
<img src="docs/features/result_1.png">
</details>

- If the user lost all his life, the result screen wiil display guessed word and will offer to play again

<details><summary>Result screen 2</summary>
<img src="docs/features/result_2.png">
</details>

## Testing
I have manually tested this project by doing the following:
- Passed the code through a PEP8 linter and confirmed there are no problems
- Given invalid inputs
- Tested in my local terminal and the Code Institute Heroku terminal

### Validation
PEP8 online was used to check the code for PEP8 requirements.
All code passes with no errors and warnings to show

<details><summary>run.py</summary>
<img src="docs/validation/pep8_validation_run.png">
</details>

<details><summary>words.py</summary>
<img src="docs/validation/pep8_validation_words.png">
</details>

<details><summary>hangman.py</summary>
<img src="docs/validation/pep8_validation_hangman.png">
</details>
<br>

### Testing user stories
1. As a user, I want to read the rules of the game

| Feature | Action | Expected Result | Actual Result |
|-------------|------------|---------------------|-------------------|
| Read rules of the game | On main menu choose and input number "2" | Rules screen is displayed| Works as expected 

<details><summary>Screenshots</summary>
<img src="docs/user_stories/user_story_1.png">
</details>
<br>
2. As a user, I want to be able to choose different theme for words to guess

| Feature | Action | Expected Result | Actual Result |
|-------------|------------|---------------------|-------------------|
| Start the game | On main menu choose and input number "1" |  Start game screen is displayed| Works as expected 

<details><summary>Screenshots</summary>
<img src="docs/user_stories/user_story_2.png">
</details>
<br>

3. As a user, I want to start the game

| Feature | Action | Expected Result | Actual Result |
|-------------|------------|---------------------|-------------------|
| Start the game | Choose the theme of word and input "C","A" or "M"  |  Game screen is displayed| Works as expected 

<details><summary>Screenshots</summary>
<img src="docs/user_stories/user_story_3.png">
</details>
<br>

4. As a user, I want to see which letters I guessed correctly

| Feature | Action | Expected Result | Actual Result |
|-------------|------------|---------------------|-------------------|
| Right input |  A user provides letter that is in the word | Line "guessed letter is in the word" is displayed, appears in place of "__" | Works as expected 

<details><summary>Screenshots</summary>
<img src="docs/user_stories/user_story_4.png">
</details>
<br>

5. As a user, I want to see which letter 
 I guessed wrong

| Feature | Action | Expected Result | Actual Result |
|-------------|------------|---------------------|-------------------|
| Wrong input |  A user provides letter that is not in the word | Line "guessed letter  is not in the word" is displayed, user lose one life and an image og hangman appears adding different parts of the body | Works as expected 

<details><summary>Screenshots</summary>
<img src="docs/user_stories/user_story_5.png">
</details>
<br>

6. As user, I want to know what letter I already guessed

| Feature | Action | Expected Result | Actual Result |
|-------------|------------|---------------------|-------------------|
| Repeated input  |  A user provides letter that he already guessed | Line "You already guessed letter" is displayed | Works as expected 

<details><summary>Screenshots</summary>
<img src="docs/user_stories/user_story_6.png">
</details>
<br>

7. As a user, I want to get the result

| Feature | Action | Expected Result | Actual Result |
|-------------|------------|---------------------|-------------------|
| Result |  Users guessed the word or lose all his lifes  | Result screen is displayed | Works as expected 

<details><summary>Screenshots Result 1</summary>
<img src="docs/user_stories/user_story_8.png">
</details>

<details><summary>Screenshots Result 2</summary>
<img src="docs/user_stories/user_story_9.png">
</details>
<br>
8. As a user, I want to play again

| Feature | Action | Expected Result | Actual Result |
|-------------|------------|---------------------|-------------------|
| Play again |  Users chose and input "Y"  | Game screen is displayed | Works as expected 

<details><summary>Screenshots</summary>
<img src="docs/user_stories/user_story_10.png">
</details>
<br>

### Site Owner Stories
9. As a site owner, I want the user to get feedback in case of wrong input

| Feature | Action | Expected Result | Actual Result |
|-------------|------------|---------------------|-------------------|
| Input validation |	A user provides invalid input|A message explaining the error is displayed and the user is prompted to try again	| Works as expected

<details><summary>Screenshots</summary>
<img src="docs/user_stories/user_story_7.png">
</details>

## Bugs

| Bug | Fix |
| ----------- | ----------- |
| On the main menu "PLAY GAME" and "HOW TO PLAY" are not displayed in the center and have different positions| Add .center(80) to the both|
The user didn`t lose his lifes | Fix code and add lives_qv -= 1 to the run.py |
Some phrases of the game have different position | Add * 30 to the print line

## Deployment
The website was deployed using Heroku by "following these steps:
1. Use the "pip freeze -> requiremnts.txt" command in the terminal to save any libraries that need to be instaled in the file
2. Login or create a Heroku account
3. Click the "new" button in the upper right corner and select "create new app"
4. Choose an app name and your region and click "Create app"
5. Go to the "settings" tab, add the python build pack and then the node.js build pack
6. Go to the "deploy" tab and pick GitHub as a deployment method
7. Search for a repository to connect to
8. Click enable automatic deploys and then deploy branch
9. Wait for the app to build and then click on the "View" link

You can fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on the Fork button in the upper right-hand corner

You can clone the repository by following these steps:
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone

## Credits
- Code Institute for the terminal for the deploy to a live site
- ASCII art was taken from Texteditor

### Code
- Hangman youtube tutorial (how to build a hangman game)

## Acknowledgments
- Spenser Barriball, my mentor. Thank you for your guidance and feedback.



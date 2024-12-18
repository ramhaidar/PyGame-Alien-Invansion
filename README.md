# PyGame-Alien-Invasion

This project implements an **Alien Invasion** game using the Pygame library. It allows users to control a spaceship, shoot bullets, and destroy aliens while avoiding collisions.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Game Mechanics](#game-mechanics)
4. [How to Play](#how-to-play)
5. [Code Description](#code-description)
6. [Dependencies](#dependencies)
7. [Example Usage](#example-usage)
8. [Acknowledgments](#acknowledgments)
9. [License](#license)

---

## Project Overview

The Alien Invasion project enables users to:

1. **Control a Spaceship** to move left and right.
2. **Shoot Bullets** to destroy aliens.
3. **Avoid Collisions** with aliens.
4. **Track Scores and Levels** as the game progresses.

This system uses **Pygame** to create and manage the game elements.

---

## Features

1. **Spaceship Control**  
   Users can control the spaceship using the arrow keys.

2. **Bullet Shooting**  
   Shoot bullets to destroy aliens by pressing the spacebar.

3. **Alien Fleet**  
   A fleet of aliens moves across the screen and drops down periodically.

4. **Score Tracking**  
   Track the player's score and high score.

5. **Level Progression**  
   Increase the game difficulty as the player progresses through levels.

---

## Game Mechanics

The game consists of:

-   **Spaceship** controlled by the player.
-   **Bullets** fired by the spaceship.
-   **Aliens** that move and drop down the screen.
-   **Scoreboard** to display the current score, high score, and level.

---

## How to Play

### Step 1: Clone the Repository

```bash
git clone https://github.com/filzarahma/PyGame-Alien-Invansion.git
```

### Step 2: Install Dependencies

Ensure you have Python and Pygame installed. You can install Pygame using pip:

```python
pip install pygame
```

### Step 3: Run the Game

Navigate to the project directory and run the game:

```python
python alien_invasion.py
```

### Controls

-   Arrow Keys: Move the spaceship left and right.
-   Spacebar: Shoot bullets.
-   Q Key: Quit the game.

---

### Code Description

The project is organized into several modules:

-   alien_invasion.py: Main game class that manages game assets and behavior.
-   settings.py: Stores all settings for the game.
-   game_stats.py: Tracks statistics and scoring.
-   scoreboard.py: Manages scoring information.
-   button.py: Creates and manages game buttons.
-   ship.py: Manages the player's spaceship.
-   bullet.py: Manages projectiles fired from the ship.
-   alien.py: Represents a single alien in the fleet.

### Dependencies

-   Python 3.x
-   Pygame

### Example Usage

To start the game, simply run the [alien_invasion.py](/alien_invasion.py) script:

### Acknowledgments

This project is inspired by the book "Python Crash Course" by Eric Matthes. Special thanks to the Pygame community for their support and resources.

### License

This project is licensed under the Apache License 2.0. See the [LICENSE](/LICENSE) file for details.

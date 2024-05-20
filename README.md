Remigijus Kaminskas EKf-23
Course Work - Plateformer Shooter Game


Introduction:
The objective of this coursework was to develop a platformer shooter game,
featuring a controllable player character, shooting mechanics, grenades, basic enemy AI,
two levels, and level restarting functionality. The game was created using Python programming
language and the Pygame module. Execution of the program is initiated by opening the "main.py" file
and running the code. Players can start by pressing the "Start" button.
The controls for the game:
W - Jump
A - Move left
D - Move right
Space - Shoot
Q - Throw Grenade
Escape - Close program


Body Analysis:
The main.py file is the core of the program, it has the game loop which handeles everything from whats happening
on the screen to player imputs. Soldier class is used for both the controllable player and the enemy. World is loaded
from a cvs file, tiles are read into 2D list and tiles are split up into obstacles, water, itemboxes, exit and decorations.
Soldier class has the most complicated code which is responsible for everything the player or enemies do.
Implementation:

Modules: The game is implemented using the Pygame library in Python, making use of various modules like pygame.sprite for
managing sprites, csv for loading level data, and custom modules for managing game entities.

Classes: The game features classes for the player character, enemies, bullets, items, and level elements like obstacles,
water bodies, and exits. Each class encapsulates specific behaviors and properties.

Game Loop: The core game loop handles player input, updates game state, and renders graphics to the screen. It incorporates
collision detection, enemy AI, and level progression logic.

Level Design: Level data is loaded from CSV files, which define the layout of tiles, enemies, items, and other elements.
The World class processes this data to generate levels dynamically.

Animation: Sprite animations for characters are implemented using a list of images for different actions (idle, run, jump,
death), with frames updated over time to create animation effects.

1. Abstraction: In game.py, the Game class abstracts away the game logic, 
providing a generic interface for initializing and running the game. 
The Player and Enemy classes also abstract away their respective behaviors, 
making it easier to reuse and maintain the code.

2. Encapsulation: In player.py and enemy.py, the Player and Enemy classes 
encapsulate their properties and behaviors, controlling their own state and 
limiting access to their internal implementation details. For example, the Player 
class has private properties like image and rect, which are not directly accessible from outside the class.

3. Inheritance: In player.py and enemy.py, the Player and Enemy classes inherit from the pygame.
sprite.Sprite class, inheriting its properties and behaviors. This allows them to reuse the common 
functionality provided by the Sprite class and focus on their specific implementations.

4. Polymorphism: In game.py, the Game class uses polymorphism when updating and rendering the game objects. 
The update and render methods are called on both Player and Enemy objects, which have their own 
implementations of these methods. This allows the Game class to treat both types of objects uniformly, 
without knowing their specific implementations.

Factory Method: In game.py, the Game class uses the Factory Method pattern to create instances of Player
and Enemy classes. The create_player and create_enemy methods act as factory methods, creating and returning
instances of the respective classes.

Builder pattern: The WorldBuilder class has methods like add_player, add_enemy, and add_wall,
which are used to add individual components to the World object. The build method is
responsible for creating and returning the final World object. This is a clear example
of the Builder pattern, where the construction process is separated from the final object representation.


Result and Summary:
By choosing a more difficult subject that interested me, I had the opportunity to learn coding with Python
on a completely different level. I had never undertaken such a fun and interesting coding project that helped
me learn so many different things. I gained proficiency in utilizing a multi-structured file system, comprehended
the fundamentals of Object-Oriented Programming (OOP), explored design patterns, and adeptly managed object groups.
Even though this project was mostly based on a YouTube tutorial, I can confidently say that I could create a similar
game on my own without relying heavily on others' code. I learned a significant lesson from this experience, realizing
that everything is "figureoutable" and can be built up from the ground one step at a time. With the help of
BlackBox.ai, I was able to figure out and learn from bugs and errors while programming. The only issue I wasn't able
to fix was the player "twitching" while standing on the tile; nothing on the internet helped me solvethe problem.

In summary, exploring a challenging project expanded my Python skills, and I found profound value in comprehending
the intricate components that make a program whole. Despite relying on a tutorial, I gained confidence in
independent game development and learned to persevere through challenges with tools like BlackBox.ai.
If I ever program another game, I will definitely use a game engine because writing a game purely by code
is very inconvenient.


Recources and reference list:
Youtube tutorial by Coding With Russ
https://www.youtube.com/watch?v=DHgj5jhMJKg&list=PLjcN1EyupaQm20hlUE11y9y8EY2aXLpnv
Assets and source code
http://www.codingwithruss.com/gamepage/Shooter/
Big help from BlackBox.ai
Github repository
https://github.com/Nezumi-Remis/Plateform_Shooter_game.git

images of the game:
https://github.com/Nezumi-Remis/Plateform_Shooter_game/blob/main/img1.jpg
https://github.com/Nezumi-Remis/Plateform_Shooter_game/blob/main/img2.jpg
vidoe dowloand:
https://github.com/Nezumi-Remis/Plateform_Shooter_game/blob/main/Desktop%202024.05.14%20-%2021.03.15.03.mp4

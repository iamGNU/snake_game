# 🐍 Snake Game

A classic Snake Game built using **Python** and the **Turtle Graphics** library. Control the snake, eat food to grow longer, beat your high score, and avoid crashing into the walls or your own tail.

---

## 🎮 Features

* Classic Snake gameplay
* Smooth movement using keyboard controls
* Randomly spawning food
* Score tracking
* High score saved locally
* Automatic game reset after collision
* Clean object-oriented Python code

---

## 📂 Project Structure

```
snake_game/
│── main.py           # Main game loop
│── snake.py          # Snake class and movement logic
│── food.py           # Food generation
│── scoreboard.py     # Score and high score management
│── Assets/           # Screenshots
└── README.md
```

The high score is saved to `data.txt`, which the game creates automatically next to `scoreboard.py`.

---

## 🛠️ Technologies Used

* Python 3
* Turtle Graphics
* Object-Oriented Programming (OOP)

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/CodeCopAkash/snake_game.git
```

2. Navigate to the project folder:

```bash
cd snake_game
```

3. Run the game:

```bash
python main.py
```

> Make sure Python 3 is installed. The Turtle module comes pre-installed with Python.

---

## 🎯 Controls

| Key | Action     |
| --- | ---------- |
| ↑   | Move Up    |
| ↓   | Move Down  |
| ←   | Move Left  |
| →   | Move Right |

---

## 🕹️ Gameplay

* Eat the white food to increase your score.
* Every food collected makes the snake grow longer.
* Hitting the wall or your own tail resets the game.
* Your highest score is saved to `data.txt` as soon as you beat it.
* Food never spawns on top of the snake.

---

## 📸 Screenshots

| Start | Gameplay |
| --- | --- |
| ![Start screen](Assets/start-screen.png) | ![Gameplay](Assets/gameplay.png) |

---

## 📚 Concepts Practiced

* Classes and Objects
* Inheritance
* Event Handling
* Collision Detection
* File Handling
* Game Loop
* Turtle Graphics

---

## 🚀 Future Improvements

* Sound effects
* Pause and Resume feature
* Difficulty levels
* Obstacles
* Start Menu
* Better graphics and animations

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository, improve the game, and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

### ⭐ If you enjoyed this project, consider giving it a star on GitHub!

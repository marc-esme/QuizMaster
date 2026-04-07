# QuizMaster

A modern, customizable quiz application built with Python and PyQt5. This app features a clean, responsive UI with background images and a separate scoring system.

## 🚀 Features

- **Customizable Questions**: Easily add, remove, or modify quiz content via a JSON file.
- **Modern Responsive Design**: Dynamic background images for each screen (Start, Quiz, Result).
- **Style Customization**: The entire look and feel is managed through a single `.qss` stylesheet.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

## 🛠️ Requirements

The project requires Python 3.x and the following packages:
- `PyQt5`

To install the necessary dependencies, run:
```bash
pip install -r requirements.txt
```

## 📁 Project Structure

- `main.py`: Entry point of the application.
- `Controller/`: Application logic and user interaction handling.
- `Model/`: Data management and scoring logic.
- `View/`: User interface definitions (PyQt5).
- `Resources/`: Background images, application icon, and JSON question data.

## 📝 Customizable JSON Format

You can customize the quiz by editing `Resources/questions.json`. The application follows a simple structure:

```json
[
  {
    "question": "Your question text here?",
    "answers": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "correct": "Option 1"
  }
]
```

- **`question`**: The text to display to the user.
- **`answers`**: A list of four choices.
- **`correct`**: The exact string representing the correct answer (must match one of the choices).

## 🎨 Styling

The application's appearance (colors, fonts, buttons, and background images) can be modified in `Resources/style.qss`. The background images are applied to the following objects:
- `#startScreen`: Background for the start menu.
- `#quizScreen`: Background during the quiz.
- `#resultScreen`: Background for the final score screen.

## 🏃 Running the Application

To start the quiz, simply run:
```bash
python main.py
```

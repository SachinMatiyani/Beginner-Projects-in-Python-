# 📝 My Python Projects

This repository contains all the Python projects I make during my learning journey.  
I will keep updating this repo with new projects as I learn more.

---

## 📌 Project No. 1 – Snake Game 🐍

**Description:**  
A simple Snake Game made using Python and Pygame.  
The snake eats food to grow longer, and the game ends if it hits the wall.

**Features:**
- Score display
- Restart and Quit option after Game Over
- Smooth movement

**Controls:**
| Key | Action |
|-----|--------|
| ⬅️ Left Arrow | Move Left |
| ➡️ Right Arrow | Move Right |
| ⬆️ Up Arrow | Move Up |
| ⬇️ Down Arrow | Move Down |
| **P** | Play Again |
| **Q** | Quit Game |

**How to Run:**
1. Install Python (>= 3.6)
2. Install Pygame:
```bash
pip install pygame
```
3. Run the game:
```bash
python snake_game.py
```

---

## 📌 Project No. 2 – Face Detection System 👤

**Description:**  
A real-time Face Detection system built using Python and OpenCV.  
The application uses your webcam to detect human faces and draws green rectangles around detected faces in real-time.

**Features:**
- Real-time face detection using webcam
- Multiple face detection capability
- Green bounding boxes around detected faces
- Smooth video processing
- Easy exit functionality

**Technology Used:**
- **OpenCV** - Computer Vision library
- **Haar Cascade Classifier** - Pre-trained face detection model
- **Python** - Programming language

**Controls:**
| Key | Action |
|-----|--------|
| **A** | Exit/Quit the application |

**How to Run:**
1. Install Python (>= 3.6)
2. Install OpenCV:
```bash
pip install opencv-python
```
3. Make sure your webcam is connected and working
4. Run the Python script:
```bash
python face_detection.py
```

**Requirements:**
- Python 3.6+
- OpenCV library
- Working webcam/camera
- Haar Cascade XML file (included with OpenCV)

**How it Works:**
1. Captures video from your default camera (index 0)
2. Converts each frame to grayscale for better detection
3. Uses Haar Cascade classifier to detect faces
4. Draws green rectangles around detected faces
5. Displays the live video feed with face detection
6. Press 'A' key to exit the application

**Note:**
Make sure to allow camera permissions when prompted by your system.

---

## 📌 Project No. 3 – Tkinter Calculator 🧮

**Description:**  
A fully functional GUI Calculator built using Python's Tkinter library.  
The calculator can perform basic arithmetic operations with a user-friendly graphical interface.

**Features:**
- Clean and intuitive GUI design
- Basic arithmetic operations (+, -, *, /)
- Decimal point support
- Error handling for invalid expressions
- Clear function to reset calculator
- Responsive button layout

**Technology Used:**
- **Tkinter** - Python's built-in GUI library
- **Python** - Programming language

**Calculator Layout:**
| Button | Function |
|--------|----------|
| **0-9** | Number input |
| **+** | Addition |
| **-** | Subtraction |
| **\*** | Multiplication |
| **/** | Division |
| **.** | Decimal point |
| **=** | Calculate result |
| **C** | Clear display |

**How to Run:**
1. Install Python (>= 3.6) - Tkinter comes pre-installed with Python
2. Run the calculator:
```bash
python calculator.py
```

**Requirements:**
- Python 3.6+ (with Tkinter - usually included by default)
- No additional libraries needed

**How it Works:**
1. GUI window opens with calculator interface (300x350 pixels)
2. Click number buttons to input numbers
3. Click operation buttons (+, -, *, /) for calculations
4. Press '=' button to get the result
5. Use 'C' button to clear the display
6. Error handling shows "Error" for invalid expressions

**Features in Detail:**
- **Display Screen**: Shows current input and results
- **Number Pad**: 0-9 digits for input
- **Operations**: Addition, subtraction, multiplication, division
- **Equals Button**: Evaluates the mathematical expression
- **Clear Button**: Resets the calculator to start fresh
- **Error Handling**: Displays "Error" for invalid calculations

---

**Keep Learning, Keep Coding!** 💻✨
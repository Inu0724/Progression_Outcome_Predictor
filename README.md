# Student Progression Predictor

## 📌 Project Overview

This is a Python-based command-line application developed as part of the module **4COSC006C: Software Development I**. It predicts student progression outcomes based on credit input and university-defined rules.

This project fulfills the following Learning Outcomes:
- Design solutions with algorithmic techniques.
- Implement Python programs using conditional logic and loops.
- Handle input validation and error reporting.
- Use data structures like lists and file I/O for data management.
- Render graphical histograms using `graphics.py`.

---

## 🚀 Features

### ✅ Part 1: Outcome Prediction
- Accepts user inputs: `Pass`, `Defer`, and `Fail` credits.
- Validates each input:
  - Non-integer → `Integer required`
  - Out of range → `Out of range`
  - Total ≠ 120 → `Total incorrect`
- Predicts progression:
  - `Progress`
  - `Progress (module trailer)`
  - `Do not Progress – module retriever`
  - `Exclude`

### 🔁 Part 1C: Loop for Multiple Students
- Allows staff to enter multiple sets of data.
- Typing `q` exits and triggers the histogram.

### 📊 Part 1D: Histogram Output
- Displays a graphical histogram using `graphics.py`.
- Shows counts for each outcome type and total students.

### 📝 Part 2: Store Data in List
- Inputs are saved in a list of records.
- Displays all progression outcomes with their respective credit combinations.

### 💾 Part 3: Write & Read from File
- Saves progression outcomes to a text file.
- Retrieves and prints them later.

---

## 🖥️ Screenshots

### 📊 Histogram Window
<img src="Screenshot/Histogram.jpg" alt="Histogram Screenshot" width="300"/>

### 📋 Part 2 - List Output
<img src="Screenshot/list_output.png" alt="List Output Screenshot" width="300"/>

---

## 🧪 Test Plan

A comprehensive [Test Plan](./w2051581_Text%20Plan.docx) is included that covers all possible scenarios:
- Valid outcomes
- Input validation
- Multiple entries
- Graphical output verification

---

## 🛠️ How to Run

1. Clone this repo or download the code.
2. Ensure Python 3 is installed.
3. Run the script using:

```bash
python student_id.py

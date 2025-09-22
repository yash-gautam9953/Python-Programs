<<<<<<< HEAD
# Python Projects Collection

A collection of simple Python projects demonstrating various programming concepts and libraries.

## 📁 Projects Overview

### 1. QR Code Generator (`qrstyle.py`)

- **Description**: Creates custom QR codes with personalized styling
- **Features**:
  - Customizable colors (white fill, purple background)
  - High error correction level
  - Adjustable box size and border
- **Dependencies**: `qrcode`, `PIL (Pillow)`
- **Output**: Generates `yash.png` with the QR code

### 2. Rock Paper Scissors Game (`rock paper.py`)

- **Description**: Interactive console-based Rock Paper Scissors game
- **Features**:
  - Play against computer with random choices
  - Continuous gameplay until user exits
  - Win/Lose/Draw detection logic
  - Input validation
- **How to Play**: Choose 1 (Rock), 2 (Paper), 3 (Scissors), or 0 (Exit)

### 3. Email Validator (`yash.py`)

- **Description**: Simple email validation system
- **Features**:
  - Validates Gmail addresses
  - Account creation confirmation
  - Input loop until valid email is entered
- **Validation**: Checks for "@gmail.com" format

### 4. Banking System (`yashbank.py`)

- **Description**: Simple banking application with basic operations
- **Features**:
  - Account balance management
  - Debit and Credit operations
  - Balance inquiry with account verification
  - Interactive menu system
- **Account Details**: Default account number `9953047014` with initial balance of ₹100,000

## 🚀 How to Run

### Prerequisites

```bash
pip install qrcode[pil]
```

### Running Individual Projects

1. **QR Code Generator**:

   ```bash
   python qrstyle.py
   ```

2. **Rock Paper Scissors**:

   ```bash
   python "rock paper.py"
   ```

3. **Email Validator**:

   ```bash
   python yash.py
   ```

4. **Banking System**:
   ```bash
   python yashbank.py
   ```

## 🛠️ Technologies Used

- **Python 3.x**
- **Libraries**:
  - `qrcode` - QR code generation
  - `PIL (Pillow)` - Image processing
  - `random` - Random number generation
  - Built-in Python modules

## 📝 Features by Project

| Project             | Input/Output                      | Main Concept                  |
| ------------------- | --------------------------------- | ----------------------------- |
| QR Generator        | Text → QR Image                   | Image processing, QR encoding |
| Rock Paper Scissors | User choice → Game result         | Game logic, Random generation |
| Email Validator     | Email string → Validation         | String validation, Loops      |
| Banking System      | Menu choices → Account operations | OOP, Class methods            |

## 🎯 Learning Outcomes

- **Object-Oriented Programming** (Banking System)
- **Image Processing** (QR Code Generator)
- **Game Development Logic** (Rock Paper Scissors)
- **Input Validation** (Email Validator)
- **File I/O Operations** (QR Code saving)
- **User Interface Design** (Console-based interactions)

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements or additional features!

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

**Author**: Yash Gautam  
**Created**: 2024
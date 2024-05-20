# Typing Speed Test App

## Overview

The Typing Speed Test App is a simple application built using Python and tkinter, designed to measure typing speed by timing how quickly the user can accurately type a shuffled list of words. It provides real-time feedback on Characters Per Minute (CPM), Correct Words Per Minute (WPM), and highlights the current word being typed.

After 60 seconds, the test ends and the typing box is frozen until you restart the typing session.

![Typing Speed Test - GUI.png](resource%2FTyping%20Speed%20Test%20-%20GUI.png)

## Features

- **Timer and Statistics**: The app starts a timer when the user begins typing and displays statistics such as CPM and WPM.
- **Interactive Interface**: Users interact through a graphical interface where they type in a dedicated textbox.
- **Word Highlighting**: Words in the displayed text change color based on correctness while typing.
- **Restart Functionality**: Allows users to restart the typing session with a new shuffled word list.

## Usage

1. **Start Typing**: Type the words displayed in the textbox.
2. **Press Space After Each Word**: Space-bar triggers validation and progression to the next word.
3. **Monitor Progress**: See real-time feedback on CPM, WPM, and remaining time.
4. **Restart**: Click the "Restart" button to begin a new typing session.

## Installation

Ensure you have Python 3 installed. Clone the repository and install required dependencies using:

Make sure that you have installed the following modules: `customtkinter` and `tkinter` in you Python environment.

## How to Run

Execute the application by running the `main.py` script: `python main.py`

## Dependencies

- `tkinter`: Standard Python interface to the Tk GUI toolkit.
- `customtkinter`: Custom module providing enhanced tkinter widgets and styling capabilities.

## Files

- **main.py**: Main script containing the typing speed test application.
- **words.txt**: Text file containing the list of words used for the typing test.

## Development

- **Author**: Cristian M.
- **Version**: 1.0
- **Date**: 20.05.2024

## Contributing
Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests to help improve the application.



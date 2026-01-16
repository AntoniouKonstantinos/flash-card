# 📘 Flashy – Python Flash Card App

Flashy is a Python-based graphical flash card application designed to help users learn French vocabulary interactively.
The app displays a French word, automatically flips the card to show the English translation, and allows users to track words they’ve already learned.

This project is built using Tkinter for the GUI and pandas for data handling.

🎯 How It Works

    A French word is displayed on a flash card.

    After 3 seconds, the card flips automatically to reveal the English translation.

    The user can:

    ❌ Skip the word (wrong button)

    ✅ Mark the word as learned (right button)

    Learned words are removed from the learning list and saved locally.

    Progress is preserved using a CSV file so users can continue learning where they left off.

✨ Features

     Graphical User Interface using Tkinter

     Automatic card flipping after a delay

     CSV-based vocabulary storage

     Progress saving (learned words are removed)

     Random word selection

     Visual card flipping with images

🛠️ Technologies Used

    Python 3

    Tkinter – GUI framework

    pandas – CSV data handling

    random – word selection logic

📂 Project Structure

    flash-card/
    ├── data/
    │   ├── french_words.csv        # Original vocabulary list
    │   └── words_to_learn.csv      # Progress file (auto-generated)
    ├── images/
    │   ├── card_front.png
    │   ├── card_back.png
    │   ├── right.png
    │   └── wrong.png
    ├── main.py                     # Application entry point
    └── README.md

📌 Data Files Explained

    french_words.csv
    Contains the original list of French–English word pairs.

    words_to_learn.csv
    Automatically created after you mark words as learned.
    The app prioritizes this file so you don’t relearn known words.

💡 Possible Improvements

    Add a score or progress counter

    Add more languages

    Add manual flip button

    Improve UI responsiveness

    Add sound effects or animations

    With very little changes the project can handle any TRUE/FALSE type Quiz

📜 License

    This project is open-source and free to use for learning and personal development.

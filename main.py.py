# main.py
import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

# --------------------
# GPT4All Large Model
# --------------------
from gpt4all import GPT4All

# Load your large model once at startup
# Make sure the filename matches your downloaded model
model = GPT4All("gpt4all-j.bin")  # <-- your large model file

def ai_coach_advice(question):
    response = model.generate(question)
    return response

# --------------------
# Offline Fortnite stats (mock)
# --------------------
def get_mock_stats(username):
    return {
        "Username": username,
        "Platform": "PC",
        "Wins": random.randint(0, 1000),
        "Kills": random.randint(0, 20000),
        "Matches": random.randint(100, 5000),
        "K/D": round(random.uniform(0, 10), 2)
    }

# --------------------
# PyQt5 GUI
# --------------------
class AI_Coach_App(QWidget):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("AI Coach + Fortnite Tracker (Offline)")
        self.setGeometry(200, 200, 600, 400)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # AI Coach Section
        self.layout.addWidget(QLabel("AI Coach Question:"))
        self.input_question = QLineEdit()
        self.layout.addWidget(self.input_question)
        self.button_advice = QPushButton("Get Advice")
        self.layout.addWidget(self.button_advice)
        self.output_advice = QTextEdit()
        self.output_advice.setReadOnly(True)
        self.layout.addWidget(self.output_advice)
        self.button_advice.clicked.connect(self.get_advice)

        # Fortnite Tracker Section
        self.layout.addWidget(QLabel("Fortnite Username:"))
        self.input_username = QLineEdit()
        self.layout.addWidget(self.input_username)
        self.button_stats = QPushButton("Get Fortnite Stats")
        self.layout.addWidget(self.button_stats)
        self.output_stats = QTextEdit()
        self.output_stats.setReadOnly(True)
        self.layout.addWidget(self.output_stats)
        self.button_stats.clicked.connect(self.get_stats)

    def get_advice(self):
        question = self.input_question.text().strip()
        if not question:
            self.output_advice.setText("Please type a question for AI Coach.")
            return
        advice = ai_coach_advice(question)
        self.output_advice.setText(f"AI Coach Advice:\n{advice}")

    def get_stats(self):
        username = self.input_username.text().strip()
        if not username:
            self.output_stats.setText("Please type a Fortnite username.")
            return
        stats = get_mock_stats(username)
        display = (
            f"Stats for {stats['Username']} ({stats['Platform']}):\n"
            f"Wins: {stats['Wins']}\n"
            f"Kills: {stats['Kills']}\n"
            f"Matches: {stats['Matches']}\n"
            f"K/D: {stats['K/D']}"
        )
        self.output_stats.setText(display)

# --------------------
# Run the app
# --------------------
if __name__ == "_main_":
    app = QApplication(sys.argv)
    window = AI_Coach_App()
    window.show()
    sys.exit(app.exec_())
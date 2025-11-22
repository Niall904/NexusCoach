# main.py
import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox

# --------------------
# GPT4All Model
# --------------------
try:
    from gpt4all import GPT4All
    model = GPT4All("gpt4all-j.bin")  # Ensure this file is in the same folder
except Exception:
    model = None

def ai_coach_advice(question):
    if model:
        return model.generate(question)
    else:
        return "GPT4All model not found. Place 'gpt4all-j.bin' in the project folder."

# --------------------
# Mock Fortnite Stats
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
# Training Sessions
# --------------------
def generate_training():
    exercises = [
        "30 min aim training",
        "15 min building drills",
        "10 min editing practice",
        "5 matches focused on rotations",
        "Replay analysis of last match"
    ]
    return "\n".join(random.sample(exercises, k=3))

# --------------------
# Staff / Client Keys
# --------------------
STAFF_CLIENT_KEYS = [
    "ClientNorthern81910#+71",
    "ClientPonyta41629#-5",
    "ClientSandman71619#-2",
    "StaffNiall61518#-2",
    "StaffKronos24190#+3"
]

# --------------------
# PyQt5 GUI
# --------------------
class AI_Coach_App(QWidget):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Nexus Coach – Fortnite AI Coach")
        self.setGeometry(200, 200, 650, 500)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Login / Key Entry
        self.layout.addWidget(QLabel("Enter your access key:"))
        self.input_key = QLineEdit()
        self.layout.addWidget(self.input_key)
        self.button_verify = QPushButton("Verify Key / Login")
        self.layout.addWidget(self.button_verify)
        self.button_verify.clicked.connect(self.verify_key)

        self.label_status = QLabel("")
        self.layout.addWidget(self.label_status)

        # AI Coach Section
        self.layout.addWidget(QLabel("Ask AI Coach:"))
        self.input_question = QLineEdit()
        self.layout.addWidget(self.input_question)
        self.button_advice = QPushButton("Get Advice")
        self.layout.addWidget(self.button_advice)
        self.output_advice = QTextEdit()
        self.output_advice.setReadOnly(True)
        self.layout.addWidget(self.output_advice)
        self.button_advice.clicked.connect(self.get_advice)
        self.button_advice.setEnabled(False)

        # Fortnite Stats Section
        self.layout.addWidget(QLabel("Fortnite Username:"))
        self.input_username = QLineEdit()
        self.layout.addWidget(self.input_username)
        self.button_stats = QPushButton("Get Stats")
        self.layout.addWidget(self.button_stats)
        self.output_stats = QTextEdit()
        self.output_stats.setReadOnly(True)
        self.layout.addWidget(self.output_stats)
        self.button_stats.clicked.connect(self.get_stats)
        self.button_stats.setEnabled(False)

        # Training Session Section
        self.button_training = QPushButton("Generate Training Session")
        self.layout.addWidget(self.button_training)
        self.output_training = QTextEdit()
        self.output_training.setReadOnly(True)
        self.layout.addWidget(self.output_training)
        self.button_training.clicked.connect(self.get_training)
        self.button_training.setEnabled(False)

        # State
        self.user_is_staff_client = False
        self.user_subscribed = False

    # --------------------
    # Verify access key
    # --------------------
    def verify_key(self):
        key = self.input_key.text().strip()
        if not key:
            QMessageBox.warning(self, "Error", "Please enter your access key.")
            return

        if key in STAFF_CLIENT_KEYS:
            self.user_is_staff_client = True
            self.user_subscribed = True
            self.label_status.setText("Staff/Client key accepted! Full access unlocked 24/7.")
            self.enable_features()
        else:
            self.label_status.setText(
                "Non-client key. Please subscribe via your website to unlock features."
            )
            # Enable buttons for demo, but could disable if you want

    # Enable features after key verification
    def enable_features(self):
        self.button_advice.setEnabled(True)
        self.button_stats.setEnabled(True)
        self.button_training.setEnabled(True)

    # --------------------
    # AI Coach Advice
    # --------------------
    def get_advice(self):
        question = self.input_question.text().strip()
        if not question:
            self.output_advice.setText("Please type a question for AI Coach.")
            return
        advice = ai_coach_advice(question)
        self.output_advice.setText(f"AI Coach Advice:\n{advice}")

    # --------------------
    # Fortnite Stats
    # --------------------
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
    # Training Session
    # --------------------
    def get_training(self):
        training = generate_training()
        self.output_training.setText(f"Today's Training Session:\n{training}")

# --------------------
# Run App
# --------------------
if __name__ == "_main_":
    app = QApplication(sys.argv)
    window = AI_Coach_App()
    window.show()
    sys.exit(app.exec_())

import json, os
from datetime import date, timedelta

class ProgressManager:
    # Get the directory where this file is located, then go up 1 level to English_Game root
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    FILE = os.path.join(BASE_DIR, "data", "progress.json")

    def __init__(self, username):
        self.username = username
        self.data = self.load()

    def load(self):
        if not os.path.exists(self.FILE):
            return self.default()

        with open(self.FILE) as f:
            all_data = json.load(f)

        return all_data.get(self.username, self.default())

    def default(self):
        return {
            "name": self.username,
            "total_score": 0,
            "games_played": 0,
            "current_streak": 0,
            "last_played": None,
            "badges": []
        }

    def update_streak(self):
        today = date.today()
        last = self.data["last_played"]

        if last:
            last = date.fromisoformat(last)
            self.data["current_streak"] = (
                self.data["current_streak"] + 1
                if today == last + timedelta(days=1)
                else 1
            )
        else:
            self.data["current_streak"] = 1

        self.data["last_played"] = today.isoformat()
        self.save()

    def update_after_game(self, score, level, theme):
        self.data["total_score"] += score
        self.data["games_played"] += 1

    def save(self):
        os.makedirs("data", exist_ok=True)
        if os.path.exists(self.FILE):
            with open(self.FILE) as f:
                all_data = json.load(f)
        else:
            all_data = {}

        all_data[self.username] = self.data

        with open(self.FILE, "w") as f:
            json.dump(all_data, f, indent=4)

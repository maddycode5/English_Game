import json, os

class Leaderboard:
    # Get the directory where this file is located, then go up 1 level to English_Game root
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    FILE = os.path.join(BASE_DIR, "data", "progress.json")

    @staticmethod
    def get_top(n=5):
        if not os.path.exists(Leaderboard.FILE):
            return []

        with open(Leaderboard.FILE) as f:
            data = json.load(f)

        players = [
            {
                "name": name,
                "score": d.get("total_score", 0),
                "streak": d.get("current_streak", 0)
            }
            for name, d in data.items()
        ]

        return sorted(
            players,
            key=lambda x: (x["score"], x["streak"]),
            reverse=True
        )[:n]

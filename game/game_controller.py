from game.story_engine import StoryEngine
from progress.progress_manager import ProgressManager

class GameController:
    def __init__(self):
        self.engine = StoryEngine()
        self.progress = None
        self.current_template = None
        self.current_words = None
        self.level = None
        self.theme = None

    def load_user(self, username):
        self.progress = ProgressManager(username)
        self.progress.update_streak()

    def get_level_and_theme_data(self):
        return self.engine.get_levels()

    def prepare_round(self, level, theme):
        self.level = level
        self.theme = theme
        self.current_template, self.current_words = self.engine.get_round(level, theme)

    def get_questions(self):
        return self.engine.get_questions(self.current_words)

    def finish_round(self, answers):
        # Guard against missing round data (e.g. user posts /result directly)
        if not self.current_template or not self.current_words:
            return ("No active round. Please start a new game.", 0)

        try:
            story, score = self.engine.generate_story(
                self.current_template,
                self.current_words,
                answers
            )
        except Exception:
            # Avoid raising 500 on unexpected formatting/answer errors
            return ("Could not generate story. Please try again.", 0)

        self.progress.update_after_game(score, self.level, self.theme)
        self.progress.save()
        return story, score

    def get_progress(self):
        return self.progress.data

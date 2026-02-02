import random
from game.word_data import WORD_TYPES, LEVELS

class StoryEngine:

    def get_levels(self):
        return LEVELS

    def get_round(self, level, theme):
        theme_data = LEVELS[level]["themes"][theme]
        template = random.choice(theme_data["templates"])
        words = theme_data["words"]
        return template, words

    def get_questions(self, words):
        questions = []
        for w in words:
            data = WORD_TYPES[w]
            questions.append({
                "type": w,
                "definition": data["definition"],
                "example": data["example"]
            })
        return questions

    def generate_story(self, template, words, answers):
        score = 0
        # defensively handle words/answers so missing data doesn't throw
        if not words:
            words = []

        for w in words:
            if answers.get(w):
                score += 10

        # Only fill placeholders for the expected words to avoid KeyError
        fill = {w: answers.get(w, "") for w in words}
        try:
            story = template.format(**fill)
        except Exception:
            story = ""

        return story, score

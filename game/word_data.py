WORD_TYPES = {
    "adjective": {
        "definition": "Describes a noun",
        "example": "happy, brave"
    },
    "noun": {
        "definition": "Name of a person, place, animal, or thing",
        "example": "boy, city, teacher"
    },
    "verb": {
        "definition": "Shows an action or state",
        "example": "run, explore, study"
    },
    "adverb": {
        "definition": "Describes how an action is done",
        "example": "quickly, silently"
    },
    "place": {
        "definition": "A location where something happens",
        "example": "school, forest, market"
    },
    "emotion": {
        "definition": "A feeling or emotion",
        "example": "excited, nervous, happy"
    },
    "object": {
        "definition": "A thing that can be touched or used",
        "example": "book, sword, bag"
    }
}


LEVELS = {
    # =========================
    # LEVEL 1 – BEGINNER
    # =========================
    1: {
        "name": "Beginner",
        "themes": {
            "Adventure": {
                "templates": [
                    "A {adjective} {noun} decided to {verb} in the {place}.",
                    "One day, a {adjective} {noun} went to the {place} to {verb}.",
                    "In the {place}, a {adjective} {noun} likes to {verb}."
                ],
                "words": ["adjective", "noun", "verb", "place"]
            },

            "School": {
                "templates": [
                    "At school, a {adjective} {noun} likes to {verb} in the {place}.",
                    "Every day, a {adjective} {noun} goes to the {place} to {verb}.",
                    "In the {place}, the {adjective} {noun} tries to {verb}."
                ],
                "words": ["adjective", "noun", "verb", "place"]
            }
        }
    },

    # =========================
    # LEVEL 2 – INTERMEDIATE
    # =========================
    2: {
        "name": "Intermediate",
        "themes": {
            "Adventure": {
                "templates": [
                    "A {adjective} {noun} {verb} {adverb} in the {place}, feeling {emotion}.",
                    "While in the {place}, a {adjective} {noun} decided to {verb} {adverb}.",
                    "Feeling {emotion}, the {adjective} {noun} began to {verb} {adverb}."
                ],
                "words": ["adjective", "noun", "verb", "adverb", "place", "emotion"]
            },

            "Daily Life": {
                "templates": [
                    "Every morning, a {adjective} {noun} {verb} {adverb} and feels {emotion}.",
                    "At the {place}, a {adjective} {noun} likes to {verb} {adverb}.",
                    "A {adjective} {noun} often feels {emotion} while trying to {verb}."
                ],
                "words": ["adjective", "noun", "verb", "adverb", "place", "emotion"]
            }
        }
    },

    # =========================
    # LEVEL 3 – ADVANCED
    # =========================
    3: {
        "name": "Advanced",
        "themes": {
            "Fantasy": {
                "templates": [
                    "In the enchanted {place}, a {adjective} {noun} {verb} {adverb} with a {object}, feeling {emotion}.",
                    "Holding a {object}, the {adjective} {noun} felt {emotion} as they began to {verb} {adverb}.",
                    "A {adjective} {noun}, feeling {emotion}, carried a {object} while trying to {verb} {adverb} in the {place}."
                ],
                "words": ["adjective", "noun", "verb", "adverb", "place", "emotion", "object"]
            },

            "Adventure": {
                "templates": [
                    "With a {object} in hand, the {adjective} {noun} {verb} {adverb} through the {place}, feeling {emotion}.",
                    "The {adjective} {noun} carried a {object} and decided to {verb} {adverb} in the {place}.",
                    "Feeling {emotion}, a {adjective} {noun} prepared a {object} before going to the {place} to {verb}."
                ],
                "words": ["adjective", "noun", "verb", "adverb", "place", "emotion", "object"]
            }
        }
    }
}

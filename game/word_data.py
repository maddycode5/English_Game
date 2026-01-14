WORD_TYPES = {
    "adjective": {
        "definition": "Describes a noun",
        "example": "happy, brave"
    },
    "noun": {
        "definition": "Name of person, place or thing",
        "example": "boy, city"
    },
    "verb": {
        "definition": "Action word",
        "example": "run, explore"
    },
    "adverb": {
        "definition": "Describes a verb",
        "example": "quickly, silently"
    },
    "place": {
        "definition": "Location",
        "example": "school, forest"
    },
    "emotion": {
        "definition": "Feeling",
        "example": "excited, nervous"
    }
}

LEVELS = {
    1: {
        "name": "Beginner",
        "themes": {
            "Adventure": {
                "templates": [
                    "A {adjective} {noun} decided to {verb} in the {place}."
                ],
                "words": ["adjective", "noun", "verb", "place"]
            }
        }
    }
}

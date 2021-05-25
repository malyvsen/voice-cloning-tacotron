mapping = {
    "a": "aa",
    "ɑ": "aa",
    "aj": "igh",
    "ɔ̃": "aw",
    "t͡s": "ts",
    "t͡ɕ": "tch",
    "t͡ʂ": "tch",
    "d͡ʐ": "j",
    "d͡ʑ": "j",
    "ɛ": "e",
    **{f"ɛ{symbol}": f"u{symbol}" for symbol in [" ", ",", ".", "?", "!"]},
    **{f"ɛ̃{symbol}": f"em{symbol}" for symbol in ["", " ", ",", ".", "?", "!"]},
    "ə": "e",
    "g": "gg",
    "x": "h",
    "i": "ee",
    "j": "y",
    "ʲ": "y",
    "ɲ": "n",
    "ŋ": "n",
    "ɔ": "o",
    "ʁ": "r",
    "ʂ": "sh",
    "ɕ": "sh",
    "u": "oo",
    "ʋ": "v",
    "y": "i",
    "ɨ": "i",
    "ʑ": "sh",
    "ʐ": "sh",
    "ː": "",
}

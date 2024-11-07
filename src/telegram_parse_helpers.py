import json
import numpy
from wordcloud import WordCloud, STOPWORDS
from constants import FORBIDDEN_CHAR
from constants import ParserSortWords


def parse_json_chat(json_data: dict,
                    min_word_size: int = 0,
                    sorting: ParserSortWords = ParserSortWords.DESCENDING) -> list[tuple[str, int]]:
    """
    This function is used to parse JSON chat and return a list with tuples.
    Every tuple contain a string with a word plus its frequency.
    :param json_data: JSON chat loaded in Python. Please use json.loads() before this function.
    :param min_word_size: You can pop too short words right at the moment of parsing if you want.
    :param sorting: How to sort words -- from most used to least or vice-versa
    :return: List of tuple pairs ("word": str, frequency: int).
    """

    words_stat: dict[str, int] = {}

    for message in json_data["messages"]:  # Parse thru all messages
        # Omit empty messages and nested messages (like links etc.)
        if (type(message["text"]) is not list) and (message["text"] != ""):
            # Split messages by whitespaces.
            for word in message["text"].split(" "):
                # Replace all forbidden characters.
                # TODO see TODO in FORBIDDEN_CHAR variable. Fix it.
                for char in FORBIDDEN_CHAR:
                    word = word.replace(char, "")
                # Create new dict. entry or add frequency to it.
                if word not in words_stat:
                    words_stat[word] = 1
                else:
                    words_stat[word] += 1

    # Sort words in DESC or ASC order
    should_reverse: bool = False
    if sorting == ParserSortWords.DESCENDING:
        should_reverse = True

    words_list_clean: list[tuple[str, int]] = sorted(words_stat.items(), key=lambda x: x[1], reverse=should_reverse)

    # Original dictionary is not needed anymore
    del words_stat

    # TODO STILL SUCKS HARD but a bit better now. Still needs rework.
    # Evil hack to remove too short words. Prob could be optimized
    list_words_to_remove: list = []
    # First create a list with words to remove
    for word in words_list_clean:
        if len(word[0]) < min_word_size:
            list_words_to_remove.append(word)

    # Then remove those words
    for i in range(0, len(list_words_to_remove)):
        words_list_clean.remove(list_words_to_remove[i])

    return words_list_clean

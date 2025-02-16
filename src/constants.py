import enum

# This should be upgraded in the future.
# For example, I can't add '-' since it can be inside of a word.
# TODO Please fix the algorithm in newer versions
FORBIDDEN_CHAR: list[str] = [',', '.', '(', ')', '\n', '\'', '"', "*", '%', '&', '?', "!", "…"]


class ParserSortWords(enum.Enum):
    ASCENDING = 1,   # From least to most used
    DESCENDING = 0,  # From most to least used

# Make sure it corresponds to orders of checkbox in ModalFileOpenDialog
class FileParsingMode(enum.IntEnum):
    JSON = 0,
    PLAIN_TXT = 1,

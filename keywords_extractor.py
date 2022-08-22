import re
from dataclasses import dataclass

@dataclass
class KeywordsExtractor:
    regex: str

    def __extract_regex(self, string):
        matched = re.match(self.regex, string)
        return matched.group(1)

    def extract_zip(self, string):
        if string:
            try:
                return self.__extract_regex(string)
            except AttributeError as e:
                return None
        else:
            return None

class String:
    def __init__(self, characters):
        self.characters = str(characters)

    def _is_empty(self):
        return len(self.characters) == 0

    def _is_not_equal_pair(self, string1, string2):
        return len(string1) != len(string2)

    def is_palindrome(self):
        if self._is_empty():
            return False

        size = len(self.characters) - 1
        for i in range(size // 2):
            if self.characters[i] != self.characters[-(i + 1)]:
                return False

        return True

    def is_anagram1(self, string1, string2):
        if self._is_not_equal_pair(string1, string2):
            return False
        difference = set(string1).symmetric_difference(set(string2))
        is_not_anagram = len(difference) > 0
        return False if is_not_anagram else True

    def is_anagram2(self, string1, string2):
        difference = dict()

        if self._is_not_equal_pair(string1, string2):
            return False

        for char1 in string1:
            if difference.get(char1):
                difference[char1] += 1
            else:
                difference[char1] = 1

        for char2 in string2:
            if difference.get(char2):
                difference[char2] -= 1

        is_not_anagram = sum(difference.values()) > 0

        return False if is_not_anagram else True


st = String("racecar")
# print("Is Empty String: ", st.is_empty())
print("Is Palindrome String: ", st.is_palindrome())
print("Is Anagram Strings: ", st.is_anagram2("fatan", "fanta"))

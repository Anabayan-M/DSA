class Solution(object):
    def findWords(self, words):
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]

        result = []

        for word in words:
            word_set = set(word.lower())

            for row in rows:
                if word_set.issubset(row):
                    result.append(word)
                    break

        return result
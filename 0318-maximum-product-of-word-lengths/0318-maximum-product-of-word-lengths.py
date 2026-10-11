class Solution(object):
    def maxProduct(self, words):
        maximum = 0
        masks = []
        for word in words:
            mask = 0

            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))

            masks.append(mask)
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if masks[i] & masks[j] == 0:
                    product = len(words[i]) * len(words[j])
                    maximum = max(maximum, product)
        return maximum
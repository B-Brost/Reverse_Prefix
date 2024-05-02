class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        word = list(word)
        for i in range(len(word)):
            if word[i] == ch:
                word[:i+1] = word[:i+1][::-1]
                break
        return ''.join(word)

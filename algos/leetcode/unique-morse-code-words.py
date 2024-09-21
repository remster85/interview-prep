#https://leetcode.com/problems/unique-morse-code-words/
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabetInMorse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        transformations = set()
        for word in words:
            wordInMorse = ""
            for c in word:
                wordInMorse += alphabetInMorse[ord(c)-ord('a')]
            transformations.add(wordInMorse)
        return len(transformations) 

        
# your code goes here!
class Anagram:
  def __init__(self, word):
    self.word = word.lower()  

  def is_anagram(self, word):
    other_word = word.lower()  
    return sorted(self.word) == sorted(other_word)

  def match(self, words):
    anagrams = []
    for word in words:
      if self.is_anagram(word) and word != self.word:  
        anagrams.append(word)
    return anagrams


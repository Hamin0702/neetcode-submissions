class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list) #{}

        for word in strs:
            char_freq = [0] * 26

            for char in word:
                char_freq[ord(char) - ord('a')] += 1

            tuple_key = tuple(char_freq)
            anagrams[tuple_key].append(word)
            
            # only if setting anagrams = {}, using defaultlist(list) makes an empty list
            # if tuple_key not in anagrams:
            #     anagrams[tuple_key] = [word]
            # else:
            #     anagrams[tuple_key].append(word)


        return list(anagrams.values())
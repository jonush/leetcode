"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.
"""

import string

def uniqueMorseRepresentations(words) -> int:
        """
        given a list of words:
        - transform each word into its morse code representation
        - return the number of different transformations
        """
        
        alphabet = list(string.ascii_lowercase)
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        # create a dictionary "letters"& store all morse code letter representations
        letters = dict(zip(alphabet, morse))
        
        # create another dictionary morse_words
        morse_words = {}
        
        # transform each word into its morse code representation
        for w in words:
            code = ""
            for i in w:
                code += letters[i]
            
            # store that into another dictionary "morse_words"
            if code not in morse_words:
                morse_words[code] = 0
                
        # return the number of keys in "morse_words"
        return len(morse_words.keys())

test_case = ["gin", "zen", "gig", "msg"]
uniqueMorseRepresentations(test_case)

"""
TIME & SPACE COMPLEXITY

TIME: O(n²)

Utilizes two dictionaries for O(1) searching, but there is the nested for loops used to create the morse code representation of a full word, leading to a O(n²) run time. Could possibly be refactored to improve runtime by splitting up operations inside the nested for loops.

SPACE: O(n)

Utilizes two dictionaries: one to store the alphabet and morse code, and the other to store the morse code representation of a whole word. The alphabet/morse code dictionary is always a set length, but the morse code representation of a whole word will depend on the length of the parameter "words" list.
"""
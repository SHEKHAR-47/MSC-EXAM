# Aim: Write a program to Implement a tri-gram model.

# Background Information:
# N-gram: N-grams are contiguous sequences of items that are collected from a
# sequence of text or speech corpus or almost any type of data. The n in n-grams
# specify the size of number of items to consider, unigram for n =1, bigram for n
# = 2, and trigram for n = 3, and so on.

Code:
import nltk
from nltk.util import ngrams
text = &quot;The flame that burns Twice as bright burns half as long&quot;
words = nltk.word_tokenize(text)
trigrams = ngrams(words, 3)
for trigram in trigrams:
print(trigram)

# Output:
# (&#39;The&#39;, &#39;flame&#39;, &#39;that&#39;)
# (&#39;flame&#39;, &#39;that&#39;, &#39;burns&#39;)
# (&#39;that&#39;, &#39;burns&#39;, &#39;Twice&#39;)
# (&#39;burns&#39;, &#39;Twice&#39;, &#39;as&#39;)
# (&#39;Twice&#39;, &#39;as&#39;, &#39;bright&#39;)
# (&#39;as&#39;, &#39;bright&#39;, &#39;burns&#39;)
# (&#39;bright&#39;, &#39;burns&#39;, &#39;half&#39;)
# (&#39;burns&#39;, &#39;half&#39;, &#39;as&#39;)
# (&#39;half&#39;, &#39;as&#39;, &#39;long&#39;)
  
# Conclusion: Thus, we have successfully a tri-gram model.

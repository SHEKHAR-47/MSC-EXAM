#Write a program to implement sentence segmentation and word tokenization.

# Background Information:
# Sentence Segmentation: Sentence tokenization (also called sentence
# segmentation) is the problem of dividing a string of written language into its
# component sentences.

# Word Tokenization: Tokenization is used in natural language processing to
# split paragraphs and sentences into smaller units that can be more easily
# assigned meaning.

#code :
import nltk
import spacy
nlp = spacy.load(&quot;en_core_web_sm&quot;)
# sentence segmentation (part 1)
doc = nlp(u&quot;I Love Coding. Geeks for Geeks helped me in this regard very
much. I Love Geeks
for Geeks.&quot;)
for sent in doc.sents:
print(sent)
# word Tokenization (part 2)
text = &quot;A good traveler has no fixed plans and is not intent on arriving&quot;
sentences = nltk.sent_tokenize(text)
for sentence in sentences:
words = nltk.word_tokenize(sentence) print(words)

# Output:
# I Love Coding.
# Geeks for Geeks helped me in this regard very much.
# I Love Geeks for Geeks.

# Conclusion: Thus, we have successfully implemented sentence segmentation
# and word
# tokenization.




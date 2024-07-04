# Aim: Write a program to Implement dependency parsing of a given text.

# Background Information:
# Dependency Parsing: The term Dependency Parsing (DP) refers to the process
# of examining the dependencies between the phrases of a sentence in order to
# determine its grammatical structure. A sentence is divided into many sections
# based mostly on this. The process is based on the assumption that there is a
# direct relationship between each linguistic unit in a sentence. These
# hyperlinks are called dependencies.
  
Code:
import spacy
nlp = spacy.load(&quot;en_core_web_sm&quot;) #nlp model
text = &quot;John likes Mary because she is beautiful.&quot;
doc = nlp(text)
for token in doc:
print(token.text, token.dep_, token.head.text, token.head.pos_,[child for child
in token.children])


# Output:
# John nsubj likes VERB []
# likes ROOT likes VERB [John, Mary, is, .]
# Mary dobj likes VERB []
# because mark is AUX []
# she nsubj is AUX []
# is advcl likes VERB [because, she, beautiful]
# beautiful acomp is AUX []
# . punct likes VERB []

# Conclusion: Thus, we have successfully implemented Implement dependency
# parsing of a given text.

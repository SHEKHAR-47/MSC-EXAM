# Aim: Write a program to Implement Named Entity Recognition (NER).

# Background Information:
# Named Entity Recognition: The named entity recognition (NER) is one of the
# most popular data preprocessing task. It involves the identification of key
# information in the text and classification into a set of predefined categories. An
# entity is basically the thing that is consistentlytalked about or refer to in the text.
# Some of the categories that are the most important architecture in NER such
# that:
# Person
# Organization
# Place/ location

# Code:
import spacy
nlp = spacy.load(&quot;en_core_web_sm&quot;)
text = &quot;Nitin is studying at Indian Institute of technology Bombay.&quot;
doc = nlp(text)
for entity in doc.ents:
print(entity.label_, entity.text)

# Output:
# PERSON Nitin
# ORG Indian Institute of technology
# GPE Bombay

# Conclusion: Thus, we have successfully implemented Named Entity
# Recognition (NER)

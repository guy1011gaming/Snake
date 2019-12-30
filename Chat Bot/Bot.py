from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ['hi %1']],
    ['how are you', ['good']]
]

chat = Chat(pairs, reflections)
chat.converse()
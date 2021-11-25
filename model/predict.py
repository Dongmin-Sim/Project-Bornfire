from .model import new_model
from .tokenizer import tokenizer, stopwords, okt
from tensorflow.keras.preprocessing.sequence import pad_sequences


def get_sentiment(sen):
    sen = okt.morphs(sen, stem=True)
    sen = [word for word in sen if word not in stopwords]
    encoded = tokenizer.texts_to_sequences([sen])       # label encoding
    padded = pad_sequences(encoded, maxlen=len(sen))       # padding
    # print(padded)
    score = float(new_model.predict(padded))
    if score >= 0.4:
        return (score, 1)
    else:
        return (score, -1)

sen = '좆같은 하루네 이거 못하겠네'
predicted = get_sentiment(sen)
print(predicted)

sen = '좋은 하루에요 다들 희망찬 하루되세요~~~!!'
predicted = get_sentiment(sen)
print(predicted)

sen = '오늘 너무 힘드네요 조금 너무 졸려요 배가 고파요'
predicted = get_sentiment(sen)
print(predicted)


from konlpy.tag import Okt      
from tensorflow.keras.preprocessing.text import Tokenizer   
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Embedding, Dense, LSTM, Bidirectional


okt = Okt()
tokenizer = Tokenizer()

stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다','이', '있', '하', '것', '들', '그',\
     '되', '수', '이', '보', '않', '없', '나', '사람', '주', '아니', '등', '같', '우리', '때', '년', '가', '한', '지', '대하', '오', '말', '일',\
          '그렇', '위하', '인해']
          
stopwords = list(set(stopwords))

padding_len = 200

emb_dim = 100
cur_dim = 26663     # vocab size
padding_len = 35

model = Sequential([
    Embedding(cur_dim, emb_dim, input_length=padding_len),      
    Bidirectional(LSTM(128, return_sequences=True)),
    LSTM(32),
    Dense(1, activation='sigmoid')
])

load_model = model.load_weights('static/assets/model/lstm_model.h5')

def get_sentiment(loaded_model, sen):
    sen = okt.morphs(sen, stem=True)
    sen = [word for word in sen if word not in stopwords]
    encoded = tokenizer.texts_to_sequences([sen])       # label encoding
    padded = pad_sequences(encoded, maxlen=padding_len)       # padding
    # print(padded)
    score = float(loaded_model.predict(padded))
    if score >= 0.65:
        return 1
    else:
        return -1


sen = '안녕하세요'
predicted = get_sentiment(load_model, sen)

print(predicted)


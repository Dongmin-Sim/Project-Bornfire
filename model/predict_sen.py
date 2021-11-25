from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, LSTM, Bidirectional
import pickle
from konlpy.tag import Okt
import re

# 형태소 분석기
okt = Okt()
# 불용어
stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다','이', '있', '하', '것', '들', '그',\
     '되', '수', '이', '보', '않', '없', '나', '사람', '주', '아니', '등', '같', '우리', '때', '년', '가', '한', '지', '대하', '오', '말', '일',\
          '그렇', '위하', '인해']

# loading
with open('model/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

padding_len = 30

emb_dim = 100
cur_dim = 26663     # vocab size
new_model = Sequential([
    Embedding(cur_dim, emb_dim, input_length=padding_len),      
    Bidirectional(LSTM(128, return_sequences=True)),
    LSTM(32),
    Dense(1, activation='sigmoid')
])


new_model.load_weights('static/assets/model/lstm_model.h5')
print('모델 로드 완료')

def get_sentiment(sen):
    sen = re.sub("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "", sen)
    sen = re.sub('^ +', "", sen)
    sen = okt.morphs(sen, stem=True)
    sen = [word for word in sen if word not in stopwords]
    encoded = tokenizer.texts_to_sequences([sen])
    padded = pad_sequences(encoded, maxlen=padding_len)
    # print(padded)
    score = float(new_model.predict(padded))
    if score >= 0.6:
        return (score, 1)
    else:
        return (score, 0)


from konlpy.tag import Okt      
from tensorflow.keras.preprocessing.text import Tokenizer   
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, LSTM, Bidirectional
from tqdm import tqdm
import pandas as pd


document = pd.read_csv('static/assets/model/document.csv')
print(document.head())
okt = Okt()
tokenizer =  Tokenizer()

stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다','이', '있', '하', '것', '들', '그',\
     '되', '수', '이', '보', '않', '없', '나', '사람', '주', '아니', '등', '같', '우리', '때', '년', '가', '한', '지', '대하', '오', '말', '일',\
          '그렇', '위하', '인해']
stopwords = list(set(stopwords))

x_train = []
for sentence in tqdm(document['document']):
    tokenized_sent = okt.morphs(sentence, stem=True)      # 형태소 별로 문장 분할
    tokenized_sent = [word for word in tokenized_sent if word not in stopwords]   # 불용어 제거
    x_train.append(tokenized_sent)


# 단어사전 생성
tokenizer.fit_on_texts(x_train)

print('tokenizer 생성 완료')

emb_dim = 100
cur_dim = 26663     # vocab size
padding_len = 35

new_model = Sequential([
    Embedding(cur_dim, emb_dim, input_length=padding_len),      
    Bidirectional(LSTM(128, return_sequences=True)),
    LSTM(32),
    Dense(1, activation='sigmoid')
])

new_model.load_weights('static/assets/model/lstm_model.h5')
print('모델 로드 완료')


def get_sentiment(sen):
    sen = okt.morphs(sen, stem=True)
    sen = [word for word in sen if word not in stopwords]
    encoded = tokenizer.texts_to_sequences([sen])       # label encoding
    padded = pad_sequences(encoded, maxlen=padding_len)       # padding
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
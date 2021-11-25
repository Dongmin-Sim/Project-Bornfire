from konlpy.tag import Okt      
from tensorflow.keras.preprocessing.text import Tokenizer   
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, LSTM, Bidirectional
from tqdm import tqdm
import pandas as pd
import pickle


document = pd.read_csv('static/assets/model/document.csv')
print(document.head())
print(document.shape)

okt = Okt()
tokenizer =  Tokenizer()

stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다','이', '있', '하', '것', '들', '그',\
     '되', '수', '이', '보', '않', '없', '나', '사람', '주', '아니', '등', '같', '우리', '때', '년', '가', '한', '지', '대하', '오', '말', '일',\
          '그렇', '위하', '인해']

x_train = []
for sentence in tqdm(document['document']):
    tokenized_sent = okt.morphs(sentence, stem=True)      # 형태소 별로 문장 분할
    tokenized_sent = [word for word in tokenized_sent if word not in stopwords]   # 불용어 제거
    x_train.append(tokenized_sent)


# 단어사전 생성
tokenizer.fit_on_texts(x_train)

# tokernizer 저장
import pickle

# saving
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

print('tokenizer 생성 완료')

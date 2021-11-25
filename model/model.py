from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, LSTM, Bidirectional

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


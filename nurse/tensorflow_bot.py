#Simple chat bot with tensorflow/keras
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Ebedding, LSTM, Dense

model = Sequential([
    Ebedding(input_dim=vocab_size, output_dim==embedding_dim, input_length=max_length),
    LSTM(units=100)
    Dense(units=vocab_size, activation='softmax')
])

model.compile(optimize='adam', loss='categorical_crossentropy', metrics=['acurracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32)

def generate_bot_reponse(user_message):

    return bot_response
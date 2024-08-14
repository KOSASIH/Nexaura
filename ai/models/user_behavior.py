import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout

class UserBehaviorModel:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = pd.read_csv(self.data_path)
        self.X = self.data.drop(['user_id', 'label'], axis=1)
        self.y = self.data['label']
        self.scaler = StandardScaler()
        self.X_scaled = self.scaler.fit_transform(self.X)

    def train_random_forest(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X_scaled, self.y, test_size=0.2, random_state=42)
        rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
        rf_model.fit(X_train, y_train)
        y_pred = rf_model.predict(X_test)
        print("Random Forest Accuracy:", accuracy_score(y_test, y_pred))
        print("Random Forest Classification Report:")
        print(classification_report(y_test, y_pred))

    def train_lstm(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X_scaled, self.y, test_size=0.2, random_state=42)
        lstm_model = Sequential()
        lstm_model.add(LSTM(units=50, return_sequences=True, input_shape=(self.X_scaled.shape[1], 1)))
        lstm_model.add(Dropout(0.2))
        lstm_model.add(LSTM(units=50, return_sequences=False))
        lstm_model.add(Dropout(0.2))
        lstm_model.add(Dense(1, activation='sigmoid'))
        lstm_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        lstm_model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))
        y_pred = lstm_model.predict(X_test)
        print("LSTM Accuracy:", accuracy_score(y_test, np.round(y_pred)))
        print("LSTM Classification Report:")
        print(classification_report(y_test, np.round(y_pred)))

if __name__ == "__main__":
    data_path = 'user_behavior_data.csv'
    model = UserBehaviorModel(data_path)
    model.train_random_forest()
    model.train_lstm()

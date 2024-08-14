import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout

class TransactionPatternsModel:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = pd.read_csv(self.data_path)
        self.X = self.data.drop(['transaction_id', 'label'], axis=1)
        self.y = self.data['label']
        self.scaler = MinMaxScaler()
        self.X_scaled = self.scaler.fit_transform(self.X)

    def train_kmeans(self):
        kmeans_model = KMeans(n_clusters=5, random_state=42)
        kmeans_model.fit(self.X_scaled)
        print("K-Means Clustering Report:")
        print(kmeans_model.labels_)

    def train_pca(self):
        pca_model = PCA(n_components=0.95)
        pca_model.fit(self.X_scaled)
        print("PCA Explained Variance Ratio:", pca_model.explained_variance_ratio_)
        print("PCA Components:", pca_model.components_)

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

    def anomaly_detection(self):
        from sklearn.svm import OneClassSVM
        ocsvm_model = OneClassSVM(kernel='rbf', gamma=0.1, nu=0.1)
        ocsvm_model.fit(self.X_scaled)
        y_pred = ocsvm_model.predict(self.X_scaled)
        print("Anomaly Detection Report:")
        print("Number of anomalies:", np.sum(y_pred == -1))

if __name__ == "__main__":
    data_path = 'transaction_patterns_data.csv'
    model = TransactionPatternsModel(data_path)
    model.train_kmeans()
    model.train_pca()
    model.train_lstm()
    model.anomaly_detection()

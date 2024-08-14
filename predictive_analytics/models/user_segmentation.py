import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

class UserSegmentation:
    def __init__(self, data):
        self.data = data

    def preprocess_data(self):
        scaler = StandardScaler()
        self.data[['feature1', 'feature2', 'feature3']] = scaler.fit_transform(self.data[['feature1', 'feature2', 'feature3']])
        pca = PCA(n_components=2)
        self.data[['pca1', 'pca2']] = pca.fit_transform(self.data[['feature1', 'feature2', 'feature3']])

    def cluster_users(self, n_clusters):
        kmeans = KMeans(n_clusters=n_clusters)
        self.data['cluster'] = kmeans.fit_predict(self.data[['pca1', 'pca2']])

    def get_segmentation_results(self):
        return self.data.groupby('cluster').agg({'feature1': 'mean', 'feature2': 'mean', 'feature3': 'mean'})

# Example usage:
data = pd.read_csv('user_data.csv')
user_segmentation = UserSegmentation(data)
user_segmentation.preprocess_data()
user_segmentation.cluster_users(n_clusters=5)
print(user_segmentation.get_segmentation_results())

# mod.py
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.mixture import GaussianMixture
import pandas as pd
from sklearn.cluster import AgglomerativeClustering


def preprocess(df, k, n_clusters):
    """
    Przetwarzanie danych dotyczących składników.

    :param df: DataFrame z danymi.
    :param ingredients_df: DataFrame z danymi składników (zawierającymi odpowiednie kolumny).
    :param n_clusters: Liczba klastrów do użycia w klasteryzacji K-means.
    :return: DataFrame z przypisanymi klastrami i wynikami PCA.
    """
    # przygotowanie danych
    columns = k.columns[0:]
    # wybieram kolumny, które są w columns
    X_ingredients = df[columns]
    n_cluster = n_clusters
    # standaryzacja
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_ingredients)

    # klasteryzacja k-means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df["cluster"] = kmeans.fit_predict(X_scaled)

    # Redukcja wymiarów za pomocą PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    pca_df = pd.DataFrame(data=X_pca, columns=["PCA1", "PCA2"])
    pca_df["cluster"] = df["cluster"]

    return pca_df, n_cluster


def gmm_clustering(df, k, n_clusters):
    """
    Przetwarzanie danych za pomocą Gaussian Mixture Model.

    :param df: DataFrame z danymi.
    :param k: DataFrame z kolumnami, które mają być użyte do klasteryzacji.
    :param n_clusters: Liczba klastrów do użycia w Gaussian Mixture Model.
    :return: DataFrame z przypisanymi klastrami i wynikami PCA.
    """
    columns = k.columns[0:]
    X_ingredients = df[columns]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_ingredients)

    # Klasteryzacja Gaussian Mixture Model
    gmm = GaussianMixture(n_components=n_clusters, random_state=42)
    df["cluster_gmm"] = gmm.fit_predict(X_scaled)

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    pca_df = pd.DataFrame(data=X_pca, columns=["PCA1", "PCA2"])
    pca_df["cluster_gmm"] = df["cluster_gmm"]

    return pca_df, n_clusters

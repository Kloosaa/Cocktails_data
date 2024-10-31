from processing import clean_data, load_data
from model import preprocess, gmm_clustering


# Wczytanie i oczyszczenie danych
df = load_data("cocktail_dataset.json")
df, ingredients_df = clean_data(df)

# k-means
pca_df_ing = preprocess(df, ingredients_df, 3)

# Gaussian Mixture Model
n_clusters = 3
pca_df_gmm, _ = gmm_clustering(df, ingredients_df, n_clusters)

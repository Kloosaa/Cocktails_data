import pandas as pd


def load_data(filepath):
    """
    Wczytuje dane z pliku JSON do DataFrame.

    Parameters:
    filepath : Ścieżka do pliku JSON z danymi.

    Returns:
    pd.DataFrame: Wczytany DataFrame z surowymi danymi.
    """
    df = pd.read_json(filepath)
    return df


def remove_unnecessary_columns(df):
    """
    Usuwa niepotrzebne kolumny z DataFrame.

    Parameters:
    df : DataFrame zawierający wszystkie kolumny

    Returns:
    pd.DataFrame: DataFrame bez kolumn ["tags", "alcoholic", "createdAt", "updatedAt", "imageUrl", "instructions", "ingredients"].
    """

    return df.drop(
        [
            "ingredients",
            "tags",
            "instructions",
            "imageUrl",
            "alcoholic",
            "createdAt",
            "updatedAt",
            "name",
        ],
        axis=1,
        errors="ignore",
    )


def add_num_ingredients_column(df):
    """
    Dodaje kolumnę z liczbą składników dla każdego wpisu.

    Parameters:
    df : DataFrame zawierający kolumnę "ingredients" z listą składników.

    Returns:
    pd.DataFrame: DataFrame z nową kolumną "num_ingredients" zawierającą liczbę składników.
    """
    df["num_ingredients"] = df["ingredients"].apply(len)
    return df


def extract_ingredient_columns(df):
    """
    Przekształca składniki na kolumny binarne, gdzie 1 oznacza obecność składnika w danym wpisie, a 0 jego brak.

    Parameters:
    df : DataFrame zawierający kolumnę "ingredients", w której każdy wpis to lista składników.

    Returns:
    pd.DataFrame: DataFrame zawierający kolumny binarne dla każdego unikalnego składnika.
    """
    # zbiór unikalnych składników z listy składników df
    all_ingredients = set(
        ing["name"]
        for ingredients_list in df["ingredients"]
        for ing in ingredients_list
    )
    # stworzenie df z kolumnami składników
    ingredients_df = pd.DataFrame(
        {
            ingredient: df["ingredients"].apply(
                lambda x: 1 if any(ing["name"] == ingredient for ing in x) else 0
            )
            for ingredient in all_ingredients
        }
    )
    return ingredients_df


def extract_category_and_glass_columns(df):
    """
    Tworzy kolumny binarne dla każdej kategorii i typu szkła, gdzie 1 oznacza wystąpienie danej kategorii/szkła w wpisie.

    Parameters:
    df : DataFrame zawierający kolumny "category" oraz "glass".

    Returns:
    Tuple[pd.DataFrame, pd.DataFrame]: Dwa DataFrame zawierające kolumny binarne:
                                        - pierwszy dla unikalnych typów szkła,
                                        - drugi dla unikalnych kategorii.
    """

    # stworzenie df dla szklanek
    glasses_df = pd.DataFrame(
        {
            glass: df["glass"].apply(lambda x: 1 if x == glass else 0)
            for glass in df["glass"].unique()
        }
    )
    # df dla kategorii
    categories_df = pd.DataFrame(
        {
            category: df["category"].apply(lambda x: 1 if x == category else 0)
            for category in df["category"].unique()
        }
    )
    return glasses_df, categories_df


def combine_dataframes(df, glasses_df, categories_df, ingredients_df):
    """
    Łączy główny DataFrame z DataFrame zawierającymi informacje o składnikach, szkle i kategorii.

    Parameters:
    df : Główny DataFrame zawierający podstawowe dane o wpisach.
    glasses_df : DataFrame z kolumnami binarnymi dla typów szkła.
    categories_df : DataFrame z kolumnami binarnymi dla kategorii.
    ingredients_df : DataFrame z kolumnami binarnymi dla składników.

    Returns:
    pd.DataFrame: Połączony DataFrame zawierający wszystkie informacje o każdym wpisie.
    """
    return pd.concat([df, glasses_df, categories_df, ingredients_df], axis=1)


def clean_data(df):
    """
    Wykonuje pełne czyszczenie danych: dodaje kolumnę "num_ingredients", tworzy kolumny binarne
    dla składników, typów szkła oraz kategorii, usuwa zbędne kolumny.

    Parameters:
    df : Główny DataFrame zawierający surowe dane z pliku JSON.

    Returns:
    Tuple[pd.DataFrame, pd.DataFrame]:
        - Pierwszy element to wyczyszczony i rozszerzony DataFrame z wszystkimi danymi.
        - Drugi element to DataFrame zawierający wyłącznie kolumny składników w formacie binarnym.
    """
    df = add_num_ingredients_column(df)

    ingredients_df = extract_ingredient_columns(df)
    glasses_df, categories_df = extract_category_and_glass_columns(df)

    df = combine_dataframes(df, glasses_df, categories_df, ingredients_df)

    df = remove_unnecessary_columns(df)
    return df, ingredients_df

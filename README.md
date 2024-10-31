# Cocktails_data

#Projekt eksploracyjnej analizy danych oraz klasteryzacji

#Opis projektu
Projekt ma na celu analizę i klasteryzację danych dotyczących napojów. Wykorzystuje różne kroki przetwarzania danych, takie jak standaryzacja, redukcja wymiarów oraz klasteryzacja algorytmem K-means i
Gaussian Mixture Model, aby pogrupować napoje na podstawie składników i innych cech.

#Pliki w projekcie
main.py - Skrypt główny, w którym używa się funkcji do czyszczenia danych i klasteryzacji.
model.py - Moduł zawierający funkcje klasteryzacji i standaryzacji danych.
processing.py - Moduł przetwarzający dane; zawiera funkcje do wczytywania, czyszczenia i przygotowania danych do analizy.
wiz.ipynb - Moduł, w którym pokolei oczyszczane są dane i tłumaczone dlaczego tak a nie inaczej. Zawiera też wizualizacje wyników

#Struktura
Dane: Projekt wykorzystuje dane napojów, które są przetwarzane w celu ekstrakcji składników i innych atrybutów.
Przetwarzanie danych: Skrypt wczytuje dane z pliku JSON, usuwa niepotrzebne kolumny i zamienia składniki na kolumny binarne tzw. one-hot encoding.
Klasteryzacja i Wizualizacja: Klasteryzacja algorytmem K-means jest zastosowana na znormalizowanych danych. Wyniki są prezentowane na wykresach.

#Wymagania
Python 3.8 lub nowszy
Biblioteki:
pandas
scikit-learn
matplotlib
seaborn
notatnik jupyter

#Instalacja
Aby uruchomić projekt, zainstaluj wymagane pakiety, uruchamiając poniższe polecenie w terminalu:

pip install pandas scikit-learn matplotlib seaborn notebook


#Instrukcja Użycia
pliki powinny znajdować sie w jednym folderze
1.Wczytywanie i Przetwarzanie Danych
W processing.py znajdują się funkcje do przetwarzania danych:
Clean_data - odpowiada za pełne przygotowanie danych do analizy. Wykonuje następujące operacje:
Dodanie kolumny num_ingredients - zawiera liczbę składników w każdym drinku.
Tworzenie kolumn binarnych - przekształca składniki, typy szkła oraz kategorie na format binarny (1/0), gdzie 1 oznacza obecność danego składnika, typu szkła lub kategorii.
Usuwanie zbędnych kolumn - usuwa niepotrzebne informacje, takie jak tags, instructions, imageUrl itd.

2.Klasteryzacja i Redukcja Wymiarów
W model.py znajduje się funkcja preprocess(df, ingredients_df, n_clusters), która:

Standaryzuje dane.
Klasteryzuje dane algorytmem K-means i Gaussian Mixture Model.
Redukuje dane do dwóch wymiarów za pomocą PCA.

3.Użycie i wizualizacja, użyć funkcji można w pliku main.py, wizualizacje przedstawiono w pliku wiz.ipynb

Aby powtórzyć wykonane czynności w uruchomionym pliky py lub ipynb na początku zaimportować potrzebne biblioteki a następnie używając from (nazwa modułu) import (nazwa funkcji), importować funkcje z modułów processing.py i model.py, wykonywać czyszczenie danych w kolejności jak w jupyterze, po wyczyszczeniu danych użyć funkcji z modułu model.py do przygotowania danych pod klasteryzację, argumentów które zwracają nam funkcje użyć do wykresów tworzonych w matplotlib i seaborn, wzory są w pliku wiz.ipynb



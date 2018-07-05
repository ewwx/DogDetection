# DogDetection
## Budowa modelu kaskadowego, przeznaczonego do detekcji. 
Celem projektu jest zbudowanie modelu dokonującego detekcji psów na obrazie, opierając się na metodzie Viola_Jonesa.

Projekt powstał na podstawie [instrucji](https://www.cs.auckland.ac.nz/~m.rezaei/Tutorials/Creating_a_Cascade_of_Haar-Like_Classifiers_Step_by_Step.pdf). Pliki \cadcade2xml oraz \training są pobrane z: [źródło](https://www.cs.auckland.ac.nz/~m.rezaei/Tutorials/Haar-Training.zip), którego autorem jest Mahdi Rezaei - m.rezaei@auckland.ac.nz from Department of Computer Science, the University of Auckland.

Baza zdjęć z której pobrano zdjęcia psów znajduje się [tutaj](https://drive.google.com/drive/folders/1XaFM8BJFligrqeQdE-_5Id0V_SubJAZe).

Cała procedura opiasana w pliku nie jest trudna, jednak największy problem stanowi opracowanie zdjęc. Każde zdjęcie musi zostać opisane w pliku tekstowym, aby możliwe było stworzenie wektora zawierającego obrazy poszukiwanych obiektów, w tym przypadku psów. Projekt na którym bazowano zawiera program specjanie stworzony do wyodrębninaia takich obiektórw  obrazu. Po zazanczeniu obszaru myszką i klkinięciu klawisza space do pliku dodane jest położenie prostokąta dla zaznaczonego obiektu. Po zatwierdzenia obrazu Enterem, otwiera się kolejny obraz. Dla każdego zdjęcia można zaznaczyć kilka obiektów w rożnych miejscach, każdy powinien być zatwierdzony klawiszem Space.
Wykonując procedurę opisaną w powyżej zamieszczonej instrukcji, otrzymujemy model z roszrzeniem xml gotowy do detekcji.

W folderach \cadcade2xml oraz \training  znajdują się wszystkie potrzebne programy do wykonania instrukcji. 

## Zastosowanie modelu do detekcji psów na filmie.
Wczytując stworzony poprzednio model xml do programu, używając następującej linii kodu:

```
dogCascade = cv2.CascadeClassifier('model.xml')
```

można dokonać detekcji obiektów zarówno przy użyciu kamery oraz wczytując nagrany film. 

Programy wykorzystane do detekcji znajdują się w folderze \code. 

Aby uruchomić program niezbędny jest Python 3.6 oraz bilioteka openCV, którą można pobrać używająć pip:

```
pip install opencv-python
```

## Ocena uzyskanej skuteczności detekcji.
Niestety na chwilę obecną nie udało się wykonać statystycznej oceny wyników. Obserwując jak przebiega detekcja na filmie, można uznać, że wynik nie jest dobry, gdyż model ma zbyt niski próg detekcji i wyszukuje zbyt wiele obektów. Może to być spowodawane złym doborem parametrów lub zbyt małą liczbą opisanych obrazów (do użytego modelu opisano ok. 400 zdjęć - dogdetector1.xml, 200 - dogdetector2.xml). Dodatkowo na niektórych zdjęciach wybierano całą sylwetkę psa, a w innych jedynie jego głowę, co mogło negatywnie wpłynąć na działanie modelu.  

## Dodatkowe pliki

W folderze \code zamieszczono rónież program konwertujący zdjęcia do formatu bmp. 

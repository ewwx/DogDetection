# DogDetection
## Budowa modelu kaskadowego, przeznaczonego do detekcji. 
Celem projektu jest zbudowanie modelu dokonującego detekcji psów na obrazie, opierając się na metodzie Viola_Jonesa.

Projekt powstał na podstawie [instrucji](https://www.cs.auckland.ac.nz/~m.rezaei/Tutorials/Creating_a_Cascade_of_Haar-Like_Classifiers_Step_by_Step.pdf).

Baza zdjęć z której pobrano zdjęcia psów znajduje się [tutaj](https://drive.google.com/drive/folders/1XaFM8BJFligrqeQdE-_5Id0V_SubJAZe).

Cała procedura opiasana w pliku nie jest trudna, jednak największy problem stanowi opracowanie zdjęc. Każde zdjęcie musi zostać opisane w pliku tekstowym, aby możliwe byo stworzenie wektora zawierajacego obrazy poszukiwanych obiektów, w tym przypadku psów. Projekt na którym bazowano zawiera program specjanie stworzony do wyodrębninaia takich obiektórw  obrazu. Po zazanczeniu obszaru myszką i klkinięciu klawisza space do pliku dodane jest położenie prostokąta dla zaznaczonego obiektu. Po zatwierdzenia obrazu Enterem, otwiera się kolejny obraz. Dla każdego zdjęcia można zaznaczyć kilka obiektów w rożnych miejscach, każdy powinien być zatwierdzony klawiszem Space. 

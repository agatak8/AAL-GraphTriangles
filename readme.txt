 Autor: Agata Kłoss 5-ISI 277310
 Problem: Dana jest lista n punktów w przestrzeni, każda para pktów ma przypisane 0 lub 1. Znaleźć liczbę trójek pktów z tą samą przypisaną liczbą.
 
 =====================================================================
 Polecenia aktywacji programu:
 =====================================================================
 
Program posiada trzy tryby o różnych poleceniach aktywacji.
Aby poznać ich opis należy uruchomić program/tryb z parametrem -h:

main.py -h - opis trybów
main.py stdio -h - opis trybu wejście/wyjście standardowe
main.py gen -h - opis trybu generacji
main.py test -h - opis trybu testowania

Uwaga - program został docelowo napisany pod Python w wersji 3.x, może nie działać poprawnie dla wersji 2.x

 =====================================================================
 Konwencje danych wejściowych i prezentacji wyników:
 =====================================================================
 
Dane grafu wejściowego są w następującym formacie:
N
v1 x y
...
vN x y
vi vj
...
va vz

gdzie N - liczba wierzchołków grafu
v1 - numer wierzchołka - int od 0 do N-1, x i y - współrzędne 2D - float
vi vj - numery dwóch wierzchołków - krawędź

Dane wyjściowe znalezionych trójek pktów są w następującym formacie:
vi vj vk
...
va vb vc
gdzie vj to numer wierzchołka


 =====================================================================
 Opis rozwiązania
 =====================================================================
 
Lista n pktów w przestrzeni z przypisaniem 0-1 parze pktów jest równoważna grafowi gdzie pkt to wierzchołek a krawędź między pktami istnieje, jeśli pkty mają przypisaną liczbę 1. Rozwiązanie polega na znalezieniu liczby trójkątów w tym grafie oraz w jego odwrotności.

Porównywane są 4 algorytmy znajdowania trójkątów w grafie:
- naiwny - sprawdzenie każdej trójki punktów
- macierzowy - tworzy macierz incydencji A i zwraca ślad(A**3)/6
- listowy - tworzy listę sąsiadów dla każdego wierzchołka, sprawdza pary punktów w listach
- wierzchołkowy - modyfikacja listowego - sortuje wierzchołki wg malejących stopni, usuwa wierzchołek po sprawdzeniu jego listy

Wykorzystane struktury danych:
naiwny - lista
macierzowy - macierz
listowy - zbiór (pozwala na szybsze sprawdzenie istnienia wierzchołka na liście incydencji)
wierzchołkowy - zbiór


 =====================================================================
 Pliki źródłowe
 =====================================================================
Program dzieli się na 3 główne części:

- algorytmiczna - folder algorithms
    solvers - algorytmy znajdowania trójkątów
    graph - reprezentacja grafu jako listy incydencji
    folder tests - testy jednostkowe sprawdzające poprawność algorytmów
    
- pomocnicza - folder helpers
    io - ładowanie/zapisywanie grafów/wyników do plików
    generator - generacja grafów losowych, pełnych, dwudzielnych itd.
    measure - pomiar czasu wykonania algorytmu
    
- ui - folder główny
    modes - realizacja trzech trybów działania programu
    main - główny interfejs, parser linii poleceń

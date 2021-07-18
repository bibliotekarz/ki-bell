# Projekt ki-bell

Skrypt w pythonie sprawdzający stan napięcia na pinach analogowych NodeMCU ESP8286 i w zależności od jego poziomu zwraca stronę www z aktualnymi wynikami.
Ten konkretny przykład monitoruje stan fotorezystora sprawdzającego czy w łazience jest włączone światło.

Układ wymaga stabilnego zasilacza, zwłaszcza przy długiej linii kablowej z fotorezystorem. W moim przypadku układ działał na pojedyńczej parze skrętki długości ponad 20 metrów. Stabilność oprócz zasilacza wynikała również z użytego modułu ESP, jedne miały notoryczne zawieszenia i wymagały resetu zasilaniem, inne działały miesiącami bezproblemowo. nie było korelacji między częstotliwością zawieszenia a źródłem pochodzenia (drogi renomowany sklep w polsce, o połowę tańsze z aliexpress)

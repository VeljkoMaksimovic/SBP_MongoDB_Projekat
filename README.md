# SBP_MongoDB_Projekat
Projekat iz predmeta Sistemi Baza Podataka, MongoDB baza sa upitima.

Baza sa podacima iz **Fantasy Premier League** igrice. Data set koji je koriscen: https://github.com/vaastav/Fantasy-Premier-League
Da bi python skripte za popunjavanje baza radile bez modifikacija potrebno je skinuti dataset sa linka i ubaciti folder u root directory ovog repozitorijuma.

U sklopu projekta je napravljeno vise razlicitih baza sa drugacijim semama nad kojim ce se izvrsavati isti upiti kako bi se na kraju uporedile performanse razlicitih pristupa. Svaka sema ce imati posebnu kolekciju za svaku sezonu, zato sto se ni jedan upit nece koristiti informacije iz razlicitih sezona.

**Prva verzija** baze ima poseban dokument za svaku kolo (*gw*)u sklopu kog se nalazi lista statistika svih igraca za to kolo, tako da cemo za prolazak i filtriranje igraca prvo morati da koristimo .unwind() kako bi od niza napravili zasebne dokumente. Velicina ove baze je **6.43 GB**

**Druga verzija** baze uopste nece imati entitet *gw* vec ce unutar kolekcije imati dokumente koji predstavljaju statistike igraca za odredjeno kolo, i svaki dokument ce imati polje *gw* gde ce se cuvati redni broj kola. **6.3 GB**

**Treca verzija** baze ima identicnu strukturu kao i druga, te koristi i iste upite, ali su dodati indeksi kako $sort i $match metode ne bi morale da prolaze kroz svih 20,000+ dokumenata. **7.78 GB**

Performanse su merene koristeci .explain("executionStats") metodu MongoDB-a.

**v3 se ne nalazi na grafu jer za sada ne primecujem razlike u izvrsavanju izmedju v2 i v3. Kada pokusam da optimizujem malo vise query-e sa indexima, i ako bude razlika, plotovacu i v3**
![Plot](https://github.com/VeljkoMaksimovic/SBP_MongoDB_Projekat/blob/master/v1_and_v2.png)

### TO-DO
- Pokusati re-organizovati komande unutar aggregation pipeline-a kako bi se ubrzalo izvrsavanje
- U par query-a radim $push i odma zatim $unwind. Treba pokusati to na neki nacin zaobici, verovatno ima efikasniji nacin da se to uradi.

### Pitanja
- Posto vreme izvrsavanja istih upita na mongoDB serveru (*executionTimeMillis*) varira, da li ima bolji pristup merenja "brzine"?
- Procitao sam da indexi pomazu pri aggregate upitima jedino ako se na pocetku pipeline-a nalaze $match ili $sort metode?? Zasto ne bi mogli da se koriste i ako sort i match imamo kasnije u pipeine-u??
- Upit 8 ima $match metodu i odma zatim $sort. Postoje indexi i za polje *position*, po kom se radi $match, i za kombinaciju polja *gw* i *value*, po kojima se radi sort. Nakon izvrsavanja upita sam primetio da mongoDB koristi samo index za *gw* i *value*, a da ne koristi index za *match*, zasto?? Kada izbacim $sort iz pipeline-a, tek onda pocne da koristi index nad poljem *position* za match. Pored toga, vidim da radi sortiranje nad svih 23000+ dokumenata, iako se $sort nalazi nakon $match-a koji treba da smanji broj dokumenata na ~3000! Znam da Mongo aggregation optimizer menja redosled metoda unutar pipeline-a radi optimizacije, ali zasto bi prebacio sort pre match-a, zar nije bolje da se prvo smanji broj dokumenata pa da tek onda sortira?

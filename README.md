# SBP_MongoDB_Projekat
Projekat iz predmeta Sistemi Baza Podataka, MongoDB baza sa upitima.

Baza sa podacima iz **Fantasy Premier League** igrice. Data set koji je koriscen: https://github.com/vaastav/Fantasy-Premier-League
Da bi python skripte za popunjavanje baza radile bez modifikacija potrebno je skinuti dataset sa linka i ubaciti folder u root directory ovog repozitorijuma.

U sklopu projekta je napravljeno vise razlicitih baza sa drugacijim semama nad kojim ce se izvrsavati isti upiti kako bi se na kraju uporedile performanse razlicitih pristupa. Svaka sema ce imati posebnu kolekciju za svaku sezonu, zato sto se ni jedan upit nece koristiti informacije iz razlicitih sezona.

Prva verzija baze ima poseban dokument za svaku kolo (*gw*)u sklopu kog se nalazi lista statistika svih igraca za to kolo, tako da cemo za prolazak i filtriranje igraca prvo morati da koristimo .unwind() kako bi od niza napravili zasebne dokumente.

Druga verzija baze uopste nece imati entitet *gw* vec ce unutar kolekcije imati dokumente koji predstavljaju statistike igraca za odredjeno kolo, i svaki dokument ce imati polje *gw* gde ce se cuvati redni broj kola.

Treca verzija baze ima identicnu strukturu kao i druga, ali su dodati indeksi kako $sort i $match metode ne bi morale da prolaze kroz svih 20,000+ dokumenata

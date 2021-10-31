- [X] Tilføj oberserver pattern - Troels
  - [X] Tilføj console observer - Troels
  - [X] Tilføj Websocket observer - Troels
- [X] Tilføj tests - Bovle
- [ ] Lav UI - Harder
  - [x]  slider for hænder i kamp
  - [ ]  vis action som skrift på avatar
  - [ ]  vis score for kamp
  - [ ]  vis hånd typer ved showdown
  - [ ]  vis chips vundet ved showdown
  - [ ]  fix state 0 og slider ændringer korrekt
- [X] Lav UI Data
  - [X] JSON kamp data 
- [X] Hjælp til bot udvikling
  - [X] preflop hånd rang 
  - [X] postflop hånd rang
  - [X] Bedre bot eksempler
- [X] Håndter multiple kampe samtidig
  - [X] Spil N bots mod hinanden alle mod alle
  - [X] Gem resultat som matchup tabel
- [X] Fejlhåndtering
  - [X] Hvis de crasher
  - [X] Hvis de tager for lang tid (1 sekund?)
- [X] Reimplment scoreboard using Google docs
  - [X] Gather results (in observer?) 
  - [ ] Upload raw data to Google sheets
  - [ ] Make Google Sheet that displays data in a pretty way

Nice to have:

- [X] løbende turneringer
  - [X] GitHub gist?





Challenge:
 - Much faster (10x) with pypy3 (https://www.pypy.org/download.html)


Sort dependencies:
 - `isort -l 120 bots environment utils main.py read_results.py challenge.py`

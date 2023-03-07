# Praktični zadatak - Analiza kompleksne mreže

**Autor:** Toni Baskijera  

**Datum:** 4. ožujka 2023.  

**Kolegij:** Prikaz znanja i rezoniranje o znanju

**Akademska godina:** 2022./2023.

---

## Istraživačka pitanja

1. Odrediti najefikasnije rute od luke u Stockohlmu do svih ostalih luka s kojima je povezana, uzimajući u obzir gustoću prometa, te ispitati doseg navedene luke

2. Identificirati kritične luke čijim bi se isključivanjem iz mreže značajno utjecalo na promet morem, odnosno na strukturu i funckiju mreže

3. Istražiti utjecaj grupiranja luka u zajednice s obzirom na njihove koordinate, odnosno geografski položaj

## Podaci i konstrukcija mreže

Mreža na kojoj će se vršiti analiza pripada domeni transporta. Zapisana je u obliku dvije Excel tablice, `nodelist.xlsx` i `edgelist.xlsx`, u kojima se nalaze čvorovi i bridovi mreže, respektivno.

U tablici `nodelist.xlsx`, koja ima ukupno 125 unosa, svaki čvor predstavlja jednu brodsku luku i sadrži sljedeće atribute:

- ID - jedinstveni identifikator luke
- LABEL - oznaka/naziv luke
- LAT - geografska širina lokacije luke
- LNG - geografska dužina lokacije luke

U tablici `edgelist.xlsx`, koja ima ukupno 321 unosa, svaki unos predstavlja vezu između dva čvora mreže, a definirane su atributima:

- SOURCE - polazišna luka (čvor)
- TARGET - odredišna luka (čvor)
- WEIGHT - broj putovanja između polazišne i odredišne luke

S obzirom na podatke, zasigurno se može zaključiti kako je najprikladnije koristiti direktni, težinski graf. Naime, direktni graf nam je potreban iz razloga što svako putovanje odrađeno istom rutom nije jednako, već je u obzir potrebno uzeti i smjer. Konkretno, ruta `P1-P2` i `P2-P1` nisu jednake i potrebno ih je razlikovati. Nadalje, prikladno je da graf bude težinski, kako svaki brid (ruta) ima i atribut `WEIGHT`, koji pruža informaciju o broju odrađenih putovanja na pripadnoj ruti, odnosno gustoću prometa.

## Analiza mreže i vizualizacije

### Promatranje 1

Za početak, na mrežu ćemo primjeniti Djikstrin algoritam. Poslužiti će nam za pronalaženje najkraćeg puta između dva čvora u grafu s pozitivnim težinama bridova. Algoritam radi tako da iterativno proširuje pretragu s izvornog čvora na sve njegove susjedne čvorove, ažurirajući minimalne udaljenosti potrebne za dostizanje svakog susjednog čvora, redom. Zatim odabire čvor s minimalnom udaljenošću i ponavlja postupak dok se ne dosegne odredišni čvor.

Primjenom istog algoritma dobiti ćemo rute s najmanje prometa od luke u Stockholmu (`P78`) do svih ostalih luka s kojima je povezana, te broj ostvarenih putovanja na svakoj:

| Luka     | Najmanje prometna ruta                                                                                       |   Broj putovanja |
|:-----|:----------------------------------------------------------------------------------------------------|--------------:|
| P78  | ['P78']                                                                                             |             0 |
| P63  | ['P78', 'P63']                                                                                      |             2 |
| P67  | ['P78', 'P63', 'P67']                                                                               |             6 |
| P57  | ['P78', 'P63', 'P67', 'P57']                                                                        |             8 |
| P91  | ['P78', 'P63', 'P67', 'P91']                                                                        |             8 |
| P123 | ['P78', 'P63', 'P67', 'P123']                                                                       |             8 |
| P106 | ['P78', 'P63', 'P67', 'P57', 'P106']                                                                |             9 |
| P117 | ['P78', 'P63', 'P67', 'P117']                                                                       |            10 |
| P48  | ['P78', 'P63', 'P67', 'P57', 'P48']                                                                 |            10 |
| P10  | ['P78', 'P63', 'P67', 'P91', 'P10']                                                                 |            10 |
| P95  | ['P78', 'P63', 'P67', 'P91', 'P95']                                                                 |            10 |
| P45  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45']                                                         |            11 |
| P55  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P55']                                                         |            11 |
| P119 | ['P78', 'P63', 'P67', 'P119']                                                                       |            12 |
| P5   | ['P78', 'P63', 'P67', 'P57', 'P5']                                                                  |            12 |
| P52  | ['P78', 'P63', 'P67', 'P117', 'P52']                                                                |            12 |
| P3   | ['P78', 'P63', 'P67', 'P57', 'P48', 'P3']                                                           |            12 |
| P1   | ['P78', 'P63', 'P67', 'P91', 'P95', 'P1']                                                           |            12 |
| P29  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P29']                                                  |            13 |
| P36  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P36']                                                  |            13 |
| P51  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P51']                                                  |            13 |
| P112 | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112']                                                 |            13 |
| P118 | ['P78', 'P63', 'P67', 'P57', 'P106', 'P55', 'P118']                                                 |            13 |
| P35  | ['P78', 'P35']                                                                                      |            14 |
| P43  | ['P78', 'P63', 'P67', 'P91', 'P95', 'P43']                                                          |            14 |
| P11  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P51', 'P11']                                           |            15 |
| P30  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P30']                                          |            15 |
| P40  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P40']                                          |            15 |
| P89  | ['P78', 'P63', 'P67', 'P91', 'P10', 'P89']                                                          |            16 |
| P81  | ['P78', 'P63', 'P67', 'P57', 'P5', 'P81']                                                           |            16 |
| P62  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P62']                                          |            17 |
| P125 | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P30', 'P125']                                  |            17 |
| P97  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P62', 'P97']                                   |            19 |
| P101 | ['P78', 'P63', 'P67', 'P91', 'P10', 'P89', 'P101']                                                  |            20 |
| P27  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P62', 'P97', 'P27']                            |            21 |
| P86  | ['P78', 'P63', 'P67', 'P91', 'P10', 'P89', 'P101', 'P86']                                           |            22 |
| P56  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P55', 'P56']                                                  |            23 |
| P24  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P51', 'P24']                                           |            23 |
| P96  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P30', 'P125', 'P96']                           |            23 |
| P19  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P62', 'P97', 'P27', 'P19']                     |            23 |
| P72  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P72']                                                  |            25 |
| P111 | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P62', 'P97', 'P111']                           |            25 |
| P33  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P55', 'P56', 'P33']                                           |            25 |
| P76  | ['P78', 'P63', 'P67', 'P57', 'P48', 'P3', 'P76']                                                    |            26 |
| P39  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P40', 'P39']                                   |            27 |
| P21  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P55', 'P56', 'P33', 'P21']                                    |            29 |
| P105 | ['P78', 'P63', 'P67', 'P91', 'P10', 'P89', 'P105']                                                  |            30 |
| P61  | ['P78', 'P63', 'P67', 'P91', 'P10', 'P89', 'P61']                                                   |            32 |
| P53  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P55', 'P56', 'P53']                                           |            37 |
| P87  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P62', 'P97', 'P27', 'P19', 'P87']              |            37 |
| P94  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P62', 'P97', 'P27', 'P19', 'P94']              |            39 |
| P93  | ['P78', 'P63', 'P67', 'P91', 'P10', 'P89', 'P101', 'P86', 'P93']                                    |            42 |
| P80  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P55', 'P56', 'P33', 'P21', 'P80']                             |            43 |
| P70  | ['P78', 'P63', 'P67', 'P70']                                                                        |            44 |
| P23  | ['P78', 'P63', 'P67', 'P91', 'P10', 'P89', 'P101', 'P86', 'P93', 'P23']                             |            44 |
| P54  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P36', 'P54']                                           |            45 |
| P113 | ['P78', 'P63', 'P67', 'P113']                                                                       |            48 |
| P31  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P62', 'P97', 'P31']                            |            51 |
| P34  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P55', 'P56', 'P33', 'P21', 'P80', 'P34']                      |            55 |
| P14  | ['P78', 'P63', 'P67', 'P91', 'P10', 'P89', 'P14']                                                   |            56 |
| P65  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P62', 'P97', 'P27', 'P65']                     |            57 |
| P102 | ['P78', 'P63', 'P67', 'P113', 'P102']                                                               |            62 |
| P44  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P62', 'P97', 'P44']                            |            67 |
| P107 | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P72', 'P107']                                          |            67 |
| P32  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P62', 'P97', 'P27', 'P19', 'P94', 'P32']       |            67 |
| P85  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P62', 'P97', 'P27', 'P19', 'P94', 'P85']       |            67 |
| P109 | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P109']                                                 |            89 |
| P9   | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P62', 'P97', 'P27', 'P65', 'P9']               |            91 |
| P108 | ['P78', 'P63', 'P67', 'P113', 'P108']                                                               |           102 |
| P46  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P62', 'P97', 'P27', 'P65', 'P9', 'P46']        |           115 |
| P47  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P62', 'P97', 'P27', 'P47']                     |           151 |
| P16  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P62', 'P97', 'P27', 'P65', 'P9', 'P16']        |           171 |
| P124 | ['P78', 'P63', 'P67', 'P113', 'P108', 'P124']                                                       |           184 |
| P58  | ['P78', 'P63', 'P67', 'P57', 'P106', 'P45', 'P112', 'P62', 'P97', 'P27', 'P65', 'P9', 'P16', 'P58'] |           263 |

Zatim navedene podatke možemo prikazati i na interaktivnoj mapi:

![Screenshot from 2023-03-07 21-04-43](https://user-images.githubusercontent.com/68339659/223546763-c47b0989-37c1-4562-8c14-e414b938e181.png)
> Vizualizacija dosega luke u Stockholmu

Proučavanjem interaktivne mape **možemo zaključiti da je doseg luke u Stockholmu uglavnom Skandinavsko područje i Velika Britanija, a rijetko Europa.**

### Promatranje 2

Nadalje, na mrežu će se primjeniti dvije mjere kojima se može utvrditi važnost i utjecaj pojedinih čvorova u mreži.

Stupanj centralnosti čvora je mjera koja se temelji na broju bridova (veza) koje čvor ima. Čvorovi s visokim stupnjem centralnosti su oni koji su izravno povezani s mnogim drugim čvorovima u mreži. U kontekstu kompleksne mreže u domeni transporta, čvorovi s visokim stupnjem centralnosti mogu predstavljati glavna prometna čvorišta ili raskrižja koja povezuju više ruta ili načina prijevoza.

Stupnjevi centralnosti za svaki čvor u našoj mreži, silazno:

|      |   Stupanj centralnosti |
|:-----|-----------------------:|
| P45  |             0.185484   |
| P67  |             0.169355   |
| P97  |             0.120968   |
| P7   |             0.120968   |
| P40  |             0.120968   |
| P50  |             0.112903   |
| P125 |             0.0967742  |
| P112 |             0.0967742  |
| P51  |             0.0967742  |
| P27  |             0.0887097  |
| P106 |             0.0887097  |
| P43  |             0.0806452  |
| P95  |             0.0806452  |
| P18  |             0.0806452  |
| P89  |             0.0806452  |
| P48  |             0.0806452  |
| P57  |             0.0725806  |
| P120 |             0.0725806  |
| P66  |             0.0725806  |
| P94  |             0.0645161  |
| P2   |             0.0645161  |
| P83  |             0.0645161  |
| P82  |             0.0645161  |
| P36  |             0.0645161  |
| P113 |             0.0645161  |
| P72  |             0.0645161  |
| P100 |             0.0564516  |
| P12  |             0.0564516  |
| P5   |             0.0564516  |
| P81  |             0.0483871  |
| P78  |             0.0483871  |
| P84  |             0.0483871  |
| P55  |             0.0483871  |
| P56  |             0.0483871  |
| P59  |             0.0483871  |
| P49  |             0.0483871  |
| P92  |             0.0483871  |
| P3   |             0.0483871  |
| P91  |             0.0483871  |
| P93  |             0.0483871  |
| P98  |             0.0483871  |
| P9   |             0.0483871  |
| P116 |             0.0483871  |
| P22  |             0.0483871  |
| P10  |             0.0483871  |
| P20  |             0.0483871  |
| P19  |             0.0483871  |
| P117 |             0.0403226  |
| P52  |             0.0403226  |
| P11  |             0.0403226  |
| P21  |             0.0403226  |
| P101 |             0.0403226  |
| P123 |             0.0322581  |
| P65  |             0.0322581  |
| P86  |             0.0322581  |
| P108 |             0.0322581  |
| P71  |             0.0322581  |
| P111 |             0.0322581  |
| P88  |             0.0322581  |
| P74  |             0.0322581  |
| P80  |             0.0322581  |
| P64  |             0.0322581  |
| P63  |             0.0322581  |
| P15  |             0.0322581  |
| P30  |             0.0322581  |
| P4   |             0.0322581  |
| P34  |             0.0322581  |
| P6   |             0.0322581  |
| P37  |             0.0322581  |
| P8   |             0.0322581  |
| P13  |             0.0322581  |
| P26  |             0.0322581  |
| P16  |             0.0322581  |
| P1   |             0.0241935  |
| P103 |             0.0241935  |
| P33  |             0.0241935  |
| P39  |             0.0241935  |
| P42  |             0.0241935  |
| P99  |             0.0241935  |
| P60  |             0.0241935  |
| P68  |             0.0241935  |
| P121 |             0.016129   |
| P25  |             0.016129   |
| P24  |             0.016129   |
| P102 |             0.016129   |
| P124 |             0.016129   |
| P104 |             0.016129   |
| P14  |             0.016129   |
| P110 |             0.016129   |
| P23  |             0.016129   |
| P119 |             0.016129   |
| P107 |             0.016129   |
| P17  |             0.016129   |
| P118 |             0.016129   |
| P109 |             0.016129   |
| P115 |             0.016129   |
| P105 |             0.016129   |
| P62  |             0.016129   |
| P28  |             0.016129   |
| P96  |             0.016129   |
| P58  |             0.016129   |
| P69  |             0.016129   |
| P70  |             0.016129   |
| P54  |             0.016129   |
| P53  |             0.016129   |
| P73  |             0.016129   |
| P47  |             0.016129   |
| P75  |             0.016129   |
| P76  |             0.016129   |
| P77  |             0.016129   |
| P46  |             0.016129   |
| P79  |             0.016129   |
| P44  |             0.016129   |
| P41  |             0.016129   |
| P38  |             0.016129   |
| P85  |             0.016129   |
| P87  |             0.016129   |
| P35  |             0.016129   |
| P90  |             0.016129   |
| P32  |             0.016129   |
| P31  |             0.016129   |
| P61  |             0.016129   |
| P29  |             0.016129   |
| P114 |             0.00806452 |
| P122 |             0.00806452 |

Za čvorove s najvećim stupnjem centralnosti prikladno je i napraviti vizualizaciju u obliku ego grafa:

![Figure_1](https://user-images.githubusercontent.com/68339659/223547400-3f54f191-fa4a-4968-a65d-267d26e0a9d2.png)
>Ego graf čvora P45

![Figure_2](https://user-images.githubusercontent.com/68339659/223547405-4cc31e6b-2230-479a-be52-f15d1da34f37.png)
>Ego graf čvora P67

![Figure_3](https://user-images.githubusercontent.com/68339659/223547409-f6cd3c6d-d661-4bc7-b740-c331b6688bc9.png)
>Ego graf čvora P97

![Figure_4](https://user-images.githubusercontent.com/68339659/223547413-8900dcd6-fc3a-48a1-a45f-e6d259baf144.png)

>Ego graf čvora P7

![Figure_5](https://user-images.githubusercontent.com/68339659/223547416-bbcc87a0-5ea6-4340-9208-c754417c3d7f.png)
>Ego graf čvora P40

![Figure_6](https://user-images.githubusercontent.com/68339659/223547418-e1951f81-6e92-4207-bb9f-616cbcbdd1af.png)
>Ego graf čvora P50

S druge strane, mjera međupoloženosti čvora služi za procjenu metrike u kojoj se mjeri čvor nalazi na najkraćem putu između parova drugih čvorova u mreži. Čvorovi s visokom međupoloženosti su oni koji će vjerojatno biti ključni za protok informacija, resursa ili, u kontekstu kompleksne mreže u domeni transporta, prometa kroz mrežu.

Međupoloženost za svaki čvor u našoj mreži, silazno:

|      |   Stupanj međupoloženosti |
|:-----|--------------------------:|
| P45  |               0.114553    |
| P27  |               0.093308    |
| P67  |               0.0865272   |
| P40  |               0.0656083   |
| P97  |               0.0652578   |
| P112 |               0.0541279   |
| P125 |               0.0533471   |
| P48  |               0.0457695   |
| P19  |               0.0387053   |
| P89  |               0.0376322   |
| P10  |               0.036721    |
| P65  |               0.036192    |
| P55  |               0.035731    |
| P51  |               0.035107    |
| P101 |               0.0317598   |
| P106 |               0.0305496   |
| P94  |               0.0305424   |
| P113 |               0.0286144   |
| P9   |               0.0277996   |
| P91  |               0.0260661   |
| P56  |               0.0212393   |
| P95  |               0.0210658   |
| P43  |               0.0199751   |
| P93  |               0.019003    |
| P66  |               0.0176676   |
| P57  |               0.0171096   |
| P72  |               0.0170513   |
| P86  |               0.0159979   |
| P34  |               0.0149527   |
| P18  |               0.0148822   |
| P50  |               0.0147587   |
| P7   |               0.0136518   |
| P36  |               0.0102327   |
| P3   |               0.00996507  |
| P12  |               0.00953099  |
| P78  |               0.00950695  |
| P16  |               0.00944138  |
| P108 |               0.00944138  |
| P123 |               0.00917912  |
| P63  |               0.00917912  |
| P82  |               0.00726353  |
| P84  |               0.00661771  |
| P80  |               0.00644017  |
| P5   |               0.00627529  |
| P118 |               0.00601279  |
| P21  |               0.00525614  |
| P120 |               0.00502994  |
| P98  |               0.00458301  |
| P116 |               0.00421475  |
| P81  |               0.0031017   |
| P117 |               0.00238727  |
| P83  |               0.00216584  |
| P20  |               0.00210901  |
| P71  |               0.00184894  |
| P33  |               0.00181589  |
| P37  |               0.00169049  |
| P15  |               0.00165006  |
| P2   |               0.00118017  |
| P100 |               0.000852347 |
| P59  |               0.000852347 |
| P52  |               0.000625519 |
| P111 |               0.000620684 |
| P30  |               0.000599713 |
| P74  |               0.000524521 |
| P92  |               0.000393391 |
| P6   |               0.000393391 |
| P115 |               0.000377    |
| P11  |               0.000363158 |
| P49  |               0.000340939 |
| P13  |               0.000262261 |
| P90  |               0.00013113  |
| P26  |               0.00013113  |
| P103 |               0.000127852 |
| P64  |               6.55652e-05 |
| P22  |               6.55652e-05 |
| P17  |               0           |
| P121 |               0           |
| P4   |               0           |
| P96  |               0           |
| P14  |               0           |
| P124 |               0           |
| P122 |               0           |
| P109 |               0           |
| P119 |               0           |
| P110 |               0           |
| P114 |               0           |
| P102 |               0           |
| P104 |               0           |
| P105 |               0           |
| P107 |               0           |
| P8   |               0           |
| P99  |               0           |
| P41  |               0           |
| P88  |               0           |
| P87  |               0           |
| P39  |               0           |
| P44  |               0           |
| P38  |               0           |
| P46  |               0           |
| P47  |               0           |
| P35  |               0           |
| P53  |               0           |
| P54  |               0           |
| P32  |               0           |
| P31  |               0           |
| P58  |               0           |
| P60  |               0           |
| P61  |               0           |
| P62  |               0           |
| P29  |               0           |
| P28  |               0           |
| P68  |               0           |
| P69  |               0           |
| P70  |               0           |
| P25  |               0           |
| P73  |               0           |
| P75  |               0           |
| P76  |               0           |
| P77  |               0           |
| P24  |               0           |
| P79  |               0           |
| P42  |               0           |
| P85  |               0           |
| P23  |               0           |
| P1   |               0           |

U tablici možemo prikazati i deset najznačajnih čvorova na temelju svake mjere:

| Stupanj centralnosti | Međupoloženost|
|----------|----------|
| P45      | P45      |
| P27      | P67      |
| P67      | P97      |
| P40      | P7       |
| P97      | P40      |
| P112     | P50      |
| P125     | P125     |
| P48      | P112     |
| P19      | P51      |
| P89      | P27      |

Čvorovi koje obe mjere centralnosti identiciraju kao deset najvažnijih su: `P45, P67, P97, P40, P112, P125, P27`. Sukladno tome, **možemo zaključiti kako su luke s navedenim oznakama od kritične važnosti, te bi se njihovim isključivanjem iz mreže značajno utjecalo na promet morem, odnosno na strukturu i funckiju anlizirane mreže.**

### Promatranje 3

Za detekciju zajednica u mreži korišten je Louvain algoritam. Temelji se na pohlepnom optimizacijskom pristupu kojemu je cilj maksimizirati modularnost mreže. Modularnost je mjera kvalitete particioniranja mreže u zajednice, koja kvantificira stupanj kojim su čvorovi unutar iste zajednice povezani jedni s drugima, u odnosu na čvorove u drugim zajednicama.

U analiziranoj mreži identificirano je ukupno 18 zajednica. Za svaku zajednicu konstruiran je i odgovorajući podgraf, za kojeg je u tablici izračunata i gustoća. Mjera gustoće izračunava se kao omjer stvarnog broja veza (bridova) u mreži i maksimalnog broja veza koji bi mogli postojati u mreži.

Identificirane zajednice:

| Zajednica   | Čvorovi                                                                                                                                   |   Gustoća |
|---:|:------------------------------------------------------------------------------------------------------------------------------------------|----------:|
|  0 | ['P1', 'P29', 'P45', 'P109']                                                                                                              |  0.416667 |
|  1 | ['P35', 'P78', 'P123']                                                                                                                    |  0.666667 |
|  2 | ['P41', 'P121']                                                                                                                           |  1        |
|  3 | ['P4', 'P8', 'P12', 'P22', 'P50', 'P84', 'P92', 'P114', 'P122']                                                                           |  0.305556 |
|  4 | ['P3', 'P5', 'P36', 'P54', 'P57', 'P76', 'P106', 'P118']                                                                                  |  0.214286 |
|  5 | ['P42', 'P60', 'P64']                                                                                                                     |  0.833333 |
|  6 | ['P7', 'P15', 'P18', 'P20', 'P37', 'P49', 'P66', 'P68', 'P71', 'P73', 'P82', 'P83', 'P88', 'P98', 'P103', 'P110', 'P115', 'P116', 'P120'] |  0.154971 |
|  7 | ['P9', 'P16', 'P27', 'P46', 'P47', 'P58', 'P65']                                                                                          |  0.285714 |
|  8 | ['P10', 'P14', 'P61', 'P89', 'P101', 'P105']                                                                                              |  0.333333 |
|  9 | ['P24', 'P30', 'P31', 'P44', 'P48', 'P51', 'P62', 'P91', 'P96', 'P97', 'P111', 'P112', 'P125']                                            |  0.179487 |
| 10 | ['P52', 'P72', 'P81', 'P107', 'P117']                                                                                                     |  0.45     |
| 11 | ['P17', 'P26', 'P28']                                                                                                                     |  0.666667 |
| 12 | ['P19', 'P23', 'P32', 'P85', 'P86', 'P87', 'P93', 'P94']                                                                                  |  0.25     |
| 13 | ['P11', 'P21', 'P33', 'P34', 'P39', 'P40', 'P53', 'P55', 'P56', 'P80']                                                                    |  0.233333 |
| 14 | ['P6', 'P13', 'P59', 'P90', 'P99', 'P100', 'P104']                                                                                        |  0.333333 |
| 15 | ['P2', 'P38', 'P69', 'P74', 'P75', 'P79']                                                                                                 |  0.333333 |
| 16 | ['P25', 'P77']                                                                                                                            |  1        |
| 17 | ['P43', 'P63', 'P67', 'P70', 'P95', 'P102', 'P108', 'P113', 'P119', 'P124']                                                               |  0.222222 |

Vizualni primjeri nekih zajednica:

![6c90a527-e848-4cbc-9f90-84c35f4c5364](https://user-images.githubusercontent.com/68339659/223547081-a79b8a76-c4c2-4cc4-8dfe-0cdc8e1c5d99.png)
> Zajednica 4

![85cf5bfc-2fad-4082-9c38-638b1abac695](https://user-images.githubusercontent.com/68339659/223547087-eff86176-a36d-44ab-85c2-602d13825980.png)
> Zajednica3

![232a8630-5b2b-4c83-b718-b7b181b6a003](https://user-images.githubusercontent.com/68339659/223547091-4fee6f4a-7d59-4dd0-8add-b30b630e1e7b.png)
> Zajednica 9

![14912be1-c8ce-483d-a737-5c4f628a2f25](https://user-images.githubusercontent.com/68339659/223547097-91a8d324-9670-471f-a16f-accacb474c5e.png)
> Zajednica 11

![457643a6-0283-4dbd-bb3f-a9984380ab8c](https://user-images.githubusercontent.com/68339659/223547098-d81de163-8cd7-4f3b-9d03-fb97610a6b18.png)
>Zajednica 10

Navedene zajednice možemo prikazati i sve zajedno, raspršenim grafom, gdje je svaka zajednica drukčijeg oblika i/ili boje:

![Screenshot from 2023-03-07 20-30-22](https://user-images.githubusercontent.com/68339659/223547360-f09a0fc4-6dc6-44e5-a5bb-7f840a0e9ea0.png)
> Zajednice

Uvećani prikaz središnjeg dijela prošle vizualizacije:

![Screenshot from 2023-03-07 20-30-09](https://user-images.githubusercontent.com/68339659/223547352-54a815c4-243c-4507-ad74-1f4c6e9a0ba9.png)
> Zajednice (uvećani prikaz)

Možemo vidjeti kako su zajednice relativno dobro grupirane, ali ne i savršeno.

Pojedine luke unutar određene zajednice većinom su u neposrednoj blizini. Težina veze, očekivano, ne utječe na grupiranje. Sukladno tome, **možemo zaključiti kako se luke pretežno grupiraju ovisno o njihovim koordinatama, odnosno geografskom položaju.** .

## Literatura

[1] <https://networkx.org/documentation/stable/reference/index.html>

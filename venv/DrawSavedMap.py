from Pygame_setup import *



lan = {
"geometry" : "hexagon",
"regions" : 
   {
      "Norrbotten" : (5, 0),
      "Västerbott" : (3, 0),
      "Västernorr" : (4, 1),
      "Jämtland" : (2, 1),
      "Gävleborg" : (3, 2),
      "Dalarna" : (2, 3),
      "Uppsala" : (5, 2),
      "Värmland" : (1, 4),
      "Västmanlan" : (4, 3),
      "Stockholms" : (7, 4),
      "Örebro" : (3, 4),
      "Södermanla" : (5, 4),
      "Östergötla" : (4, 5),
      "Jönköping" : (2, 5),
      "Västra Göt" : (0, 5),
      "Kalmar" : (3, 6),
      "Halland" : (1, 6),
      "Kronoberg" : (2, 7),
      "Blekinge" : (4, 7),
      "Skåne" : (1, 8),
      "Gotland" : (7, 6)
   }
}
lan2 = {
"geometry" : "square",
"regions" :
   {
      "Norrbotten" : (2, 0),
      "Västerbott" : (1, 0),
      "Västernorr" : (2, 1),
      "Jämtland" : (1, 1),
      "Gävleborg" : (2, 2),
      "Dalarna" : (1, 2),
      "Uppsala" : (2, 3),
      "Värmland" : (1, 3),
      "Västmanlan" : (2, 4),
      "Stockholms" : (3, 4),
      "Örebro" : (1, 4),
      "Södermanla" : (2, 5),
      "Östergötla" : (1, 5),
      "Jönköping" : (1, 6),
      "Västra Göt" : (0, 5),
      "Kalmar" : (2, 6),
      "Halland" : (0, 6),
      "Kronoberg" : (1, 7),
      "Blekinge" : (2, 7),
      "Skåne" : (1, 8),
      "Gotland" : (4, 6)
   }
}
europe = {
"geometry" : "hexagon",
"regions" :
   {
      "Switzerlan" : (5, 6),
      "Albania" : (13, 8),
      "Bosnia and" : (11, 6),
      "Belgium" : (6, 5),
      "Bulgaria" : (15, 6),
      "Belarus" : (13, 4),
      "Austria" : (9, 6),
      "Czech Rep." : (10, 5),
      "Germany" : (9, 4),
      "Denmark" : (10, 3),
      "Spain" : (2, 7),
      "Estonia" : (16, 1),
      "Finland" : (12, 1),
      "France" : (3, 6),
      "Greece" : (15, 8),
      "Croatia" : (8, 7),
      "Hungary" : (12, 5),
      "Italy" : (4, 7),
      "Kosovo" : (14, 7),
      "Luxembourg" : (8, 5),
      "Lithuania" : (14, 3),
      "Latvia" : (15, 2),
      "Moldova" : (15, 4),
      "Macedonia" : (12, 7),
      "Montenegro" : (10, 7),
      "Netherland" : (7, 4),
      "Norway" : (10, 1),
      "Poland" : (11, 4),
      "Portugal" : (1, 8),
      "Romania" : (16, 5),
      "Russia" : (18, 3),
      "Slovakia" : (14, 5),
      "Serbia" : (13, 6),
      "Sweden" : (11, 2),#(13, 0),
      "Slovenia" : (7, 6),
      "Ukraine" : (16, 3),
        "Iceland" : (6, 1),
       "UK" : (3, 4),
       "Ireland" : (1, 4),
       "Turkey" : (17, 8)
   }
}

european_union = {
   "geometry" : "hexagon",
   "regions" :
      {
         "Belgium" : (6, 5),
         "Bulgaria" : (15, 6),
         "Austria" : (9, 6),
         "Czech Rep." : (10, 5),
         "Germany" : (9, 4),
         "Denmark" : (10, 3),
         "Spain" : (2, 7),
         "Estonia" : (16, 1),
         "Finland" : (12, 1),
         "France" : (3, 6),
         "Greece" : (15, 8),
         "Croatia" : (8, 7),
         "Hungary" : (12, 5),
         "Italy" : (4, 7),
         "Luxembourg" : (8, 5),
         "Lithuania" : (14, 3),
         "Latvia" : (15, 2),
         "Netherland" : (7, 4),
         "Poland" : (11, 4),
         "Portugal" : (1, 8),
         "Romania" : (16, 5),
         "Slovakia" : (14, 5),
         "Sweden" : (11, 2),
         "Slovenia" : (7, 6),
         "Ireland" : (1, 4),
      }
}

sweden_municipalities = {
"geometry" : "hexagon",
"regions" :
   {
      "Norrtälje" : (24, 13),
      "Sigtuna" : (23, 14),
      "Nynäshamn" : (25, 24),
      "Varberg" : (4, 27),
      "Krokom" : (20, 5),
      "Solna" : (24, 17),
      "Strömstad" : (7, 20),
      "Tidaholm" : (13, 24),
      "Forshaga" : (15, 14),
      "Ludvika" : (18, 13),
      "Örnsköldsv" : (29, 6),
      "Gällivare" : (26, 1),
      "Upplands V" : (21, 16),
      "Trosa" : (24, 23),
      "Gnosjö" : (11, 26),
      "Hässleholm" : (12, 31),
      "Tibro" : (12, 23),
      "Ulricehamn" : (9, 26),
      "Mariestad" : (10, 21),
      "Hofors" : (24, 9),
      "Hudiksvall" : (25, 8),
      "Sollefteå" : (25, 6),
      "Lycksele" : (25, 4),
      "Lidingö" : (23, 18),
      "Sävsjö" : (13, 28),
      "Herrljunga" : (9, 24),
      "Kungälv" : (2, 23),
      "Örebro" : (16, 19),
      "Jokkmokk" : (24, 1),
      "Övertorneå" : (29, 0),
      "Järfälla" : (24, 19),
      "Nyköping" : (21, 22),
      "Växjö" : (15, 28),
      "Högsby" : (17, 28),
      "Åstorp" : (9, 30),
      "Sotenäs" : (4, 21),
      "Mellerud" : (10, 19),
      "Hallsberg" : (16, 21),
      "Ånge" : (19, 8),
      "Kramfors" : (27, 6),
      "Överkalix" : (30, 1),
      "Luleå" : (31, 2),
      "Värmdö" : (28, 19),
      "Sundbyberg" : (24, 21),
      "Heby" : (23, 12),
      "Boxholm" : (17, 24),
      "Norrköping" : (19, 22),
      "Aneby" : (15, 26),
      "Härryda" : (3, 26),
      "Trollhätta" : (4, 23),
      "Årjäng" : (8, 17),
      "Hagfors" : (15, 12),
      "Leksand" : (18, 11),
      "Ockelbo" : (22, 9),
      "Härnösand" : (24, 7),
      "Haparanda" : (31, 0),
      "Ekerö" : (22, 17),
      "Knivsta" : (25, 16),
      "Vetlanda" : (16, 27),
      "Emmaboda" : (16, 31),
      "Lund" : (11, 32),
      "Lilla Edet" : (8, 21),
      "Åmål" : (11, 18),
      "Hällefors" : (16, 15),
      "Hedemora" : (20, 11),
      "Bollnäs" : (23, 8),
      "Skellefteå" : (28, 3),
      "Tierp" : (25, 10),
      "Enköping" : (22, 15),
      "Ydre" : (18, 25),
      "Valdemarsv" : (23, 24),
      "Ljungby" : (9, 28),
      "Bromölla" : (16, 33),
      "Malmö" : (6, 33),
      "Eslöv" : (8, 33),
      "Halmstad" : (5, 28),
      "Göteborg" : (2, 25),
      "Askersund" : (15, 20),
      "Sandviken" : (22, 11),
      "Arvidsjaur" : (27, 2),
      "Arjeplog" : (23, 2),
      "Kalix" : (32, 1),
      "Nacka" : (25, 18),
      "Flen" : (20, 21),
      "Mjölby" : (16, 23),
      "Borgholm" : (20, 29),
      "Simrishamn" : (17, 34),
      "Laholm" : (8, 29),
      "Dals-Ed" : (7, 18),
      "Gullspång" : (12, 19),
      "Vänersborg" : (6, 21),
      "Fagersta" : (19, 16),
      "Salem" : (26, 17),
      "Skurup" : (12, 33),
      "Ystad" : (12, 35),
      "Kristianst" : (13, 32),
      "Hylte" : (7, 28),
      "Lerum" : (6, 25),
      "Svenljunga" : (8, 27),
      "Lysekil" : (3, 22),
      "Skara" : (11, 22),
      "Degerfors" : (13, 18),
      "Gagnef" : (16, 13),
      "Rättvik" : (19, 10),
      "Timrå" : (21, 6),
      "Dorotea" : (22, 5),
      "Vännäs" : (28, 5),
      "Vallentuna" : (24, 15),
      "Österåker" : (27, 18),
      "Botkyrka" : (25, 20),
      "Värnamo" : (11, 28),
      "Oskarshamn" : (20, 27),
      "Helsingbor" : (5, 30),
      "Tranemo" : (10, 25),
      "Lidköping" : (9, 20),
      "Kil" : (13, 16),
      "Berg" : (17, 8),
      "Vaxholm" : (26, 21),
      "Ödeshög" : (15, 24),
      "Åtvidaberg" : (21, 24),
      "Gislaved" : (10, 27),
      "Partille" : (3, 24),
      "Bräcke" : (20, 7),
      "Malå" : (26, 3),
      "Pajala" : (27, 0),
      "Habo" : (14, 25),
      "Vaggeryd" : (12, 27),
      "Tjörn" : (1, 26),
      "Vansbro" : (16, 11),
      "Ovanåker" : (20, 9),
      "Håbo" : (23, 16),
      "Eskilstuna" : (19, 18),
      "Motala" : (17, 22),
      "Landskrona" : (7, 32),
      "Norberg" : (21, 12),
      "Arboga" : (18, 19),
      "Ragunda" : (23, 6),
      "Umeå" : (29, 4),
      "Älvsbyn" : (29, 2),
      "Eksjö" : (17, 26),
      "Klippan" : (4, 31),
      "Båstad" : (3, 28),
      "Höganäs" : (6, 29),
      "Stenungsun" : (6, 23),
      "Mark" : (5, 26),
      "Nordanstig" : (26, 7),
      "Alvesta" : (14, 29),
      "Älmhult" : (12, 29),
      "Karlskrona" : (18, 33),
      "Ängelholm" : (4, 29),
      "Kungsbacka" : (2, 27),
      "Skövde" : (13, 22),
      "Storfors" : (14, 15),
      "Mora" : (17, 10),
      "Danderyd" : (25, 22),
      "Finspång" : (18, 21),
      "Sollentuna" : (21, 20),
      "Katrinehol" : (19, 20),
      "Vadstena" : (14, 23),
      "Kalmar" : (18, 31),
      "Svalöv" : (10, 31),
      "Svedala" : (9, 34),
      "Sjöbo" : (10, 35),
      "Vara" : (9, 22),
      "Töreboda" : (12, 21),
      "Mölndal" : (4, 25),
      "Arvika" : (11, 14),
      "Sorsele" : (24, 3),
      "Tyresö" : (26, 23),
      "Södertälje" : (23, 20),
      "Östhammar" : (26, 9),
      "Gnesta" : (22, 21),
      "Hultsfred" : (18, 27),
      "Borås" : (8, 25),
      "Borlänge" : (17, 12),
      "Storuman" : (22, 3),
      "Boden" : (28, 1),
      "Upplands-B" : (20, 19),
      "Tranås" : (16, 25),
      "Tingsryd" : (15, 30),
      "Sölvesborg" : (14, 33),
      "Kävlinge" : (11, 34),
      "Hörby" : (10, 33),
      "Munkedal" : (5, 20),
      "Färgelanda" : (8, 19),
      "Bollebygd" : (7, 26),
      "Uddevalla" : (5, 22),
      "Skinnskatt" : (17, 14),
      "Norsjö" : (25, 2),
      "Uppvidinge" : (16, 29),
      "Mönsterås" : (19, 28),
      "Burlöv" : (8, 35),
      "Örkelljung" : (7, 30),
      "Alingsås" : (8, 23),
      "Torsby" : (13, 12),
      "Munkfors" : (12, 15),
      "Surahammar" : (20, 13),
      "Sundsvall" : (22, 7),
      "Åre" : (18, 7),
      "Nykvarn" : (21, 18),
      "Älvkarleby" : (27, 8),
      "Vingåker" : (17, 20),
      "Karlshamn" : (15, 32),
      "Orust" : (1, 24),
      "Grästorp" : (7, 22),
      "Falköping" : (11, 24),
      "Lindesberg" : (16, 17),
      "Sala" : (21, 14),
      "Östersund" : (19, 6),
      "Bjurholm" : (26, 5),
      "Robertsfor" : (31, 4),
      "Kinda" : (19, 24),
      "Mullsjö" : (12, 25),
      "Vimmerby" : (19, 26),
      "Öckerö" : (0, 25),
      "Ale" : (5, 24),
      "Kumla" : (13, 20),
      "Orsa" : (18, 9),
      "Smedjeback" : (19, 14),
      "Falun" : (21, 10),
      "Avesta" : (24, 11),
      "Ljusdal" : (21, 8),
      "Åsele" : (24, 5),
      "Vårgårda" : (10, 23),
      "Sunne" : (12, 13),
      "Karlstad" : (13, 14),
      "Lekeberg" : (15, 18),
      "Laxå" : (14, 19),
      "Nora" : (14, 17),
      "Gävle" : (23, 10),
      "Strömsund" : (21, 4),
      "Stockholm" : (23, 22),
      "Olofström" : (14, 31),
      "Bjuv" : (6, 31),
      "Höör" : (8, 31),
      "Tomelilla" : (13, 34),
      "Falkenberg" : (6, 27),
      "Essunga" : (7, 24),
      "Eda" : (10, 15),
      "Nordmaling" : (30, 5),
      "Vindeln" : (27, 4),
      "Piteå" : (30, 3),
      "Täby" : (22, 19),
      "Strängnäs" : (20, 17),
      "Söderköpin" : (20, 23),
      "Nässjö" : (14, 27),
      "Torsås" : (19, 32),
      "Västervik" : (20, 25),
      "Vellinge" : (9, 36),
      "Lomma" : (7, 34),
      "Osby" : (11, 30),
      "Tanum" : (6, 19),
      "Hjo" : (15, 22),
      "Ljusnarsbe" : (17, 16),
      "Karlskoga" : (15, 16),
      "Västerås" : (20, 15),
      "Köping" : (18, 15),
      "Oxelösund" : (22, 23),
      "Jönköping" : (13, 26),
      "Lessebo" : (17, 30),
      "Mörbylånga" : (19, 30),
      "Nybro" : (18, 29),
      "Perstorp" : (9, 32),
      "Götene" : (11, 20),
      "Kungsör" : (17, 18),
      "Malung-Säl" : (14, 11),
      "Kiruna" : (25, 0),
      "Huddinge" : (26, 19),
      "Uppsala" : (22, 13),
      "Linköping" : (18, 23),
      "Markaryd" : (10, 29),
      "Ronneby" : (17, 32),
      "Staffansto" : (5, 32),
      "Östra Göin" : (13, 30),
      "Trelleborg" : (11, 36),
      "Bengtsfors" : (9, 18),
      "Grums" : (9, 16),
      "Härjedalen" : (16, 9),
      "Vilhelmina" : (23, 4),
      "Haninge" : (27, 20),
      "Karlsborg" : (14, 21),
      "Hammarö" : (10, 17),
      "Kristineha" : (12, 17),
      "Filipstad" : (14, 13),
      "Säffle" : (11, 16),
      "Hallstaham" : (18, 17),
      "Älvdalen" : (15, 10),
      "Säter" : (19, 12),
      "Söderhamn" : (28, 7),
      "Öland" : (22, 31),
      "Gotland" : (23, 26)
   }
}


is_in_european_union = {
"Switzerlan" : False,
      "Albania" : False,
      "Bosnia and" : False,
      "Belgium" : True,
      "Bulgaria" : True,
      "Belarus" : False,
      "Austria" : True,
      "Czech Rep." : True,
      "Germany" : True,
      "Denmark" : True,
      "Spain" : True,
      "Estonia" : True,
      "Finland" : True,
      "France" : True,
      "Greece" : True,
      "Croatia" : True,
      "Hungary" : True,
      "Italy" : True,
      "Kosovo" : False,
      "Luxembourg" : True,
      "Lithuania" : True,
      "Latvia" : True,
      "Moldova" : False,
      "Macedonia" : False,
      "Montenegro" : False,
      "Netherland" : True,
      "Norway" : False,
      "Poland" : True,
      "Portugal" : True,
      "Romania" : True,
      "Russia" : False,
      "Slovakia" : True,
      "Serbia" : False,
      "Sweden" : True,
      "Slovenia" : True,
      "Ukraine" : False,
        "Iceland" : False,
       "UK" : False,
       "Ireland" : True,
    "Turkey" : False
}


latin_america = {
"geometry" : "hexagon",
"regions" :
   {
      "Belize" : (4, 0),
      "Costa Rica" : (7, 3),
      "Guatemala" : (5, 1),
      "Honduras" : (7, 1),
      "Mexico" : (2, 0),
      "Nicaragua" : (8, 2),
      "Panama" : (9, 3),
      "El Salvado" : (6, 2),
      "Argentina" : (13, 7),
      "Bolivia" : (11, 5),
      "Brazil" : (13, 5),
      "Chile" : (12, 8),
      "Colombia" : (10, 4),
      "Ecuador" : (9, 5),
      "Guyana" : (14, 4),
      "Peru" : (10, 6),
      "Paraguay" : (12, 6),
      "Suriname" : (15, 5),
      "Uruguay" : (14, 6),
      "Venezuela" : (12, 4)
   }
}

american_continent = {
   "geometry" : "hexagon",
   "regions" :
      {
         "Belize" : (3, 4),
         "Costa Rica" : (4, 7),
         "Guatemala" : (2, 5),
         "Honduras" : (4, 5),
         "Haiti" : (9, 4),
         "Dom R." : (11, 4),
         "Jamaica" : (7, 4),
         "Bahamas" : (5, 2),
         "Mexico" : (2, 3),
         "Cuba" : (6, 3),
         "USA" : (1, 2),
         "Canada" : (2, 1),
         "Nicaragua" : (5, 6),
         "Panama" : (6, 7),
         "El Salvado" : (3, 6),
         "Argentina" : (10, 11),
         "Bolivia" : (8, 9),
         "Brazil" : (10, 9),
         "Chile" : (9, 12),
          "Falkland" : (13, 12),
         "Colombia" : (7, 8),
         "Ecuador" : (6, 9),
         "Guyana" : (11, 8),
         "Peru" : (7, 10),
         "Paraguay" : (9, 10),
         "Suriname" : (12, 9),
         "Uruguay" : (11, 10),
         "Venezuela" : (9, 8)
      }
}

asia = {
   "geometry" : "hexagon",
   "regions" :
      {
         "Afghanista" : (13, 3),
         "United Ara" : (8, 4),
         "Armenia" : (9, 1),
         "Azerbaijan" : (11, 1),
         "Bangladesh" : (16, 4),
         "Bhutan" : (14, 4),
         "China" : (17, 3),
         "Georgia" : (7, 1),
         "India" : (13, 5),
          "Sri Lanka" : (14, 6),
         "Iran" : (10, 2),
         "Iraq" : (8, 2),
         "Israel" : (3, 3),
         "Jordan" : (4, 4),
         "Kazakhstan" : (13, 1),
         "Kyrgyzstan" : (16, 2),
         "Cambodia" : (19, 5),
         "S. Korea" : (18, 2),
         "Kuwait" : (7, 3),
         "Lao PDR" : (18, 4),
         "Lebanon" : (4, 2),
         "Myanmar" : (17, 5),
         "Mongolia" : (17, 1),
         "Nepal" : (15, 3),
         "Oman" : (7, 5),
         "Pakistan" : (12, 4),
         "N. Korea" : (19, 1),
         "Palestine" : (5, 3),
         "Qatar" : (9, 3),
         "Saudi Arab" : (6, 4),
         "Syria" : (6, 2),
         "Thailand" : (18, 6),
         "Tajikistan" : (15, 1),
         "Turkmenist" : (12, 2),
         "Turkey" : (5, 1),
         "Uzbekistan" : (14, 2),
         "Vietnam" : (21, 5),
         "Yemen" : (5, 5),
         "Tiawan" : (21, 3),
         "Japan" : (23, 1),
          "Phillipines" : (25, 5),
          "Malaysia" : (19, 7),
          "Singapore" : (20, 8),
          "Brunei" : (21, 7),
          "Indonesia" : (25, 7),
          "P N Guinea" : (27, 7)
      }
}

africa = {
   "geometry" : "hexagon",
   "regions" :
      {
         "Burundi" : (17, 6),
         "Morocco" : (12, 1),
         "Mauritania" : (5, 2),
         "W. Sahara" : (6, 1),
         "Angola" : (13, 6),
         "Central Af" : (14, 5),
         "Botswana" : (15, 8),
         "Burkina Fa" : (6, 3),
         "Benin" : (10, 3),
         "Algeria" : (9, 2),
         "Ivory Coast" : (6, 5),
         "Cameroon" : (13, 4),
         "Dem. Rep. " : (15, 6),
         "Eritrea" : (15, 2),
         "Djibouti" : (18, 3),
         "Ethiopia" : (17, 4),
         "Egypt" : (17, 2),
         "Congo" : (12, 5),
         "Ghana" : (7, 4),
         "Gabon" : (11, 4),
         "Guinea" : (4, 3),
         "Gambia" : (2, 3),
         "Guinea-Bis" : (3, 4),
         "Eq. Guinea" : (9, 4),
         "Kenya" : (20, 5),
         "Liberia" : (4, 5),
         "Lesotho" : (16, 9),
         "Libya" : (13, 2),
         "Mali" : (7, 2),
         "Malawi" : (18, 7),
         "Mozambique" : (19, 8),
         "Namibia" : (14, 7),
         "Nigeria" : (12, 3),
         "Niger" : (11, 2),
         "Rwanda" : (16, 5),
         "Sudan" : (16, 3),
         "S. Sudan" : (15, 4),
         "Senegal" : (3, 2),
         "Sierra Leo" : (5, 4),
         "Somalia" : (19, 4),
         "Somaliland" : (20, 3),
         "Swaziland" : (18, 9),
         "Chad" : (14, 3),
         "Togo" : (8, 3),
         "Tunisia" : (14, 1),
         "Tanzania" : (19, 6),
         "Uganda" : (18, 5),
         "South Afri" : (17, 10),
         "Zimbabwe" : (17, 8),
         "Zambia" : (16, 7),
         "Madagascar" : (22, 7),
      }
}

africa_area = {
"Burundi" : 2.135367306308651,
"Congo" : 27.620749097832327,
"Cameroon" : 37.60672352398318,
"Benin" : 9.641192873181259,
"Burkina Fa" : 22.5746248658036,
"Botswana" : 51.83766988185895,
"Central Af" : 50.861075547061255,
"Dem. Rep. " : 189.51523247761224,
"Angola" : 103.59943926071952,
"Ivory Coast" : 27.032682464703225,
"Djibouti" : 1.8148018637142527,
"Algeria" : 213.60277173919098,
"Egypt" : 90.39596041062852,
"Eritrea" : 10.045471935635167,
"Ethiopia" : 93.130692503862,
"Gabon" : 21.89922976260136,
"Ghana" : 19.973899443114085,
"Guinea" : 19.785731962248434,
"Gambia" : 1.1711736519968703,
"Guinea-Bis" : 3.002730069769035,
"Eq. Guinea" : 2.204018821470197,
"Kenya" : 48.033194821283914,
"Liberia" : 8.029139405641521,
"Libya" : 148.8531472105571,
"Lesotho" : 2.5618799159564,
"Mali" : 105.0970335422739,
"Morocco" : 55.38899164809157,
"Mozambique" : 69.07383609252932,
"Mauritania" : 91.12872767192049,
"Malawi" : 9.276727516337129,
"Namibia" : 72.33595289473432,
"Niger" : 100.56008888471872,
"Nigeria" : 74.59171156482155,
"Rwanda" : 1.899405495325027,
"W. Sahara" : 8.60398420747207,
"Sudan" : 156.44454329743394,
"S. Sudan" : 51.19611245073621,
"Senegal" : 16.29205333245675,
"Somaliland" : 13.800282773814006,
"Sierra Leo" : 6.240571594626415,
"Somalia" : 39.52818648039665,
"Swaziland" : 1.6399831040728154,
"Chad" : 107.16736397814981,
"Togo" : 5.0072200677795395,
"Tunisia" : 15.28595199625452,
"Uganda" : 19.976558658694515,
"Tanzania" : 76.30199150912908,
"South Afri" : 115.28040353636761,
"Zambia" : 62.789498527012164,
"Zimbabwe" : 32.28037069094718,
"Madagascar" : 25
}

india = {
"geometry" : "hexagon",
"regions" :
   {
      "Tamil Nadu" : (4, 5),
      "Kerala" : (3, 6),
      "Karnataka" : (2, 5),
      "Andhra Pradesh" : (5, 4),
      "Goa" : (1, 4),
      "Maharashtra" : (3, 4),
      "Ghhatisgarh" : (6, 3),
      "Orissa" : (6, 5),
      "West Bengal" : (8, 3),
      "Jharkand" : (7, 4),
      "Bihar" : (7, 2),
      "Uttar Pradesh" : (5, 2),
      "Uttarranchal" : (6, 1),
      "Himmachal Pradesh" : (5, 0),
      "Punjab" : (2, 1),
      "Jammu & Kashmir" : (3, 0),
      "Haryana" : (4, 1),
      "Rajasthan" : (3, 2),
      "Madya Pradesh" : (4, 3),
      "Gujarat" : (2, 3),
"Arunachal " : (12, 1),
         "Assam" : (11, 2),
         "Nagaland" : (13, 2),
         "Manipur" : (12, 3),
         "Meghalaya" : (9, 2),
         "Tripura" : (10, 3),
         "Mizoram" : (11, 4),
   }
}


usa = {
   "geometry" : "hexagon",
   "regions" :
      {
         "Maine" : (22, 1),
         "Massachuse" : (20, 1),
         "Michigan" : (13, 0),
         "Montana" : (6, 1),
         "Nevada" : (3, 2),
         "New Jersey" : (18, 1),
         "New York" : (22, 3),
         "North Caro" : (19, 4),
         "Ohio" : (14, 1),
         "Pennsylvan" : (16, 1),
         "Rhode Isla" : (21, 2),
         "Tennessee" : (12, 3),
         "Texas" : (10, 5),
         "Utah" : (5, 2),
         "Washington" : (2, 1),
         "Wisconsin" : (11, 0),
         "Maryland" : (17, 4),
         "Alabama" : (15, 4),
         "Arizona" : (4, 3),
         "Arkansas" : (9, 4),
         "California" : (2, 3),
         "Colorado" : (6, 3),
         "Connecticu" : (19, 2),
         "Delaware" : (20, 3),
         "District o" : (17, 2),
         "Florida" : (17, 6),
         "Georgia" : (16, 5),
         "Idaho" : (4, 1),
         "Illinois" : (11, 2),
         "Indiana" : (12, 1),
         "Iowa" : (10, 1),
         "Kansas" : (8, 3),
         "Kentucky" : (13, 2),
         "Louisiana" : (11, 4),
         "Minnesota" : (9, 0),
         "Mississipp" : (13, 4),
         "Missouri" : (10, 3),
         "Nebraska" : (9, 2),
         "New Hampsh" : (21, 0),
         "New Mexico" : (5, 4),
         "North Dako" : (7, 0),
         "Oklahoma" : (7, 4),
         "Oregon" : (1, 2),
         "South Caro" : (18, 5),
         "South Dako" : (8, 1),
         "Vermont" : (19, 0),
         "Virginia" : (18, 3),
         "West Virgi" : (16, 3),
         "Wyoming" : (7, 2),
         "Alaska" : (-1, 0),
         "Hawaii" : (-1, 6),
      }
}

world = {
   "geometry" : "hexagon",
   "regions" :
      {
         "Belize" : (3, 8),
         "Costa Rica" : (4, 11),
         "Guatemala" : (2, 9),
         "Honduras" : (4, 9),
         "Haiti" : (9, 8),
         "Dom R." : (11, 8),
         "Jamaica" : (7, 8),
         "Bahamas" : (5, 6),
         "Mexico" : (2, 7),
         "Cuba" : (6, 7),
         "USA" : (1, 6),
         "Canada" : (2, 5),
         "Nicaragua" : (5, 10),
         "Panama" : (6, 11),
         "El Salvado" : (3, 10),
         "Argentina" : (10, 15),
         "Bolivia" : (8, 13),
         "Brazil" : (10, 13),
         "Chile" : (9, 16),
         "Falkland" : (13, 16),
         "Colombia" : (7, 12),
         "Ecuador" : (6, 13),
         "Guyana" : (11, 12),
         "Peru" : (7, 14),
         "Paraguay" : (9, 14),
         "Suriname" : (12, 13),
         "Uruguay" : (11, 14),
         "Venezuela" : (9, 12),
"Switzerlan" : (23, 6),
         "Albania" : (31, 8),
         "Bosnia and" : (29, 6),
         "Belgium" : (24, 5),
         "Bulgaria" : (33, 6),
         "Belarus" : (31, 4),
         "Austria" : (27, 6),
         "Czech Rep." : (28, 5),
         "Germany" : (27, 4),
         "Denmark" : (28, 3),
         "Spain" : (20, 7),
         "Estonia" : (34, 1),
         "Finland" : (30, 1),
         "France" : (21, 6),
         "Greece" : (33, 8),
         "Croatia" : (26, 7),
         "Hungary" : (30, 5),
         "Italy" : (22, 7),
         "Kosovo" : (32, 7),
         "Luxembourg" : (26, 5),
         "Lithuania" : (32, 3),
         "Latvia" : (33, 2),
         "Moldova" : (33, 4),
         "Macedonia" : (30, 7),
         "Montenegro" : (28, 7),
         "Netherland" : (25, 4),
         "Norway" : (28, 1),
         "Poland" : (29, 4),
         "Portugal" : (19, 8),
         "Romania" : (34, 5),
         "Russia" : (36, 3),
         "Slovakia" : (32, 5),
         "Serbia" : (31, 6),
         "Sweden" : (29, 2),
         "Slovenia" : (25, 6),
         "Ukraine" : (34, 3),
         "Iceland" : (24, 1),
         "UK" : (21, 4),
         "Ireland" : (19, 4),
         "Turkey" : (35, 8),
"Burundi" : (33, 15),
         "Morocco" : (28, 10),
         "Mauritania" : (21, 11),
         "W. Sahara" : (22, 10),
         "Angola" : (29, 15),
         "Central Af" : (30, 14),
         "Botswana" : (31, 17),
         "Burkina Fa" : (22, 12),
         "Benin" : (26, 12),
         "Algeria" : (25, 11),
         "Ivory Coast" : (22, 14),
         "Cameroon" : (29, 13),
         "Dem. Rep. " : (31, 15),
         "Eritrea" : (31, 11),
         "Djibouti" : (34, 12),
         "Ethiopia" : (33, 13),
         "Egypt" : (33, 11),
         "Congo" : (28, 14),
         "Ghana" : (23, 13),
         "Gabon" : (27, 13),
         "Guinea" : (20, 12),
         "Gambia" : (18, 12),
         "Guinea-Bis" : (19, 13),
         "Eq. Guinea" : (25, 13),
         "Kenya" : (36, 14),
         "Liberia" : (20, 14),
         "Lesotho" : (32, 18),
         "Libya" : (29, 11),
         "Mali" : (23, 11),
         "Malawi" : (34, 16),
         "Mozambique" : (35, 17),
         "Namibia" : (30, 16),
         "Nigeria" : (28, 12),
         "Niger" : (27, 11),
         "Rwanda" : (32, 14),
         "Sudan" : (32, 12),
         "S. Sudan" : (31, 13),
         "Senegal" : (19, 11),
         "Sierra Leo" : (21, 13),
         "Somalia" : (35, 13),
         "Somaliland" : (36, 12),
         "Swaziland" : (34, 18),
         "Chad" : (30, 12),
         "Togo" : (24, 12),
         "Tunisia" : (30, 10),
         "Tanzania" : (35, 15),
         "Uganda" : (34, 14),
         "South Afri" : (33, 19),
         "Zimbabwe" : (33, 17),
         "Zambia" : (32, 16),
         "Madagascar" : (38, 16),
"Afghanista" : (49, 5),
         "United Ara" : (44, 6),
         "Armenia" : (45, 3),
         "Azerbaijan" : (47, 3),
         "Bangladesh" : (52, 6),
         "Bhutan" : (50, 6),
         "China" : (53, 5),
         "Georgia" : (43, 3),
         "India" : (49, 7),
         "Sri Lanka" : (50, 8),
         "Iran" : (46, 4),
         "Iraq" : (44, 4),
         "Israel" : (39, 5),
         "Jordan" : (40, 6),
         "Kazakhstan" : (49, 3),
         "Kyrgyzstan" : (52, 4),
         "Cambodia" : (55, 7),
         "S. Korea" : (54, 4),
         "Kuwait" : (43, 5),
         "Lao PDR" : (54, 6),
         "Lebanon" : (40, 4),
         "Myanmar" : (53, 7),
         "Mongolia" : (53, 3),
         "Nepal" : (51, 5),
         "Oman" : (43, 7),
         "Pakistan" : (48, 6),
         "N. Korea" : (55, 3),
         "Palestine" : (41, 5),
         "Qatar" : (45, 5),
         "Saudi Arab" : (42, 6),
         "Syria" : (42, 4),
         "Thailand" : (54, 8),
         "Tajikistan" : (51, 3),
         "Turkmenist" : (48, 4),
         "Turkey" : (41, 3),
         "Uzbekistan" : (50, 4),
         "Vietnam" : (57, 7),
         "Yemen" : (41, 7),
         "Tiawan" : (57, 5),
         "Japan" : (59, 3),
         "Phillipines" : (61, 7),
         "Malaysia" : (55, 9),
         "Singapore" : (56, 10),
         "Brunei" : (57, 9),
         "Indonesia" : (61, 9),
         "P N Guinea" : (63, 9),
          "Australia" : (52, 14),
          "New Zeeland" : (55, 15)
      }
}

china = {
   "geometry" : "hexagon",
   "regions" :
      {
         "Tibet" : (-1, 3),
         "Xinjiang" : (0, 2),
         "Qinghai" : (1, 3),
         "Gansu" : (3, 1),
         "Inner Mongolia" : (5, 1),
         "Heilongjiang" : (11, -1),
         "Jilin" : (7, 1),
         "Liaoning" : (10, 0),
         "Heibei" : (8, 0),
         "Tianjin" : (8, 2),
         "Beijing" : (9, 1),
         "Shanxi" : (6, 2),
         "Heinan" : (7, 3),
         "Shandong" : (10, 2),
         "Hubei" : (5, 3),
         "Guizhou" : (4, 4),
         "Yunnan" : (2, 4),
         "Sichuan" : (2, 2),
         "Chongqing" : (3, 3),
         "Ningxia" : (4, 2),
         "Jiangsu" : (11, 3),
         "Anhui" : (9, 3),
         "Jiangxi" : (8, 4),
         "Zhejiang" : (9, 5),
         "Shanghai" : (10, 4),
         "Fujian" : (7, 5),
         "Guangdong" : (5, 5),
          "Hainan" : (5, 7),
         "Hunan" : (6, 4),
         "Guangxi" : (3, 5),
      }
}


def select(positions):
    mousex, mousey = pg.mouse.get_pos()
    distances = {}
    for region in positions.keys():
        x, y = positions[region]
        disSquared = (x - mousex) **2 + (y - mousey) **2
        distances[disSquared] = region
    minDis = min(distances.keys())
    return (distances[minDis], positions[distances[minDis]])


def drawSavedMap(dict, width=WIDTH, height=HEIGHT, text=True, transformchange=0, Xborder=10, Yborder=10):
    myfont = pg.font.SysFont("Times New Roman", 12)

    running = True
    selecting = False
    selected = None
    transformchange = 0

    while running:
        pg.draw.rect(screen, (255, 255, 255), (0, 0, WIDTH, HEIGHT))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    printMove(dict)
                if event.key == pg.K_1:
                    transformchange += 5
                elif event.key == pg.K_2:
                    transformchange -= 5
                elif event.key == pg.K_a:
                    Xborder += 15
                elif event.key == pg.K_d:
                    Xborder -= 15
                elif event.key == pg.K_w:
                    Yborder += 15
                elif event.key == pg.K_s:
                    Yborder -= 15
                if selected is not None:
                    if event.key == pg.K_RIGHT:
                        x, y = dict["regions"][selected]
                        dict["regions"][selected] = (x + 2, y)
                    if event.key == pg.K_LEFT:
                        x, y = dict["regions"][selected]
                        dict["regions"][selected] = (x - 2, y)
                    if event.key == pg.K_UP:
                        x, y = dict["regions"][selected]
                        dict["regions"][selected] = (x + 1, y - 1)
                    if event.key == pg.K_DOWN:
                        x, y = dict["regions"][selected]
                        dict["regions"][selected] = (x - 1, y + 1)

            if event.type == pg.MOUSEBUTTONDOWN:
                selecting = True
            if event.type == pg.MOUSEBUTTONUP:
                selecting = False

        border = 10
        geometry = dict["geometry"]
        regions = dict["regions"]

        maxX = max([i[0] for i in regions.values()])
        maxY = max([i[1] for i in regions.values()])

        if geometry == "hexagon": transform = min( (WIDTH - 2*border) / maxX, (HEIGHT - 2*border) / (maxY*0.866) ) + transformchange
        elif geometry == "square": transform = min( (WIDTH - 2*border) / maxX, (HEIGHT - 2*border) / maxY ) + transformchange

        positions = {}

        if geometry == "hexagon":
            maxi = max(africa_area.values())
            for region in regions.keys():
                x, y = regions[region]
                x = x*transform*0.5 + border + Xborder
                y = y*transform*0.866 + border*0.866 + Yborder
                s = transform/2
                corner_points = [(x, y + s), (x + 0.866 * s, y + s / 2), (x + 0.866 * s, y - s / 2), (x, y - s),
                                 (x - 0.866 * s, y - s / 2), (x - 0.866 * s, y + s / 2)]
                corner_points = [(int(x), int(y)) for x, y in corner_points]
                positions[region] = (x, y)

                color = (255, 50, 50)

                pg.draw.polygon(screen, color, corner_points)

                letters = 8
                region_name_text = myfont.render(region[:letters], 1, (255, 255, 255))

                if text:
                    width, height = region_name_text.get_rect().width, region_name_text.get_rect().height
                    while width > 0.866 * s * 2 - 3:
                        letters -= 1
                        region_name_text = myfont.render(region[:letters] + ".", 1, (255, 255, 255))
                        width, height = region_name_text.get_rect().width, region_name_text.get_rect().height
                    text_position = (int(x - width / 2), int(y - height / 2))
                    screen.blit(region_name_text, text_position)

        elif geometry == "square":
            for region in regions.keys():
                x, y = regions[region]
                x = int(x * transform + border)
                y = int(y * transform + border)
                positions[region] = (x, y)

                """if is_in_european_union[region]:
                    color = (50, 50, 100)
                else:
                    color = (100, 50, 50)"""

                pg.draw.rect(screen, color, (x, y, int(transform - 1), int(transform-1)))

                region_name_text = myfont.render(region, 1, (0, 0, 0))

                if text:
                    width, height = region_name_text.get_rect().width, region_name_text.get_rect().height
                    text_position = (x + transform // 2 - width // 2, y + transform // 2 - height // 2)
                    screen.blit(region_name_text, text_position)

        if selecting:
            selected, pos = select(positions)
            pg.draw.circle(screen, (0,0,0), [int(i) for i in pos], 10)

        pg.display.flip()

def printMove(dict, y=0, x=0):
    print("{")
    print('   "geometry" : "{}",'.format(dict["geometry"]))
    print('   "regions" : ')
    print("      {")
    for region in dict["regions"].keys():
        X, Y = dict["regions"][region]
        X += x
        Y += y
        print('         "{}" : ({}, {}),'.format(region, X, Y))
    print("      }")
    print("}")




#printMove(american_continent, 4, 0)
#printMove(africa, 9, 16)
#printMove(eu, 0, 18)
drawSavedMap(world, transformchange=0, text=True)
#printMove(asia, 2, 36)
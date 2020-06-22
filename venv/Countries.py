from math import sin, cos
#https://public.opendatasoft.com/explore/dataset/sverige-lan-counties-of-sweden/table/
#http://kodapan.se/geodata/
# https://geojson-maps.ash.ms/ !!!!!!
# geojson.io !!!!!

USA = {
    "regions" : 
        {
            "Maine" : {'coordinates': (-69.22532171969658, 45.36948088392073), 'neighbors': ['New Hampshire']},
            "Massachusetts" : {'coordinates': (-71.79545555710746, 42.25229282014122), 'neighbors': ['New York', 'Rhode Island', 'Connecticut', 'New Hampshire', 'Vermont']},
            "Michigan" : {'coordinates': (-85.43751121959318, 44.353227748974255), 'neighbors': ['Ohio', 'Wisconsin', 'Indiana']},
            "Montana" : {'coordinates': (-109.64506843658087, 47.033547910637424), 'neighbors': ['Idaho', 'North Dakota', 'South Dakota', 'Wyoming']},
            "Nevada" : {'coordinates': (-116.65539608977707, 39.356459156275726), 'neighbors': ['Utah', 'Arizona', 'California', 'Idaho', 'Oregon']},
            "New Jersey" : {'coordinates': (-74.66099163412024, 40.183926646067555), 'neighbors': ['New York', 'Pennsylvania', 'Delaware']},
            "New York" : {'coordinates': (-75.50198354788088, 42.93929513591405), 'neighbors': ['Massachusetts', 'New Jersey', 'Pennsylvania', 'Connecticut', 'Vermont']},
            "North Carolina" : {'coordinates': (-79.35541612056524, 35.53980403043663), 'neighbors': ['Tennessee', 'Georgia', 'South Carolina', 'Virginia']},
            "Ohio" : {'coordinates': (-82.7901769841484, 40.293328455794956), 'neighbors': ['Michigan', 'Pennsylvania', 'Indiana', 'Kentucky', 'West Virginia']},
            "Pennsylvania" : {'coordinates': (-77.79953189437393, 40.87381687285712), 'neighbors': ['New Jersey', 'New York', 'Ohio', 'Maryland', 'Delaware', 'West Virginia']},
            "Rhode Island" : {'coordinates': (-71.55250269935327, 41.676193552764225), 'neighbors': ['Massachusetts', 'Connecticut']},
            "Tennessee" : {'coordinates': (-86.3432909613107, 35.84298759864114), 'neighbors': ['North Carolina', 'Alabama', 'Arkansas', 'Georgia', 'Kentucky', 'Mississippi', 'Missouri', 'Virginia']},
            "Texas" : {'coordinates': (-99.35528230271987, 31.490514799872358), 'neighbors': ['Arkansas', 'Louisiana', 'New Mexico', 'Oklahoma']},
            "Utah" : {'coordinates': (-111.67820486515582, 39.323788862245614), 'neighbors': ['Nevada', 'Arizona', 'Colorado', 'Idaho', 'New Mexico', 'Wyoming']},
            "Washington" : {'coordinates': (-120.45017296280312, 47.38107777541827), 'neighbors': ['Idaho', 'Oregon']},
            "Wisconsin" : {'coordinates': (-90.01113174999028, 44.63829015646044), 'neighbors': ['Michigan', 'Illinois', 'Iowa', 'Minnesota']},
            "Maryland" : {'coordinates': (-76.76446080307487, 39.030413058293085), 'neighbors': ['Pennsylvania', 'Delaware', 'District of Columbia', 'Virginia', 'West Virginia']},
            "Alabama" : {'coordinates': (-86.82843467764218, 32.78969213202673), 'neighbors': ['Tennessee', 'Florida', 'Georgia', 'Mississippi']},
            "Arizona" : {'coordinates': (-111.66458282124002, 34.293260853221966), 'neighbors': ['Nevada', 'Utah', 'California', 'Colorado', 'New Mexico']},
            "Arkansas" : {'coordinates': (-92.43927556717503, 34.89974058219506), 'neighbors': ['Tennessee', 'Texas', 'Louisiana', 'Mississippi', 'Missouri', 'Oklahoma']},
            "California" : {'coordinates': (-119.61076705882292, 37.2461209740046), 'neighbors': ['Nevada', 'Arizona', 'Oregon']},
            "Colorado" : {'coordinates': (-105.54781991091092, 38.998549290485606), 'neighbors': ['Utah', 'Arizona', 'Kansas', 'Nebraska', 'New Mexico', 'Oklahoma', 'Wyoming']},
            "Connecticut" : {'coordinates': (-72.72576286018278, 41.620550069867356), 'neighbors': ['Massachusetts', 'New York', 'Rhode Island']},
            "Delaware" : {'coordinates': (-75.50017652512045, 38.99177706648977), 'neighbors': ['New Jersey', 'Pennsylvania', 'Maryland']},
            "District of Columbia" : {'coordinates': (-77.01629978160432, 38.90472697478343), 'neighbors': ['Maryland', 'Virginia']},
            "Florida" : {'coordinates': (-82.50162321295583, 28.640962840519993), 'neighbors': ['Alabama', 'Georgia']},
            "Georgia" : {'coordinates': (-83.44606104105794, 32.64908013932673), 'neighbors': ['North Carolina', 'Tennessee', 'Alabama', 'Florida', 'South Carolina']},
            "Idaho" : {'coordinates': (-114.65932614019067, 44.38912388040411), 'neighbors': ['Montana', 'Nevada', 'Utah', 'Washington', 'Oregon', 'Wyoming']},
            "Illinois" : {'coordinates': (-89.19828243150049, 40.064744278543486), 'neighbors': ['Wisconsin', 'Indiana', 'Iowa', 'Kentucky', 'Missouri']},
            "Indiana" : {'coordinates': (-86.27528896249993, 39.90853156291497), 'neighbors': ['Michigan', 'Ohio', 'Illinois', 'Kentucky']},
            "Iowa" : {'coordinates': (-93.50003752656892, 42.07461994318595), 'neighbors': ['Wisconsin', 'Illinois', 'Minnesota', 'Missouri', 'Nebraska', 'South Dakota']},
            "Kansas" : {'coordinates': (-98.38021576885671, 38.484699232527994), 'neighbors': ['Colorado', 'Missouri', 'Nebraska', 'Oklahoma']},
            "Kentucky" : {'coordinates': (-85.29049099257188, 37.52666180142173), 'neighbors': ['Ohio', 'Tennessee', 'Illinois', 'Indiana', 'Missouri', 'Virginia', 'West Virginia']},
            "Louisiana" : {'coordinates': (-91.98047958435316, 31.052640279723146), 'neighbors': ['Texas', 'Arkansas', 'Mississippi']},
            "Minnesota" : {'coordinates': (-94.30869910827926, 46.31644638252222), 'neighbors': ['Wisconsin', 'Iowa', 'North Dakota', 'South Dakota']},
            "Mississippi" : {'coordinates': (-89.66510236112605, 32.75039751207963), 'neighbors': ['Tennessee', 'Alabama', 'Arkansas', 'Louisiana']},
            "Missouri" : {'coordinates': (-92.47742177522969, 38.367615587136335), 'neighbors': ['Tennessee', 'Arkansas', 'Illinois', 'Iowa', 'Kansas', 'Kentucky', 'Nebraska', 'Oklahoma']},
            "Nebraska" : {'coordinates': (-99.81080403010135, 41.527145632413614), 'neighbors': ['Colorado', 'Iowa', 'Kansas', 'Missouri', 'South Dakota', 'Wyoming']},
            "New Hampshire" : {'coordinates': (-71.57760331998418, 43.68568569263635), 'neighbors': ['Maine', 'Massachusetts', 'Vermont']},
            "New Mexico" : {'coordinates': (-106.10837873693659, 34.42136536928094), 'neighbors': ['Texas', 'Utah', 'Arizona', 'Colorado', 'Oklahoma']},
            "North Dakota" : {'coordinates': (-100.46931454621287, 47.446336034226874), 'neighbors': ['Montana', 'Minnesota', 'South Dakota']},
            "Oklahoma" : {'coordinates': (-97.50844066270588, 35.58349594000576), 'neighbors': ['Texas', 'Arkansas', 'Colorado', 'Kansas', 'Missouri', 'New Mexico']},
            "Oregon" : {'coordinates': (-120.55529048244831, 43.93673097459646), 'neighbors': ['Nevada', 'Washington', 'California', 'Idaho']},
            "South Carolina" : {'coordinates': (-80.89549885791106, 33.90710470638993), 'neighbors': ['North Carolina', 'Georgia']},
            "South Dakota" : {'coordinates': (-100.23048944341096, 44.43615201832776), 'neighbors': ['Montana', 'Iowa', 'Minnesota', 'Nebraska', 'North Dakota', 'Wyoming']},
            "Vermont" : {'coordinates': (-72.66271648660559, 44.07518209714273), 'neighbors': ['Massachusetts', 'New York', 'New Hampshire']},
            "Virginia" : {'coordinates': (-78.80562363153308, 37.515389784521176), 'neighbors': ['North Carolina', 'Tennessee', 'Maryland', 'District of Columbia', 'Kentucky', 'West Virginia']},
            "West Virginia" : {'coordinates': (-80.61385445603683, 38.642510057228655), 'neighbors': ['Ohio', 'Pennsylvania', 'Maryland', 'Kentucky', 'Virginia']},
            "Wyoming" : {'coordinates': (-107.55144626079414, 42.99963537644683), 'neighbors': ['Montana', 'Utah', 'Colorado', 'Idaho', 'Nebraska', 'South Dakota']}
        },
    "outliers" : 
        {
            "Alaska" : {"closest_to" : "Washington", "coordinates" : (-151.577762, 65.846764)},
            "Hawaii" : {"closest_to" : "California", "coordinates" : (-155.587776, 20.088784)}
        }
}


USA_full = {
"Maine" : {'coordinates': (-69.22532171969658, 45.36948088392073), 'neighbors': ['New Hampshire']},
"Massachusetts" : {'coordinates': (-71.79545555710746, 42.25229282014122), 'neighbors': ['New York', 'Rhode Island', 'Connecticut', 'New Hampshire', 'Vermont']},
"Michigan" : {'coordinates': (-85.43751121959318, 44.353227748974255), 'neighbors': ['Ohio', 'Wisconsin', 'Indiana']},
"Montana" : {'coordinates': (-109.64506843658087, 47.033547910637424), 'neighbors': ['Idaho', 'North Dakota', 'South Dakota', 'Wyoming']},
"Nevada" : {'coordinates': (-116.65539608977707, 39.356459156275726), 'neighbors': ['Utah', 'Arizona', 'California', 'Idaho', 'Oregon']},
"New Jersey" : {'coordinates': (-74.66099163412024, 40.183926646067555), 'neighbors': ['New York', 'Pennsylvania', 'Delaware']},
"New York" : {'coordinates': (-75.50198354788088, 42.93929513591405), 'neighbors': ['Massachusetts', 'New Jersey', 'Pennsylvania', 'Connecticut', 'Vermont']},
"North Carolina" : {'coordinates': (-79.35541612056524, 35.53980403043663), 'neighbors': ['Tennessee', 'Georgia', 'South Carolina', 'Virginia']},
"Ohio" : {'coordinates': (-82.7901769841484, 40.293328455794956), 'neighbors': ['Michigan', 'Pennsylvania', 'Indiana', 'Kentucky', 'West Virginia']},
"Pennsylvania" : {'coordinates': (-77.79953189437393, 40.87381687285712), 'neighbors': ['New Jersey', 'New York', 'Ohio', 'Maryland', 'Delaware', 'West Virginia']},
"Rhode Island" : {'coordinates': (-71.55250269935327, 41.676193552764225), 'neighbors': ['Massachusetts', 'Connecticut']},
"Tennessee" : {'coordinates': (-86.3432909613107, 35.84298759864114), 'neighbors': ['North Carolina', 'Alabama', 'Arkansas', 'Georgia', 'Kentucky', 'Mississippi', 'Missouri', 'Virginia']},
"Texas" : {'coordinates': (-99.35528230271987, 31.490514799872358), 'neighbors': ['Arkansas', 'Louisiana', 'New Mexico', 'Oklahoma']},
"Utah" : {'coordinates': (-111.67820486515582, 39.323788862245614), 'neighbors': ['Nevada', 'Arizona', 'Colorado', 'Idaho', 'New Mexico', 'Wyoming']},
"Washington" : {'coordinates': (-120.45017296280312, 47.38107777541827), 'neighbors': ['Idaho', 'Oregon']},
"Wisconsin" : {'coordinates': (-90.01113174999028, 44.63829015646044), 'neighbors': ['Michigan', 'Illinois', 'Iowa', 'Minnesota']},
"Puerto Rico" : {'coordinates': (-66.46619956833777, 18.22274629022535), 'neighbors': []},
"Maryland" : {'coordinates': (-76.76446080307487, 39.030413058293085), 'neighbors': ['Pennsylvania', 'Delaware', 'District of Columbia', 'Virginia', 'West Virginia']},
"Alabama" : {'coordinates': (-86.82843467764218, 32.78969213202673), 'neighbors': ['Tennessee', 'Florida', 'Georgia', 'Mississippi']},
"Alaska" : {'coordinates': (-152.2230675122248, 64.20984281728794), 'neighbors': []},
"Arizona" : {'coordinates': (-111.66458282124002, 34.293260853221966), 'neighbors': ['Nevada', 'Utah', 'California', 'Colorado', 'New Mexico']},
"Arkansas" : {'coordinates': (-92.43927556717503, 34.89974058219506), 'neighbors': ['Tennessee', 'Texas', 'Louisiana', 'Mississippi', 'Missouri', 'Oklahoma']},
"California" : {'coordinates': (-119.61076705882292, 37.2461209740046), 'neighbors': ['Nevada', 'Arizona', 'Oregon']},
"Colorado" : {'coordinates': (-105.54781991091092, 38.998549290485606), 'neighbors': ['Utah', 'Arizona', 'Kansas', 'Nebraska', 'New Mexico', 'Oklahoma', 'Wyoming']},
"Connecticut" : {'coordinates': (-72.72576286018278, 41.620550069867356), 'neighbors': ['Massachusetts', 'New York', 'Rhode Island']},
"Delaware" : {'coordinates': (-75.50017652512045, 38.99177706648977), 'neighbors': ['New Jersey', 'Pennsylvania', 'Maryland']},
"District of Columbia" : {'coordinates': (-77.01629978160432, 38.90472697478343), 'neighbors': ['Maryland', 'Virginia']},
"Florida" : {'coordinates': (-82.50162321295583, 28.640962840519993), 'neighbors': ['Alabama', 'Georgia']},
"Georgia" : {'coordinates': (-83.44606104105794, 32.64908013932673), 'neighbors': ['North Carolina', 'Tennessee', 'Alabama', 'Florida', 'South Carolina']},
"Hawaii" : {'coordinates': (-156.3835256019836, 20.262886701493127), 'neighbors': []},
"Idaho" : {'coordinates': (-114.65932614019067, 44.38912388040411), 'neighbors': ['Montana', 'Nevada', 'Utah', 'Washington', 'Oregon', 'Wyoming']},
"Illinois" : {'coordinates': (-89.19828243150049, 40.064744278543486), 'neighbors': ['Wisconsin', 'Indiana', 'Iowa', 'Kentucky', 'Missouri']},
"Indiana" : {'coordinates': (-86.27528896249993, 39.90853156291497), 'neighbors': ['Michigan', 'Ohio', 'Illinois', 'Kentucky']},
"Iowa" : {'coordinates': (-93.50003752656892, 42.07461994318595), 'neighbors': ['Wisconsin', 'Illinois', 'Minnesota', 'Missouri', 'Nebraska', 'South Dakota']},
"Kansas" : {'coordinates': (-98.38021576885671, 38.484699232527994), 'neighbors': ['Colorado', 'Missouri', 'Nebraska', 'Oklahoma']},
"Kentucky" : {'coordinates': (-85.29049099257188, 37.52666180142173), 'neighbors': ['Ohio', 'Tennessee', 'Illinois', 'Indiana', 'Missouri', 'Virginia', 'West Virginia']},
"Louisiana" : {'coordinates': (-91.98047958435316, 31.052640279723146), 'neighbors': ['Texas', 'Arkansas', 'Mississippi']},
"Minnesota" : {'coordinates': (-94.30869910827926, 46.31644638252222), 'neighbors': ['Wisconsin', 'Iowa', 'North Dakota', 'South Dakota']},
"Mississippi" : {'coordinates': (-89.66510236112605, 32.75039751207963), 'neighbors': ['Tennessee', 'Alabama', 'Arkansas', 'Louisiana']},
"Missouri" : {'coordinates': (-92.47742177522969, 38.367615587136335), 'neighbors': ['Tennessee', 'Arkansas', 'Illinois', 'Iowa', 'Kansas', 'Kentucky', 'Nebraska', 'Oklahoma']},
"Nebraska" : {'coordinates': (-99.81080403010135, 41.527145632413614), 'neighbors': ['Colorado', 'Iowa', 'Kansas', 'Missouri', 'South Dakota', 'Wyoming']},
"New Hampshire" : {'coordinates': (-71.57760331998418, 43.68568569263635), 'neighbors': ['Maine', 'Massachusetts', 'Vermont']},
"New Mexico" : {'coordinates': (-106.10837873693659, 34.42136536928094), 'neighbors': ['Texas', 'Utah', 'Arizona', 'Colorado', 'Oklahoma']},
"North Dakota" : {'coordinates': (-100.46931454621287, 47.446336034226874), 'neighbors': ['Montana', 'Minnesota', 'South Dakota']},
"Oklahoma" : {'coordinates': (-97.50844066270588, 35.58349594000576), 'neighbors': ['Texas', 'Arkansas', 'Colorado', 'Kansas', 'Missouri', 'New Mexico']},
"Oregon" : {'coordinates': (-120.55529048244831, 43.93673097459646), 'neighbors': ['Nevada', 'Washington', 'California', 'Idaho']},
"South Carolina" : {'coordinates': (-80.89549885791106, 33.90710470638993), 'neighbors': ['North Carolina', 'Georgia']},
"South Dakota" : {'coordinates': (-100.23048944341096, 44.43615201832776), 'neighbors': ['Montana', 'Iowa', 'Minnesota', 'Nebraska', 'North Dakota', 'Wyoming']},
"Vermont" : {'coordinates': (-72.66271648660559, 44.07518209714273), 'neighbors': ['Massachusetts', 'New York', 'New Hampshire']},
"Virginia" : {'coordinates': (-78.80562363153308, 37.515389784521176), 'neighbors': ['North Carolina', 'Tennessee', 'Maryland', 'District of Columbia', 'Kentucky', 'West Virginia']},
"West Virginia" : {'coordinates': (-80.61385445603683, 38.642510057228655), 'neighbors': ['Ohio', 'Pennsylvania', 'Maryland', 'Kentucky', 'Virginia']},
"Wyoming" : {'coordinates': (-107.55144626079414, 42.99963537644683), 'neighbors': ['Montana', 'Utah', 'Colorado', 'Idaho', 'Nebraska', 'South Dakota']}
}


sweden = {
    "regions": 
        {
            "Norrbotten":       {"coordinates": (20.4, 66.8), "neighbors" : ["Västerbotten"]},
            "Västerbotten":     {"coordinates": (16.5, 65.4), "neighbors" : ["Norrbotten", "Västernorrland", "Jämtland"]},
            "Västernorrland":   {"coordinates": (17.7, 63.4), "neighbors" : ["Västerbotten", "Jämtland", "Gävleborg"]},
            "Jämtland":         {"coordinates": (14.9, 63.2), "neighbors" : ["Västerbotten", "Västernorrland", "Gävleborg", "Dalarna"]},
            "Gävleborg":        {"coordinates": (16.1, 61.2), "neighbors" : ["Västernorrland", "Jämtland", "Dalarna", "Västmanland"]},
            "Dalarna":          {"coordinates": (14.7, 61.0), "neighbors" : ["Gävleborg", "Jämtland", "Västmanland", "Örebro", "Värmland"]},
            "Uppsala":          {"coordinates": (17.3, 60.0), "neighbors" : ["Gävleborg", "Västmanland", "Stockholms län", "Södermanland"]},
            "Värmland":         {"coordinates": (13.2, 59.7), "neighbors" : ["Dalarna", "Örebro", "Dalarna"]},
            "Västmanland":      {"coordinates": (16.2, 59.6), "neighbors" : ["Gävleborg", "Dalarna", "Örebro", "Södermanland", "Stockholms län", "Uppsala"]},
            "Stockholms län":   {"coordinates": (18.1, 59.6), "neighbors" : ["Uppsala", "Södermanland"]},
            "Örebro":           {"coordinates": (14.0, 59.5), "neighbors" : ["Dalarna", "Värmland", "Östergötland"]},
            "Södermanland":     {"coordinates": (16.7, 59.0), "neighbors" : ["Stockholms län", "Uppsala", "Västmanland", "Örebro", "Östergötland"]},
            "Östergötland":     {"coordinates": (15.5, 58.3), "neighbors" : ["Södermanland", "Örebro", "Västra Götaland", "Jönköping", "Kalmar"]},
            "Jönköping" :       {"coordinates": (14.2, 57.7), "neighbors" : ["Östergötland", "Västra Götaland", "Halland", "Kronoberg", "Kalmar"]},
            "Västra Götaland":  {"coordinates": (13.0, 58.2), "neighbors" : ["Värmland", "Örebro", "Östergötland", "Jönköping", "Halland"]},
            "Kalmar":           {"coordinates": (16.2, 57.2), "neighbors" : ["Östergötland", "Jönköping", "Kronoberg", "Blekinge"]},
            "Halland":          {"coordinates": (12.8, 56.9), "neighbors" : ["Västra Götaland", "Jönköping", "Kronoberg", "Skåne"]},
            "Kronoberg":        {"coordinates": (14.4, 56.7), "neighbors" : ["Jönköping", "Kalmar", "Blekinge", "Skåne", "Halland"]},
            "Blekinge":         {"coordinates": (15.0, 56.2), "neighbors" : ["Kalmar", "Kronoberg", "Skåne"]},
            "Skåne":            {"coordinates": (13.5, 55.9), "neighbors" : ["Halland", "Kronoberg", "Blekinge"]}
    },
    "outliers":
        {
            "Gotland": {"closest_to" : "Kalmar", "coordinates": (18.49, 57.38)}
        }
}
sweden_border = [(20.6, 69.0), (23.7, 67.9), (23.9, 65.7), (22.3, 65.8), (21.5, 64.4), (18.0, 62.7), (17.3, 61.0), (19.3, 59.6), (18.3, 59.0), (16.6, 57.7), (16.1, 56.1), (14.3, 55.4), (12.9, 55.4), (12.1, 55.3), #(12.8, 56.5),
                 (11.8, 57.7), (11.2, 59.0), (12.2, 63.5), (16.5, 67.6)]

def genCircleBorder(mid, rad, step):
    border = []
    i = 0
    while i < 3.141592*2:
        border.append((cos(i)*rad + mid[0], sin(i)*rad + mid[1]))
        i += step
    return border

circle_border = genCircleBorder((-90, 30), 30, 0.05)


sweden_municipalities = {
    "regions" :
        {
            "Norrtälje" : {'coordinates': (18.839739305485477, 59.78848776839939), 'neighbors': ['Sigtuna', 'Värmdö', 'Knivsta', 'Vallentuna', 'Österåker', 'Östhammar', 'Uppsala']},
            "Sigtuna" : {'coordinates': (17.890804077413094, 59.648408222048815), 'neighbors': ['Norrtälje', 'Upplands Väsby', 'Knivsta', 'Vallentuna', 'Håbo', 'Upplands-Bro']},
            "Nynäshamn" : {'coordinates': (17.884630999725996, 58.897588766845736), 'neighbors': ['Trosa', 'Botkyrka', 'Södertälje', 'Haninge']},
            "Varberg" : {'coordinates': (12.381207822159372, 57.18040253113724), 'neighbors': ['Mark', 'Kungsbacka', 'Falkenberg']},
            "Krokom" : {'coordinates': (14.209732015941956, 63.77779044855708), 'neighbors': ['Åre', 'Östersund', 'Strömsund']},
            "Solna" : {'coordinates': (18.00831570570283, 59.36902593127), 'neighbors': ['Sundbyberg', 'Danderyd', 'Sollentuna', 'Stockholm']},
            "Strömstad" : {'coordinates': (11.229937467038889, 58.9465410070105), 'neighbors': ['Tanum']},
            "Tidaholm" : {'coordinates': (13.944818415637423, 58.14708427352214), 'neighbors': ['Habo', 'Skövde', 'Falköping', 'Mullsjö', 'Hjo']},
            "Forshaga" : {'coordinates': (13.508181472682814, 59.651413973708124), 'neighbors': ['Hagfors', 'Kil', 'Munkfors', 'Sunne', 'Karlstad']},
            "Ludvika" : {'coordinates': (14.762383709271514, 60.182030662161466), 'neighbors': ['Hällefors', 'Gagnef', 'Vansbro', 'Borlänge', 'Smedjebacken', 'Ljusnarsberg', 'Filipstad', 'Säter']},
            "Örnsköldsvik" : {'coordinates': (18.266196047446098, 63.527221771983946), 'neighbors': ['Sollefteå', 'Kramfors', 'Bjurholm', 'Åsele', 'Nordmaling']},
            "Gällivare" : {'coordinates': (20.078249256569308, 67.28925686170342), 'neighbors': ['Jokkmokk', 'Överkalix', 'Pajala', 'Boden', 'Kiruna']},
            "Upplands Väsby" : {'coordinates': (17.90517183776612, 59.52132448583391), 'neighbors': ['Sigtuna', 'Järfälla', 'Vallentuna', 'Sollentuna', 'Upplands-Bro', 'Täby']},
            "Trosa" : {'coordinates': (17.568079698821233, 58.82927922197026), 'neighbors': ['Nynäshamn', 'Nyköping', 'Södertälje', 'Gnesta']},
            "Gnosjö" : {'coordinates': (13.804517654303734, 57.35635493830691), 'neighbors': ['Värnamo', 'Gislaved', 'Vaggeryd']},
            #"Gotland" : {'coordinates': (18.55607963676659, 57.509142020563), 'neighbors': []},
            "Hässleholm" : {'coordinates': (13.724484904332684, 56.20270994976344), 'neighbors': ['Kristianstad', 'Klippan', 'Hörby', 'Örkelljunga', 'Höör', 'Osby', 'Perstorp', 'Markaryd', 'Östra Göinge']},
            "Tibro" : {'coordinates': (14.222103436695894, 58.451250378035496), 'neighbors': ['Skövde', 'Töreboda', 'Hjo', 'Karlsborg']},
            "Ulricehamn" : {'coordinates': (13.46237369383691, 57.811328151373786), 'neighbors': ['Herrljunga', 'Tranemo', 'Borås', 'Falköping', 'Mullsjö', 'Jönköping']},
            "Mariestad" : {'coordinates': (13.805561164522059, 58.748727857610454), 'neighbors': ['Gullspång', 'Skövde', 'Töreboda', 'Götene']},
            "Hofors" : {'coordinates': (16.418345035252838, 60.491262860068105), 'neighbors': ['Hedemora', 'Sandviken', 'Avesta']},
            "Hudiksvall" : {'coordinates': (16.822103362189914, 61.775347298015426), 'neighbors': ['Bollnäs', 'Nordanstig', 'Ljusdal', 'Söderhamn']},
            "Sollefteå" : {'coordinates': (16.885540431857798, 63.44029295821205), 'neighbors': ['Örnsköldsvik', 'Kramfors', 'Härnösand', 'Timrå', 'Dorotea', 'Ragunda', 'Sundsvall', 'Åsele', 'Strömsund']},
            "Lycksele" : {'coordinates': (18.460158592484838, 64.65375822554225), 'neighbors': ['Malå', 'Sorsele', 'Storuman', 'Norsjö', 'Bjurholm', 'Åsele', 'Vindeln', 'Vilhelmina']},
            "Lidingö" : {'coordinates': (18.18137226822699, 59.364668949282766), 'neighbors': ['Nacka', 'Vaxholm', 'Danderyd', 'Stockholm']},
            "Sävsjö" : {'coordinates': (14.58126353681224, 57.327818096926975), 'neighbors': ['Växjö', 'Vetlanda', 'Värnamo', 'Vaggeryd', 'Alvesta', 'Nässjö']},
            "Herrljunga" : {'coordinates': (13.110748348375713, 58.01323184985013), 'neighbors': ['Ulricehamn', 'Vara', 'Borås', 'Falköping', 'Vårgårda', 'Essunga']},
            "Kungälv" : {'coordinates': (11.801273439357372, 57.890403929767956), 'neighbors': ['Lilla Edet', 'Göteborg', 'Tjörn', 'Stenungsund', 'Öckerö', 'Ale']},
            "Örebro" : {'coordinates': (15.331307978256666, 59.263752880526155), 'neighbors': ['Hallsberg', 'Arboga', 'Finspång', 'Katrineholm', 'Vingåker', 'Lindesberg', 'Kumla', 'Lekeberg', 'Nora', 'Karlskoga']},
            "Jokkmokk" : {'coordinates': (18.649624020583257, 66.89779018087208), 'neighbors': ['Gällivare', 'Arvidsjaur', 'Arjeplog', 'Älvsbyn', 'Boden']},
            "Övertorneå" : {'coordinates': (23.49894505282695, 66.53024418736368), 'neighbors': ['Överkalix', 'Haparanda', 'Kalix', 'Pajala']},
            "Järfälla" : {'coordinates': (17.818667965444966, 59.43328048964999), 'neighbors': ['Upplands Väsby', 'Ekerö', 'Sollentuna', 'Upplands-Bro', 'Stockholm']},
            "Nyköping" : {'coordinates': (16.989691196561473, 58.79320070933011), 'neighbors': ['Trosa', 'Norrköping', 'Flen', 'Katrineholm', 'Gnesta', 'Oxelösund']},
            "Växjö" : {'coordinates': (14.87361132432785, 56.93123602401158), 'neighbors': ['Sävsjö', 'Vetlanda', 'Alvesta', 'Tingsryd', 'Uppvidinge', 'Lessebo']},
            "Högsby" : {'coordinates': (15.934651236412446, 57.134210618475414), 'neighbors': ['Oskarshamn', 'Hultsfred', 'Uppvidinge', 'Mönsterås', 'Nybro']},
            "Åstorp" : {'coordinates': (12.991730643142429, 56.130887544362224), 'neighbors': ['Helsingborg', 'Klippan', 'Ängelholm', 'Svalöv', 'Bjuv']},
            "Sotenäs" : {'coordinates': (11.301615190461153, 58.40371426931668), 'neighbors': ['Lysekil', 'Munkedal', 'Tanum']},
            "Mellerud" : {'coordinates': (12.42326304729376, 58.69814871404429), 'neighbors': ['Åmål', 'Vänersborg', 'Färgelanda', 'Bengtsfors']},
            "Hallsberg" : {'coordinates': (15.245349799365117, 59.00381802190696), 'neighbors': ['Örebro', 'Askersund', 'Motala', 'Finspång', 'Kumla', 'Lekeberg', 'Laxå']},
            "Ånge" : {'coordinates': (15.72178058703437, 62.47270466716457), 'neighbors': ['Berg', 'Bräcke', 'Nordanstig', 'Sundsvall', 'Härjedalen']},
            "Kramfors" : {'coordinates': (17.97605079942429, 62.97804068052199), 'neighbors': ['Örnsköldsvik', 'Sollefteå', 'Härnösand']},
            "Överkalix" : {'coordinates': (22.584234604621745, 66.46589644690306), 'neighbors': ['Gällivare', 'Övertorneå', 'Luleå', 'Kalix', 'Pajala', 'Boden']},
            "Luleå" : {'coordinates': (22.218052547647765, 65.70345651193931), 'neighbors': ['Överkalix', 'Kalix', 'Älvsbyn', 'Boden', 'Piteå']},
            "Värmdö" : {'coordinates': (18.803443126554445, 59.30866592279618), 'neighbors': ['Norrtälje', 'Nacka', 'Österåker', 'Vaxholm', 'Tyresö', 'Haninge']},
            "Sundbyberg" : {'coordinates': (17.96020464100769, 59.37828798107331), 'neighbors': ['Solna', 'Sollentuna', 'Stockholm']},
            "Heby" : {'coordinates': (17.01486161879805, 60.08922585529433), 'neighbors': ['Tierp', 'Enköping', 'Sandviken', 'Sala', 'Gävle', 'Uppsala']},
            "Boxholm" : {'coordinates': (15.12217234362079, 58.1422172700099), 'neighbors': ['Ydre', 'Mjölby', 'Ödeshög', 'Tranås', 'Kinda', 'Linköping']},
            "Norrköping" : {'coordinates': (16.38101121180749, 58.59067082101151), 'neighbors': ['Nyköping', 'Finspång', 'Katrineholm', 'Söderköping', 'Linköping']},
            "Aneby" : {'coordinates': (14.79578296186173, 57.86561191616024), 'neighbors': ['Ydre', 'Eksjö', 'Tranås', 'Nässjö', 'Jönköping']},
            "Härryda" : {'coordinates': (12.31961659487797, 57.66945825873167), 'neighbors': ['Göteborg', 'Lerum', 'Partille', 'Mark', 'Mölndal', 'Bollebygd']},
            "Trollhättan" : {'coordinates': (12.347059460438835, 58.21772132307189), 'neighbors': ['Lilla Edet', 'Vänersborg', 'Alingsås', 'Grästorp', 'Ale', 'Essunga']},
            "Årjäng" : {'coordinates': (12.081334274121687, 59.42457404488395), 'neighbors': ['Arvika', 'Eda', 'Bengtsfors', 'Säffle']},
            "Hagfors" : {'coordinates': (13.630789147626993, 60.08427414255917), 'neighbors': ['Forshaga', 'Torsby', 'Munkfors', 'Sunne', 'Karlstad', 'Malung-Sälen', 'Filipstad']},
            "Leksand" : {'coordinates': (14.928915849061797, 60.71818350773783), 'neighbors': ['Gagnef', 'Rättvik', 'Vansbro', 'Mora', 'Borlänge', 'Falun']},
            "Ockelbo" : {'coordinates': (16.573701747785943, 60.924934808289336), 'neighbors': ['Bollnäs', 'Sandviken', 'Falun', 'Gävle', 'Söderhamn']},
            "Härnösand" : {'coordinates': (17.72429173690285, 62.71303107493376), 'neighbors': ['Sollefteå', 'Kramfors', 'Timrå']},
            "Haparanda" : {'coordinates': (23.818248495955036, 65.84633347721186), 'neighbors': ['Övertorneå', 'Kalix']},
            "Ekerö" : {'coordinates': (17.648596457623615, 59.352279073925814), 'neighbors': ['Järfälla', 'Enköping', 'Salem', 'Botkyrka', 'Södertälje', 'Upplands-Bro', 'Stockholm', 'Strängnäs', 'Huddinge']},
            "Knivsta" : {'coordinates': (17.857889012669688, 59.75431104259707), 'neighbors': ['Norrtälje', 'Sigtuna', 'Håbo', 'Uppsala']},
            "Vetlanda" : {'coordinates': (15.159924062697558, 57.36714004541035), 'neighbors': ['Sävsjö', 'Växjö', 'Eksjö', 'Hultsfred', 'Uppvidinge', 'Nässjö']},
            "Emmaboda" : {'coordinates': (15.554403512659551, 56.63611485425439), 'neighbors': ['Karlskrona', 'Kalmar', 'Tingsryd', 'Torsås', 'Lessebo', 'Nybro', 'Ronneby']},
            "Lund" : {'coordinates': (13.373024897698855, 55.66777537965461), 'neighbors': ['Eslöv', 'Skurup', 'Svedala', 'Sjöbo', 'Kävlinge', 'Lomma', 'Staffanstorp']},
            "Lilla Edet" : {'coordinates': (12.142353576319692, 58.13303391649139), 'neighbors': ['Kungälv', 'Trollhättan', 'Vänersborg', 'Stenungsund', 'Uddevalla', 'Alingsås', 'Ale']},
            "Åmål" : {'coordinates': (12.58715668333265, 58.99240819787407), 'neighbors': ['Mellerud', 'Bengtsfors', 'Säffle']},
            "Hällefors" : {'coordinates': (14.616687077914, 59.777716727559756), 'neighbors': ['Ludvika', 'Storfors', 'Lindesberg', 'Nora', 'Ljusnarsberg', 'Karlskoga', 'Filipstad']},
            "Hedemora" : {'coordinates': (16.06020263144781, 60.3546485340844), 'neighbors': ['Hofors', 'Norberg', 'Smedjebacken', 'Falun', 'Avesta', 'Säter']},
            "Bollnäs" : {'coordinates': (16.37811075509578, 61.31248695066982), 'neighbors': ['Hudiksvall', 'Ockelbo', 'Ovanåker', 'Falun', 'Ljusdal', 'Söderhamn']},
            "Skellefteå" : {'coordinates': (20.593364291560235, 64.80639381427078), 'neighbors': ['Arvidsjaur', 'Umeå', 'Norsjö', 'Robertsfors', 'Vindeln', 'Piteå']},
            "Tierp" : {'coordinates': (17.666920039642633, 60.388799799466405), 'neighbors': ['Heby', 'Östhammar', 'Älvkarleby', 'Gävle', 'Uppsala']},
            "Enköping" : {'coordinates': (17.143486745685564, 59.66318261170238), 'neighbors': ['Heby', 'Ekerö', 'Håbo', 'Upplands-Bro', 'Sala', 'Strängnäs', 'Västerås', 'Uppsala']},
            "Ydre" : {'coordinates': (15.255096829281511, 57.8554999089591), 'neighbors': ['Boxholm', 'Aneby', 'Eksjö', 'Tranås', 'Kinda', 'Vimmerby']},
            "Valdemarsvik" : {'coordinates': (16.68491250601178, 58.19379658838357), 'neighbors': ['Åtvidaberg', 'Söderköping', 'Västervik']},
            "Ljungby" : {'coordinates': (13.827688419759184, 56.81430692790502), 'neighbors': ['Halmstad', 'Laholm', 'Hylte', 'Värnamo', 'Gislaved', 'Alvesta', 'Älmhult', 'Markaryd']},
            "Bromölla" : {'coordinates': (14.49569216611394, 56.12437189776675), 'neighbors': ['Kristianstad', 'Sölvesborg', 'Olofström']},
            "Malmö" : {'coordinates': (13.010869915314654, 55.56553243542101), 'neighbors': ['Svedala', 'Burlöv', 'Vellinge', 'Lomma', 'Staffanstorp']},
            "Eslöv" : {'coordinates': (13.367547910583768, 55.835960068276655), 'neighbors': ['Lund', 'Klippan', 'Svalöv', 'Sjöbo', 'Kävlinge', 'Hörby', 'Höör']},
            "Halmstad" : {'coordinates': (12.967414295744232, 56.7441000012417), 'neighbors': ['Ljungby', 'Laholm', 'Hylte', 'Falkenberg']},
            "Göteborg" : {'coordinates': (11.88344206403496, 57.69293170582427), 'neighbors': ['Kungälv', 'Härryda', 'Lerum', 'Partille', 'Kungsbacka', 'Mölndal', 'Öckerö', 'Ale']},
            "Askersund" : {'coordinates': (14.953249972031042, 58.853166115006424), 'neighbors': ['Hallsberg', 'Motala', 'Laxå', 'Karlsborg']},
            "Sandviken" : {'coordinates': (16.656728428713308, 60.54073252624249), 'neighbors': ['Hofors', 'Heby', 'Ockelbo', 'Sala', 'Falun', 'Avesta', 'Gävle']},
            "Arvidsjaur" : {'coordinates': (19.258794927789825, 65.68405449596814), 'neighbors': ['Jokkmokk', 'Skellefteå', 'Arjeplog', 'Malå', 'Älvsbyn', 'Sorsele', 'Norsjö', 'Piteå']},
            "Arjeplog" : {'coordinates': (17.239312159528293, 66.36484758961339), 'neighbors': ['Jokkmokk', 'Arvidsjaur', 'Sorsele']},
            "Kalix" : {'coordinates': (23.002790708876887, 65.91360467342076), 'neighbors': ['Övertorneå', 'Överkalix', 'Luleå', 'Haparanda']},
            "Nacka" : {'coordinates': (18.2543302497662, 59.3003399972132), 'neighbors': ['Lidingö', 'Värmdö', 'Vaxholm', 'Tyresö', 'Stockholm']},
            "Flen" : {'coordinates': (16.701712334521517, 59.06550699779402), 'neighbors': ['Nyköping', 'Eskilstuna', 'Katrineholm', 'Gnesta', 'Strängnäs']},
            "Mjölby" : {'coordinates': (15.167576538435238, 58.32287124396582), 'neighbors': ['Boxholm', 'Ödeshög', 'Motala', 'Vadstena', 'Linköping']},
            "Borgholm" : {'coordinates': (16.846355196617342, 56.990339446155126), 'neighbors': ['Mönsterås', 'Mörbylånga']},
            "Simrishamn" : {'coordinates': (14.20764549341289, 55.58104794290046), 'neighbors': ['Ystad', 'Kristianstad', 'Tomelilla']},
            "Laholm" : {'coordinates': (13.180138634254067, 56.501579007199226), 'neighbors': ['Ljungby', 'Halmstad', 'Båstad', 'Ängelholm', 'Örkelljunga', 'Markaryd']},
            "Dals-Ed" : {'coordinates': (11.885790123187832, 58.964526672177364), 'neighbors': ['Munkedal', 'Färgelanda', 'Tanum', 'Bengtsfors']},
            "Gullspång" : {'coordinates': (14.164413069659863, 58.9330014380733), 'neighbors': ['Mariestad', 'Degerfors', 'Töreboda', 'Laxå', 'Karlsborg', 'Kristinehamn']},
            "Vänersborg" : {'coordinates': (12.358089683150205, 58.456461991358225), 'neighbors': ['Mellerud', 'Trollhättan', 'Lilla Edet', 'Lidköping', 'Färgelanda', 'Uddevalla', 'Grästorp']},
            "Fagersta" : {'coordinates': (15.887079989097922, 59.94734113427747), 'neighbors': ['Norberg', 'Skinnskatteberg', 'Surahammar', 'Sala', 'Smedjebacken']},
            "Salem" : {'coordinates': (17.68925001287113, 59.23892372256209), 'neighbors': ['Ekerö', 'Botkyrka', 'Södertälje']},
            "Skurup" : {'coordinates': (13.54938451421161, 55.468979681759194), 'neighbors': ['Lund', 'Ystad', 'Svedala', 'Sjöbo', 'Trelleborg']},
            "Ystad" : {'coordinates': (13.896667479618817, 55.45962087967787), 'neighbors': ['Simrishamn', 'Skurup', 'Sjöbo', 'Tomelilla']},
            "Kristianstad" : {'coordinates': (14.15240852156035, 56.00055913144052), 'neighbors': ['Hässleholm', 'Bromölla', 'Simrishamn', 'Hörby', 'Olofström', 'Tomelilla', 'Osby', 'Östra Göinge']},
            "Hylte" : {'coordinates': (13.277700009295296, 56.974362381342104), 'neighbors': ['Ljungby', 'Halmstad', 'Gislaved', 'Falkenberg']},
            "Lerum" : {'coordinates': (12.324385779814945, 57.8247680535841), 'neighbors': ['Härryda', 'Göteborg', 'Partille', 'Bollebygd', 'Alingsås', 'Ale']},
            "Svenljunga" : {'coordinates': (13.061991348088672, 57.39037136037102), 'neighbors': ['Tranemo', 'Gislaved', 'Mark', 'Borås', 'Falkenberg']},
            "Lysekil" : {'coordinates': (11.448667333453274, 58.327690121858005), 'neighbors': ['Sotenäs', 'Munkedal', 'Uddevalla', 'Orust']},
            "Skara" : {'coordinates': (13.478008706833421, 58.37945804089786), 'neighbors': ['Lidköping', 'Skövde', 'Vara', 'Falköping', 'Götene']},
            "Degerfors" : {'coordinates': (14.424040373988737, 59.162656687614025), 'neighbors': ['Gullspång', 'Storfors', 'Lekeberg', 'Laxå', 'Karlskoga', 'Kristinehamn']},
            "Gagnef" : {'coordinates': (14.896129361773836, 60.47661462135913), 'neighbors': ['Ludvika', 'Leksand', 'Vansbro', 'Borlänge']},
            "Rättvik" : {'coordinates': (15.296746307220829, 61.11707434110786), 'neighbors': ['Leksand', 'Ovanåker', 'Mora', 'Orsa', 'Falun', 'Ljusdal']},
            "Timrå" : {'coordinates': (17.362847230883574, 62.613086068162254), 'neighbors': ['Sollefteå', 'Härnösand', 'Sundsvall']},
            "Dorotea" : {'coordinates': (15.909708858564088, 64.52098620889471), 'neighbors': ['Sollefteå', 'Åsele', 'Strömsund', 'Vilhelmina']},
            "Vännäs" : {'coordinates': (19.714928787518673, 63.94739054514875), 'neighbors': ['Umeå', 'Bjurholm', 'Nordmaling', 'Vindeln']},
            "Vallentuna" : {'coordinates': (18.19839184419877, 59.587649379669074), 'neighbors': ['Norrtälje', 'Sigtuna', 'Upplands Väsby', 'Österåker', 'Täby']},
            "Österåker" : {'coordinates': (18.55746055703722, 59.502043850427924), 'neighbors': ['Norrtälje', 'Värmdö', 'Vallentuna', 'Vaxholm', 'Danderyd', 'Täby']},
            "Botkyrka" : {'coordinates': (17.81998803298706, 59.158909944946274), 'neighbors': ['Nynäshamn', 'Ekerö', 'Salem', 'Södertälje', 'Huddinge', 'Haninge']},
            "Värnamo" : {'coordinates': (14.096227855772337, 57.147582365914616), 'neighbors': ['Gnosjö', 'Sävsjö', 'Ljungby', 'Gislaved', 'Vaggeryd', 'Alvesta']},
            "Oskarshamn" : {'coordinates': (16.424029802386443, 57.38647310605162), 'neighbors': ['Högsby', 'Hultsfred', 'Mönsterås', 'Vimmerby', 'Västervik']},
            "Helsingborg" : {'coordinates': (12.784200957141804, 56.06519317690568), 'neighbors': ['Åstorp', 'Landskrona', 'Höganäs', 'Ängelholm', 'Svalöv', 'Bjuv']},
            "Tranemo" : {'coordinates': (13.411303988014799, 57.5131768816277), 'neighbors': ['Ulricehamn', 'Svenljunga', 'Gislaved', 'Borås', 'Jönköping']},
            "Lidköping" : {'coordinates': (13.037970373939702, 58.50814954412647), 'neighbors': ['Vänersborg', 'Skara', 'Vara', 'Grästorp', 'Götene']},
            "Kil" : {'coordinates': (13.20208314074413, 59.57126386573509), 'neighbors': ['Forshaga', 'Arvika', 'Sunne', 'Karlstad', 'Grums']},
            "Berg" : {'coordinates': (13.783934310401964, 62.768894033799974), 'neighbors': ['Ånge', 'Bräcke', 'Åre', 'Östersund', 'Härjedalen']},
            "Vaxholm" : {'coordinates': (18.301919094159008, 59.40176492393627), 'neighbors': ['Lidingö', 'Värmdö', 'Nacka', 'Österåker', 'Danderyd', 'Täby']},
            "Ödeshög" : {'coordinates': (14.709744089750732, 58.203725474968195), 'neighbors': ['Boxholm', 'Mjölby', 'Vadstena', 'Tranås', 'Jönköping']},
            "Åtvidaberg" : {'coordinates': (16.110015809863768, 58.224347961289745), 'neighbors': ['Valdemarsvik', 'Kinda', 'Söderköping', 'Västervik', 'Linköping']},
            "Gislaved" : {'coordinates': (13.508039642888466, 57.25429607084459), 'neighbors': ['Gnosjö', 'Ljungby', 'Hylte', 'Svenljunga', 'Värnamo', 'Tranemo', 'Vaggeryd', 'Falkenberg', 'Jönköping']},
            "Partille" : {'coordinates': (12.12816722979807, 57.73167488651813), 'neighbors': ['Härryda', 'Göteborg', 'Lerum']},
            "Bräcke" : {'coordinates': (15.595917298415682, 62.856993047763744), 'neighbors': ['Ånge', 'Berg', 'Ragunda', 'Sundsvall', 'Östersund']},
            "Malå" : {'coordinates': (18.726285852572765, 65.23696430081674), 'neighbors': ['Lycksele', 'Arvidsjaur', 'Sorsele', 'Norsjö']},
            "Pajala" : {'coordinates': (22.89355664236559, 67.31506599300943), 'neighbors': ['Gällivare', 'Övertorneå', 'Överkalix', 'Kiruna']},
            "Habo" : {'coordinates': (14.062499341760969, 57.97073448583948), 'neighbors': ['Tidaholm', 'Mullsjö', 'Hjo', 'Jönköping']},
            "Vaggeryd" : {'coordinates': (14.122582004517524, 57.473264293659966), 'neighbors': ['Gnosjö', 'Sävsjö', 'Värnamo', 'Gislaved', 'Nässjö', 'Jönköping']},
            "Tjörn" : {'coordinates': (11.594331412109687, 57.99990185224475), 'neighbors': ['Kungälv', 'Stenungsund', 'Orust']},
            "Vansbro" : {'coordinates': (14.258656872032024, 60.44495348578173), 'neighbors': ['Ludvika', 'Leksand', 'Gagnef', 'Mora', 'Malung-Sälen', 'Filipstad']},
            "Ovanåker" : {'coordinates': (15.769932558943273, 61.3662767824036), 'neighbors': ['Bollnäs', 'Rättvik', 'Falun', 'Ljusdal']},
            "Håbo" : {'coordinates': (17.503355758967793, 59.62692716950793), 'neighbors': ['Sigtuna', 'Knivsta', 'Enköping', 'Upplands-Bro', 'Uppsala']},
            "Eskilstuna" : {'coordinates': (16.423831094564314, 59.31817723779169), 'neighbors': ['Flen', 'Arboga', 'Katrineholm', 'Strängnäs', 'Västerås', 'Kungsör', 'Hallstahammar']},
            "Motala" : {'coordinates': (15.170247087317422, 58.63143667042614), 'neighbors': ['Hallsberg', 'Askersund', 'Mjölby', 'Finspång', 'Vadstena', 'Linköping']},
            "Landskrona" : {'coordinates': (12.870098814254757, 55.890034379524785), 'neighbors': ['Helsingborg', 'Svalöv', 'Kävlinge']},
            "Norberg" : {'coordinates': (15.968916985070567, 60.076806507397066), 'neighbors': ['Hedemora', 'Fagersta', 'Sala', 'Smedjebacken', 'Avesta']},
            "Arboga" : {'coordinates': (15.785510253736568, 59.354835757498954), 'neighbors': ['Örebro', 'Eskilstuna', 'Katrineholm', 'Lindesberg', 'Köping', 'Kungsör']},
            "Ragunda" : {'coordinates': (16.055804868463696, 63.1875830026388), 'neighbors': ['Sollefteå', 'Bräcke', 'Sundsvall', 'Östersund', 'Strömsund']},
            "Umeå" : {'coordinates': (20.264712319507055, 63.88015809269144), 'neighbors': ['Skellefteå', 'Vännäs', 'Robertsfors', 'Nordmaling', 'Vindeln']},
            "Älvsbyn" : {'coordinates': (20.65803424564429, 65.74347503244326), 'neighbors': ['Jokkmokk', 'Luleå', 'Arvidsjaur', 'Boden', 'Piteå']},
            "Eksjö" : {'coordinates': (15.209333764365075, 57.61902291377261), 'neighbors': ['Aneby', 'Vetlanda', 'Ydre', 'Hultsfred', 'Vimmerby', 'Nässjö']},
            "Klippan" : {'coordinates': (13.2464469671731, 56.11181450567896), 'neighbors': ['Hässleholm', 'Åstorp', 'Eslöv', 'Ängelholm', 'Svalöv', 'Örkelljunga', 'Höör', 'Perstorp']},
            "Båstad" : {'coordinates': (12.76673145727683, 56.40287328088997), 'neighbors': ['Laholm', 'Ängelholm']},
            "Höganäs" : {'coordinates': (12.604260184657548, 56.22424514663041), 'neighbors': ['Helsingborg']},
            "Stenungsund" : {'coordinates': (11.902679379763436, 58.054848923679366), 'neighbors': ['Kungälv', 'Lilla Edet', 'Tjörn', 'Uddevalla', 'Orust']},
            "Mark" : {'coordinates': (12.606798033615876, 57.46420533771747), 'neighbors': ['Varberg', 'Härryda', 'Svenljunga', 'Kungsbacka', 'Mölndal', 'Borås', 'Bollebygd', 'Falkenberg']},
            "Nordanstig" : {'coordinates': (17.055972145455048, 62.05129854660697), 'neighbors': ['Hudiksvall', 'Ånge', 'Sundsvall', 'Ljusdal']},
            "Alvesta" : {'coordinates': (14.495686533536007, 56.84952430474396), 'neighbors': ['Sävsjö', 'Växjö', 'Ljungby', 'Värnamo', 'Älmhult', 'Tingsryd']},
            "Älmhult" : {'coordinates': (14.175186245094423, 56.57351976571412), 'neighbors': ['Ljungby', 'Alvesta', 'Tingsryd', 'Olofström', 'Osby', 'Markaryd']},
            "Karlskrona" : {'coordinates': (15.680019988526947, 56.25649453128314), 'neighbors': ['Emmaboda', 'Torsås', 'Ronneby']},
            "Ängelholm" : {'coordinates': (12.960987861240522, 56.26564899296439), 'neighbors': ['Åstorp', 'Laholm', 'Helsingborg', 'Klippan', 'Båstad', 'Örkelljunga']},
            "Kungsbacka" : {'coordinates': (12.091370135565608, 57.43634429624746), 'neighbors': ['Varberg', 'Göteborg', 'Mark', 'Mölndal']},
            "Skövde" : {'coordinates': (13.905375888683198, 58.42857436890089), 'neighbors': ['Tidaholm', 'Tibro', 'Mariestad', 'Skara', 'Töreboda', 'Falköping', 'Hjo', 'Götene']},
            "Storfors" : {'coordinates': (14.257452572033325, 59.48926665938474), 'neighbors': ['Hällefors', 'Degerfors', 'Karlstad', 'Karlskoga', 'Kristinehamn', 'Filipstad']},
            "Mora" : {'coordinates': (14.260213627863111, 61.03254608710586), 'neighbors': ['Leksand', 'Rättvik', 'Vansbro', 'Orsa', 'Malung-Sälen', 'Härjedalen', 'Älvdalen']},
            "Danderyd" : {'coordinates': (18.054439162018465, 59.406284801276136), 'neighbors': ['Solna', 'Lidingö', 'Österåker', 'Vaxholm', 'Sollentuna', 'Stockholm', 'Täby']},
            "Finspång" : {'coordinates': (15.776032793766054, 58.80469308985851), 'neighbors': ['Örebro', 'Hallsberg', 'Norrköping', 'Motala', 'Katrineholm', 'Vingåker', 'Linköping']},
            "Sollentuna" : {'coordinates': (17.93080146171378, 59.451140515353686), 'neighbors': ['Solna', 'Upplands Väsby', 'Järfälla', 'Sundbyberg', 'Danderyd', 'Stockholm', 'Täby']},
            "Katrineholm" : {'coordinates': (16.26671765567423, 59.013471819482355), 'neighbors': ['Örebro', 'Nyköping', 'Norrköping', 'Flen', 'Eskilstuna', 'Arboga', 'Finspång', 'Vingåker']},
            "Vadstena" : {'coordinates': (14.85268222366732, 58.41893052229876), 'neighbors': ['Mjölby', 'Ödeshög', 'Motala']},
            "Kalmar" : {'coordinates': (16.17039746587638, 56.68577503154672), 'neighbors': ['Emmaboda', 'Mönsterås', 'Torsås', 'Nybro']},
            "Svalöv" : {'coordinates': (13.12533940892315, 55.958591050243555), 'neighbors': ['Åstorp', 'Eslöv', 'Helsingborg', 'Landskrona', 'Klippan', 'Kävlinge', 'Bjuv']},
            "Svedala" : {'coordinates': (13.262274874542253, 55.534086820374284), 'neighbors': ['Lund', 'Malmö', 'Skurup', 'Vellinge', 'Staffanstorp', 'Trelleborg']},
            "Sjöbo" : {'coordinates': (13.744151768421938, 55.642772976031964), 'neighbors': ['Lund', 'Eslöv', 'Skurup', 'Ystad', 'Hörby', 'Tomelilla']},
            "Vara" : {'coordinates': (13.060490819403716, 58.245129630143126), 'neighbors': ['Herrljunga', 'Skara', 'Lidköping', 'Grästorp', 'Falköping', 'Essunga']},
            "Töreboda" : {'coordinates': (14.167425864543114, 58.67019935014932), 'neighbors': ['Tibro', 'Mariestad', 'Gullspång', 'Skövde', 'Laxå', 'Karlsborg']},
            "Mölndal" : {'coordinates': (12.090004971421537, 57.609245710306496), 'neighbors': ['Härryda', 'Göteborg', 'Mark', 'Kungsbacka']},
            "Arvika" : {'coordinates': (12.630230312814874, 59.68619445524468), 'neighbors': ['Årjäng', 'Kil', 'Torsby', 'Sunne', 'Eda', 'Grums', 'Säffle']},
            "Sorsele" : {'coordinates': (16.735520606724407, 65.72196483190709), 'neighbors': ['Lycksele', 'Arvidsjaur', 'Arjeplog', 'Malå', 'Storuman']},
            "Tyresö" : {'coordinates': (18.326630745500072, 59.21543384998606), 'neighbors': ['Värmdö', 'Nacka', 'Stockholm', 'Huddinge', 'Haninge']},
            "Södertälje" : {'coordinates': (17.54255050397588, 59.10235047198516), 'neighbors': ['Nynäshamn', 'Trosa', 'Ekerö', 'Salem', 'Botkyrka', 'Gnesta', 'Nykvarn', 'Strängnäs']},
            "Östhammar" : {'coordinates': (18.271448039151867, 60.2547811866141), 'neighbors': ['Norrtälje', 'Tierp', 'Uppsala']},
            "Gnesta" : {'coordinates': (17.148927597880178, 59.08227403584528), 'neighbors': ['Trosa', 'Nyköping', 'Flen', 'Södertälje', 'Nykvarn', 'Strängnäs']},
            "Hultsfred" : {'coordinates': (15.801699518244838, 57.39846507893624), 'neighbors': ['Högsby', 'Vetlanda', 'Oskarshamn', 'Eksjö', 'Uppvidinge', 'Vimmerby']},
            "Borås" : {'coordinates': (12.940844307416882, 57.7323030508009), 'neighbors': ['Ulricehamn', 'Herrljunga', 'Svenljunga', 'Tranemo', 'Mark', 'Bollebygd', 'Vårgårda']},
            "Borlänge" : {'coordinates': (15.360673914280378, 60.4488964807476), 'neighbors': ['Ludvika', 'Leksand', 'Gagnef', 'Smedjebacken', 'Falun', 'Säter']},
            "Storuman" : {'coordinates': (16.04945352045629, 65.43750339644153), 'neighbors': ['Lycksele', 'Sorsele', 'Vilhelmina']},
            "Boden" : {'coordinates': (21.341587720033584, 66.06213089488753), 'neighbors': ['Gällivare', 'Jokkmokk', 'Överkalix', 'Luleå', 'Älvsbyn']},
            "Upplands-Bro" : {'coordinates': (17.651331301421532, 59.52625600997782), 'neighbors': ['Sigtuna', 'Upplands Väsby', 'Järfälla', 'Ekerö', 'Enköping', 'Håbo']},
            "Tranås" : {'coordinates': (14.83846256187805, 58.0270364869319), 'neighbors': ['Boxholm', 'Aneby', 'Ydre', 'Ödeshög', 'Jönköping']},
            "Tingsryd" : {'coordinates': (14.974390934656599, 56.535724720182394), 'neighbors': ['Växjö', 'Emmaboda', 'Alvesta', 'Älmhult', 'Karlshamn', 'Olofström', 'Lessebo', 'Ronneby']},
            "Sölvesborg" : {'coordinates': (14.66475091282573, 56.0691794738015), 'neighbors': ['Bromölla', 'Karlshamn', 'Olofström']},
            "Kävlinge" : {'coordinates': (13.04101537874436, 55.7875874249003), 'neighbors': ['Lund', 'Eslöv', 'Landskrona', 'Svalöv', 'Lomma']},
            "Hörby" : {'coordinates': (13.730624808385866, 55.83750982742291), 'neighbors': ['Hässleholm', 'Eslöv', 'Kristianstad', 'Sjöbo', 'Höör', 'Tomelilla']},
            "Munkedal" : {'coordinates': (11.708754334608551, 58.57910552018227), 'neighbors': ['Sotenäs', 'Dals-Ed', 'Lysekil', 'Färgelanda', 'Uddevalla', 'Tanum']},
            "Färgelanda" : {'coordinates': (12.015206665877596, 58.631072462022196), 'neighbors': ['Mellerud', 'Dals-Ed', 'Vänersborg', 'Munkedal', 'Uddevalla', 'Bengtsfors']},
            "Bollebygd" : {'coordinates': (12.618963303132235, 57.73823076016107), 'neighbors': ['Härryda', 'Lerum', 'Mark', 'Borås', 'Alingsås', 'Vårgårda']},
            "Uddevalla" : {'coordinates': (11.857829033993792, 58.32277464670927), 'neighbors': ['Lilla Edet', 'Vänersborg', 'Lysekil', 'Stenungsund', 'Munkedal', 'Färgelanda', 'Orust']},
            "Skinnskatteberg" : {'coordinates': (15.721177189084004, 59.79708535735643), 'neighbors': ['Fagersta', 'Surahammar', 'Lindesberg', 'Smedjebacken', 'Köping']},
            "Norsjö" : {'coordinates': (19.551204883833968, 64.93138947343903), 'neighbors': ['Lycksele', 'Skellefteå', 'Arvidsjaur', 'Malå', 'Vindeln']},
            "Uppvidinge" : {'coordinates': (15.424879773735247, 57.040476552418774), 'neighbors': ['Växjö', 'Högsby', 'Vetlanda', 'Hultsfred', 'Lessebo', 'Nybro']},
            "Mönsterås" : {'coordinates': (16.434576087108585, 57.05585191473175), 'neighbors': ['Högsby', 'Borgholm', 'Oskarshamn', 'Kalmar', 'Nybro']},
            "Burlöv" : {'coordinates': (13.094814659701562, 55.63332941346089), 'neighbors': ['Malmö', 'Lomma', 'Staffanstorp']},
            "Örkelljunga" : {'coordinates': (13.33967143584645, 56.31709611753074), 'neighbors': ['Hässleholm', 'Laholm', 'Klippan', 'Ängelholm', 'Perstorp', 'Markaryd']},
            "Alingsås" : {'coordinates': (12.535088053491737, 57.98679469870316), 'neighbors': ['Trollhättan', 'Lilla Edet', 'Lerum', 'Bollebygd', 'Ale', 'Vårgårda', 'Essunga']},
            "Torsby" : {'coordinates': (12.872964758148267, 60.53194629833144), 'neighbors': ['Hagfors', 'Arvika', 'Sunne', 'Malung-Sälen']},
            "Munkfors" : {'coordinates': (13.478914738849902, 59.82150681350338), 'neighbors': ['Forshaga', 'Hagfors', 'Sunne']},
            "Surahammar" : {'coordinates': (16.121585573799816, 59.76720994676572), 'neighbors': ['Fagersta', 'Skinnskatteberg', 'Sala', 'Västerås', 'Köping', 'Hallstahammar']},
            "Sundsvall" : {'coordinates': (16.951059541406714, 62.47503855516175), 'neighbors': ['Sollefteå', 'Ånge', 'Timrå', 'Bräcke', 'Ragunda', 'Nordanstig']},
            "Åre" : {'coordinates': (12.984922215871698, 63.415063386782315), 'neighbors': ['Krokom', 'Berg', 'Östersund']},
            "Nykvarn" : {'coordinates': (17.395045330485235, 59.1937926858316), 'neighbors': ['Södertälje', 'Gnesta', 'Strängnäs']},
            "Älvkarleby" : {'coordinates': (17.46598683427392, 60.576158437934616), 'neighbors': ['Tierp', 'Gävle']},
            "Vingåker" : {'coordinates': (15.886365964613418, 59.05997755393868), 'neighbors': ['Örebro', 'Finspång', 'Katrineholm']},
            "Karlshamn" : {'coordinates': (14.868748304440498, 56.24777942541342), 'neighbors': ['Tingsryd', 'Sölvesborg', 'Olofström', 'Ronneby']},
            "Orust" : {'coordinates': (11.587228761871545, 58.16112225176543), 'neighbors': ['Lysekil', 'Tjörn', 'Stenungsund', 'Uddevalla']},
            "Grästorp" : {'coordinates': (12.659858925194206, 58.3302373350634), 'neighbors': ['Trollhättan', 'Vänersborg', 'Lidköping', 'Vara', 'Essunga']},
            "Falköping" : {'coordinates': (13.550200998079061, 58.145254557471475), 'neighbors': ['Tidaholm', 'Ulricehamn', 'Herrljunga', 'Skara', 'Skövde', 'Vara', 'Mullsjö']},
            "Lindesberg" : {'coordinates': (15.331980354922521, 59.64889612073788), 'neighbors': ['Örebro', 'Hällefors', 'Arboga', 'Skinnskatteberg', 'Smedjebacken', 'Nora', 'Ljusnarsberg', 'Köping']},
            "Sala" : {'coordinates': (16.489143041996154, 59.95987826325827), 'neighbors': ['Heby', 'Enköping', 'Sandviken', 'Fagersta', 'Norberg', 'Surahammar', 'Avesta', 'Västerås']},
            "Östersund" : {'coordinates': (14.867366570536015, 63.23857586585784), 'neighbors': ['Krokom', 'Berg', 'Bräcke', 'Ragunda', 'Åre', 'Strömsund']},
            "Bjurholm" : {'coordinates': (18.99147048926508, 63.946394306645466), 'neighbors': ['Örnsköldsvik', 'Lycksele', 'Vännäs', 'Åsele', 'Nordmaling', 'Vindeln']},
            "Robertsfors" : {'coordinates': (20.788642853121583, 64.18528960910118), 'neighbors': ['Skellefteå', 'Umeå']},
            "Kinda" : {'coordinates': (15.730144041399978, 57.99918103835639), 'neighbors': ['Boxholm', 'Ydre', 'Åtvidaberg', 'Vimmerby', 'Västervik', 'Linköping']},
            "Mullsjö" : {'coordinates': (13.828097310403706, 57.953120639312516), 'neighbors': ['Tidaholm', 'Ulricehamn', 'Habo', 'Falköping', 'Jönköping']},
            "Vimmerby" : {'coordinates': (15.872146128995496, 57.69132321356424), 'neighbors': ['Ydre', 'Oskarshamn', 'Eksjö', 'Hultsfred', 'Kinda', 'Västervik']},
            "Öckerö" : {'coordinates': (11.639665833669675, 57.731032028359536), 'neighbors': ['Kungälv', 'Göteborg']},
            "Ale" : {'coordinates': (12.230146095077792, 57.96670264058287), 'neighbors': ['Kungälv', 'Trollhättan', 'Lilla Edet', 'Göteborg', 'Lerum', 'Alingsås']},
            "Kumla" : {'coordinates': (15.139435222105993, 59.12422973919865), 'neighbors': ['Örebro', 'Hallsberg', 'Lekeberg']},
            "Orsa" : {'coordinates': (14.716205593435978, 61.31813975654381), 'neighbors': ['Rättvik', 'Mora', 'Ljusdal', 'Härjedalen']},
            "Smedjebacken" : {'coordinates': (15.454892036435634, 60.08806573831864), 'neighbors': ['Ludvika', 'Hedemora', 'Fagersta', 'Norberg', 'Borlänge', 'Skinnskatteberg', 'Lindesberg', 'Ljusnarsberg', 'Säter']},
            "Falun" : {'coordinates': (15.839403580085234, 60.75132919745835), 'neighbors': ['Leksand', 'Ockelbo', 'Hedemora', 'Bollnäs', 'Sandviken', 'Rättvik', 'Ovanåker', 'Borlänge', 'Säter']},
            "Avesta" : {'coordinates': (16.365110509993368, 60.213648403399034), 'neighbors': ['Hofors', 'Hedemora', 'Sandviken', 'Norberg', 'Sala']},
            "Ljusdal" : {'coordinates': (15.53768595967687, 61.85319680770033), 'neighbors': ['Hudiksvall', 'Bollnäs', 'Rättvik', 'Ovanåker', 'Nordanstig', 'Orsa', 'Härjedalen']},
            "Åsele" : {'coordinates': (17.627118905780442, 64.17455394095498), 'neighbors': ['Örnsköldsvik', 'Sollefteå', 'Lycksele', 'Dorotea', 'Bjurholm', 'Vilhelmina']},
            "Vårgårda" : {'coordinates': (12.764955065494185, 57.988287555992045), 'neighbors': ['Herrljunga', 'Borås', 'Bollebygd', 'Alingsås', 'Essunga']},
            "Sunne" : {'coordinates': (13.059914242067162, 59.896891470661004), 'neighbors': ['Forshaga', 'Hagfors', 'Kil', 'Arvika', 'Torsby', 'Munkfors']},
            "Karlstad" : {'coordinates': (13.620911318504163, 59.475419606436816), 'neighbors': ['Forshaga', 'Hagfors', 'Kil', 'Storfors', 'Grums', 'Hammarö', 'Kristinehamn', 'Filipstad', 'Säffle']},
            "Lekeberg" : {'coordinates': (14.791381143957114, 59.17941539042562), 'neighbors': ['Örebro', 'Hallsberg', 'Degerfors', 'Kumla', 'Laxå', 'Karlskoga']},
            "Laxå" : {'coordinates': (14.547543866614792, 58.918864334202915), 'neighbors': ['Hallsberg', 'Askersund', 'Gullspång', 'Degerfors', 'Töreboda', 'Lekeberg', 'Karlsborg']},
            "Nora" : {'coordinates': (14.88967632176154, 59.53488371837902), 'neighbors': ['Örebro', 'Hällefors', 'Lindesberg', 'Karlskoga']},
            "Gävle" : {'coordinates': (17.114990811838148, 60.68105254258601), 'neighbors': ['Heby', 'Ockelbo', 'Tierp', 'Sandviken', 'Älvkarleby', 'Söderhamn']},
            "Strömsund" : {'coordinates': (15.225630587168906, 64.22189259973656), 'neighbors': ['Krokom', 'Sollefteå', 'Dorotea', 'Ragunda', 'Östersund', 'Vilhelmina']},
            "Stockholm" : {'coordinates': (17.996890371462623, 59.32202870611867), 'neighbors': ['Solna', 'Lidingö', 'Järfälla', 'Sundbyberg', 'Ekerö', 'Nacka', 'Danderyd', 'Sollentuna', 'Tyresö', 'Huddinge']},
            "Olofström" : {'coordinates': (14.563290310352965, 56.32112489739678), 'neighbors': ['Bromölla', 'Kristianstad', 'Älmhult', 'Tingsryd', 'Sölvesborg', 'Karlshamn', 'Osby']},
            "Bjuv" : {'coordinates': (12.9664108931785, 56.05393512895047), 'neighbors': ['Åstorp', 'Helsingborg', 'Svalöv']},
            "Höör" : {'coordinates': (13.513933399976848, 55.949568117159565), 'neighbors': ['Hässleholm', 'Eslöv', 'Klippan', 'Hörby']},
            "Tomelilla" : {'coordinates': (14.012873558565488, 55.61464890364939), 'neighbors': ['Simrishamn', 'Ystad', 'Kristianstad', 'Sjöbo', 'Hörby']},
            "Falkenberg" : {'coordinates': (12.717246475539213, 57.03491866650346), 'neighbors': ['Varberg', 'Halmstad', 'Hylte', 'Svenljunga', 'Gislaved', 'Mark']},
            "Essunga" : {'coordinates': (12.748655780670394, 58.186482241975774), 'neighbors': ['Herrljunga', 'Trollhättan', 'Vara', 'Alingsås', 'Grästorp', 'Vårgårda']},
            "Eda" : {'coordinates': (12.193261783862507, 59.79669538035473), 'neighbors': ['Årjäng', 'Arvika']},
            "Nordmaling" : {'coordinates': (19.412701274509033, 63.642203108734286), 'neighbors': ['Örnsköldsvik', 'Vännäs', 'Umeå', 'Bjurholm']},
            "Vindeln" : {'coordinates': (19.51397278047393, 64.35624600009109), 'neighbors': ['Lycksele', 'Skellefteå', 'Vännäs', 'Umeå', 'Norsjö', 'Bjurholm']},
            "Piteå" : {'coordinates': (21.00769238628575, 65.37635413712502), 'neighbors': ['Luleå', 'Skellefteå', 'Arvidsjaur', 'Älvsbyn']},
            "Täby" : {'coordinates': (18.071464905432126, 59.46564134679865), 'neighbors': ['Upplands Väsby', 'Vallentuna', 'Österåker', 'Vaxholm', 'Danderyd', 'Sollentuna']},
            "Strängnäs" : {'coordinates': (17.06927728798245, 59.35633018916162), 'neighbors': ['Ekerö', 'Enköping', 'Flen', 'Eskilstuna', 'Södertälje', 'Gnesta', 'Nykvarn', 'Västerås']},
            "Söderköping" : {'coordinates': (16.58402694290829, 58.39380014717865), 'neighbors': ['Norrköping', 'Valdemarsvik', 'Åtvidaberg', 'Linköping']},
            "Nässjö" : {'coordinates': (14.654833761395443, 57.61647143097446), 'neighbors': ['Sävsjö', 'Aneby', 'Vetlanda', 'Vaggeryd', 'Eksjö', 'Jönköping']},
            "Torsås" : {'coordinates': (15.921773245693611, 56.41962443106706), 'neighbors': ['Emmaboda', 'Karlskrona', 'Kalmar']},
            "Västervik" : {'coordinates': (16.448911201211892, 57.83837002931679), 'neighbors': ['Valdemarsvik', 'Oskarshamn', 'Åtvidaberg', 'Kinda', 'Vimmerby']},
            "Vellinge" : {'coordinates': (12.977797621516562, 55.44395906809709), 'neighbors': ['Malmö', 'Svedala', 'Trelleborg']},
            "Lomma" : {'coordinates': (13.065163813552891, 55.704963681609605), 'neighbors': ['Lund', 'Malmö', 'Kävlinge', 'Burlöv', 'Staffanstorp']},
            "Osby" : {'coordinates': (14.14752924378081, 56.41568381669726), 'neighbors': ['Hässleholm', 'Kristianstad', 'Älmhult', 'Olofström', 'Östra Göinge']},
            "Tanum" : {'coordinates': (11.387572443020362, 58.696968220105134), 'neighbors': ['Strömstad', 'Sotenäs', 'Dals-Ed', 'Munkedal']},
            "Hjo" : {'coordinates': (14.22912255286946, 58.27213428766593), 'neighbors': ['Tidaholm', 'Tibro', 'Habo', 'Skövde', 'Karlsborg']},
            "Ljusnarsberg" : {'coordinates': (14.967853426240644, 59.93709056899388), 'neighbors': ['Ludvika', 'Hällefors', 'Lindesberg', 'Smedjebacken']},
            "Karlskoga" : {'coordinates': (14.566113755432559, 59.377488722980274), 'neighbors': ['Örebro', 'Hällefors', 'Degerfors', 'Storfors', 'Lekeberg', 'Nora']},
            "Västerås" : {'coordinates': (16.567376270953783, 59.62795691871251), 'neighbors': ['Enköping', 'Eskilstuna', 'Surahammar', 'Sala', 'Strängnäs', 'Hallstahammar']},
            "Köping" : {'coordinates': (15.887900423810438, 59.574616322807955), 'neighbors': ['Arboga', 'Skinnskatteberg', 'Surahammar', 'Lindesberg', 'Kungsör', 'Hallstahammar']},
            "Oxelösund" : {'coordinates': (17.11814553724397, 58.672104770258144), 'neighbors': ['Nyköping']},
            "Jönköping" : {'coordinates': (14.191000520744076, 57.77456467991051), 'neighbors': ['Ulricehamn', 'Aneby', 'Tranemo', 'Ödeshög', 'Gislaved', 'Habo', 'Vaggeryd', 'Tranås', 'Mullsjö', 'Nässjö']},
            "Lessebo" : {'coordinates': (15.318741858454832, 56.775091978945376), 'neighbors': ['Växjö', 'Emmaboda', 'Tingsryd', 'Uppvidinge', 'Nybro']},
            "Mörbylånga" : {'coordinates': (16.514735428356275, 56.50437982971156), 'neighbors': ['Borgholm']},
            "Nybro" : {'coordinates': (15.885403021675772, 56.83623489733832), 'neighbors': ['Högsby', 'Emmaboda', 'Kalmar', 'Uppvidinge', 'Mönsterås', 'Lessebo']},
            "Perstorp" : {'coordinates': (13.374704111583565, 56.18712733815827), 'neighbors': ['Hässleholm', 'Klippan', 'Örkelljunga']},
            "Götene" : {'coordinates': (13.475960399180748, 58.55814271504121), 'neighbors': ['Mariestad', 'Skara', 'Lidköping', 'Skövde']},
            "Kungsör" : {'coordinates': (16.086795003098324, 59.415274987182094), 'neighbors': ['Eskilstuna', 'Arboga', 'Köping', 'Hallstahammar']},
            "Malung-Sälen" : {'coordinates': (13.368506312153793, 60.88440353951544), 'neighbors': ['Hagfors', 'Vansbro', 'Mora', 'Torsby', 'Filipstad', 'Älvdalen']},
            "Kiruna" : {'coordinates': (20.711061668039097, 68.16268959455388), 'neighbors': ['Gällivare', 'Pajala']},
            "Huddinge" : {'coordinates': (18.016480693084663, 59.21394417236057), 'neighbors': ['Ekerö', 'Botkyrka', 'Tyresö', 'Stockholm', 'Haninge']},
            "Uppsala" : {'coordinates': (17.716486368381123, 59.94494288853963), 'neighbors': ['Norrtälje', 'Heby', 'Knivsta', 'Tierp', 'Enköping', 'Håbo', 'Östhammar']},
            "Linköping" : {'coordinates': (15.599243528471563, 58.37157198496463), 'neighbors': ['Boxholm', 'Norrköping', 'Mjölby', 'Åtvidaberg', 'Motala', 'Finspång', 'Kinda', 'Söderköping']},
            "Markaryd" : {'coordinates': (13.613181768276197, 56.541027745410844), 'neighbors': ['Hässleholm', 'Ljungby', 'Laholm', 'Älmhult', 'Örkelljunga']},
            "Ronneby" : {'coordinates': (15.240434931866977, 56.2916115776658), 'neighbors': ['Emmaboda', 'Karlskrona', 'Tingsryd', 'Karlshamn']},
            "Staffanstorp" : {'coordinates': (13.210872161552128, 55.64581282383846), 'neighbors': ['Lund', 'Malmö', 'Svedala', 'Burlöv', 'Lomma']},
            "Östra Göinge" : {'coordinates': (14.144373905258728, 56.265349592283115), 'neighbors': ['Hässleholm', 'Kristianstad', 'Osby']},
            "Trelleborg" : {'coordinates': (13.272508128619187, 55.41100847465563), 'neighbors': ['Skurup', 'Svedala', 'Vellinge']},
            "Bengtsfors" : {'coordinates': (12.203016338820156, 59.03457021944128), 'neighbors': ['Mellerud', 'Årjäng', 'Åmål', 'Dals-Ed', 'Färgelanda', 'Säffle']},
            "Grums" : {'coordinates': (13.015623904240552, 59.39108949111095), 'neighbors': ['Kil', 'Arvika', 'Karlstad', 'Säffle']},
            "Härjedalen" : {'coordinates': (13.703281533143114, 62.21275107328242), 'neighbors': ['Ånge', 'Berg', 'Mora', 'Orsa', 'Ljusdal', 'Älvdalen']},
            "Vilhelmina" : {'coordinates': (16.006612191160123, 64.9360671212106), 'neighbors': ['Lycksele', 'Dorotea', 'Storuman', 'Åsele', 'Strömsund']},
            "Haninge" : {'coordinates': (18.28408061942015, 59.02305612703154), 'neighbors': ['Nynäshamn', 'Värmdö', 'Botkyrka', 'Tyresö', 'Huddinge']},
            "Karlsborg" : {'coordinates': (14.459768003445863, 58.606726223075206), 'neighbors': ['Tibro', 'Askersund', 'Gullspång', 'Töreboda', 'Laxå', 'Hjo']},
            "Hammarö" : {'coordinates': (13.540332966588286, 59.310618574623525), 'neighbors': ['Karlstad']},
            "Kristinehamn" : {'coordinates': (14.094194219017961, 59.2436063014126), 'neighbors': ['Gullspång', 'Degerfors', 'Storfors', 'Karlstad']},
            "Filipstad" : {'coordinates': (14.15317655195858, 59.852450693252784), 'neighbors': ['Ludvika', 'Hagfors', 'Hällefors', 'Vansbro', 'Storfors', 'Karlstad', 'Malung-Sälen']},
            "Säffle" : {'coordinates': (12.894157163202888, 59.152956723966724), 'neighbors': ['Årjäng', 'Åmål', 'Arvika', 'Karlstad', 'Bengtsfors', 'Grums']},
            "Hallstahammar" : {'coordinates': (16.22033265477059, 59.58840951603029), 'neighbors': ['Eskilstuna', 'Surahammar', 'Västerås', 'Köping', 'Kungsör']},
            "Älvdalen" : {'coordinates': (13.138036257807444, 61.64598018709971), 'neighbors': ['Mora', 'Malung-Sälen', 'Härjedalen']},
            "Säter" : {'coordinates': (15.696074195131166, 60.37433801373657), 'neighbors': ['Ludvika', 'Hedemora', 'Borlänge', 'Smedjebacken', 'Falun']},
            "Söderhamn" : {'coordinates': (16.96508237170555, 61.25440006829088), 'neighbors': ['Hudiksvall', 'Ockelbo', 'Bollnäs', 'Gävle']}
        },
    "outliers" :
        {
            "Öland" : {"closest_to" : "Kalmar", "coordinates" : (16.637221, 56.690403)},
            "Gotland" : {"closest_to" : "Norrköping", "coordinates" : (18.483518, 57.483507)}
        }
}




sweden_border_medium = [[22.183173455501926,65.72374054632017],[21.21351687997722,65.02600535751527],[21.369631381930958,64.41358795842429],[19.77887576669022,63.60955434839504],[17.84777916837521,62.74940013289681],[17.119554884518124,61.34116567651097],[17.83134606290639,60.63658336042741],[18.78772179533209,60.081914374422595],[17.86922488777634,58.9537661810587],[16.829185011470088,58.71982697207339],[16.447709588291474,57.041118069071885],[15.879785597403783,56.10430186626866],[14.666681349352075,56.200885118222175],[14.100721062891465,55.40778107362265],[12.942910597392057,55.36173737245058],[12.625100538797028,56.30708018658197],[11.787942335668674,57.44181712506307],[11.027368605196866,58.85614940045936],[11.468271925511146,59.43239329694604],[12.3003658382749,60.11793284773003],[12.631146681375183,61.293571682370136],[11.992064243221563,61.80036245385656],[11.93056928879423,63.12831757267698],[12.579935336973932,64.06621898055833],[13.571916131248711,64.04911408146971],[13.919905226302204,64.44542064071608],[13.55568973150909,64.78702769638151],[15.108411492583002,66.19386688909547],[16.108712192456778,67.30245555283689],[16.768878614985482,68.01393667263139],[17.729181756265348,68.01055186631628],[17.993868442464333,68.56739126247736],[19.878559604581255,68.40719432237258],[20.025268995857886,69.0651386583127],[20.645592889089528,69.10624726020087],[21.978534783626117,68.6168456081807],[23.53947309743444,67.93600861273525],[23.565879754335583,66.39605093043743],[23.903378533633802,66.00692739527962],[22.183173455501926,65.72374054632017]]

USA_border_simple = [[-123.3984375, 49.61070993807422], [-124.71679687499999, 40.78054143186033], [-122.08007812499999, 36.10237644873644], [-116.98242187499999, 32.47269502206151], [-106.962890625, 31.653381399664], [-103.447265625, 28.998531814051795], [-101.337890625, 29.611670115197377], [-99.228515625, 26.352497858154024], [-97.20703125, 26.03704188651584], [-95.00976562499999, 29.916852233070173], [-90.439453125, 29.152161283318915], [-89.736328125, 30.221101852485987], [-84.0234375, 29.76437737516313], [-81.298828125, 25.24469595130604], [-80.5078125, 25.799891182088334], [-80.85937499999999, 31.653381399664], [-75.9375, 35.746512259918504], [-75.5859375, 39.639537564366684], [-71.015625, 41.50857729743935], [-67.1484375, 45.336701909968134], [-68.203125, 47.517200697839414], [-71.015625, 45.089035564831036], [-81.5625, 43.068887774169625], [-82.96875, 47.040182144806664], [-92.8125, 49.38237278700955], [-123.3984375, 49.61070993807422]]

def printIDs(dict):
    i = 0
    for country in dict.keys():
        print(country, i)
        i += 1


south_america = {
    "regions" :
        {
            "Suriname" : {'coordinates': (-55.91145629952074, 4.120008031758886), 'neighbors': ['Brazil', 'Guyana', 'French Guyana']},
            "Brazil" : {'coordinates': (-53.05434003576708, -10.80677364349891), 'neighbors': ['Suriname', 'Guyana', 'Venezuela', 'Colombia', 'Bolivia', 'Peru', 'Paraguay', 'Argentina', 'Uruguay', 'French Guyana']},
            "Guyana" : {'coordinates': (-58.97120310856249, 4.790225375174757), 'neighbors': ['Suriname', 'Brazil', 'Venezuela']},
            "Venezuela" : {'coordinates': (-66.16382727830239, 7.162132267639009), 'neighbors': ['Brazil', 'Guyana', 'Colombia']},
            "Colombia" : {'coordinates': (-73.0777320869748, 3.9272138627097037), 'neighbors': ['Brazil', 'Venezuela', 'Ecuador', 'Peru']},
            "Chile" : {'coordinates': (-71.52064394516434, -39.04701430994845), 'neighbors': ['Bolivia', 'Argentina']},
            "Ecuador" : {'coordinates': (-78.38416674608372, -1.4547717055405802), 'neighbors': ['Colombia', 'Peru']},
            "Bolivia" : {'coordinates': (-64.64140560603106, -16.728987015305826), 'neighbors': ['Brazil', 'Chile', 'Peru', 'Paraguay', 'Argentina']},
            "Peru" : {'coordinates': (-74.39180581684721, -9.19156290513455), 'neighbors': ['Brazil', 'Colombia', 'Ecuador', 'Bolivia']},
            "Paraguay" : {'coordinates': (-58.38738783350569, -23.248041946292066), 'neighbors': ['Brazil', 'Bolivia', 'Argentina']},
            "Argentina" : {'coordinates': (-65.17536077114171, -35.446821489495115), 'neighbors': ['Brazil', 'Chile', 'Bolivia', 'Paraguay', 'Uruguay']},
            "Uruguay" : {'coordinates': (-56.00327866654844, -32.78090436523081), 'neighbors': ['Brazil', 'Argentina']},
            "French Guyana" : {'coordinates': (-53.284505, 3.965683), 'neighbors': ['Suriname', 'Brazil']}
        },
    "outliers" :
        {
        }
}

south_america_border = [[-72.0703125, 11.695272733029402], [-77.6953125, 8.233237111274565], [-77.6953125, 4.740675384778373], [-79.8046875, 1.2303741774326145], [-81.2109375, -5.44102230371796], [-78.3984375, -10.141931686131018], [-71.3671875, -17.811456088564473], [-70.83984375, -22.105998799750566], [-74.00390625, -35.46066995149529], [-75.5859375, -49.95121990866204], [-71.71875, -54.97761367069625], [-65.0390625, -54.572061655658516], [-68.90625, -51.835777520452474], [-65.7421875, -47.1598400130443], [-67.1484375, -46.55886030311717], [-64.6875, -42.94033923363181], [-64.6875, -40.3130432088809], [-62.57812500000001, -41.37680856570234], [-61.17187499999999, -39.09596293630548], [-56.6015625, -37.300275281344305], [-58.71093750000001, -34.30714385628803], [-55.01953125, -35.02999636902566], [-51.67968749999999, -32.10118973232094], [-48.515625, -27.839076094777802], [-46.40625, -24.046463999666567], [-41.8359375, -22.91792293614603], [-35.68359375, -9.275622176792098], [-35.859375, -5.0909441750333855], [-48.515625, -0.17578097424708533], [-52.20703125, 5.965753671065536], [-57.12890625, 6.489983332670651], [-62.57812500000001, 10.487811882056695], [-72.0703125, 11.695272733029402]]


africa = {
    "regions" :
        {
            "Burundi" : {'coordinates': (29.913900893071045, -3.3773918124285855), 'neighbors': ['Dem. Rep. Congo', 'Rwanda', 'Tanzania']},
            "Morocco" : {'coordinates': (-8.420479544549638, 29.885394698302107), 'neighbors': ['W. Sahara', 'Algeria']},
            "Mauritania" : {'coordinates': (-10.326396925234992, 20.209267206353772), 'neighbors': ['W. Sahara', 'Algeria', 'Mali', 'Senegal']},
            "W. Sahara" : {'coordinates': (-12.137831111607795, 24.291172960208606), 'neighbors': ['Morocco', 'Mauritania', 'Algeria']},
            "Angola" : {'coordinates': (17.470572552313453, -12.245869036133163), 'neighbors': ['Dem. Rep. Congo', 'Congo', 'Namibia', 'Zambia']},
            "Central African Rep." : {'coordinates': (20.374347291243925, 6.542778705921305), 'neighbors': ['Cameroon', 'Dem. Rep. Congo', 'Congo', 'Chad']},
            "Botswana" : {'coordinates': (23.773081465789428, -22.099711378826413), 'neighbors': ['Namibia', 'South Africa', 'Zimbabwe', 'Zambia']},
            "Burkina Faso" : {'coordinates': (-1.7765374520559394, 12.311650494136709), 'neighbors': ['Benin', "CÃ´te d'Ivoire", 'Ghana', 'Mali', 'Niger', 'Togo']},
            "Benin" : {'coordinates': (2.337377553496161, 9.647430780663717), 'neighbors': ['Burkina Faso', 'Nigeria', 'Niger', 'Togo']},
            "Algeria" : {'coordinates': (2.598047791618353, 28.185481278657562), 'neighbors': ['Morocco', 'Mauritania', 'W. Sahara', 'Libya', 'Mali', 'Niger', 'Tunisia']},
            "CÃ´te d'Ivoire" : {'coordinates': (-5.612043645225224, 7.553755007010496), 'neighbors': ['Burkina Faso', 'Ghana', 'Guinea', 'Liberia', 'Mali']},
            "Cameroon" : {'coordinates': (12.611552515136589, 5.663098130302125), 'neighbors': ['Central African Rep.', 'Congo', 'Gabon', 'Eq. Guinea', 'Nigeria', 'Niger', 'Chad']},
            "Dem. Rep. Congo" : {'coordinates': (23.582955831479076, -2.8502757110956676), 'neighbors': ['Burundi', 'Angola', 'Central African Rep.', 'Congo', 'Rwanda', 'S. Sudan', 'Tanzania', 'Uganda', 'Zambia']},
            "Eritrea" : {'coordinates': (38.678177342214305, 15.427275657917882), 'neighbors': ['Djibouti', 'Ethiopia', 'Sudan']},
            "Djibouti" : {'coordinates': (42.49801973604448, 11.773044395533917), 'neighbors': ['Eritrea', 'Ethiopia', 'Somaliland']},
            "Ethiopia" : {'coordinates': (39.551255792937724, 8.653999188132627), 'neighbors': ['Eritrea', 'Djibouti', 'Kenya', 'Sudan', 'S. Sudan', 'Somalia', 'Somaliland']},
            "Egypt" : {'coordinates': (29.844461513124397, 26.50661999974955), 'neighbors': ['Libya', 'Sudan']},
            "Congo" : {'coordinates': (15.134461767413525, -0.8378010872252889), 'neighbors': ['Angola', 'Central African Rep.', 'Cameroon', 'Dem. Rep. Congo', 'Gabon']},
            "Ghana" : {'coordinates': (-1.2369685557063996, 7.928651813099649), 'neighbors': ['Burkina Faso', "CÃ´te d'Ivoire", 'Togo']},
            "Gabon" : {'coordinates': (11.687751174902047, -0.6470481398040284), 'neighbors': ['Cameroon', 'Congo', 'Eq. Guinea']},
            "Guinea" : {'coordinates': (-11.060853741185454, 10.448272877271341), 'neighbors': ["CÃ´te d'Ivoire", 'Guinea-Bissau', 'Liberia', 'Mali', 'Senegal', 'Sierra Leone']},
            "Gambia" : {'coordinates': (-15.431872807730839, 13.475334358701662), 'neighbors': ['Senegal']},
            "Guinea-Bissau" : {'coordinates': (-15.110623751667886, 12.022704382325685), 'neighbors': ['Guinea', 'Senegal']},
            "Eq. Guinea" : {'coordinates': (10.366031325064027, 1.6458643199600755), 'neighbors': ['Cameroon', 'Gabon']},
            "Kenya" : {'coordinates': (37.791555286661385, 0.5959662521769519), 'neighbors': ['Ethiopia', 'S. Sudan', 'Somalia', 'Tanzania', 'Uganda']},
            "Liberia" : {'coordinates': (-9.410836154371122, 6.431619862252995), 'neighbors': ["CÃ´te d'Ivoire", 'Guinea', 'Sierra Leone']},
            "Lesotho" : {'coordinates': (28.170105295170504, -29.62529049369201), 'neighbors': ['South Africa']},
            "Libya" : {'coordinates': (17.974352779160437, 26.99746040702029), 'neighbors': ['Algeria', 'Egypt', 'Niger', 'Sudan', 'Chad', 'Tunisia']},
            "Mali" : {'coordinates': (-3.5432943394533396, 17.267772061700708), 'neighbors': ['Mauritania', 'Burkina Faso', 'Algeria', "CÃ´te d'Ivoire", 'Guinea', 'Niger', 'Senegal']},
            "Malawi" : {'coordinates': (34.19360532557932, -13.172832716661869), 'neighbors': ['Mozambique', 'Tanzania', 'Zambia']},
            "Mozambique" : {'coordinates': (35.472617154124826, -17.23044659781375), 'neighbors': ['Malawi', 'Swaziland', 'Tanzania', 'South Africa', 'Zimbabwe', 'Zambia']},
            "Namibia" : {'coordinates': (17.15616812619408, -22.099776931731057), 'neighbors': ['Angola', 'Botswana', 'South Africa', 'Zambia']},
            "Nigeria" : {'coordinates': (7.995127754089794, 9.548318418209975), 'neighbors': ['Benin', 'Cameroon', 'Niger']},
            "Niger" : {'coordinates': (9.324429338177225, 17.34555235332918), 'neighbors': ['Burkina Faso', 'Benin', 'Algeria', 'Cameroon', 'Libya', 'Mali', 'Nigeria', 'Chad']},
            "Rwanda" : {'coordinates': (29.918965837079956, -2.0135155258787054), 'neighbors': ['Burundi', 'Dem. Rep. Congo', 'Tanzania', 'Uganda']},
            "Sudan" : {'coordinates': (29.86260401225794, 15.990585003116735), 'neighbors': ['Eritrea', 'Ethiopia', 'Egypt', 'Libya', 'S. Sudan', 'Chad']},
            "S. Sudan" : {'coordinates': (30.198617582275244, 7.292889714818289), 'neighbors': ['Dem. Rep. Congo', 'Ethiopia', 'Kenya', 'Sudan', 'Uganda']},
            "Senegal" : {'coordinates': (-14.509802785859428, 14.354139988452015), 'neighbors': ['Mauritania', 'Guinea', 'Gambia', 'Guinea-Bissau', 'Mali']},
            "Sierra Leone" : {'coordinates': (-11.795257428559948, 8.530353726153049), 'neighbors': ['Guinea', 'Liberia']},
            "Somalia" : {'coordinates': (45.72670076723565, 4.752347756504952), 'neighbors': ['Ethiopia', 'Kenya', 'Somaliland']},
            "Somaliland" : {'coordinates': (46.23074776134347, 9.757970293312711), 'neighbors': ['Djibouti', 'Ethiopia', 'Somalia']},
            "Swaziland" : {'coordinates': (31.39525590206532, -26.489855288520005), 'neighbors': ['Mozambique', 'South Africa']},
            "Chad" : {'coordinates': (18.581329525332887, 15.328867399839647), 'neighbors': ['Central African Rep.', 'Cameroon', 'Libya', 'Niger', 'Sudan']},
            "Togo" : {'coordinates': (0.9964039436703579, 8.439541954669616), 'neighbors': ['Burkina Faso', 'Benin', 'Ghana']},
            "Tunisia" : {'coordinates': (9.534716120695832, 34.172939036882376), 'neighbors': ['Algeria', 'Libya']},
            "Tanzania" : {'coordinates': (34.75298813146112, -6.2577327208456195), 'neighbors': ['Burundi', 'Dem. Rep. Congo', 'Kenya', 'Malawi', 'Mozambique', 'Rwanda', 'Uganda', 'Zambia']},
            "Uganda" : {'coordinates': (32.35754815372394, 1.2954869630971055), 'neighbors': ['Dem. Rep. Congo', 'Kenya', 'Rwanda', 'S. Sudan', 'Tanzania']},
            "South Africa" : {'coordinates': (25.11739621239432, -28.962106191124374), 'neighbors': ['Botswana', 'Mozambique', 'Namibia', 'Swaziland', 'Zimbabwe', 'Lesotho']},
            "Zimbabwe" : {'coordinates': (29.78854837189254, -18.9069879478588), 'neighbors': ['Botswana', 'Mozambique', 'South Africa', 'Zambia']},
            "Zambia" : {'coordinates': (27.72759193998216, -13.39506752005761), 'neighbors': ['Angola', 'Botswana', 'Dem. Rep. Congo', 'Malawi', 'Mozambique', 'Namibia', 'Tanzania', 'Zimbabwe']},
        },
    "outliers" :
        {
            "Madagascar" : {"coordinates" : (46.318322, -19.378809), "closest_to" : "Mozambique"}
        }
}

africa_border = [[-5.2734375, 35.746512259918504], [-6.416015625, 34.379712580462204], [-9.228515625, 33.137551192346145], [-10.283203125, 29.305561325527698], [-13.53515625, 27.916766641249065], [-17.05078125, 21.94304553343818], [-16.611328125, 12.382928338487396], [-13.359375, 8.146242825034385], [-7.207031249999999, 4.390228926463396], [-2.63671875, 4.740675384778373], [1.0546875, 6.140554782450308], [4.74609375, 6.140554782450308], [5.712890625, 4.653079918274051], [8.4375, 4.565473550710278], [9.755859375, 3.0746950723696944], [8.876953125, -0.9667509997666298], [10.107421874999998, -2.8991526985043006], [12.3046875, -6.402648405963884], [13.798828125, -11.5230875068685], [12.3046875, -13.325484885597936], [11.689453125, -18.062312304546715], [14.326171874999998, -22.593726063929296], [14.677734375000002, -25.324166525738384], [18.193359375, -32.175612478499325], [17.666015625, -32.916485347314385], [19.775390625, -34.59704151614416], [22.236328125, -33.9433599465788], [25.048828125, -34.234512362369856], [29.619140624999996, -31.42866311735861], [32.255859375, -28.84467368077178], [32.51953125, -25.324166525738384], [35.68359375, -23.88583769986199], [35.15625, -19.642587534013032], [40.60546875, -15.623036831528252], [40.25390625, -12.897489183755892], [39.55078125, -3.513421045640032], [47.109375, 3.162455530237848], [51.328125, 11.867350911459308], [44.29687499999999, 10.660607953624776], [39.90234375, 16.29905101458183], [33.3984375, 28.14950321154457], [34.80468749999999, 28.14950321154457], [34.80468749999999, 31.952162238024975], [29.179687499999996, 30.90222470517144], [21.09375, 33.137551192346145], [19.335937499999996, 30.44867367928756], [11.953125, 33.137551192346145], [9.31640625, 37.3002752813443], [-1.9335937499999998, 35.31736632923788], [-5.2734375, 35.746512259918504]]


europe = {
    "regions" : 
        {
            "Switzerland" : {'coordinates': (8.118300613385488, 46.79173768366761), 'neighbors': ['Austria', 'Germany', 'France', 'Italy']},
            "Albania" : {'coordinates': (20.032426431443216, 41.141353306048764), 'neighbors': ['Greece', 'Kosovo', 'Macedonia', 'Montenegro']},
            "Bosnia and Herz." : {'coordinates': (17.81688342129797, 44.180767841386206), 'neighbors': ['Croatia', 'Montenegro', 'Serbia']},
            "Belgium" : {'coordinates': (4.580831590651697, 50.65244260645211), 'neighbors': ['Germany', 'France', 'Luxembourg', 'Netherlands']},
            "Bulgaria" : {'coordinates': (25.195110953277123, 42.753118762021685), 'neighbors': ['Greece', 'Macedonia', 'Romania', 'Serbia']},
            "Belarus" : {'coordinates': (27.981353986903663, 53.50634440475128), 'neighbors': ['Lithuania', 'Latvia', 'Poland', 'Russia', 'Ukraine']},
            "Austria" : {'coordinates': (14.076158884337074, 47.61394879274627), 'neighbors': ['Switzerland', 'Czech Rep.', 'Germany', 'Hungary', 'Italy', 'Slovakia', 'Slovenia']},
            "Czech Rep." : {'coordinates': (15.334558102365818, 49.77524529436901), 'neighbors': ['Austria', 'Germany', 'Poland', 'Slovakia']},
            "Germany" : {'coordinates': (10.288485092742889, 51.13372269040781), 'neighbors': ['Switzerland', 'Belgium', 'Austria', 'Czech Rep.', 'Denmark', 'France', 'Luxembourg', 'Netherlands', 'Poland']},
            "Denmark" : {'coordinates': (9.87637293767504, 56.06393446179454), 'neighbors': ['Germany']},
            "Spain" : {'coordinates': (-3.6170206023873726, 40.34865610622673), 'neighbors': ['France', 'Portugal']},
            "Estonia" : {'coordinates': (25.824728375319907, 58.64369524070696), 'neighbors': ['Latvia', 'Russia']},
            "Finland" : {'coordinates': (26.211764697394553, 64.50409391856745), 'neighbors': ['Norway', 'Russia', 'Sweden']},
            "France" : {'coordinates': (-2.8805991914037654, 42.45771810478777), 'neighbors': ['Switzerland', 'Belgium', 'Germany', 'Spain', 'Italy', 'Luxembourg']},
            "Greece" : {'coordinates': (22.719813447095095, 39.066715899714), 'neighbors': ['Albania', 'Bulgaria', 'Macedonia']},
            "Croatia" : {'coordinates': (16.566191106662163, 45.016234367971094), 'neighbors': ['Bosnia and Herz.', 'Hungary', 'Montenegro', 'Serbia', 'Slovenia']},
            "Hungary" : {'coordinates': (19.35762862774592, 47.19995117195425), 'neighbors': ['Austria', 'Croatia', 'Romania', 'Slovakia', 'Serbia', 'Slovenia', 'Ukraine']},
            "Italy" : {'coordinates': (12.140788372235894, 42.75118305296426), 'neighbors': ['Switzerland', 'Austria', 'France', 'Slovenia']},
            "Kosovo" : {'coordinates': (20.89535248119785, 42.579364825825884), 'neighbors': ['Albania', 'Macedonia', 'Montenegro', 'Serbia']},
            "Luxembourg" : {'coordinates': (5.965223432343994, 49.765705074151), 'neighbors': ['Belgium', 'Germany', 'France']},
            "Lithuania" : {'coordinates': (23.88064027584349, 55.28431948476603), 'neighbors': ['Belarus', 'Latvia', 'Poland', 'Russia']},
            "Latvia" : {'coordinates': (24.833296149803438, 56.80717513427927), 'neighbors': ['Belarus', 'Estonia', 'Lithuania', 'Russia']},
            "Moldova" : {'coordinates': (28.410482790803297, 47.20367642606755), 'neighbors': ['Romania', 'Ukraine']},
            "Macedonia" : {'coordinates': (21.697896816140062, 41.60592893075937), 'neighbors': ['Albania', 'Bulgaria', 'Greece', 'Kosovo', 'Serbia']},
            "Montenegro" : {'coordinates': (19.286180967198234, 42.789038331401294), 'neighbors': ['Albania', 'Bosnia and Herz.', 'Croatia', 'Kosovo', 'Serbia']},
            "Netherlands" : {'coordinates': (5.512217100965402, 52.298700374441786), 'neighbors': ['Belgium', 'Germany']},
            "Norway" : {'coordinates': (15.468126122726208, 69.15685639713278), 'neighbors': ['Finland', 'Russia', 'Sweden']},
            "Poland" : {'coordinates': (19.31101430844868, 52.14826021933187), 'neighbors': ['Belarus', 'Czech Rep.', 'Germany', 'Lithuania', 'Russia', 'Slovakia', 'Ukraine']},
            "Portugal" : {'coordinates': (-8.055765588295687, 39.63404977497817), 'neighbors': ['Spain']},
            "Romania" : {'coordinates': (24.943252494635384, 45.85710103573803), 'neighbors': ['Bulgaria', 'Hungary', 'Moldova', 'Serbia', 'Ukraine']},
            "Russia" : {'coordinates': (40.87522325596443, 61.980840750712574), 'neighbors': ['Belarus', 'Estonia', 'Finland', 'Lithuania', 'Latvia', 'Norway', 'Poland', 'Ukraine']},
            "Slovakia" : {'coordinates': (19.507657147433704, 48.7267113517275), 'neighbors': ['Austria', 'Czech Rep.', 'Hungary', 'Poland', 'Ukraine']},
            "Serbia" : {'coordinates': (20.819651267430178, 44.233037203635156), 'neighbors': ['Bosnia and Herz.', 'Bulgaria', 'Croatia', 'Hungary', 'Kosovo', 'Macedonia', 'Montenegro', 'Romania']},
            "Sweden" : {'coordinates': (16.59626584684802, 62.811484968080336), 'neighbors': ['Finland', 'Norway']},
            "Slovenia" : {'coordinates': (14.938152320795728, 46.125422059010376), 'neighbors': ['Austria', 'Croatia', 'Hungary', 'Italy']},
            "Ukraine" : {'coordinates': (31.369533080356277, 48.97301796820208), 'neighbors': ['Belarus', 'Hungary', 'Moldova', 'Poland', 'Romania', 'Russia', 'Slovakia']}
        },
    "outliers" : 
        {
            #"Iceland" : {"closest_to" : "Norway", "coordinates": "?"},
            #"United Kingdom" : {"closest_to" : "France"},
            #"Ireland" : {"closest_to" : "France"}
        }

}

european_union = {
    "regions" :
        {
            "Belgium" : {'coordinates': (4.580831590651697, 50.65244260645211), 'neighbors': ['Germany', 'France', 'Luxembourg', 'Netherlands']},
            "Bulgaria" : {'coordinates': (25.195110953277123, 42.753118762021685), 'neighbors': ['Greece', 'Macedonia', 'Romania', 'Serbia']},
            "Belarus" : {'coordinates': (27.981353986903663, 53.50634440475128), 'neighbors': ['Lithuania', 'Latvia', 'Poland', 'Russia', 'Ukraine']},
            "Austria" : {'coordinates': (14.076158884337074, 47.61394879274627), 'neighbors': ['Switzerland', 'Czech Rep.', 'Germany', 'Hungary', 'Italy', 'Slovakia', 'Slovenia']},
            "Czech Rep." : {'coordinates': (15.334558102365818, 49.77524529436901), 'neighbors': ['Austria', 'Germany', 'Poland', 'Slovakia']},
            "Germany" : {'coordinates': (10.288485092742889, 51.13372269040781), 'neighbors': ['Switzerland', 'Belgium', 'Austria', 'Czech Rep.', 'Denmark', 'France', 'Luxembourg', 'Netherlands', 'Poland']},
            "Denmark" : {'coordinates': (9.87637293767504, 56.06393446179454), 'neighbors': ['Germany']},
            "Spain" : {'coordinates': (-3.6170206023873726, 40.34865610622673), 'neighbors': ['France', 'Portugal']},
            "Estonia" : {'coordinates': (25.824728375319907, 58.64369524070696), 'neighbors': ['Latvia', 'Russia']},
            "Finland" : {'coordinates': (26.211764697394553, 64.50409391856745), 'neighbors': ['Norway', 'Russia', 'Sweden']},
            "France" : {'coordinates': (-2.8805991914037654, 42.45771810478777), 'neighbors': ['Switzerland', 'Belgium', 'Germany', 'Spain', 'Italy', 'Luxembourg']},
            "Greece" : {'coordinates': (22.719813447095095, 39.066715899714), 'neighbors': ['Bulgaria', 'Macedonia']},
            "Croatia" : {'coordinates': (16.566191106662163, 45.016234367971094), 'neighbors': ['Hungary', 'Montenegro', 'Serbia', 'Slovenia']},
            "Hungary" : {'coordinates': (19.35762862774592, 47.19995117195425), 'neighbors': ['Austria', 'Croatia', 'Romania', 'Slovakia', 'Serbia', 'Slovenia', 'Ukraine']},
            "Italy" : {'coordinates': (12.140788372235894, 42.75118305296426), 'neighbors': ['Switzerland', 'Austria', 'France', 'Slovenia']},
            "Kosovo" : {'coordinates': (20.89535248119785, 42.579364825825884), 'neighbors': ['Macedonia', 'Montenegro', 'Serbia']},
            "Luxembourg" : {'coordinates': (5.965223432343994, 49.765705074151), 'neighbors': ['Belgium', 'Germany', 'France']},
            "Lithuania" : {'coordinates': (23.88064027584349, 55.28431948476603), 'neighbors': ['Belarus', 'Latvia', 'Poland', 'Russia']},
            "Latvia" : {'coordinates': (24.833296149803438, 56.80717513427927), 'neighbors': ['Belarus', 'Estonia', 'Lithuania', 'Russia']},
            "Moldova" : {'coordinates': (28.410482790803297, 47.20367642606755), 'neighbors': ['Romania', 'Ukraine']},
            "Macedonia" : {'coordinates': (21.697896816140062, 41.60592893075937), 'neighbors': ['Bulgaria', 'Greece', 'Kosovo', 'Serbia']},
            "Montenegro" : {'coordinates': (19.286180967198234, 42.789038331401294), 'neighbors': ['Croatia', 'Kosovo', 'Serbia']},
            "Netherlands" : {'coordinates': (5.512217100965402, 52.298700374441786), 'neighbors': ['Belgium', 'Germany']},
            "Norway" : {'coordinates': (15.468126122726208, 69.15685639713278), 'neighbors': ['Finland', 'Russia', 'Sweden']},
            "Poland" : {'coordinates': (19.31101430844868, 52.14826021933187), 'neighbors': ['Belarus', 'Czech Rep.', 'Germany', 'Lithuania', 'Russia', 'Slovakia', 'Ukraine']},
            "Portugal" : {'coordinates': (-8.055765588295687, 39.63404977497817), 'neighbors': ['Spain']},
            "Romania" : {'coordinates': (24.943252494635384, 45.85710103573803), 'neighbors': ['Bulgaria', 'Hungary', 'Moldova', 'Serbia', 'Ukraine']},
            "Russia" : {'coordinates': (40.87522325596443, 61.980840750712574), 'neighbors': ['Belarus', 'Estonia', 'Finland', 'Lithuania', 'Latvia', 'Norway', 'Poland', 'Ukraine']},
            "Slovakia" : {'coordinates': (19.507657147433704, 48.7267113517275), 'neighbors': ['Austria', 'Czech Rep.', 'Hungary', 'Poland', 'Ukraine']},
            "Serbia" : {'coordinates': (20.819651267430178, 44.233037203635156), 'neighbors': ['Bulgaria', 'Croatia', 'Hungary', 'Kosovo', 'Macedonia', 'Montenegro', 'Romania']},
            "Sweden" : {'coordinates': (16.59626584684802, 62.811484968080336), 'neighbors': ['Finland', 'Norway']},
            "Slovenia" : {'coordinates': (14.938152320795728, 46.125422059010376), 'neighbors': ['Austria', 'Croatia', 'Hungary', 'Italy']},
            "Ukraine" : {'coordinates': (31.369533080356277, 48.97301796820208), 'neighbors': ['Belarus', 'Hungary', 'Moldova', 'Poland', 'Romania', 'Russia', 'Slovakia']}
        },
    "outliers" :
        {
            #"Iceland" : {"closest_to" : "Norway", "coordinates": "?"},
            #"United Kingdom" : {"closest_to" : "France"},
            #"Ireland" : {"closest_to" : "France"}
        }

}


europe_border = [[39.90234375, 48.45835188280866], [47.8125, 60.326947742998414], [41.66015625, 66.23145747862573], [36.5625, 63.93737246791484], [32.34375, 67.13582938531948], [39.55078125, 66.30220547599842], [41.1328125, 67.7427590666639], [28.125, 70.95969716686398], [17.05078125, 69.71810669906763], [5.44921875, 61.938950426660604], [5.09765625, 57.89149735271034], [11.074218749999998, 59.17592824927136], [12.480468749999998, 55.7765730186677], [17.2265625, 56.46249048388979], [22.32421875, 65.73062649311031], [24.78515625, 65.73062649311031], [21.4453125, 62.99515845212052], [21.4453125, 60.23981116999893], [29.003906249999996, 60.326947742998414], [28.652343749999996, 59.5343180010956], [23.027343749999996, 59.265880628258095], [20.56640625, 55.178867663281984], [11.42578125, 54.470037612805754], [12.65625, 55.27911529201561], [9.4921875, 57.51582286553883], [7.3828125, 56.17002298293205], [8.0859375, 54.57206165565852], [-4.74609375, 48.69096039092549], [-1.58203125, 43.197167282501276], [-8.96484375, 43.45291889355465], [-9.31640625, 37.71859032558816], [-5.80078125, 36.03133177633187], [-0.52734375, 37.16031654673677], [4.04296875, 43.32517767999296], [9.31640625, 44.08758502824516], [15.292968749999998, 40.3130432088809], [13.18359375, 38.272688535980976], [15.644531250000002, 36.59788913307022], [18.28125, 40.17887331434696], [12.83203125, 44.715513732021336], [13.359375, 45.706179285330855], [19.335937499999996, 42.16340342422401], [19.335937499999996, 39.50404070558415], [21.4453125, 36.87962060502676], [24.08203125, 36.87962060502676], [23.5546875, 40.04443758460856], [28.125, 40.58058466412761], [30.05859375, 41.244772343082076], [28.30078125, 42.293564192170095], [31.113281249999996, 46.07323062540835], [33.57421875, 44.33956524809713], [36.38671875, 45.336701909968134], [39.90234375, 48.45835188280866]]


american_continent = {
    "regions" :
        {
            #"Bahamas" : {'coordinates': (-77.92997080393516, 25.515491725336627), 'neighbors': []},
            "Belize" : {'coordinates': (-88.7034212529932, 17.197089911451542), 'neighbors': ['Guatemala', 'Mexico']},
            "Canada" : {'coordinates': (-98.14238137209692, 61.469076145348886), 'neighbors': ['United States']},
            "Costa Rica" : {'coordinates': (-84.17542309600944, 9.965671127464525), 'neighbors': ['Nicaragua', 'Panama']},
            #"Cuba" : {'coordinates': (-78.96068490970252, 21.63175154102521), 'neighbors': []},
            #"Dominican Rep." : {'coordinates': (-70.46235845697531, 18.884487087982254), 'neighbors': ['Haiti']},
            #"Greenland" : {'coordinates': (-41.50018111492091, 74.7704876939898), 'neighbors': []},
            "Guatemala" : {'coordinates': (-90.36945836053151, 15.699360612026899), 'neighbors': ['Belize', 'Honduras', 'Mexico', 'El Salvador']},
            "Honduras" : {'coordinates': (-86.58996383801541, 14.822947081652927), 'neighbors': ['Guatemala', 'Nicaragua', 'El Salvador']},
            #"Haiti" : {'coordinates': (-72.65801330535577, 18.90070069184333), 'neighbors': ['Dominican Rep.']},
            #"Jamaica" : {'coordinates': (-77.32425480164892, 18.137636127868436), 'neighbors': []},
            "Mexico" : {'coordinates': (-102.57634952398678, 23.93537190224481), 'neighbors': ['Belize', 'Guatemala', 'United States']},
            "Nicaragua" : {'coordinates': (-85.02031850080247, 12.848190428036972), 'neighbors': ['Costa Rica', 'Honduras']},
            "Panama" : {'coordinates': (-80.10916483549379, 8.530019388864654), 'neighbors': ['Costa Rica', 'Colombia']},
            #"Puerto Rico" : {'coordinates': (-66.47922227695507, 18.2372245709719), 'neighbors': []},
            "El Salvador" : {'coordinates': (-88.87290317032377, 13.726091625794199), 'neighbors': ['Guatemala', 'Honduras']},
            #"Trinidad and Tobago" : {'coordinates': (-61.33036691444967, 10.428237089201879), 'neighbors': []},
            "United States" : {'coordinates': (-112.59943837732717, 45.70562953540304), 'neighbors': ['Canada', 'Mexico']},
            "Argentina" : {'coordinates': (-65.17536077114171, -35.446821489495115), 'neighbors': ['Bolivia', 'Brazil', 'Chile', 'Paraguay', 'Uruguay']},
            "Bolivia" : {'coordinates': (-64.64140560603106, -16.728987015305826), 'neighbors': ['Argentina', 'Brazil', 'Chile', 'Peru', 'Paraguay']},
            "Brazil" : {'coordinates': (-53.05434003576708, -10.80677364349891), 'neighbors': ['Argentina', 'Bolivia', 'Colombia', 'Guyana', 'Peru', 'Paraguay', 'Suriname', 'Uruguay', 'Venezuela']},
            "Chile" : {'coordinates': (-71.52064394516434, -39.04701430994845), 'neighbors': ['Argentina', 'Bolivia']},
            "Colombia" : {'coordinates': (-73.0777320869748, 3.9272138627097037), 'neighbors': ['Panama', 'Brazil', 'Ecuador', 'Peru', 'Venezuela']},
            "Ecuador" : {'coordinates': (-78.38416674608372, -1.4547717055405802), 'neighbors': ['Colombia', 'Peru']},
            #"Falkland Is." : {'coordinates': (-59.420972793110195, -51.71322176551184), 'neighbors': []},
            "Guyana" : {'coordinates': (-58.97120310856249, 4.790225375174757), 'neighbors': ['Brazil', 'Suriname', 'Venezuela']},
            "Peru" : {'coordinates': (-74.39180581684721, -9.19156290513455), 'neighbors': ['Bolivia', 'Brazil', 'Colombia', 'Ecuador']},
            "Paraguay" : {'coordinates': (-58.38738783350569, -23.248041946292066), 'neighbors': ['Argentina', 'Bolivia', 'Brazil']},
            "Suriname" : {'coordinates': (-55.91145629952074, 4.120008031758886), 'neighbors': ['Brazil', 'Guyana']},
            "Uruguay" : {'coordinates': (-56.00327866654844, -32.78090436523081), 'neighbors': ['Argentina', 'Brazil']},
            "Venezuela" : {'coordinates': (-66.16382727830239, 7.162132267639009), 'neighbors': ['Brazil', 'Colombia', 'Guyana']}
        },
    "outliers" :
    {
    }
}

american_continent_border = [[-87.890625, 69.41124235697256], [-101.6015625, 68.13885164925573], [-129.7265625, 70.37785394109224], [-137.8125, 69.53451763078358], [-156.4453125, 71.30079291637452], [-166.2890625, 69.16255790810501], [-158.55468749999997, 58.81374171570782], [-141.6796875, 60.413852350464914], [-132.1875, 55.3791104480105], [-125.5078125, 47.27922900257082], [-123.04687499999999, 37.71859032558816], [-114.60937499999999, 31.052933985705163], [-106.5234375, 21.289374355860424], [-103.0078125, 15.284185114076433], [-93.515625, 14.604847155053898], [-87.978515625, 12.811801316582619], [-86.396484375, 11.26461221250444], [-86.748046875, 10.660607953624776], [-80.5078125, 7.100892668623654], [-79.98046875, 7.972197714386879], [-78.57421875, 7.972197714386879], [-77.607421875, 3.5134210456400448], [-80.85937499999999, 0.26367094433665017], [-81.5625, -5.0909441750333855], [-76.81640625, -13.068776734357694], [-70.83984375, -18.47960905583197], [-74.35546875, -41.640078384678915], [-75.76171875, -48.57478991092885], [-74.53125, -53.748710796898976], [-69.43359375, -55.578344672182055], [-65.21484375, -55.07836723201513], [-68.90625, -51.835777520452474], [-65.7421875, -47.5172006978394], [-62.57812500000001, -41.50857729743933], [-48.33984375, -27.994401411046148], [-45.703125, -24.367113562651262], [-40.78125, -22.91792293614603], [-38.49609375, -12.554563528593656], [-34.27734375, -5.9657536710655235], [-48.8671875, -0.17578097424708533], [-52.734375, 6.489983332670651], [-58.00781249999999, 7.18810087117902], [-62.05078125, 11.350796722383672], [-70.6640625, 12.382928338487396], [-75.9375, 10.487811882056695], [-76.904296875, 8.754794702435618], [-78.837890625, 9.925565912405506], [-81.2109375, 9.318990192397905], [-83.6279296875, 11.480024648555816], [-83.14453125, 15.072123545811683], [-87.5390625, 16.804541076383455], [-86.484375, 22.105998799750566], [-90, 22.105998799750566], [-91.93359375, 19.642587534013032], [-95.625, 19.476950206488414], [-97.3828125, 23.885837699862005], [-94.39453125, 29.22889003019423], [-86.30859375, 30.29701788337205], [-81.5625, 25.16517336866393], [-80.15625, 26.588527147308614], [-80.33203125, 30.44867367928756], [-75.76171875, 34.74161249883172], [-65.7421875, 45.336701909968134], [-55.1953125, 52.5897007687178], [-74.8828125, 62.512317938386914], [-80.33203125, 53.12040528310657], [-92.98828125, 58.53959476664049], [-83.49609375, 68.46379955520322], [-87.890625, 69.41124235697256]]


latin_america = {
    "regions" :
        {
            #"Bahamas" : {'coordinates': (-77.92997080393516, 25.515491725336627), 'neighbors': []},
            "Belize" : {'coordinates': (-88.7034212529932, 17.197089911451542), 'neighbors': ['Guatemala', 'Mexico']},
            #"Canada" : {'coordinates': (-98.14238137209692, 61.469076145348886), 'neighbors': ['United States']},
            "Costa Rica" : {'coordinates': (-84.17542309600944, 9.965671127464525), 'neighbors': ['Nicaragua', 'Panama']},
            #"Cuba" : {'coordinates': (-78.96068490970252, 21.63175154102521), 'neighbors': []},
            #"Dominican Rep." : {'coordinates': (-70.46235845697531, 18.884487087982254), 'neighbors': ['Haiti']},
            #"Greenland" : {'coordinates': (-41.50018111492091, 74.7704876939898), 'neighbors': []},
            "Guatemala" : {'coordinates': (-90.36945836053151, 15.699360612026899), 'neighbors': ['Belize', 'Honduras', 'Mexico', 'El Salvador']},
            "Honduras" : {'coordinates': (-86.58996383801541, 14.822947081652927), 'neighbors': ['Guatemala', 'Nicaragua', 'El Salvador']},
            #"Haiti" : {'coordinates': (-72.65801330535577, 18.90070069184333), 'neighbors': ['Dominican Rep.']},
            #"Jamaica" : {'coordinates': (-77.32425480164892, 18.137636127868436), 'neighbors': []},
            "Mexico" : {'coordinates': (-102.57634952398678, 23.93537190224481), 'neighbors': ['Belize', 'Guatemala']},
            "Nicaragua" : {'coordinates': (-85.02031850080247, 12.848190428036972), 'neighbors': ['Costa Rica', 'Honduras']},
            "Panama" : {'coordinates': (-80.10916483549379, 8.530019388864654), 'neighbors': ['Costa Rica', 'Colombia']},
            #"Puerto Rico" : {'coordinates': (-66.47922227695507, 18.2372245709719), 'neighbors': []},
            "El Salvador" : {'coordinates': (-88.87290317032377, 13.726091625794199), 'neighbors': ['Guatemala', 'Honduras']},
            #"Trinidad and Tobago" : {'coordinates': (-61.33036691444967, 10.428237089201879), 'neighbors': []},
            #"United States" : {'coordinates': (-112.59943837732717, 45.70562953540304), 'neighbors': ['Canada', 'Mexico']},
            "Argentina" : {'coordinates': (-65.17536077114171, -35.446821489495115), 'neighbors': ['Bolivia', 'Brazil', 'Chile', 'Paraguay', 'Uruguay']},
            "Bolivia" : {'coordinates': (-64.64140560603106, -16.728987015305826), 'neighbors': ['Argentina', 'Brazil', 'Chile', 'Peru', 'Paraguay']},
            "Brazil" : {'coordinates': (-53.05434003576708, -10.80677364349891), 'neighbors': ['Argentina', 'Bolivia', 'Colombia', 'Guyana', 'Peru', 'Paraguay', 'Suriname', 'Uruguay', 'Venezuela']},
            "Chile" : {'coordinates': (-71.52064394516434, -39.04701430994845), 'neighbors': ['Argentina', 'Bolivia']},
            "Colombia" : {'coordinates': (-73.0777320869748, 3.9272138627097037), 'neighbors': ['Panama', 'Brazil', 'Ecuador', 'Peru', 'Venezuela']},
            "Ecuador" : {'coordinates': (-78.38416674608372, -1.4547717055405802), 'neighbors': ['Colombia', 'Peru']},
            #"Falkland Is." : {'coordinates': (-59.420972793110195, -51.71322176551184), 'neighbors': []},
            "Guyana" : {'coordinates': (-58.97120310856249, 4.790225375174757), 'neighbors': ['Brazil', 'Suriname', 'Venezuela']},
            "Peru" : {'coordinates': (-74.39180581684721, -9.19156290513455), 'neighbors': ['Bolivia', 'Brazil', 'Colombia', 'Ecuador']},
            "Paraguay" : {'coordinates': (-58.38738783350569, -23.248041946292066), 'neighbors': ['Argentina', 'Bolivia', 'Brazil']},
            "Suriname" : {'coordinates': (-55.91145629952074, 4.120008031758886), 'neighbors': ['Brazil', 'Guyana']},
            "Uruguay" : {'coordinates': (-56.00327866654844, -32.78090436523081), 'neighbors': ['Argentina', 'Brazil']},
            "Venezuela" : {'coordinates': (-66.16382727830239, 7.162132267639009), 'neighbors': ['Brazil', 'Colombia', 'Guyana']}
        },
    "outliers" :
    {
    }
}

latin_america_border = [[-76.2890625, 10.31491928581316], [-82.6171875, 11.695272733029402], [-83.3203125, 16.29905101458183], [-86.8359375, 16.636191878397664], [-87.1875, 22.105998799750566], [-91.23046875, 22.43134015636061], [-93.69140625, 20.46818922264095], [-97.03125, 25.958044673317843], [-116.01562499999999, 33.137551192346145], [-104.94140625, 18.47960905583197], [-94.5703125, 15.453680224345835], [-86.30859375, 11.178401873711785], [-81.03515625, 6.140554782450308], [-78.22265625, 6.664607562172573], [-81.2109375, -1.0546279422758742], [-81.2109375, -7.362466865535738], [-71.71875, -18.979025953255267], [-74.35546875, -37.99616267972812], [-76.11328125, -51.618016548773696], [-68.203125, -55.97379820507658], [-65.7421875, -55.07836723201513], [-68.203125, -51.39920565355377], [-65.21484375, -47.1598400130443], [-63.984375, -41.37680856570234], [-53.61328124999999, -34.45221847282653], [-34.80468749999999, -6.839169626342808], [-49.74609374999999, 1.5818302639606454], [-54.140625, 7.536764322084078], [-63.984375, 10.833305983642491], [-71.3671875, 13.068776734357694], [-76.2890625, 10.31491928581316]]



asia ={
    "regions" :
        {
        "Afghanistan" : {'coordinates': (66.08669022192835, 33.85639928169076), 'neighbors': ['China', 'Iran', 'Pakistan', 'Tajikistan', 'Turkmenistan', 'Uzbekistan']},
"United Arab Emirates" : {'coordinates': (54.206714761596324, 23.868633653347622), 'neighbors': ['Oman', 'Saudi Arabia']},
"Armenia" : {'coordinates': (45.000290011014776, 40.21660761230141), 'neighbors': ['Azerbaijan', 'Georgia', 'Iran', 'Turkey']},
"Azerbaijan" : {'coordinates': (47.553909589991896, 40.22069060359237), 'neighbors': ['Armenia', 'Georgia', 'Iran', 'Turkey']},
"Bangladesh" : {'coordinates': (90.26792827719599, 23.839461795344057), 'neighbors': ['India', 'Myanmar']},
"Bhutan" : {'coordinates': (90.47242480620372, 27.427968649102024), 'neighbors': ['China', 'India']},
"China" : {'coordinates': (103.8836162891887, 36.55506853517693), 'neighbors': ['Afghanistan', 'Bhutan', 'India', 'Kazakhstan', 'Kyrgyzstan', 'Lao PDR', 'Myanmar', 'Mongolia', 'Nepal', 'Dem. Rep. Korea', 'Tajikistan', 'Vietnam']},
"Georgia" : {'coordinates': (43.48154041978167, 42.16201869983144), 'neighbors': ['Armenia', 'Azerbaijan', 'Turkey']},
"India" : {'coordinates': (79.59370376325387, 22.925006407408507), 'neighbors': ['Bangladesh', 'Bhutan', 'China', 'Myanmar', 'Nepal', 'Pakistan']},
"Iran" : {'coordinates': (54.28545149689144, 32.5189173176254), 'neighbors': ['Afghanistan', 'Armenia', 'Azerbaijan', 'Iraq', 'Pakistan', 'Turkmenistan', 'Turkey']},
"Iraq" : {'coordinates': (43.75691141871338, 33.03682234103672), 'neighbors': ['Iran', 'Jordan', 'Kuwait', 'Saudi Arabia', 'Syria', 'Turkey']},
"Israel" : {'coordinates': (35.00385004873621, 31.484917814965385), 'neighbors': ['Jordan', 'Lebanon', 'Palestine', 'Syria']},
"Jordan" : {'coordinates': (36.77945490632519, 31.245490584748413), 'neighbors': ['Iraq', 'Israel', 'Palestine', 'Saudi Arabia', 'Syria']},
"Kazakhstan" : {'coordinates': (67.28460860746559, 48.19166209249595), 'neighbors': ['China', 'Kyrgyzstan', 'Turkmenistan', 'Uzbekistan']},
"Kyrgyzstan" : {'coordinates': (74.62040481092559, 41.50689371318262), 'neighbors': ['China', 'Kazakhstan', 'Tajikistan', 'Uzbekistan']},
"Cambodia" : {'coordinates': (104.87608532525189, 12.684728629393502), 'neighbors': ['Lao PDR', 'Thailand', 'Vietnam']},
"Korea" : {'coordinates': (127.82131712833073, 36.42759860415487), 'neighbors': ['Dem. Rep. Korea']},
"Kuwait" : {'coordinates': (47.600098887626416, 29.307266634033557), 'neighbors': ['Iraq', 'Saudi Arabia']},
"Lao PDR" : {'coordinates': (103.75025989504465, 18.444978089036102), 'neighbors': ['China', 'Cambodia', 'Myanmar', 'Thailand', 'Vietnam']},
"Lebanon" : {'coordinates': (35.87098632001643, 33.91182720781993), 'neighbors': ['Israel', 'Syria']},
"Myanmar" : {'coordinates': (96.50584094206155, 21.01699987377382), 'neighbors': ['Bangladesh', 'China', 'India', 'Lao PDR', 'Thailand']},
"Mongolia" : {'coordinates': (102.94640518633797, 46.823682503548206), 'neighbors': ['China']},
"Nepal" : {'coordinates': (84.0131736769253, 28.23944001904935), 'neighbors': ['China', 'India']},
"Oman" : {'coordinates': (56.098672819975434, 20.61117437422957), 'neighbors': ['United Arab Emirates', 'Saudi Arabia']},
"Pakistan" : {'coordinates': (69.41399806318125, 29.973460025547404), 'neighbors': ['Afghanistan', 'India', 'Iran']},
"Dem. Rep. Korea" : {'coordinates': (127.16501676281221, 40.14302086084456), 'neighbors': ['China', 'Korea']},
"Palestine" : {'coordinates': (35.273319622890256, 31.941136622415154), 'neighbors': ['Israel', 'Jordan']},
"Qatar" : {'coordinates': (51.18350257891329, 25.321850974206694), 'neighbors': ['Saudi Arabia']},
"Saudi Arabia" : {'coordinates': (44.516363768264746, 24.12328983910529), 'neighbors': ['United Arab Emirates', 'Iraq', 'Jordan', 'Kuwait', 'Oman', 'Qatar', 'Yemen']},
"Syria" : {'coordinates': (38.544239419611365, 35.012614281129), 'neighbors': ['Iraq', 'Israel', 'Jordan', 'Lebanon', 'Turkey']},
"Thailand" : {'coordinates': (101.00613354626104, 15.016974991416474), 'neighbors': ['Cambodia', 'Lao PDR', 'Myanmar']},
"Tajikistan" : {'coordinates': (71.03443504896109, 38.58308146421079), 'neighbors': ['Afghanistan', 'China', 'Kyrgyzstan', 'Uzbekistan']},
"Turkmenistan" : {'coordinates': (59.275430262361446, 39.091240180175845), 'neighbors': ['Afghanistan', 'Iran', 'Kazakhstan', 'Uzbekistan']},
"Turkey" : {'coordinates': (35.11690130804056, 39.0683717414166), 'neighbors': ['Armenia', 'Azerbaijan', 'Georgia', 'Iran', 'Iraq', 'Syria']},
"Uzbekistan" : {'coordinates': (63.203639528231804, 41.74860266465224), 'neighbors': ['Afghanistan', 'Kazakhstan', 'Kyrgyzstan', 'Tajikistan', 'Turkmenistan']},
"Vietnam" : {'coordinates': (106.28584079705189, 16.657937753254927), 'neighbors': ['China', 'Cambodia', 'Lao PDR']},
"Yemen" : {'coordinates': (47.5350447585435, 15.913231950143016), 'neighbors': ['Saudi Arabia']}
    },
    "outliers":
        {

        }
}


asia_border = [[130.95703125, 42.68243539838623], [135, 49.03786794532644], [127.61718749999999, 50.064191736659104], [124.27734374999999, 53.74871079689897], [119.17968749999999, 53.64463782485651], [117.24609374999999, 49.83798245308484], [103.0078125, 50.401515322782366], [99.66796875, 52.3755991766591], [97.20703125, 50.958426723359935], [90.87890625, 50.84757295365389], [87.5390625, 49.83798245308484], [76.640625, 54.57206165565852], [70.48828125, 55.57834467218206], [60.64453125000001, 53.9560855309879], [60.1171875, 51.28940590271679], [51.85546874999999, 52.26815737376817], [46.23046874999999, 49.95121990866204], [48.8671875, 46.07323062540835], [45.52734375, 42.8115217450979], [39.7265625, 43.70759350405294], [41.30859375, 42.032974332441405], [42.36328124999999, 37.996162679728116], [36.03515625, 36.59788913307022], [33.75, 31.203404950917395], [43.76953125, 12.382928338487396], [52.03125, 16.130262012034756], [57.83203125, 19.476950206488414], [59.94140624999999, 22.268764039073968], [56.42578125, 25.3241665257384], [58.00781249999999, 26.115985925333536], [65.7421875, 25.16517336866393], [70.48828125, 20.46818922264095], [76.46484375, 8.059229627200192], [82.08984375, 16.46769474828897], [88.06640625, 21.616579336740603], [91.0546875, 22.105998799750566], [94.74609375, 15.284185114076433], [97.20703125, 16.97274101999902], [98.0859375, 6.664607562172573], [103.53515625, 0.7031073524364909], [104.94140625, 2.1088986592431382], [101.07421875, 7.536764322084078], [100.37109375, 12.211180191503997], [105.46875, 7.710991655433217], [109.6875, 11.867350911459308], [109.3359375, 15.114552871944115], [105.64453124999999, 18.979025953255267], [110.74218749999999, 20.96143961409684], [118.30078125, 23.885837699862005], [122.16796875, 29.22889003019423], [120.05859375, 35.17380831799959], [118.65234374999999, 38.54816542304656], [121.9921875, 40.17887331434696], [124.98046874999999, 38.8225909761771], [126.21093749999999, 34.161818161230386], [130.078125, 35.460669951495305], [128.671875, 39.232253141714885], [130.95703125, 42.68243539838623]]




india_main = {
   "regions" : 
   {
      "Tamil Nadu" : {"coordinates" : [244, 538], "neighbors" : ['Kerala', 'Karnataka', 'Andhra Pradesh'] },
      "Kerala" : {"coordinates" : [207, 540], "neighbors" : ['Tamil Nadu', 'Karnataka'] },
      "Karnataka" : {"coordinates" : [203, 455], "neighbors" : ['Kerala', 'Goa', 'Tamil Nadu', 'Andhra Pradesh', 'Maharashtra'] },
      "Andhra Pradesh" : {"coordinates" : [265, 425], "neighbors" : ['Karnataka', 'Tamil Nadu', 'Maharashtra', 'Ghhatisgarh', 'Orissa'] },
      "Goa" : {"coordinates" : [171, 445], "neighbors" : ['Karnataka', 'Maharashtra'] },
      "Maharashtra" : {"coordinates" : [204, 364], "neighbors" : ['Goa', 'Karnataka', 'Andhra Pradesh', 'Ghhatisgarh', 'Madya Pradesh', 'Gujarat'] },
      "Ghhatisgarh" : {"coordinates" : [316, 328], "neighbors" : ['Maharashtra', 'Andhra Pradesh', 'Orissa', 'Madya Pradesh', 'Jharkand'] },
      "Orissa" : {"coordinates" : [360, 354], "neighbors" : ['Ghhatisgarh', 'Jharkand', 'Andhra Pradesh'] },
      "West Bengal" : {"coordinates" : [421, 300], "neighbors" : ['Jharkand', 'Bihar'] },
      "Jharkand" : {"coordinates" : [373, 291], "neighbors" : ['Bihar', 'Ghhatisgarh', 'Orissa', 'West Bengal'] },
      "Bihar" : {"coordinates" : [380, 252], "neighbors" : ['Uttar Pradesh', 'Jharkand', 'West Bengal'] },
      "Uttar Pradesh" : {"coordinates" : [305, 232], "neighbors" : ['Rajasthan', 'Haryana', 'Madya Pradesh', 'Bihar'] },
      "Uttarranchal" : {"coordinates" : [284, 164], "neighbors" : ['Himmachal Pradesh', 'Haryana'] },
      "Himmachal Pradesh" : {"coordinates" : [259, 129], "neighbors" : ['Haryana', 'Jammu & Kashmir', 'Uttarranchal'] },
      "Punjab" : {"coordinates" : [226, 145], "neighbors" : ['Rajasthan', 'Haryana', 'Jammu & Kashmir'] },
      "Jammu & Kashmir" : {"coordinates" : [239, 76], "neighbors" : ['Punjab', 'Himmachal Pradesh'] },
      "Haryana" : {"coordinates" : [237, 177], "neighbors" : ['Rajasthan', 'Himmachal Pradesh', 'Punjab', 'Uttar Pradesh', 'Uttarranchal'] },
      "Rajasthan" : {"coordinates" : [184, 224], "neighbors" : ['Gujarat', 'Haryana', 'Punjab', 'Uttar Pradesh'] },
      "Madya Pradesh" : {"coordinates" : [264, 292], "neighbors" : ['Ghhatisgarh', 'Maharashtra', 'Gujarat', 'Uttar Pradesh'] },
      "Gujarat" : {"coordinates" : [149, 295], "neighbors" : ['Maharashtra', 'Madya Pradesh', 'Rajasthan'] },
   },
   "outliers" : 
   {
   }
}

india_border_main = [[444, 329], [410, 332], [395, 363], [366, 379], [316, 433], [281, 444], [283, 506], [269, 544], [229, 586], [199, 569], [186, 515], [176, 468], [158, 449], [158, 393], [158, 334], [129, 343], [106, 304], [103, 269], [146, 262], [122, 217], [145, 186], [163, 192], [188, 163], [200, 158], [216, 124], [203, 105], [201, 67], [210, 55], [189, 33], [240, 16], [263, 48], [288, 49], [304, 50], [295, 83], [293, 112], [284, 126], [277, 120], [285, 141], [312, 156], [350, 177], [422, 206], [492, 199], [448, 247], [436, 273], [441, 303], [444, 324]]


india_side = {
   "regions" : 
   {
      "Arunachal Pradesh" : {"coordinates" : [535, 193], "neighbors" : ['Assam', 'Nagaland'] },
      "Assam" : {"coordinates" : [494, 235], "neighbors" : ['Tripura', 'Meghalaya', 'Nagaland', 'Manipur', 'Arunachal Pradesh'] },
      "Nagaland" : {"coordinates" : [528, 245], "neighbors" : ['Assam', 'Arunachal Pradesh'] },
      "Manipur" : {"coordinates" : [519, 271], "neighbors" : ['Mizoram', 'Assam'] },
      "Meghalaya" : {"coordinates" : [473, 260], "neighbors" : ['Assam'] },
      "Tripura" : {"coordinates" : [477, 296], "neighbors" : ['Mizoram', 'Assam'] },
      "Mizoram" : {"coordinates" : [503, 297], "neighbors" : ['Tripura', 'Manipur'] },
   },
   "outliers" : 
   {
   }
}

india_border_side = [[493, 200], [523, 181], [567, 175], [582, 194], [577, 216], [544, 233], [531, 272], [521, 288], [515, 292], [513, 311], [510, 319], [492, 310], [479, 308], [469, 301], [469, 285], [477, 275], [473, 270], [459, 274], [450, 245], [449, 225], [479, 226], [491, 218], [486, 207]]


china = {
   "regions" : 
   {
      "Tibet" : {"coordinates" : [199, 348], "neighbors" : ['Xinjiang', 'Qinghai', 'Sichuan', 'Yunnan'] },
      "Xinjiang" : {"coordinates" : [185, 193], "neighbors" : ['Tibet', 'Gansu', 'Qinghai'] },
      "Qinghai" : {"coordinates" : [301, 293], "neighbors" : ['Tibet', 'Xinjiang', 'Gansu'] },
      "Gansu" : {"coordinates" : [380, 263], "neighbors" : ['Xinjiang', 'Qinghai', 'Inner Mongolia', 'Ningxia', 'Sichuan', 'Shanxi'] },
      "Inner Mongolia" : {"coordinates" : [537, 180], "neighbors" : ['Gansu', 'Heibei', 'Jilin', 'Heilongjiang', 'Shanxi', 'Shanxi', 'Ningxia', 'Shanxi'] },
      "Heilongjiang" : {"coordinates" : [688, 110], "neighbors" : ['Inner Mongolia', 'Jilin'] },
      "Jilin" : {"coordinates" : [669, 171], "neighbors" : ['Inner Mongolia', 'Heilongjiang', 'Liaoning'] },
      "Liaoning" : {"coordinates" : [632, 204], "neighbors" : ['Jilin', 'Heibei'] },
      "Heibei" : {"coordinates" : [546, 233], "neighbors" : ['Inner Mongolia', 'Liaoning', 'Beijing', 'Tianjin', 'Shanxi', 'Heinan', 'Shandong', 'Shanxi'] },
      "Tianjin" : {"coordinates" : [575, 246], "neighbors" : ['Heibei', 'Beijing'] },
      "Beijing" : {"coordinates" : [561, 228], "neighbors" : ['Heibei', 'Tianjin'] },
      "Shanxi" : {"coordinates" : [512, 281], "neighbors" : ['Gansu', 'Inner Mongolia', 'Inner Mongolia', 'Inner Mongolia', 'Heibei', 'Heibei', 'Heinan'] },
      "Heinan" : {"coordinates" : [528, 328], "neighbors" : ['Heibei', 'Shanxi', 'Shandong', 'Jiangsu', 'Anhui', 'Hubei'] },
      "Shandong" : {"coordinates" : [584, 289], "neighbors" : ['Heibei', 'Heinan', 'Jiangsu', 'Anhui'] },
      "Hubei" : {"coordinates" : [512, 378], "neighbors" : ['Heinan', 'Hunan', 'Anhui', 'Jiangxi'] },
      "Guizhou" : {"coordinates" : [438, 446], "neighbors" : ['Sichuan', 'Yunnan', 'Guangxi', 'Hunan'] },
      "Yunnan" : {"coordinates" : [351, 474], "neighbors" : ['Tibet', 'Guizhou', 'Sichuan', 'Guangxi'] },
      "Sichuan" : {"coordinates" : [384, 388], "neighbors" : ['Tibet', 'Gansu', 'Guizhou', 'Yunnan', 'Chongqing'] },
      "Chongqing" : {"coordinates" : [450, 396], "neighbors" : ['Sichuan', 'Hunan'] },
      "Ningxia" : {"coordinates" : [433, 283], "neighbors" : ['Gansu', 'Inner Mongolia'] },
      "Jiangsu" : {"coordinates" : [612, 340], "neighbors" : ['Heinan', 'Shandong', 'Anhui', 'Shanghai'] },
      "Anhui" : {"coordinates" : [579, 367], "neighbors" : ['Heinan', 'Shandong', 'Hubei', 'Jiangsu', 'Jiangxi', 'Zhejiang'] },
      "Jiangxi" : {"coordinates" : [560, 431], "neighbors" : ['Hubei', 'Anhui', 'Zhejiang', 'Hunan', 'Guangdong', 'Fujian'] },
      "Zhejiang" : {"coordinates" : [623, 402], "neighbors" : ['Anhui', 'Jiangxi', 'Shanghai', 'Fujian'] },
      "Shanghai" : {"coordinates" : [639, 373], "neighbors" : ['Jiangsu', 'Zhejiang'] },
      "Fujian" : {"coordinates" : [598, 454], "neighbors" : ['Jiangxi', 'Zhejiang', 'Guangdong'] },
      "Guangdong" : {"coordinates" : [537, 499], "neighbors" : ['Jiangxi', 'Fujian', 'Guangxi', 'Hunan'] },
      "Hunan" : {"coordinates" : [505, 434], "neighbors" : ['Hubei', 'Guizhou', 'Chongqing', 'Jiangxi', 'Guangdong', 'Guangxi'] },
      "Guangxi" : {"coordinates" : [466, 501], "neighbors" : ['Guizhou', 'Yunnan', 'Guangdong', 'Hunan'] },
   },
   "outliers" : 
   {
      #"Hainan" : { "coordinates" : [479, 570], "closest_to" : "Jilin" , }
   }
}

china_border = [[588, 26], [638, 25], [717, 84], [751, 79], [743, 130], [692, 198], [632, 244], [626, 224], [583, 255], [640, 273], [610, 308], [635, 353], [648, 390], [622, 444], [582, 496], [525, 533], [470, 533], [415, 511], [376, 516], [354, 533], [329, 516], [310, 480], [315, 453], [302, 403], [247, 421], [209, 403], [184, 405], [126, 380], [81, 334], [64, 286], [69, 250], [43, 218], [45, 167], [113, 159], [144, 129], [155, 103], [200, 81], [238, 64], [274, 114], [265, 132], [309, 158], [330, 182], [403, 193], [445, 195], [488, 190], [506, 162], [549, 149], [579, 129], [585, 120], [543, 112], [551, 86], [576, 72], [589, 49]]



#Eva D.
#02/27/25
#Dog Breed Creative Project
#Intro on data sets, multi-day project PART 1 + PART 2

#Purpose: To look for a specific dog breed to get

import random

#init
dog_breeds = [
    "Affenpinscher", "AfghanHound", "AiredaleTerrier", "AkbashDog", "Akita", "AlapahaBlueBloodBulldog",
    "AlaskanHusky", "AlaskanMalamute", "AmericanEskimoDog", "AmericanFoxhound", "AmericanPitBullTerrier",
    "AmericanWaterSpaniel", "AnatolianShepherdDog", "AustralianKelpie", "AustralianShepherd", "Azawakh",
    "Basenji", "BassetBleudeGascogne", "Beagle", "Beauceron", "BedlingtonTerrier", "BelgianMalinois",
    "BelgianTervuren", "BerneseMountainDog", "BlackandTanCoonhound", "Bloodhound", "BluetickCoonhound",
    "Boerboel", "BorderTerrier", "BostonTerrier", "BouvierdesFlandres", "Boxer", "BoykinSpaniel",
    "BraccoItaliano", "Briard", "Brittany", "Bullmastiff", "CairnTerrier", "CaneCorso", "CardiganWelshCorgi",
    "CatahoulaLeopardDog", "CaucasianShepherd(Ovcharka)", "CavalierKingCharlesSpaniel", "ChineseCrested",
    "Chinook", "ChowChow", "ClumberSpaniel", "CockerSpaniel(American)", "CotondeTulear", "Dalmatian",
    "DogoArgentino", "EnglishShepherd", "EnglishSpringerSpaniel", "Eurasier", "FieldSpaniel", "FinnishLapphund",
    "GermanPinscher", "GermanShepherdDog", "GermanShorthairedPointer", "GiantSchnauzer", "GlenofImaalTerrier",
    "GoldenRetriever", "GordonSetter", "GreatDane", "GreatPyrenees", "Greyhound", "Harrier", "Havanese",
    "IrishSetter", "IrishWolfhound", "ItalianGreyhound", "JapaneseChin", "Keeshond", "Komondor", "Kuvasz",
    "LabradorRetriever", "LagottoRomagnolo", "Leonberger", "LhasaApso", "Maltese", "MiniatureSchnauzer",
    "Newfoundland", "NorfolkTerrier", "Papillon", "PembrokeWelshCorgi", "PharaohHound", "Plott", "Pug",
    "RedboneCoonhound", "RhodesianRidgeback", "Rottweiler", "Samoyed", "Schipperke", "ScottishDeerhound",
    "ShihTzu", "SilkyTerrier", "SoftCoatedWheatenTerrier", "SpanishWaterDog", "Vizsla", "Weimaraner"
]

#dog weights with both minimum and maximum weights
dog_weights = [
    (6, 13),       # Affenpinscher
    (50, 60),      # Afghan Hound
    (40, 65),      # Airedale Terrier
    (90, 120),     # Akbash Dog
    (65, 115),     # Akita
    (55, 90),      # Alapaha Blue Blood Bulldog
    (38, 50),      # Alaskan Husky
    (65, 100),     # Alaskan Malamute
    (20, 40),      # American Eskimo Dog
    (65, 75),      # American Foxhound
    (30, 60),      # American Pit Bull Terrier
    (25, 45),      # American Water Spaniel
    (80, 150),     # Anatolian Shepherd Dog
    (31, 46),      # Australian Kelpie
    (35, 65),      # Australian Shepherd
    (33, 55),      # Azawakh
    (22, 24),      # Basenji
    (35, 40),      # Basset Bleu de Gascogne
    (20, 35),      # Beagle
    (80, 110),     # Beauceron
    (17, 23),      # Bedlington Terrier
    (40, 80),      # Belgian Malinois
    (40, 65),      # Belgian Tervuren
    (65, 120),     # Bernese Mountain Dog
    (65, 100),     # Black and Tan Coonhound
    (80, 110),     # Bloodhound
    (45, 80),      # Bluetick Coonhound
    (110, 200),    # Boerboel
    (12, 16),      # Border Terrier
    (10, 25),      # Boston Terrier
    (70, 110),     # Bouvier des Flandres
    (50, 70),      # Boxer
    (25, 40),      # Boykin Spaniel
    (55, 88),      # Bracco Italiano
    (70, 90),      # Briard
    (30, 45),      # Brittany
    (100, 130),    # Bullmastiff
    (13, 14),      # Cairn Terrier
    (88, 120),     # Cane Corso
    (25, 38),      # Cardigan Welsh Corgi
    (50, 95),      # Catahoula Leopard Dog
    (80, 100),     # Caucasian Shepherd (Ovcharka)
    (13, 18),      # Cavalier King Charles Spaniel
    (10, 13),      # Chinese Crested
    (50, 90),      # Chinook
    (40, 70),      # Chow Chow
    (55, 85),      # Clumber Spaniel
    (20, 30),      # Cocker Spaniel (American)
    (9, 15),       # Coton de Tulear
    (50, 55),      # Dalmatian
    (80, 100),     # Dogo Argentino
    (44, 66),      # English Shepherd
    (35, 50),      # English Springer Spaniel
    (40, 70),      # Eurasier
    (35, 50),      # Field Spaniel
    (33, 53),      # Finnish Lapphund
    (25, 45),      # German Pinscher
    (50, 90),      # German Shepherd Dog
    (45, 70),      # German Shorthaired Pointer
    (65, 90),      # Giant Schnauzer
    (32, 40),      # Glen of Imaal Terrier
    (55, 75),      # Golden Retriever
    (45, 80),      # Gordon Setter
    (110, 190),    # Great Dane
    (85, 115),     # Great Pyrenees
    (50, 70),      # Greyhound
    (40, 60),      # Harrier
    (7, 13),       # Havanese
    (35, 70),      # Irish Setter
    (105, 180),    # Irish Wolfhound
    (7, 15),       # Italian Greyhound
    (4, 9),        # Japanese Chin
    (35, 45),      # Keeshond
    (80, 100),     # Komondor
    (70, 115),     # Kuvasz
    (55, 80),      # Labrador Retriever
    (24, 35),      # Lagotto Romagnolo
    (120, 170),    # Leonberger
    (12, 18),      # Lhasa Apso
    (4, 7),        # Maltese
    (11, 20),      # Miniature Schnauzer
    (100, 150),    # Newfoundland
    (11, 12),      # Norfolk Terrier
    (3, 12),       # Papillon
    (25, 30),      # Pembroke Welsh Corgi
    (40, 60),      # Pharaoh Hound
    (40, 60),      # Plott
    (14, 18),      # Pug
    (45, 80),      # Redbone Coonhound
    (75, 80),      # Rhodesian Ridgeback
    (75, 110),     # Rottweiler
    (50, 60),      # Samoyed
    (10, 16),      # Schipperke
    (70, 130),     # Scottish Deerhound
    (9, 16),       # Shih Tzu
    (8, 10),       # Silky Terrier
    (30, 40),      # Soft Coated Wheaten Terrier
    (30, 50),      # Spanish Water Dog
    (50, 65),      # Vizsla
    (55, 90)       # Weimaraner
]

#Dog breed images(URLs)
dog_images = [
    "https://cdn2.thedogapi.com/images/0LJiOVlxp.jpg",  # Affenpinscher
    "https://cdn2.thedogapi.com/images/tChrH8dDJ.jpg",  # AfghanHound
    "https://cdn2.thedogapi.com/images/PG8UPLSVU.jpg",  # AiredaleTerrier
    "https://cdn2.thedogapi.com/images/SyfsC19NQ_1280.jpg",  # AkbashDog
    "https://cdn2.thedogapi.com/images/36TXlWMDf.jpg",  # Akita
    "https://cdn2.thedogapi.com/images/33mJ-V3RX.jpg",  # AlapahaBlueBloodBulldog
    "https://cdn2.thedogapi.com/images/-HgpNnGXl.jpg",  # AlaskanHusky
    "https://cdn2.thedogapi.com/images/GhtSdrW29.jpg",  # AlaskanMalamute
    "https://cdn2.thedogapi.com/images/EB8A5HQHX.jpg",  # AmericanEskimoDog
    "https://cdn2.thedogapi.com/images/uISezUGDV.jpg",  # AmericanFoxhound
    "https://cdn2.thedogapi.com/images/HkC31gcNm_1280.png",  # AmericanPitBullTerrier
    "https://cdn2.thedogapi.com/images/SkmRJl9VQ_1280.jpg",  # AmericanWaterSpaniel
    "https://cdn2.thedogapi.com/images/BJT0Jx5Nm_1280.jpg",  # AnatolianShepherdDog
    "https://cdn2.thedogapi.com/images/Hyq1ge9VQ_1280.jpg",  # AustralianKelpie
    "https://cdn2.thedogapi.com/images/B1-llgq4m_1280.jpg",  # AustralianShepherd
    "https://cdn2.thedogapi.com/images/SkvZgx94m_1280.jpg",  # Azawakh
    "https://cdn2.thedogapi.com/images/H1dGlxqNQ_1280.jpg",  # Basenji
    "https://cdn2.thedogapi.com/images/BkMQll94X_1280.jpg",  # BassetBleudeGascogne
    "https://cdn2.thedogapi.com/images/Syd4xxqEm_1280.jpg",  # Beagle
    "https://cdn2.thedogapi.com/images/HJQ8ge5V7_1280.jpg",  # Beauceron
    "https://cdn2.thedogapi.com/images/ByK8gx947_1280.jpg",  # BedlingtonTerrier
    "https://cdn2.thedogapi.com/images/r1f_ll5VX_1280.jpg",  # BelgianMalinois
    "https://cdn2.thedogapi.com/images/B1KdxlcNX_1280.jpg",  # BelgianTervuren
    "https://cdn2.thedogapi.com/images/S1fFlx5Em_1280.jpg",  # BerneseMountainDog
    "https://cdn2.thedogapi.com/images/HJAFgxcNQ_1280.jpg",  # BlackandTanCoonhound
    "https://cdn2.thedogapi.com/images/Skdcgx9VX_1280.jpg",  # Bloodhound
    "https://cdn2.thedogapi.com/images/rJxieg9VQ_1280.jpg",  # BluetickCoonhound
    "https://cdn2.thedogapi.com/images/HyOjge5Vm_1280.jpg",  # Boerboel
    "https://cdn2.thedogapi.com/images/HJOpge9Em_1280.jpg",  # BorderTerrier
    "https://cdn2.thedogapi.com/images/rkZRggqVX_1280.jpg",  # BostonTerrier
    "https://cdn2.thedogapi.com/images/Byd0xl5VX_1280.jpg",  # BouvierdesFlandres
    "https://cdn2.thedogapi.com/images/ry1kWe5VQ_1280.jpg",  # Boxer
    "https://cdn2.thedogapi.com/images/ryHJZlcNX_1280.jpg",  # BoykinSpaniel
    "https://cdn2.thedogapi.com/images/S13yZg5VQ_1280.jpg",  # BraccoItaliano
    "https://cdn2.thedogapi.com/images/rkVlblcEQ_1280.jpg",  # Briard
    "https://cdn2.thedogapi.com/images/HJWZZxc4X_1280.jpg",  # Brittany
    "https://cdn2.thedogapi.com/images/r1ifZl5E7_1280.jpg",  # Bullmastiff
    "https://cdn2.thedogapi.com/images/Sk7Qbg9E7_1280.jpg",  # CairnTerrier
    "https://cdn2.thedogapi.com/images/r15m-lc4m_1280.jpg",  # CaneCorso
    "https://cdn2.thedogapi.com/images/SyXN-e9NX_1280.jpg",  # CardiganWelshCorgi
    "https://cdn2.thedogapi.com/images/BJcNbec4X_1280.jpg",  # CatahoulaLeopardDog
    "https://cdn2.thedogapi.com/images/r1rrWe5Em_1280.jpg",  # CaucasianShepherd(Ovcharka)
    "https://cdn2.thedogapi.com/images/HJRBbe94Q_1280.jpg",  # CavalierKingCharlesSpaniel
    "https://cdn2.thedogapi.com/images/B1pDZx9Nm_1280.jpg",  # ChineseCrested
    "https://cdn2.thedogapi.com/images/Sypubg54Q_1280.jpg",  # Chinook
    "https://cdn2.thedogapi.com/images/ry8KWgqEQ_1280.jpg",  # ChowChow
    "https://cdn2.thedogapi.com/images/rkeqWgq4Q_1280.jpg",  # ClumberSpaniel
    "https://cdn2.thedogapi.com/images/HkRcZe547_1280.jpg",  # CockerSpaniel(American)
    "https://cdn2.thedogapi.com/images/SyviZlqNm_1280.jpg",  # CotondeTulear
    "https://cdn2.thedogapi.com/images/SkJ3blcN7_1280.jpg",  # Dalmatian
    "https://cdn2.thedogapi.com/images/S1nhWx94Q_1280.jpg",  # DogoArgentino
    "https://cdn2.thedogapi.com/images/H1QyMe5EQ_1280.jpg",  # EnglishShepherd
    "https://cdn2.thedogapi.com/images/Hk0Jfe5VQ_1280.jpg",  # EnglishSpringerSpaniel
    "https://cdn2.thedogapi.com/images/S1VWGx9Nm_1280.jpg",  # Eurasier
    "https://cdn2.thedogapi.com/images/SkJfGecE7_1280.jpg",  # FieldSpaniel
    "https://cdn2.thedogapi.com/images/S1KMGg5Vm_1280.jpg",  # FinnishLapphund
    "https://cdn2.thedogapi.com/images/B1u4zgqE7_1280.jpg",  # GermanPinscher
    "https://cdn2.thedogapi.com/images/SJyBfg5NX_1280.jpg",  # GermanShepherdDog
    "https://cdn2.thedogapi.com/images/SJqBMg5Nm_1280.jpg",  # GermanShorthairedPointer
    "https://cdn2.thedogapi.com/images/H1NIzlcV7_1280.jpg",  # GiantSchnauzer
    "https://cdn2.thedogapi.com/images/H1oLMe94m_1280.jpg",  # GlenofImaalTerrier
    "https://cdn2.thedogapi.com/images/HJ7Pzg5EQ_1280.jpg",  # GoldenRetriever
    "https://cdn2.thedogapi.com/images/SJ5vzx5NX_1280.jpg",  # GordonSetter
    "https://cdn2.thedogapi.com/images/B1Edfl9NX_1280.jpg",  # GreatDane
    "https://cdn2.thedogapi.com/images/B12uzg9V7_1280.png",  # GreatPyrenees
    "https://cdn2.thedogapi.com/images/ryNYMx94X_1280.jpg",  # Greyhound
    "https://cdn2.thedogapi.com/images/B1IcfgqE7_1280.jpg",  # Harrier
    "https://cdn2.thedogapi.com/images/rkXiGl9V7_1280.jpg",  # Havanese
    "https://cdn2.thedogapi.com/images/S1osGeqVm_1280.jpg",  # IrishSetter
    "https://cdn2.thedogapi.com/images/Hyd2zgcEX_1280.jpg",  # IrishWolfhound
    "https://cdn2.thedogapi.com/images/SJAnzg9NX_1280.jpg",  # ItalianGreyhound
    "https://cdn2.thedogapi.com/images/r1H6feqEm_1280.jpg",  # JapaneseChin
    "https://cdn2.thedogapi.com/images/S1GAGg9Vm_1280.jpg",  # Keeshond
    "https://cdn2.thedogapi.com/images/Bko0fl547_1280.jpg",  # Komondor
    "https://cdn2.thedogapi.com/images/BykZ7ecVX_1280.jpg",  # Kuvasz
    "https://cdn2.thedogapi.com/images/B1uW7l5VX_1280.jpg",  # LabradorRetriever
    "https://cdn2.thedogapi.com/images/ryzzmgqE7_1280.jpg",  # LagottoRomagnolo
    "https://cdn2.thedogapi.com/images/ByrmQlqVm_1280.jpg",  # Leonberger
    "https://cdn2.thedogapi.com/images/SJp7Qe5EX_1280.jpg",  # LhasaApso
    "https://cdn2.thedogapi.com/images/B1SV7gqN7_1280.jpg",  # Maltese
    "https://cdn2.thedogapi.com/images/SJIUQl9NX_1280.jpg",  # MiniatureSchnauzer
    "https://cdn2.thedogapi.com/images/Sk4DXl54m_1280.jpg",  # Newfoundland
    "https://cdn2.thedogapi.com/images/B1ADQg94X_1280.jpg",  # NorfolkTerrier
    "https://cdn2.thedogapi.com/images/SkJj7e547_1280.jpg",  # Papillon
    "https://cdn2.thedogapi.com/images/rJ6iQeqEm_1280.jpg",  # PembrokeWelshCorgi
    "https://cdn2.thedogapi.com/images/Byz6mgqEQ_1280.jpg",  # PharaohHound
    "https://cdn2.thedogapi.com/images/B1i67l5VQ_1280.jpg",  # Plott
    "https://cdn2.thedogapi.com/images/HyJvcl9N7_1280.jpg",  # Pug
    "https://cdn2.thedogapi.com/images/HJMzEl5N7_1280.jpg",  # RedboneCoonhound
    "https://cdn2.thedogapi.com/images/By9zNgqE7_1280.jpg",  # RhodesianRidgeback
    "https://cdn2.thedogapi.com/images/r1xXEgcNX_1280.jpg",  # Rottweiler
    "https://cdn2.thedogapi.com/images/S1T8Ee9Nm_1280.jpg",  # Samoyed
    "https://cdn2.thedogapi.com/images/SyBvVgc47_1280.jpg",  # Schipperke
    "https://cdn2.thedogapi.com/images/SkNjqx9NQ_1280.jpg",  # ScottishDeerhound
    "https://cdn2.thedogapi.com/images/BkrJjgcV7_1280.jpg",  # ShihTzu
    "https://cdn2.thedogapi.com/images/ByzGsl5Nm_1280.jpg",  # SilkyTerrier
    "https://cdn2.thedogapi.com/images/HJHmix5NQ_1280.jpg",  # SoftCoatedWheatenTerrier
    "https://cdn2.thedogapi.com/images/HJf4jl9VX_1280.jpg",  # SpanishWaterDog
    "https://cdn2.thedogapi.com/images/r1o0jx9Em_1280.jpg",  # Vizsla
    "https://cdn2.thedogapi.com/images/SyU12l9V7_1280.jpg"   # Weimaraner
]


filtered_list = []  # This list will contain our filtered list

#functions
# tiny = <11
# small = 11-15
# medium = 25-60
# large = >60
def dog_size(size):
    global filtered_list
    filtered_list = []  # Clears the list before filtering

    if size == "tiny":
        for i in range(len(dog_weights)):  # Use i for index
            if dog_weights[i][0] < 11:  # Look for minimum weights < 11
                filtered_list.append(dog_breeds[i])  # Add breed to filtered list
        print("Tiny dogs:", filtered_list)  # Print filtered list

    elif size == "small":
        for i in range(len(dog_weights)):  # Use i for index
            if 11 <= dog_weights[i][0] <= 15:  # Look for minimum weights between 11 and 15
                filtered_list.append(dog_breeds[i])  # Add breed to filtered list
        print("Small dogs:", filtered_list)  # Print filtered list

    elif size == "medium":
        for i in range(len(dog_weights)):  # Use i for index
            if 25 <= dog_weights[i][0] <= 60:  # Look for minimum weights between 25 and 60
                filtered_list.append(dog_breeds[i])  # Add breed to filtered list
        print("Medium dogs:", filtered_list)  # Print filtered list

    elif size == "large":
        for i in range(len(dog_weights)):  # Use i for index
            if dog_weights[i][0] > 60:  # Look for minimum weights > 60
                filtered_list.append(dog_breeds[i])  # Add breed to filtered list
        print("Large dogs:", filtered_list)  # Print filtered list

    else:
        print("Invalid size entered. Please choose from: tiny, small, medium, large.")


# PART 2: Dog Breed Information Lookup and Filtering

dog_temperaments = [
    "Stubborn, Curious, Playful, Adventurous, Active, Fun-loving",  # Affenpinscher
    "Aloof, Clownish, Dignified, Independent, Happy",  # Afghan Hound
    "Outgoing, Friendly, Alert, Confident, Intelligent, Courageous",  # Airedale Terrier
    "Loyal, Independent, Intelligent, Brave",  # Akbash Dog
    "Docile, Alert, Responsive, Dignified, Composed, Friendly, Receptive, Faithful, Courageous",  # Akita
    "Loving, Protective, Trainable, Dutiful, Responsible",  # Alapaha Blue Blood Bulldog
    "Friendly, Energetic, Loyal, Gentle, Confident",  # Alaskan Husky
    "Friendly, Affectionate, Devoted, Loyal, Dignified, Playful",  # Alaskan Malamute
    "Friendly, Alert, Reserved, Intelligent, Protective",  # American Eskimo Dog
    "Kind, Sweet-Tempered, Loyal, Independent, Intelligent, Loving",  # American Foxhound
    "Strong Willed, Stubborn, Friendly, Clownish, Affectionate, Loyal, Obedient, Intelligent, Courageous",  # American Pit Bull Terrier
    "Friendly, Energetic, Obedient, Intelligent, Protective, Trainable",  # American Water Spaniel
    "Steady, Bold, Independent, Confident, Intelligent, Proud",  # Anatolian Shepherd Dog
    "Friendly, Energetic, Alert, Loyal, Intelligent, Eager",  # Australian Kelpie
    "Good-natured, Affectionate, Intelligent, Active, Protective",  # Australian Shepherd
    "Aloof, Affectionate, Attentive, Rugged, Fierce, Refined",  # Azawakh
    "Affectionate, Energetic, Alert, Curious, Playful, Intelligent",  # Basenji
    "Affectionate, Lively, Agile, Curious, Happy, Active",  # Basset Bleu de Gascogne
    "Amiable, Even Tempered, Excitable, Determined, Gentle, Intelligent",  # Beagle
    "Fearless, Friendly, Intelligent, Protective, Calm",  # Beauceron
    "Affectionate, Spirited, Intelligent, Good-tempered",  # Bedlington Terrier
    "Watchful, Alert, Stubborn, Friendly, Confident, Hard-working, Active, Protective",  # Belgian Malinois
    "Energetic, Alert, Loyal, Intelligent, Attentive, Protective",  # Belgian Tervuren
    "Affectionate, Loyal, Intelligent, Faithful",  # Bernese Mountain Dog
    "Easygoing, Gentle, Adaptable, Trusting, Even Tempered, Lovable",  # Black and Tan Coonhound
    "Stubborn, Affectionate, Gentle, Even Tempered",  # Bloodhound
    "Friendly, Intelligent, Active",  # Bluetick Coonhound
    "Obedient, Confident, Intelligent, Dominant, Territorial",  # Boerboel
    "Fearless, Affectionate, Alert, Obedient, Intelligent, Even Tempered",  # Border Terrier
    "Friendly, Lively, Intelligent",  # Boston Terrier
    "Protective, Loyal, Gentle, Intelligent, Familial, Rational",  # Bouvier des Flandres
    "Devoted, Fearless, Friendly, Cheerful, Energetic, Loyal, Playful, Confident, Intelligent, Bright, Brave, Calm",  # Boxer
    "Friendly, Energetic, Companionable, Intelligent, Eager, Trainable",  # Boykin Spaniel
    "Stubborn, Affectionate, Loyal, Playful, Companionable, Trainable",  # Bracco Italiano
    "Fearless, Loyal, Obedient, Intelligent, Faithful, Protective",  # Briard
    "Agile, Adaptable, Quick, Intelligent, Attentive, Happy",  # Brittany
    "Docile, Reliable, Devoted, Alert, Loyal, Reserved, Loving, Protective, Powerful, Calm, Courageous",  # Bullmastiff
    "Hardy, Fearless, Assertive, Gay, Intelligent, Active",  # Cairn Terrier
    "Trainable, Reserved, Stable, Quiet, Even Tempered, Calm",  # Cane Corso
    "Affectionate, Devoted, Alert, Companionable, Intelligent, Active",  # Cardigan Welsh Corgi
    "Energetic, Inquisitive, Independent, Gentle, Intelligent, Loving",  # Catahoula Leopard Dog
    "Alert, Quick, Dominant, Powerful, Calm, Strong",  # Caucasian Shepherd (Ovcharka)
    "Fearless, Affectionate, Sociable, Patient, Playful, Adaptable",  # Cavalier King Charles Spaniel
    "Affectionate, Sweet-Tempered, Lively, Alert, Playful, Happy",  # Chinese Crested
    "Friendly, Alert, Dignified, Intelligent, Calm",  # Chinook
    "Aloof, Loyal, Independent, Quiet",  # Chow Chow
    "Affectionate, Loyal, Dignified, Gentle, Calm, Great-hearted",  # Clumber Spaniel
    "Outgoing, Sociable, Trusting, Joyful, Even Tempered, Merry",  # Cocker Spaniel (American)
    "Affectionate, Lively, Playful, Intelligent, Trainable, Vocal",  # Coton de Tulear
    "Outgoing, Friendly, Energetic, Playful, Sensitive, Intelligent, Active",  # Dalmatian
    "Friendly, Affectionate, Cheerful, Loyal, Tolerant, Protective",  # Dogo Argentino
    "Kind, Energetic, Independent, Adaptable, Intelligent, Bossy",  # English Shepherd
    "Affectionate, Cheerful, Alert, Intelligent, Attentive, Active",  # English Springer Spaniel
    "Alert, Reserved, Intelligent, Even Tempered, Watchful, Calm",  # Eurasier
    "Docile, Cautious, Sociable, Sensitive, Adaptable, Familial",  # Field Spaniel
    "Friendly, Keen, Faithful, Calm, Courageous",  # Finnish Lapphund
    "Spirited, Lively, Intelligent, Loving, Even Tempered, Familial",  # German Pinscher
    "Alert, Loyal, Obedient, Curious, Confident, Intelligent, Watchful, Courageous",  # German Shepherd Dog
    "Boisterous, Bold, Affectionate, Intelligent, Cooperative, Trainable",  # German Shorthaired Pointer
    "Strong Willed, Kind, Loyal, Intelligent, Dominant, Powerful",  # Giant Schnauzer
    "Spirited, Agile, Loyal, Gentle, Active, Courageous",  # Glen of Imaal Terrier
    "Intelligent, Kind, Reliable, Friendly, Trustworthy, Confident",  # Golden Retriever
    "Fearless, Alert, Loyal, Confident, Gay, Eager",  # Gordon Setter
    "Friendly, Devoted, Reserved, Gentle, Confident, Loving",  # Great Dane
    "Strong Willed, Fearless, Affectionate, Patient, Gentle, Confident",  # Great Pyrenees
    "Affectionate, Athletic, Gentle, Intelligent, Quiet, Even Tempered",  # Greyhound
    "Outgoing, Friendly, Cheerful, Sweet-Tempered, Tolerant, Active",  # Harrier
    "Affectionate, Responsive, Playful, Companionable, Gentle, Intelligent",  # Havanese
    "Affectionate, Energetic, Lively, Independent, Playful, Companionable",  # Irish Setter
    "Sweet-Tempered, Loyal, Dignified, Patient, Thoughtful, Generous",  # Irish Wolfhound
    "Mischievous, Affectionate, Agile, Athletic, Companionable, Intelligent",  # Italian Greyhound
    "Alert, Loyal, Independent, Intelligent, Loving, Cat-like",  # Japanese Chin
    "Agile, Obedient, Playful, Quick, Sturdy, Bright",  # Keeshond
    "Steady, Fearless, Affectionate, Independent, Gentle, Calm",  # Komondor
    "Clownish, Loyal, Patient, Independent, Intelligent, Protective",  # Kuvasz
    "Kind, Outgoing, Agile, Gentle, Intelligent, Trusting, Even Tempered",  # Labrador Retriever
    "Keen, Loyal, Companionable, Loving, Active, Trainable",  # Lagotto Romagnolo
    "Obedient, Fearless, Loyal, Companionable, Adaptable, Loving",  # Leonberger
    "Steady, Fearless, Friendly, Devoted, Assertive, Spirited, Energetic, Lively, Alert, Obedient, Playful, Intelligent",  # Lhasa Apso
    "Playful, Docile, Fearless, Affectionate, Sweet-Tempered, Lively, Responsive, Easygoing, Gentle, Intelligent, Active",  # Maltese
    "Fearless, Friendly, Spirited, Alert, Obedient, Intelligent",  # Miniature Schnauzer
    "Sweet-Tempered, Gentle, Trainable",  # Newfoundland
    "Self-confidence, Fearless, Spirited, Companionable, Happy, Lovable",  # Norfolk Terrier
    "Hardy, Friendly, Energetic, Alert, Intelligent, Happy",  # Papillon
    "Tenacious, Outgoing, Friendly, Bold, Playful, Protective",  # Pembroke Welsh Corgi
    "Affectionate, Sociable, Playful, Intelligent, Active, Trainable",  # Pharaoh Hound
    "Bold, Alert, Loyal, Intelligent",  # Plott
    "Docile, Clever, Charming, Stubborn, Sociable, Playful, Quiet, Attentive",  # Pug
    "Affectionate, Energetic, Independent, Companionable, Familial, Unflappable",  # Redbone Coonhound
    "Strong Willed, Mischievous, Loyal, Dignified, Sensitive, Intelligent",  # Rhodesian Ridgeback
    "Steady, Good-natured, Fearless, Devoted, Alert, Obedient, Confident, Self-assured, Calm, Courageous",  # Rottweiler
    "Stubborn, Friendly, Sociable, Lively, Alert, Playful",  # Samoyed
    "Fearless, Agile, Curious, Independent, Confident, Faithful",  # Schipperke
    "Docile, Friendly, Dignified, Gentle",  # Scottish Deerhound
    "Clever, Spunky, Outgoing, Friendly, Affectionate, Lively, Alert, Loyal, Independent, Playful, Gentle, Intelligent, Happy, Active, Courageous",  # Shih Tzu
    "Friendly, Responsive, Inquisitive, Alert, Quick, Joyful",  # Silky Terrier
    "Affectionate, Spirited, Energetic, Playful, Intelligent, Faithful",  # Soft Coated Wheaten Terrier
    "Trainable, Diligent, Affectionate, Loyal, Athletic, Intelligent",  # Spanish Water Dog
    "Affectionate, Energetic, Loyal, Gentle, Quiet",  # Vizsla
    "Steady, Aloof, Stubborn, Energetic, Alert, Intelligent, Powerful, Fast"  # Weimaraner
]

dog_bred_for = [
    "Small rodent hunting, lapdog",  # Affenpinscher
    "Coursing and hunting",  # Afghan Hound
    "Badger, otter hunting",  # Airedale Terrier
    "Sheep guarding",  # Akbash Dog
    "Hunting bears",  # Akita
    "Guarding, companionship",  # Alapaha Blue Blood Bulldog
    "Sled pulling",  # Alaskan Husky
    "Hauling heavy freight, sled pulling",  # Alaskan Malamute
    "Companionship",  # American Eskimo Dog
    "Fox hunting",  # American Foxhound
    "Bull-baiting, companionship",  # American Pit Bull Terrier
    "Waterfowl retrieving",  # American Water Spaniel
    "Livestock guarding",  # Anatolian Shepherd Dog
    "Sheep herding",  # Australian Kelpie
    "Sheep herding",  # Australian Shepherd
    "Guarding, hunting",  # Azawakh
    "Hunting, companionship",  # Basenji
    "Hunting",  # Basset Bleu de Gascogne
    "Rabbit hunting",  # Beagle
    "Herding, guarding",  # Beauceron
    "Hunting vermin",  # Bedlington Terrier
    "Herding, guarding",  # Belgian Malinois
    "Herding, guarding",  # Belgian Tervuren
    "Draft work, herding",  # Bernese Mountain Dog
    "Hunting raccoons, bears",  # Black and Tan Coonhound
    "Tracking",  # Bloodhound
    "Hunting raccoons, bears",  # Bluetick Coonhound
    "Guarding",  # Boerboel
    "Fox and vermin hunting",  # Border Terrier
    "Companionship",  # Boston Terrier
    "Cattle herding",  # Bouvier des Flandres
    "Bull-baiting, guarding",  # Boxer
    "Hunting waterfowl",  # Boykin Spaniel
    "Hunting",  # Bracco Italiano
    "Herding, guarding",  # Briard
    "Hunting",  # Brittany
    "Guarding",  # Bullmastiff
    "Hunting vermin",  # Cairn Terrier
    "Guarding, hunting",  # Cane Corso
    "Herding",  # Cardigan Welsh Corgi
    "Hunting wild boar",  # Catahoula Leopard Dog
    "Livestock guarding",  # Caucasian Shepherd (Ovcharka)
    "Companionship",  # Cavalier King Charles Spaniel
    "Companionship",  # Chinese Crested
    "Sled pulling",  # Chinook
    "Guarding",  # Chow Chow
    "Hunting",  # Clumber Spaniel
    "Hunting birds",  # Cocker Spaniel (American)
    "Companionship",  # Coton de Tulear
    "Carriage dog, guarding",  # Dalmatian
    "Big-game hunting",  # Dogo Argentino
    "Herding",  # English Shepherd
    "Hunting birds",  # English Springer Spaniel
    "Companionship",  # Eurasier
    "Hunting birds",  # Field Spaniel
    "Herding reindeer",  # Finnish Lapphund
    "Ratting",  # German Pinscher
    "Herding, guarding",  # German Shepherd Dog
    "Hunting",  # German Shorthaired Pointer
    "Guarding",  # Giant Schnauzer
    "Hunting badgers, foxes",  # Glen of Imaal Terrier
    "Retrieving game",  # Golden Retriever
    "Hunting birds",  # Gordon Setter
    "Hunting boars",  # Great Dane
    "Livestock guarding",  # Great Pyrenees
    "Coursing game",  # Greyhound
    "Hunting hares",  # Harrier
    "Companionship",  # Havanese
    "Hunting birds",  # Irish Setter
    "Wolf hunting",  # Irish Wolfhound
    "Companionship",  # Italian Greyhound
    "Companionship",  # Japanese Chin
    "Barge watchdog",  # Keeshond
    "Livestock guarding",  # Komondor
    "Livestock guarding",  # Kuvasz
    "Retrieving game",  # Labrador Retriever
    "Truffle hunting",  # Lagotto Romagnolo
    "Guarding",  # Leonberger
    "Guarding",  # Lhasa Apso
    "Companionship",  # Maltese
    "Ratting",  # Miniature Schnauzer
    "Water rescue, hauling nets",  # Newfoundland
    "Hunting vermin",  # Norfolk Terrier
    "Companionship",  # Papillon
    "Herding",  # Pembroke Welsh Corgi
    "Hunting rabbits",  # Pharaoh Hound
    "Hunting boars",  # Plott
    "Companionship",  # Pug
    "Hunting raccoons",  # Redbone Coonhound
    "Hunting lions",  # Rhodesian Ridgeback
    "Guarding, herding",  # Rottweiler
    "Herding reindeer",  # Samoyed
    "Barge watchdog",  # Schipperke
    "Hunting deer",  # Scottish Deerhound
    "Companionship",  # Shih Tzu
    "Hunting rats",  # Silky Terrier
    "Herding, guarding",  # Soft Coated Wheaten Terrier
    "Herding",  # Spanish Water Dog
    "Hunting",  # Vizsla
    "Hunting large game"  # Weimaraner
]

from PIL import Image
import requests
from io import BytesIO

def open_image(url):
    try:
        response = requests.get(url)  # Send HTTP request to get image data
        response.raise_for_status()  # Raise an exception for HTTP errors
        img = Image.open(BytesIO(response.content))  # Convert data to an image object
        img.show()  # Displays the image
        return True
    except Exception as e:
        print(f"Could not display image: {e}")
        return False


def lookup_dog_breed():
    # Prompt the user for a dog breed
    breed = input("Enter the dog breed you want to look up: ").title()

    # Check if the breed exists in the dog_breeds list
    if breed in dog_breeds:
        # Get the index of the breed
        index = dog_breeds.index(breed)

        # Display the temperament
        print("\nTemperament: " + dog_temperaments[index])

        # Display the weight range
        min_weight, max_weight = dog_weights[index]
        print("Weight: " + str(min_weight) + " - " + str(max_weight) + " lbs")

        # Display the purpose (bred_for)
        print("Bred For: " + dog_bred_for[index])

        # Display the image URL
        print("\nImage: " + dog_images[index])


        # Automatically try to show the image
        if not open_image(dog_images[index]):
            print("You can still view the image by visiting the URL above.")

    else:
        # If the breed is not found, inform the user
        print("Sorry, '" + breed + "' is not in our database. Please check the spelling or try another breed.")

def main():
    while True:  # Infinite loop (runs forever until explicitly stopped)
        # Display menu options
        print("\n--- Dog Breed Finder ---")
        print("1. Filter dog breeds by size")
        print("2. Look up a specific dog breed")
        print("3. Display all dog breeds")
        print("4. Exit")

        # Get user choice
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            # Filter dog breeds by size
            size = input("What size dog are you looking for (tiny, small, medium, large)?: ").strip().lower()
            dog_size(size)  # Call the dog_size function

        elif choice == "2":
            # Look up a specific dog breed
            lookup_dog_breed()  # Call the lookup_dog_breed function

        elif choice == "3":
            # Display all dog breeds
            print("\nAll Dog Breeds:")
            for breed in dog_breeds:
                print(breed)

        elif choice == "4":
            # Exit the program
            print("Goodbye!")
            break  # Exit the loop

        else:
            # Handle invalid input
            print("Invalid choice. Please enter a number between 1 and 4.")


#main
main()


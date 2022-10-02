data = {
    'Betelgeuse' : { 
        'description' : 'Betelgeuse is a red supergiant star that is located at around 548 light-years / 168 parsecs away from the Sun. It is among the biggest stars ever discovered and among the most luminous. Betelgeuse is 126,000 times more luminous than our Sun. It is also more massive, having 16.5 solar masses and a whooping 764 solar radii. This means that Betelgeuse is more than 1200 times bigger than our Sun.',
        'distance':'650 light-years',
        'image': 'betelgeuse-star-1.jpg',
        'location': 'RA 5h 55m 10s | Dec +7° 24′ 26″'
    },
    'Sirius': { 
        'description' : 'Also known as the Dog Star, because it’s the brightest star in Canis Major (the “Big Dog”), Sirius is also the brightest star in the night sky. The name “Sirius” is derived from the Ancient Greek “Seirios“, which translates to “glowing” or “scorcher”. Whereas it appears to be a single bright star to the naked eye, Sirius is actually a binary star system, consisting of a white main-sequence star named Sirius A, and a faint white dwarf companion named Sirius B.',
        'distance':'7 light-years',
        'image': 'sirius.jpeg',
        'location': 'RA: 06h 45m 08.9s, dec: -16° 42′ 58″'
    },
    'Polaris' :{ 
        'description' : 'Also known as the North Star (as well as the Pole Star, Lodestar, and sometimes Guiding Star), Polaris is the 45th brightest star in the night sky. It is very close to the north celestial pole, which is why it has been used as a navigational tool in the northern hemisphere for centuries. ',
        'distance':'430 light-years',
        'image': 'polaris.jfif',
        'location': 'RA 2h 41m 39s, Dec. +89° 15′ 51″'


    },
    'Alpha Centauri System' :{ 
        'description' : 'Also known as Rigel Kent or Toliman, Alpha Centauri is the brightest star in the southern constellation of Centaurus and the third brightest star in the night sky. It is also the closest star system to Earth, at just a shade over four light-years. But much like Sirius and Polaris, it is actually a multistar system, consisting of Alpha Centauri A, B, and Proxima Centauri (aka. Centauri C).' ,
        'distance':'4 light-years',
        'image': 'alpha.jpg',
        'location': 'RA 14h 39m 37s | Dec -60° 50′ 2″'


    },
    'Rigel' :{ 
        'description' : 'Rigel B is itself a binary system, consisting of two main sequence blue-white subdwarf stars. Rigel B is the more massive of the pair, weighing in at 2.5 Solar masses versus Rigel C’s 1.9. Rigel has been recognized as being a binary since at least 1831 when German astronomer F.G.W. Struve first measured it. A fourth star in the system has been proposed, but it is generally considered that this is a misinterpretation of the main star’s variability.',
        'distance':'900 light-years',
        'image': 'rigel.jfif',
        'location': 'RA: 05h 14m 32.3s, Dec: -08° 12′ 05.9”'


    },    
    'Vega' :{ 
        'description' : 'Vega is another bright blue star that anchors the otherwise faint Lyra constellation (the Harp). Along with Deneb (from Cygnus) and Altair (from Aquila), it is a part of the Summer Triangle in the Northern hemisphere. It is also the brightest star in the constellation Lyra, the fifth brightest star in the night sky and the second brightest star in the northern celestial hemisphere (after Arcturus).',
        'distance':'25 light-years',
        'image': 'vega.jpg',
        'location': 'RA 18h 36m 56s | Dec +38° 47′ 1″'


    },  
    'Pleiades' :{ 
        'description' : 'Also known as the “Seven Sisters”, Messier 45 or M45, Pleiades is actually an open star cluster located in the constellation of Taurus. At an average distance of 444 light years from our Sun, it is one of the nearest star clusters to Earth, and the most visible to the naked eye. Though the seven largest stars are the most apparent, the cluster actually consists of over 1,000 confirmed members (along with several unconfirmed binaries).',
        'distance':'444 light-years',
        'image': 'pleiades.jpg',
        'location': 'RA 3h 47m 24s | Dec +24° 7′ 0″'


    },  
    'Antares' :{ 
        'description' : 'Antares is the seventeenth brightest star that can be seen with the naked eye and the brightest star in the constellation Scorpius. Along with Aldebaran, Regulus, and Fomalhaut, Antares comprises the group known as the ‘Royal stars of Persia’ – four stars that the ancient Persians (circa. 3000 BCE) believed guarded the four districts of the heavens.',
        'distance':'550 light-years',
        'image': 'Antares.jpg',
        'location': 'RA 16h 29m 24s | Dec -26° 25′ 55″'


    }, 
    'Canopus' :{ 
        'description' : 'Thought it was not visible to the ancient Greeks and Romans, the star was known to the ancient Egyptians, as well as the Navajo, Chinese and ancient Indo-Aryan people. In Vedic literature, Canopus is associated with Agastya, a revered sage who is believed to have lived during the 6th or 7th century BCE. To the Chinese, Canopus was known as the “Star of the Old Man”, and was charted by astronomer Yi Xing in 724 CE.',
        'distance':'330 light-years',
        'image': 'canopus.jfif',
        'location': 'RA 6h 23m 57s | Dec -52° 41′ 44″'


    },   
}

print(data.keys())

for i in data.keys():
    print(i)
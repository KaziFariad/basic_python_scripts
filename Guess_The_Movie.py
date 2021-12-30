import random
movies = [
    'Jai Bhim',
    'Pariyerum Perumal',
    'Nayakan',
    'Anbe Sivam',
    'C/o Kancharapalem',
    'Kireedam',
    'Manichithrathazhu',
    'Hanky Panky',
    'The World of Apu',
    'Natsamrat',
    'Thevar Magan',
    'Sardar Udham',
    'Kumbalangi Nights',
    'Black Friday',
    '#Home',
    'Pather Panchali',
    'Visaaranai',
    'Soorarai Pottru',
    'Jersey',
    '3 Idiots',
    'Asuran',
    'Kaithi',
    'Sarpatta Parambarai',
    'Like Stars on Earth',
    'Thalapathi',
    '96',
    'Drishyam 2',
    'Devasuram',
    'Dangal',
    'Peranbu',
    'Vada Chennai',
    'Aparajito',
    'Chithram',
    'Jaane Bhi Do Yaaro',
    'Pyaasa',
    'Thani Oruvan',
    'Raatchasan',
    'Guide',
    'Spadikam',
    'Iruvar',
    'Agent Sai Srinivasa Athreya',
    'Kannathil Muthamittal',
    'Chupke Chupke',
    'Mahanati',
    'Super Deluxe',
    'Aruvi',
    'Pudhu Pettai',
    'Drishyam',
    'A Northern Strory of Valor',
    'Khosla Ka Ghosla!',
    'Anniyan',
    'Kaakkaa Muttai',
    'Tumbbad',
    'Premam',
    'Mudhalvan',
    'Vikram Vedha',
    'Bangalore Days',
    'Papanasam',
    'Satya',
    'Soodhu Kavvum',
    'Mandela',
    'Angoor',
    'Dhuruvangal Pathinaaru',
    'Pithamagan',
    'Andhadhun',
    'Shahid',
    'Jigarthanda',
    'Anand',
    'Gangs of Wasseypur',
    'Paan Singh Tomar',
    'Sairat',
    'Bhaag Milkha Bhaag',
    'Maheshinte Prathikaaram',
    'Hera Pheri',
    'Theeran Adhigaram Ondru',
    'Chhichhore',
    'Sholay',
    'Ustad Hotel',
    'Chak De! India',
    'Swades',
    'Talvar',
    'Mughal-E-Azam',
    'Baasha',
    'Jo Jeeta Wohi Sikandar',
    'Zindagi Na Milegi Dobara',
    'Virumandi',
    'Black',
    'Nil Battey Sannata',
    'Article 15',
    'Charulata',
    'Udaan',
    'Drishyam',
    'Masaan',
    'A Wednesday',
    'Alaipayuthey',
    'Munna Bhai ',
    'Sarfarosh',
    'Queen',
    'Roja',
    'Uri: The Surgical Strike',
    'Dil Chahta Hai',
    'OMG: Oh My God!',
    'Rang De Basanti',
    'Lagaan: Once Upon a Time in India',
    'Kahaani',
    'Andaz Apna Apna',
    'PK',
    'Bommarillu',
    'Lucia',
    'The Legend of Bhagat Singh',
    'Maanaadu',
    'Iqbal',
    'Barfi!',
    'Indian',
    'Section 375',
    'The Great Indian Kitchen',
    'Bombay',
    'Maqbool',
    'Pink',
    'Thadam',
    'Omkara',
    'Kshanam',
    'Pelli Choopulu',
    'Carry On, Munna Bhai',
    'Shershaah',
    'Rangasthalam',
    'Baahubali 2: The Conclusion',
    'Naduvula Konjam Pakkatha Kaanom',
    'Pranchiyettan and the Saint',
    'Deewaar',
    'Padaiyappa',
    'Athadu',
    'Evaru',
    'Padosan',
    'Gulaal',
    'Thondi Muthalum Driksakshiyum',
    'K.G.F: Chapter 1',
    'Take Off',
    'Haider',
    'Dilwale Dulhania Le Jayenge',
    'Minnal Murali',
    'Maanagaram',
    'Android Kunjappan Ver ',
    'Aadukalam',
    'Vaaranam Aayiram',
    'Ugly',
    '22 Shey Shraban',
    'Ulidavaru Kandanthe',
    'Mother India',
    'Special 26',
    'Nayattu',
    'Ship of Theseus',
    'Bajrangi Bhaijaan',
    'Badhaai Ho',
    'The Music Room',
    'Deiva Thirumagal',
    'Dev.D',
    'Karnan',
    'Vaastav: The Reality',
    'Kirik Party',
    'Vedam',
    'The Brawler',
    'Ankhon Dekhi',
    'Gully Boy',
    'Company',
    'Charlie',
    'Manjhi: The Mountain Man',
    'Poove Unakkaga',
    'Pizza',
    'Malik',
    'Memories',
    'Arjun Reddy',
    'Ayyappanum Koshiyum',
    'My Name Is Khan',
    'Dil Bechara',
    'Vinnaithaandi Varuvaayaa',
    'Border',
    'Jab We Met',
    'Kal Ho Naa Ho',
    'Kaakha..Kaakha: The Police',
    'Super 30',
    'Mumbai Police',
    'Thulladha Manamum Thullum',
    'Sonchiriya',
    'Angamaly Diaries',
    'Unnaipol Oruvan',
    'Anjaam Pathiraa',
    'Hey Ram',
    'Baahubali: The Beginning',
    'Lakshya',
    'Vettaiyaadu Vilaiyaadu',
    'Pad Man',
    'Dor',
    'Dia',
    'Baby',
    'Hindi Medium',
    'Airlift',
    'Okkadu',
    'English Vinglish',
    'Manam',
    'Gangaajal',
    'The Lunchbox',
    'M.S. Dhoni: The Untold Story',
    'Johnny Gaddaar',
    'Ab Tak Chhappan',
    'Ayirathil Oruvan',
    'Pokiri',
    'Happy Days',
    'Ennu Ninte Moideen',
    'Goodachari',
    'Badla',
    'Joji',
    'RangiTaranga',
    'Secret Superstar',
    'Stanley Ka Dabba',
    'Nayak: The Real Hero',
    'Vicky Donor',
    'Mimi',
    'Thuppakki',
    'Ko',
    'Velaiyilla Pattathari',
    'Mr. India',
    'Don',
    'Raazi',
    'Udta Punjab',
    'Aligarh',
    'Veer Zaara',
    'Kaththi',
    'Rock On!!',
    'Arya',
    'Dasvidaniya',
    'Ghilli',
    'Guru',
    'Kai Po Che',
    'Samsara',
    '24',
    'Oye Lucky! Lucky Oye!',
    'Avane Srimannarayana',
    'Rockstar',
    'Eega',
    'Kushi',
    'Mumbai Meri Jaan',
    'The Tashkent Files',
    'Ugramm',
    'Sir',
    'Darr',
    'Kabhi Haan Kabhi Naa',
    'Kapoor & Sons',
    'Newton',
    'Aamir'
]


def play():
    p1n = input("Player 1, Please input your name: ")
    p2n = input("Player 2, Please input your name: ")
    p1s = 0
    p2s = 0
    turn = 0
    c = True
    cx = 1
    while(c):
        pc = 0
        if(turn % 2 == 0):
            print(p1n, ", Your turn!")
            qd = []
            movie = random.choice(movies)
            q = movie.lower()
            length = len(q)

            for i in range(length):
                if(q[i] == ' '):
                    qd.append(' ')
                else:
                    qd.append('*')
            for i in qd:
                print(str(i), end='')
            while(cx):
                ch = input(
                    " Enter 1 to guess a letter or 2 to guess the movie: ")
                pc += 1
                if(ch == '1'):
                    a = input("Enter your letter: ").lower()
                    for i in range(len(q)):
                        if(q[i] == a):
                            qd[i] = a
                    for i in qd:
                        print(str(i), end='')
                    if(qd.count('*') == 0):
                        print(" Correct Answer")
                        p1s += 10
                        print("You took ", pc, " chances!")
                        print("Your score is:", p1s)
                        cx = 0
                elif(ch == '2'):
                    ans = input("Enter your guess: ")
                    if(ans.lower() == movie.lower()):
                        print(" Correct Answer")
                        p1s += 10
                        print("You took ", pc, " chances!")
                        print("Your score is:", p1s)
                        cx = 0
                    else:
                        print("Wrong Answer! Try Again...")
                else:
                    break
        if(turn % 2 != 0):
            print(p2n, ", Your turn!")
            qd = []
            movie = random.choice(movies)
            q = movie.lower()
            length = len(q)
            for i in range(length):
                if(q[i] == ' '):
                    qd.append(' ')
                else:
                    qd.append('*')
            for i in qd:
                print(str(i), end='')
            while(cx):
                pc += 1
                ch = input(
                    " Enter 1 to guess a letter or 2 to guess the movie: ")
                if(ch == '1'):
                    a = input("Enter your letter: ").lower()
                    for i in range(len(q)):
                        if(q[i] == a):
                            qd[i] = a
                    for i in qd:
                        print(str(i), end='')
                    if(qd.count('*') == 0):
                        print(" Correct Answer")
                        p2s += 10
                        print("You took ", pc, " chances!")
                        print("Your score is:", p2s)
                        cx = 0
                elif(ch == '2'):
                    ans = input("Enter your guess: ")
                    if(ans.lower() == movie.lower()):
                        print(" Correct Answer")
                        p2s += 10
                        print("You took ", pc, " chances!")
                        print("Your score is:", p2s)
                        cx = 0
                    else:
                        print("Wrong Answer! Try Again...")
                else:
                    break
        turn += 1
        cx = input("Enter 1 to continue or 0 to quit: ")
        if(cx == '0'):
            c = False
            break


play()

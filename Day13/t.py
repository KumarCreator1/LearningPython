import random
import time

celebrities = [
    {"name": "Virat Kohli", "followers": 272, "nation": "India", "profession": "Cricketer", "platform": "Instagram"},
    {"name": "Cristiano Ronaldo", "followers": 585, "nation": "Portugal", "profession": "Footballer", "platform": "Instagram"},
    {"name": "Lionel Messi", "followers": 462, "nation": "Argentina", "profession": "Footballer", "platform": "Instagram"},
    {"name": "Selena Gomez", "followers": 417, "nation": "United States", "profession": "Musician / Actress", "platform": "Instagram"},
    {"name": "Kylie Jenner", "followers": 389, "nation": "United States", "profession": "TV personality / Business", "platform": "Instagram"},
    {"name": "Dwayne Johnson", "followers": 379, "nation": "United States", "profession": "Actor / Wrestler", "platform": "Instagram"},
    {"name": "Ariana Grande", "followers": 368, "nation": "United States", "profession": "Singer / Actress", "platform": "Instagram"},
    {"name": "Kim Kardashian", "followers": 356, "nation": "United States", "profession": "TV personality / Model", "platform": "Instagram"},
    {"name": "Beyoncé", "followers": 309, "nation": "United States", "profession": "Singer", "platform": "Instagram"},
    {"name": "Khloé Kardashian", "followers": 305, "nation": "United States", "profession": "TV personality / Model", "platform": "Instagram"},
    {"name": "Justin Bieber", "followers": 288, "nation": "Canada", "profession": "Singer", "platform": "Instagram"},
    {"name": "Taylor Swift", "followers": 259, "nation": "United States", "profession": "Singer", "platform": "Instagram"},
    {"name": "Neymar Jr.", "followers": 174, "nation": "Brazil", "profession": "Footballer", "platform": "Instagram"},
    {"name": "Rohit Sharma", "followers": 43, "nation": "India", "profession": "Cricketer", "platform": "Instagram"},
    {"name": "MS Dhoni", "followers": 48, "nation": "India", "profession": "Cricketer", "platform": "Instagram"},
    {"name": "Hardik Pandya", "followers": 41, "nation": "India", "profession": "Cricketer", "platform": "Instagram"},
    {"name": "KL Rahul", "followers": 21, "nation": "India", "profession": "Cricketer", "platform": "Instagram"},
    {"name": "Jasprit Bumrah", "followers": 19, "nation": "India", "profession": "Cricketer", "platform": "Instagram"},
    {"name": "Sachin Tendulkar", "followers": 49, "nation": "India", "profession": "Cricketer (Retired)", "platform": "Instagram"},
    {"name": "Suryakumar Yadav", "followers": 17, "nation": "India", "profession": "Cricketer", "platform": "Instagram"},
    {"name": "Shikhar Dhawan", "followers": 18, "nation": "India", "profession": "Cricketer", "platform": "Instagram"},
    {"name": "Shubman Gill", "followers": 16, "nation": "India", "profession": "Cricketer", "platform": "Instagram"},
    {"name": "Arijit Singh", "followers": 160, "nation": "India", "profession": "Singer", "platform": "Spotify"},
    {"name": "AR Rahman", "followers": 64, "nation": "India", "profession": "Composer / Singer", "platform": "Spotify"},
    {"name": "Pritam", "followers": 52, "nation": "India", "profession": "Composer / Singer", "platform": "Spotify"},
    {"name": "Neha Kakkar", "followers": 47, "nation": "India", "profession": "Singer", "platform": "Spotify"},
    {"name": "Diljit Dosanjh", "followers": 32, "nation": "India", "profession": "Singer / Actor", "platform": "Spotify"},
    {"name": "Badshah", "followers": 28, "nation": "India", "profession": "Rapper / Singer", "platform": "Spotify"},
    {"name": "Taylor Swift (Spotify)", "followers": 138, "nation": "USA", "profession": "Singer", "platform": "Spotify"},
    {"name": "Ed Sheeran", "followers": 120, "nation": "UK", "profession": "Singer", "platform": "Spotify"},
    {"name": "Billie Eilish", "followers": 113, "nation": "USA", "profession": "Singer", "platform": "Spotify"}
]


print("start")



def Answer(folA,folB):
    if folA>folB:
        return 'a'
    else:
        return 'b'

keepgoing = True
current_score=0



previous_ques=[]

while keepgoing==True:
    random_num_A=random.randint(0,29)
    random_num_B= random.randint(0,29)
    if random_num_A==random_num_B:
        random_num_B=random.randint(0,29)
        
    person_a= random.choice(celebrities)
    person_b= random.choice(celebrities)
    followA= person_a["followers"]
    followB= person_b["followers"]
    nameA= person_a["name"]
    nameB= person_b["name"]
    professionA= person_a["profession"]
    professionB= person_b["profession"]
    nationA= person_a["nation"]
    nationB= person_b["nation"]

    print(f"Option A: {nameA} a {professionA} from {nationA}")
    print(f"Option B: {nameB} a {professionB} from {nationB}")
    User_answer = input("who has more followers ? Type 'A' or 'B' ").lower()
    correct_answer = Answer(followA,followB)

    if User_answer==correct_answer:
        print("that's correct")
        current_score+=1
        
    else:
        print(f"that's wrong! your final score is {current_score}")
        keepgoing=False


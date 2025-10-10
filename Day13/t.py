import random
import time

celebrities = [
    {"name": "Virat Kohli", "followers": 273, "nation": "India", "profession": "Cricketer", "platform": "Instagram"},
    {"name": "Cristiano Ronaldo", "followers": 586, "nation": "Portugal", "profession": "Footballer", "platform": "Instagram"},
    {"name": "Lionel Messi", "followers": 464, "nation": "Argentina", "profession": "Footballer", "platform": "Instagram"},
    {"name": "Selena Gomez", "followers": 418, "nation": "United States", "profession": "Musician / Actress", "platform": "Instagram"},
    {"name": "Kylie Jenner", "followers": 391, "nation": "United States", "profession": "TV personality / Business", "platform": "Instagram"},
    {"name": "Dwayne Johnson", "followers": 381, "nation": "United States", "profession": "Actor / Wrestler", "platform": "Instagram"},
    {"name": "Ariana Grande", "followers": 371, "nation": "United States", "profession": "Singer / Actress", "platform": "Instagram"},
    {"name": "Kim Kardashian", "followers": 357, "nation": "United States", "profession": "TV personality / Model", "platform": "Instagram"},
    {"name": "Beyoncé", "followers": 310, "nation": "United States", "profession": "Singer", "platform": "Instagram"},
    {"name": "Khloé Kardashian", "followers": 307, "nation": "United States", "profession": "TV personality / Model", "platform": "Instagram"},
    {"name": "Justin Bieber", "followers": 290, "nation": "Canada", "profession": "Singer", "platform": "Instagram"},
    {"name": "Taylor Swift", "followers": 260, "nation": "United States", "profession": "Singer", "platform": "Instagram"},
    {"name": "Neymar Jr.", "followers": 175, "nation": "Brazil", "profession": "Footballer", "platform": "Instagram"},
    {"name": "Rohit Sharma", "followers": 44, "nation": "India", "profession": "Cricketer", "platform": "Instagram"},
    {"name": "MS Dhoni", "followers": 49, "nation": "India", "profession": "Cricketer", "platform": "Instagram"},
    {"name": "Hardik Pandya", "followers": 42, "nation": "India", "profession": "Cricketer", "platform": "Instagram"},
    {"name": "KL Rahul", "followers": 22, "nation": "India", "profession": "Cricketer", "platform": "Instagram"},
    {"name": "Jasprit Bumrah", "followers": 20, "nation": "India", "profession": "Cricketer", "platform": "Instagram"},
    {"name": "Sachin Tendulkar", "followers": 50, "nation": "India", "profession": "Cricketer (Retired)", "platform": "Instagram"},
    {"name": "Suryakumar Yadav", "followers": 18, "nation": "India", "profession": "Cricketer", "platform": "Instagram"},
    {"name": "Shikhar Dhawan", "followers": 19, "nation": "India", "profession": "Cricketer", "platform": "Instagram"},
    {"name": "Shubman Gill", "followers": 17, "nation": "India", "profession": "Cricketer", "platform": "Instagram"},
    {"name": "Arijit Singh", "followers": 161, "nation": "India", "profession": "Singer", "platform": "Spotify"},
    {"name": "AR Rahman", "followers": 65, "nation": "India", "profession": "Composer / Singer", "platform": "Spotify"},
    {"name": "Pritam", "followers": 53, "nation": "India", "profession": "Composer / Singer", "platform": "Spotify"},
    {"name": "Neha Kakkar", "followers": 48, "nation": "India", "profession": "Singer", "platform": "Spotify"},
    {"name": "Diljit Dosanjh", "followers": 33, "nation": "India", "profession": "Singer / Actor", "platform": "Spotify"},
    {"name": "Badshah", "followers": 29, "nation": "India", "profession": "Rapper / Singer", "platform": "Spotify"},
    {"name": "Taylor Swift (Spotify)", "followers": 139, "nation": "USA", "profession": "Singer", "platform": "Spotify"},
    {"name": "Ed Sheeran", "followers": 121, "nation": "UK", "profession": "Singer", "platform": "Spotify"},
    {"name": "Billie Eilish", "followers": 114, "nation": "USA", "profession": "Singer", "platform": "Spotify"}
]

print("start")

random_num_A=random.randint(0,29)
random_num_B= random.randint(0,29)

person_a= random.choice(celebrities)
person_b= random.choice(celebrities)
followA= person_a["followers"]
followB= person_b["followers"]
print(followA)
print(followB)

def CorrectAnswer(folA,folB):
    if folA>folB:
        return 'a'
    else:
        return 'b'
    




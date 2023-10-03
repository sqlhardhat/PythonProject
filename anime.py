from random import choice

#create list of animes
animes = ['naruto', 'haikyuu', 'mushishi', 'march comes in like a lion']

animes_by_mood = {
    'happy': ['naruto', 'haikyuu'],
    'relaxed': ['mushishi', 'march comes in like a lion'],
}
#print a random anime
print(choice(animes))

#input mood
print('what mood are you in')
mood = input()

#loop through and find a matching mood
if mood in animes_by_mood:
        suggested_anime = choice(animes_by_mood[mood])
        print(f"Recommended anime for '{mood}' mood: {suggested_anime}")
else:
    print('No anime found for the given mood')
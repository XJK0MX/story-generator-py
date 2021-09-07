import random

sentence_starter = ['about 100 years ago ','in the 20 bc ', 'once upon a time ']

character = ['there lived a king. ','there was a man named Jack. ', 'there lived a knight. ']

time = ['one day ', 'one evening ','one night ']

story_plot = ['he was pising by ', 'he was going for war ']

place = ['the montains. ', 'wild fields. ']

second_character = ['he saw a man ','he saw dark knight ']

age = ['who seemed to be in 20s ','who seemed very old ','who seemed young ']

work = ['he searching something or someone ','singing a ballade ']

work_of_character_1 = ['the man walked over ','the man never saw him ']

say_1 = ['and he said: you are alone ','and he said: where are you from? ','and he said: what is your name? ']

reaction_say_1 = ['i am a king of mountains ','i am a man who have everything ', 'i am the old man from forest ']

print(random.choice(sentence_starter)+random.choice(character)
+random.choice(time)+random.choice(story_plot)+random.choice(place)
+random.choice(second_character)+random.choice(age)+random.choice(work)
+random.choice(work_of_character_1)+random.choice(say_1)+random.choice(reaction_say_1))
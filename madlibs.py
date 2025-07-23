def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input

# Collect inputs
name = get_input("name")
adj1 = get_input("adjective")
place = get_input("place")
plural_noun1 = get_input("plural noun")
adj2 = get_input("adjective")
noun1 = get_input("noun")
verb_past = get_input("verb (past tense)")
sound = get_input("sound (e.g., whisper, growl)")
verb_ing = get_input("verb ending in -ing")
body_part_plural = get_input("body part (plural)")
adj3 = get_input("adjective")
noun2 = get_input("noun")
verb_present = get_input("verb (present tense)")
plural_noun2 = get_input("plural noun")
adj4 = get_input("adjective")

# Story string
story = f"""
It was a cold October night when {name} wandered into the {adj1} woods near {place}. 
The moon was high, casting long shadows between the trees like reaching {plural_noun1}.

As the wind howled, a {adj2} cabin appeared through the mist. 
Drawn by curiosity—and a strange pull in their chest—{name} stepped closer. 
The door creaked open to reveal a dusty room, filled with old {noun1}s and cobwebs.

They {verb_past} forward cautiously. Suddenly, a {sound} echoed from the hallway. 
Heart pounding, they followed the noise, their breath {verb_ing}.

The hallway stretched on, darker with each step. 
Then they felt it—something cold brushing against their {body_part_plural}. 
A chill ran down their spine.

"Go back," a voice whispered.

But they didn't. They couldn't. Something about the place was {adj3}—like it had been waiting.

In the final room, they found a {noun2} on a pedestal. 
It pulsed faintly, like it was alive. When they reached out to {verb_present} it, 
the door slammed shut behind them.

Now, no one hears from {name}. 
Except sometimes, late at night, the sound of {plural_noun2} echoes through the woods, 
followed by a single, {adj4} whisper:

"Join us…"
"""

# Output the final story
print(story)

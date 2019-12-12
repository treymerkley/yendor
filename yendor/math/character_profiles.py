#! /usr/bin/python3
"""defines the beastiary. It uses the ruleset provided in Microlite20
Golden Edition. Modify as needed to balance."""
<<<<<<< HEAD:yendor/math/character_profiles.py
CHARACTER_PROFILES = {
=======
beastiary = {
>>>>>>> parent of d579d7e... modified method of populating species drop-down:yendor/math/beastiary.py
    # 'Aboleth':
    # {
    #     'STR': '16',
    #     'DEX': '8d8+40',
    #     'MIND': '76',
    #     'CHAR': '+1',
    #     'Qualities': """4 tentacles +12 (1d6+9 and transformation);
    #     transformation, psionics, enslave; mucus cloud""",
    #     'Description': """The aboleth is a revolting fishlike amphibian found
    #     primarily in subterranean lakes and rivers. An aboleth has a pink
    #     belly. Four pulsating blueblack orifices line the bottom of its body
    #     and secrete gray slime that smells like rancid grease. It uses its
    #     tail for propulsion in the water and drags itself along with its
    #     tentacles on land. An aboleth weighs about 6,500 pounds.

    #     Aboleths speak their own language,
    #     as well as Undercommon and Aquan. """
    # },

    'Human':
    {
        'strength_bonus': '0',
        'dexterity_bonus': '0',
        'mind_bonus': '0',
        'charisma_bonus': '0',
        'Qualities': """ +1 to all skill rolls.
        Move 30’/per round or 20’/round in heavy armor.""",
        'Description': """Humans are usually the most common race, thanks to
        their ability in adapting to every kind of enviroment. Due to this they
        can live in a wild range of habitats and can easily learn lots of
        competencies. Skin color and body type varies heavily. """
    },
    'Elf':
    {
        'strength_bonus': '-1',
        'dexterity_bonus': '1',
        'mind_bonus': '2',
        'charisma_bonus': '0',
        'Qualities': """Darkvision. Immunity to magic sleep effects and ghoul
        paralysis. +2 on Listen, Search, and Spot checks. An elf who passes
        within 5 feet of a secret or concealed door can to a Search check to
        notice it as if she were actively looking for it.""",
        'Description': """Smaller than humans, have more angular and defined
        facial traits, pointy ears, and an unnatural beauty and grace. They
        seem detached from the world around them, seen by some as introversion
        or xenophobia. Elves are deeply connected to magic and nature and can
        live up to 500 years."""
    },
    'Dwarf':
    {
        'strength_bonus': '2',
        'dexterity_bonus': '0',
        'mind_bonus': '0',
        'charisma_bonus': '-1',
        'Qualities': """Move 20’/per round even in heavy armour.
        Darkvision.
        Stonecunning. +4 on checks to resist
        being  bull rushed/tripped when standing on the ground
        +2 racial bonus on saves against poison, spells and spell-like effects.
        +2 racial bonus on Appraise and Craft checks related to stone or metal
        items.""",
        'Description': """Dwarves are four feet tall, with squat, broad bodies,
        proud of their long and thick beards. Dwarves mistrust half-orcs, and
        fail to appreciate elves, whom they only ally with in their many
        battles against orcs, goblins, gnolls, bugbears and trolls."""
    },
    'Halfling':
    {
        'strength_bonus': '-1',
        'dexterity_bonus': '2',
        'mind_bonus': '0',
        'charisma_bonus': '0',
        'Qualities': """Small Creature.
        Move 20’/per round or 15’/round in heavy armor.
        +1 size bonus to Armor Class.
        +4  size bonus on Subterfuge checks to hide in outdoor environments.
        +2 morale bonus to saves against fear effects.
        +2 racial bonus on Climb, Jump, Listen, and Move Silently  checks.
        +1 racial bonus on all saving throws.
        +1 racial bonus on attack rolls with thrown weapons and slings.""",
        'Description': """They have thin lean bodies, no more than three and a
        half feet tall, have pointed ears, brown eyes and straight black hair
        held in a topknot which is a source of pride. Halfl ings are intensely
        curious, rambling and speaking very quickly when excited. They are
        masters at the art of insulting people."""
    },
    'Gnome':
    {
        'strength_bonus': '0',
        'dexterity_bonus': '1',
        'mind_bonus': '1',
        'charisma_bonus': '0',
        'Qualities': """Small creature.
        Move 20’/per round or 15’/round in heavy armor.
        +1 size bonus to Armor Class.
        +2 bonus to saving throws against illusions and+1 to DC for all saving
        throws against illusion spells cast by gnomes.
        +4 size bonus on Subterfuge checks to hide in underground environments.
        Once per day  may speak with burrowing animals (duration 1 minute).
        Low-Light Vision.
        +2 racial bonus on Listen checks.
        +2 racial bonus on Craft (alchemy) checks.""",
        'Description': """Gnomes are 3-3½ feet tall, naturally friendly, highly
        social and fun loving people. They have a deep relationship with nature
        and in the eyes of a gnome, animals are people too. Gnomes can perform
        the spell-like abilities of dancing lights, ghost sound and
        prestidigitation, that play a large role in their games."""
    },
    'Lizardman':
    {
        'strength_bonus': '2',
        'dexterity_bonus': '2',
        'mind_bonus': '-2',
        'charisma_bonus': '0',
        'Qualities': """Move 30’/per round or 20’/round in heavy armor.
        +5 natural armour bonus.• Natural Weapons: 2 claws (1d4) and bite (1d4).
        A lizardfolk can hold its breath for 4xSTR  rounds before it risks
        drowning.
        +4 racial bonus on Jump, Swim, and Balance checks because of their
        tails
        +1 on Fortitude rolls and +3 on Refl exes rolls""",
        'Description': """Primitive reptilian humanoids with scaly skin,
        normally dull, earthy colors such as green, brown, or gray. They use
        their tail for balance, which measures three to four feet long. There
        are several species of lizardmen, from small and skinny to tall and
        strong ones. Lizardfolk are usually neutral."""
    },
    'Half-Orc':
    {
        'strength_bonus': '3',
        'dexterity_bonus': '0',
        'mind_bonus': '-1',
        'charisma_bonus': '-2',
        'Qualities': """Move 30’/per round.
        Darkvision.
        +4 racial bonus on intimidate checks.
        Orc Ferocity: Once per day, when brought below 0 hit points but not
        killed, he can fight on for one more round as if disabled. At the end
        of his next turn, unless brought to above 0 hit points, he falls
        unconscious and begins dying.
        Rage: once a day can enrage and gain +2 to Strength and Fortitude. At
        the end becomes fatigued.
        Natural Weapons: bite (1d4). """,
        'Description': """all and strong, they see themselves gifted with
        strength and  opportunities  beyond  those  of  either  of  their
        parent races. They tend toward a chaotic outlook drawing strength of
        character from the inequities they face. Half-orcs rarely have strong
        religious views."""
    },
}

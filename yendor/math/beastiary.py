#! /usr/bin/python3
"""defines the beastiary. It uses the ruleset provided in Microlite20
Golden Edition. Modify as needed to balance."""
BEASTIARY = {
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
    'Half-Elf':
    {
        'strength_bonus': '0',
        'dexterity_bonus': '1',
        'mind_bonus': '1',
        'charisma_bonus': '0',
        'Qualities': """+1 Comm.
        Move 30’/per round or 20’/round in heavy armor.
        +1 to any 2 Skills.
        Immunity to magic sleep effects.
        Low-Light Vision.
        +1 racial bonus on Listen, Search, and Spot checks.
        +1 racial bonus to your Will defense.
        +2 racial bonus on Diplomacy and Gather Information checks.""",
        'Description': """In them humans see the grace, the fair face and the
        pointy ears of elves while these see the opposite. A half-elf’s skin is
        pale  and  their  eyes  have  the  bright  green  or  blue  hue common
        to elves. They have the curiosity and the ambitions of humans and the
        sense for magic and love for nature of elves. """
    },
    'Mul (Half-Dwarf)':
    {
        'strength_bonus': '2',
        'dexterity_bonus': '0',
        'mind_bonus': '-1',
        'charisma_bonus': '-1',
        'Qualities': """+1 Physic.
        Move 30’/per round.
        Muls may be any chaotic alignment.
        Darkvision.
        +2 racial bonus on Intimidate checks.
        Muls are able to work longer and harder without rest than most other
        races. Regardless of the preceding type of exertion, eight hours of
        sleep will let a Mul become fully rested,
        ready to begin work again. """,
        'Description': """They  retain  the  height  and  cunning  of  humans,
        plus  the durability, raw strength and constitution of dwarves. Born
        usually as slaves, they can perform heavy work for days and have gruff
        personality and violent reactions. Fair skinned, they  have
        pale-colored  eyes,  no  hair  or  beard.  Muls are sterile."""
    },
    'Tiefling':
    {
        'strength_bonus': '0',
        'dexterity_bonus': '2',
        'mind_bonus': '1',
        'charisma_bonus': '-2',
        'Qualities': """Move 30’/per round or 20’/round in heavy armor.
        +2 racial bonus on Bluff and Hide checks.
        Darkvision out to 60 feet.
        Resistance to cold 5, electricity 5, and fire 5.
        Darkness: can use Darkness  spell once per day.""",
        'Description': """Their lineage can be traced back to to a fiend or
        demon. Tiefl ings have any of a number of features that reference
        (directly or indirectly) their fi endish lineage of humans and the
        sense for magic and love for nature of including horns of various
        styles, pointed teeth, hooves, tails, and unusually colored eyes. They
        are not necessarily evil, but usually sneaky and subtle."""
    },
    'Half-Fiend':
    {
        'strength_bonus': '-1',
        'dexterity_bonus': '-1',
        'mind_bonus': '3',
        'charisma_bonus': '-2',
        'Qualities': """Move 30’/per round or 20’/round in heavy armor.
        Darkvision out to 60 feet.
        Immunity to poison.• Resistance to acid 10, cold 10, electricity 10,
        and fire 10.
        Darkness: can use Darkness  spell once per day.
        Non-good alignment.
        Natural Weapons: claw (1d4) and bite (1d6)
        Bat wings:  can fl y at the base creature’s base land speed. """,
        'Description': """They born from fiends who have mated with a human.
        Often grotesque mockeries of humans, rarely one learns from and takes
        on characteristics of its non-fi endish parents, turning from its evil
        heritage. Never truly fi tting into society, half-fi ends are usually
        loners. They are outcasts, hated corrupters of the natural order."""
    },
    'Drow':
    {
        'strength_bonus': '-2',
        'dexterity_bonus': '2',
        'mind_bonus': '2',
        'charisma_bonus': '0',
        'Qualities': """Move 30’/per round or 20’/round in heavy armor.
        Immunity to magic sleep effects.
        +2 racial on Will saving throws against enchantment spells or effects.
        Darkvision out to 120 feet.
        +2 on Listen, Search, and Spot checks. A drow who  passes within 5 feet
        of a secret or concealed door can to a Search check to notice it as if
        she were actively looking for it.
        Spell-Like Abilities once per day: Dancing Lights, Darkness, Faerie
        Fire.
        Light Blindness: Abrupt exposure to bright light blinds drow for 1
        round. On subsequent rounds, they are dazzled as long as they remain in
        the affected area.""",
        'Description': """Drows are black-skinned and pale haired relatives of
        elves, with sharp features, large eyes and pointed ears. Drows are
        silent and swift, highly resistant to magic and capable to use some
        innate magical abilities even if not spellcasters. They are  described
        as  chaotic  or  evil  in  alignment,  and  highly intelligent."""
    },
    'Minotaur':
    {
        'strength_bonus': '2',
        'dexterity_bonus': '0',
        'mind_bonus': '-2',
        'charisma_bonus': '0',
        'Qualities': """+1 Physic
        Move 30’/per round.
        Large size: 1 to AC, 1 on attack rolls, 4 on Hide checks, +4 on grapple
        checks, double lifting and carrying limits.
        Darkvision: 60 feet.
        +2 racial bonus on Search, Spot, and Listen checks.
        +3 natural armor bonus.
        Natural  Weapon:  Gore  (1d6+STR  bonus  if  first  attack,  1d6  if
        used  as secondary).
        Powerful Charge: in addition to the normal benefits/hazards of a
        charge, allows the minotaur to make a single gore attack dealing
        4d6 + STR bonus damages.
        Natural Cunning.
        Immune to Maze spell.
        Scent
        -2 on Balance, Escape Artist and Tumble skill checks.""",
        'Description': """Their bodies (around 7ft tall) are humanoid and
        covered in short fur, but their heads are bovine and their back legs
        end in cloven hooves. They are proud, noble, tenacious and bold, deeply
        spiritual and respectful of their elders. Generally kind and
        benevolent, they become furious, savage and brutal in combat."""
    },
    'Half-Giant':
    {
        'strength_bonus': '2',
        'dexterity_bonus': '0',
        'mind_bonus': '2',
        'charisma_bonus': '0',
        'Qualities': """+2 Physic
        Move 30’/per round.
        Large size: –1 to AC, –1 on attack rolls, 4 on Hide checks, +4 on
        grapple checks, double lifting and carrying limits.
        Giant: not subject to spells or effects that affect only humanoids
        (charm person or dominate person).
        Low-Light Vision.
        +2 racial bonus on saving throws against all fire spells and effects.
        Spell-Like  Abilities  once  per  day:  Stomp  -  his  foot  stomp,
        precipitating  a psychokinetic shock wave that travels along the ground,
        topples creatures (they become prone and take 1d4 non-lethal damages)
        and loose objects. Save DC is 10+half-giant STR modifier.""",
        'Description': """A cross between humans and giants (7/8 ft tall, weigh
        250/400  pounds)  usually  held  captive  as  warriors and laborers. As
        a result, nothing is more important to them than their freedom. Like
        humans they are curious, cooperative and communicative, with a general
        tendency toward kindness. They disdain religion. """
    },
}

"""Primary combat beastiary"""
BEASTIARY = {
    "Aboleth": {
        'AC': '16',
        'HD': '8d8+40',
        'HP': '76',
        'Init': '+1',
        'Attacks and Qualities': """4 tentacles +12 (1d6+9 and transformation);
        transformation, psionics, enslave; mucus cloud"""
    },
    "Achaierai": {
        'AC': '20',
        'HD': '6d8+12',
        'HP': '39',
        'Init': '+1',
        'Attacks and Qualities': """2 claws +9 (2d6+4), bite +4 (4d6+2); black cloud; SR 19"""},
# Allip 15 4d12 26 +5incorporeal touch +3 (1d4 perm. MIND); babble,  madness;  undead,  incorporeal, +2 turn resistance
# Ani. Object, Tiny 14 1/2 d10 2 +2 slam +1 (1d3-1); construct, hardness, etc.
# Ani. Object, Small 14 1d10 5 +1 slam +1 (1d4); construct, hardness, etc.
# Ani. Object, Medium 14 2d10 11 0slam  +2  (1d6+1);  construct,  hardness, etc.
# Ani. Object, Large 14 4d10 22 0 slam  +5  (1d8+4);  construct,  hardness, etc.
# Ani. Object, Huge 13 8d10 44 -1 slam  +9  (2d6+7);  construct,  hardness, etc.
# Ani. Object, Gargantuan12 16d10 88 -2 slam +15 (2d8+10); construct, hardness, etc.
# Ani. Object, Colossal 11 32d10 176 -3 slam +25 (4d6+13); construct, hardness, etc.
# Ankheg 18 3d10+9 25 0 bite +6 (2d6+7); imp. grab, acid, spit acid; tremorsense
# Aranea 13 3d8+6 19 +6 bite  +4  (1d6  &  poison);  poison  (DC13, 1d6/2d6 Str), spells, web; alternate form
# Arrowhawk, Juv. 20 3d8+3 16+5 electricity ray +9 (2d6), bite +9 (1d6+1); electricity ray; immunities, fi re and cold resistance 20
# Arrowhawk, Adult21 7d8+7 38+5electricity ray +12 (2d8), bite +12 (1d8+2); electricity ray; immunities, fi re and cold resistance 20
# Arrowhawk, Elder 22 15d8+45 112 +5electricity ray +19 (2d8), bite +20 (2d6+9); electricity ray; immunities, fi re and cold resistance 20
# Assassin Vine 15 4d8+12 30 0slam +7 (1d6+7); camoufl age, electricity immunity,  cold  and  fi re  resistance  20, blindsight
# Basilisk 16 6d10+12 45 -1 bite +8 (1d8+3); petrifying gaze
# Beholder20 11d8+11 60 +4 eye rays +7 (var.), bite +2 (2d4); eye rays; all-around vision, antimagic cone, fly
# Blink Dog 16 4d10 22 +3 bite  +4  (1d6);  blink,  dimension  door, scent
# Bugbear 17 3d8+3 16 +1 morningstar  +4  (1d8+2),  javelin  +3 (1d6+2); darkvision 60 ft.
# Carrion Crawler 17 3d8+6 19 +2 8  tentacles  +3(par),  bite  -2(1d4+1); paralysis (DC13); scent
# Centaur 15 4d8+8 26 +2 greatclub  +7  (1d10+4),  2  hooves  +3 (1d6+2), mighty composite longbow +5 (1d8+4)
# Chimera 16 9d10+27 76 +1 bite +12 (2d6+4), bite +10 (1d8+2), butt +10 (1d8+2), 2 claws +10 (1d6+2); breath (40 or 20 ft., DC17, 3d8); scent
# Cockatrice 14 5d10 27 +3 bite +4 (1d4-2); petrifi cation; petrifi cation immunity
# Devil, Imp 18 3d8 13 +3 sting  +8  (1d4  &p);  poison  (DC13,  1d4/2d4 Dex), spell-like abilities; DR 5/silver, SR 5, poison immunity, fi re resistance 20, see in darkness, polymorph, regen. 2
# Dino, Deinonychus 16 4d10+12 34 +2 rake +6 (2d6+4), 2 claws +1 (1d3+2), bite +1 (2d4+2); scent
# Dino, Elasmosaur. 13 5d10+25 52 +2 bite +9 (2d8+12); scent
# Dino, Megaraptor 16 8d10+32 76 +2 rake +9 (2d8+5), 2 claws +4 (1d4+2), bite +4 (2d6+2); scent
# Dino, Triceratops 18 16d10+112 200 -1 gore +15 (2d8+7); charge for x2 damage, trample; scent
# Dino, Tyrannosaur. 14 18d10+72 171 +1 bite  +20  (5d8+13);  improved  grab, swallow whole; scentDire Rat 15 1d8+1 5 +3 bite +4 (1d4 &d); disease (DC12); scent
# Dire Weasel 16 3d8 13 +4 bite +6 (1d6+3); attach, blood drain (2d4 Str/rnd); scent
# Dire Badger 16 3d8+12 25 +3 2 claws +4 (1d4+2), bite -1 (1d6+1); rage; scent
# Dire Bat 20 4d8+12 30 +6 bite +5 (1d8+4); blindsight
# Dire Ape 15 5d8+10 32 +2 2 claws +8 (1d6+6), bite +3 (1d8+3); rend 2d6+12; scentDire Wolverine 16 5d8+20 42 +3 2 claws +8 (1d6+6), bite +3 (1d8+3); rage; scent
# Dire Wolf 14 6d8+18 45 +2 bite +10 (1d8+10); trip; scent
# Dire Boar 15 7d8+21 52 0 bite +12 (1d8+12); ferocity; scent
# Dire Lion 15 8d8+24 60 +2 2  claw  +12  (1d6+7),  bite  +7  (1d8+3); pounce, rake 1d6+3; scent
# Dire Bear 17 12d8+48 102 +1 2 claws +18 (2d4+10), bite +13 (2d8+5); imp. grab; scent
# Dire Tiger 16 16d8+48 120 +2 2  claw  +18(2d4+8),  bite  +13  (2d6+4); pounce, rake 2d4+4; scent
# Dire Shark 17 18d8+54 135 +2 bite  +17  (2d6+9);  impossible  grab, swallow whole; keen scent
# Doppelganger 15 4d8+4 22 +1 2 slams +4 (1d6+1); detect thoughts; alter self, immunities
# Dragon, Black, Adult 27 19d12+76 199 0 bite +24 (2d6+6), 2 claws +19 (1d8+3), 2 wings +19 (1d6+3), tail slap +19 (1d8+9); breath  (80  ft.,  DC23,  12d4),  spell-like abilities,  spells  (3rd),  fright  (180  ft., DC20);  blindsight  (180  ft.),  DR  5/+1, immunities, SR 18
# Dragon, Blue, Adult 28 21d12+105 241 +4 bite  +26  (2d8+7),  2  claws  +21  (2d6+3), 2  wings  +21  (1d8+3),  tail  slap  +21 (2d6+10);  breath  (100  ft.,  DC25,  12d8), spell-like abilities, spells (5th), fright (180 ft., DC23); blindsight (180 ft.), DR 5/+1, immunities, SR 21
# Dragon, Green, Adult 27 20d12+100 230 +4 bite  +25  (2d8+7),  2  claws  +20  (2d6+3), 2  wings  +20  (1d8+3),  tail  slap  +20 (2d6+10);  breath  (50  ft.,  DC25,  12d6), spell-like abilities, spells (5th), fright (180 ft., DC23); blindsight (180 ft.), DR 5/+1, immunities, SR 21
# Dragon, Red, Adult 29 22d12+110 253 +4bite +31 (2d8+11), 2 claws +26 (2d6+5), 2 wings +26 (1d8+5), tail slap +26 (2d6+16); breath (50 ft., DC26, 12d10), spells (7th), fright (180 ft., DC24); blindsight (180 ft.), fire  subtype,  DR  5/+1,  immunities,  SR 21
# 85Dragon, White, Adult 26 18d12+72 189 0 bite +23 (2d6+6), 2 claws +18 (1d8+3), 2 wings +18 (1d6+3), tail slap +18 (1d8+9); breath  (40  ft.,  DC23,  6d6),  spell-like abilities, spells (1st), fright (180 ft., Will DC 19); blindsight (180 ft.), cold subtype, DR 5/+1, immunities, SR 18
# Dragon, Brass, Adult 27 19d12+76 199 0 bite +24 (2d6+6), 2 claws +19 (1d8+3), 2 wings +19 (1d6+3), tail slap +19 (1d8+9); breath (80 ft., DC23, 6d6 or 40 ft., sleep 1d6+6),  spell-like  abilities,  spells  (7th), fright (180 ft., DC21); blindsight (180 ft), fire s-type, DR 5/+1, immun., SR 20
# Dragon, Copper, Adult 28 20d12+80 210 +4 bite +25 (2d6+6), 2 claws +20 (1d8+3), 2 wings +20 (1d6+3), tail slap +20 (1d8+9); breath (80 ft., DC24, 12d4 or 40 ft., slowed 1d6+6),  spell-like  abilities,  spells  (7th), fright (180 ft., DC23); blindsight (180 ft.), DR 5/+1, immunities, SR 21
# Dragon, Gold, Adult 30 23d12+115264 +4 bite +32 (2d8+11), 2 claws +27 (2d6+5), 2 wings +27(1d8+5), tail slap +27 (2d6+16); breath (50 ft., DC26, 12d10 or 6 Str), spell-like abilities, spells (7th), fright (180 ft., DC26); blindsight (180 ft.), fire subtype, DR 5/+1, immunities, SR 23
# Dragon, Silver, Adult 29 22d12+110 253 +4 bite +28 (2d8+8), 2 claws +23 (2d6+4), 2 wings +23 (1d8+4), tail slap +23 (2d6+12); breath (50 ft., DC26, 12d8 or paralyzed 1d6+6), spell-like abils, spells (7th), fright (180  ft.,  DC26);  blindsight  (180  ft.),  DR 5/+1, immunities, SR 22
# Dryad 12 2d6 7 +6 dagger  +1  (1d4);  spell-like  abilities; symbiosis
# Dwarf 16 1d8+1 5 0 waraxe +1 (1d10), short bow +1 (1d6); +1 attacks vs. orcs/goblins; +4 AC vs. giants, +2 save vs. spells/poisons, darkvision 60 ft.Dwarf, Deep 16 1d8+1 5 0 waraxe +1 (1d10), short bow +1 (1d6); +4 AC vs giants, +3 save vs. spells/poisons, darkvision  90  ft.,  light  sensitivity (-1 attacks)
# Dwarf, Derro 16 1d8+1 5 0dagger  +0  (1d4),  +0  (1d4),  repetition crossbow  +3  (1d8  &p);  poison  (DC13, 1/1d2  Con),  +1  attacks  vs  orc/goblins; +4  AC  vs  giants,  +2  saves  vs.  spells/poisons,  SR  18,  darkvision  30  ft.,  light vulnerability
# Dwarf, Gray 16 1d8+1 5 0 heavy    pick    +1    (1d6),    light crossbow+1(1d8);  +1  attacks  vs.  orc/goblins;  +4  AC  vs.  giants,  +2  saves  vs. spells/poisons,  immune  to  paralysis/phantasm; spell abilities, darkvision 120 ft., light sensitivity
# Elemental, Air, Small 17 2d8 9 +7 slam  +5  (1d4);  air  mastery,  whirlwind; elemental
# Elemental, Air, Medium 18 4d8+8 26 +9 slam +8 (1d6+1); air mastery, whirlwind; elemental
# Elemental, Air, Large 20 8d8+24 60 +11 slam  +12/+7  (2d6+3);  air  mastery, whirlwind; elemental, DR 10/+1
# Elemental, Air, Huge 21 16d8+64 136 +13 slam  +19/+14/+9  (2d8+6);  air  mastery, whirlwind; elemental, DR 10/+2
# Elemental, Air, Greater 26 21d8+84 178 +14 slam +23/+18/+13 (2d8+7); air mastery, whirlwind; elemental, DR 10/+2
# Elemental, Air, Elder 27 24d8+96 204 +15 slam  +27/+22/+17/+12  (2d8+9);  air mastery,  whirlwind;  elemental,  DR 15/+3
# Elemental, Earth, Small 17 2d8+2 11 -1 slam  +5  (1d6+4);  earth  mastery,  push; elemental
# Elemental, Earth, Medium 18 4d8+12 30 -1 slam  +8  (1d8+7);  earth  mastery,  push; elemental
# Elemental, Earth, Large 18 8d8+32 68-1 slam  +12/+7  (2d8+10);  earth  mastery, push; elemental, DR 10/+1
# Elemental, Earth, Huge 18 16d8+80 152 -1 slam   +19/+14/+9   (2d10+13);   earth mastery, push; elemental, DR 10/+2
# Elemental, Earth, Greater 20 21d8+105 199 -1 slam  +23/+18/+13  (2d10+15);  earth mastery, push; elemental, DR 10/+2
# Elemental, Earth, Elder 22 24d8+120 228 -1 slam +27/+22/+17/+12 (2d10+16); earth mastery, push; elemental, DR 15/+3
# Elemental, Fire, Small 15 2d8 9 +5 slam +3 (1d4 & 1d4 fire); burn; elemental, fire subtype
# Elemental, Fire, Medium 16 4d8+8 26 +7 slam  +6  (1d6+1  &  1d6  fire);  burn; elemental, fire subtype
# Elemental, Fire, Large 18 8d8+24 60 +9 slam  +10/+5  (2d6+3  &  2d6  fire);  burn; elemental, DR 10/+1, fire subtype
# Elemental, Fire, Huge 19 16d8+64 136 +11 slam  +17/+12/+7  (2d8+6  &  2d8  fire); burn; elemental, DR 10/+2, fire subtype
# Elemental, Fire, Greater 24 21d8+84 178 +12 slam  +21/+16/+11  (2d8+7  &  2d8  fire); burn; elemental, DR 10/+2, fire subtype
# Elemental, Fire, Elder 25 24d8+96 204 +13 slam  +25/+20/+15/+10  (2d8+9  &  2d8 fire);  burn;  elemental,  DR  15/+3,  fire subtype
# Elemental, Water, Small 17 2d8+2 11 0 slam +4 (1d6+3); water mastery, drench, vortex; elemental
# Elemental, Water, Medium 19 4d8+12 30 +1 slam +6 (1d8+4); water mastery, drench, vortex; elemental
# Elemental, Water, Large 20 8d8+32 68 +2 slam  +10/+5  (2d8+7);  water  mastery, drench, vortex; elemental, DR 10/+1
# Elemental, Water, Huge 21 16d8+80 152 +4 slam  +17/+12/+7  (2d10+10);  water mastery,  drench,  vortex;  elemental,  DR 10/+2
# Elemental, Water, Greater 22 21d8+105 199 +5 slam  +21/+16/+11  (2d10+12  );  water mastery,  drench,  vortex;  elemental,  DR 10/+2
# Elemental, Water, Elder 23 24d8+120 228 +6 slam +25/+20/+15/+10 (2d10+13); water mastery,  drench,  vortex;  elemental,  DR 15/+3
# Elf 15 1d8-1 3 +1 longsword   +1   (1d8),   longbow   +2 (1d8);  low-light  vision,  +2  saves  vs. enchantment, immune to sleep
# Elf, Aquatic 15 1d8 4 +1 trident  +1  (1d8),  light  spear  +1  (1d8), net  touch  +2  (entangle);  gills,  low-light vision, +2 save vs enchantments, immune to sleep
# Elf, Dark 15 1d8-1 3 +1 longsword  +1  (1d8),  longbow  +2  (1d8 &p);  poison  (DC17,  1  min./2d4  hours unconscious),  darkvision  120  ft.,  +2 saves vs. spells, immune to sleep, light blindness, spell abilities, SR 12
# Elf, Wild 15 1d8 4 +1 longsword   +1   (1d8),   longbow   +2 (1d8);  low-light  vision,  +2  saves  vs. enchantment, immune to sleep
# Elf, Wood 15 1d8-1 3 +1 longsword  +1  (1d8+1),  longbow  +2 (1d8);  low-light  vision,  +2  saves  vs. enchantment, immune to sleep
# Ettercap 14 5d8+5 27 +3 bite +3 (1d8 &p), 2 claws +1 (1d3); poison (DC13, 1d6/2d6 Dex), web, poison; low-light vision
# Ettin 18 10d8+20 65 +3 2   greatclubs   +12/+7   (1d10+6),   2 longspears +5/+0 (1d8+6); superior two-weapon fighting; darkvision 90 ft.
# Gargoyle 16 4d10+16 38 +2 2  claw  +6  (1d4),  bite  +4  (1d6),  gore  +4 (1d6); DR 15/+1, frz.
# Genie, Janni 18 6d8+6 33 +6 scimitar +9/+4 (1d8+4), longbow +8/+3 (1d8);  spell-like  abilities;  plane  shift, telepathy,  fire  resistance  30,  elemental endurance
# Genie, Djinni 16 7d8+14 45 +8 slam +10/+5 (1d8+6); spell-like abilities, air  mastery,  whirlwind;  plane  shift, telepathy, acid immunity
# Genie, Efreeti 18 10d8+20 65 +7 slam +15/+10 (1d8+9 and 1d6 fire); spell-like abilities, heat; plane shift, telepathy
# Ghoul 14 2d12 13 +2 bite +3 (1d6+1 & par), 2 claws +0 (1d3 &par);  paralysis  (DC14),  create  spawn; undead, +2 turn resistance
# Ghast 16 4d12 26 +2 bite +4(1d8+1 & par), 2 claws +1 (1d4 & par); stench (10 ft., DC15, -2 to all rolls), paralysis (DC15), create spawn; undead, +2 turn resistance
# Giant, Hill 20 12d8+48 102 -1 huge  greatclub  +16/+11  (2d6+10),  rock +8/+3  (2d6+7);  rock  throwing,  rock catching
# Giant, Stone 25 14d8+56 119 +2 huge  greatclub  +17/+12  (2d6+12),  rock +12/+7  (2d8+8);  rock  throwing;  rock catching
# Giant, Frost 21 14d8+70 133 -1 huge  greataxe  +18/+13  (2d8+13),  rock +9/+4  (2d6+9);  rock  throwing;  rock catching, cold subtype
# Giant, Fire 21 15d8+75 142 -1 huge greatsword +20/+15/+10 (2d8+15), rock +10/+5/+0 (2d6+10 & 2d6 fire); rock throwing; rock catching, fire subtype
# Giant, Cloud 21 17d8+102 178 +1 gargantuan  morningstar  +22/+17/+12 (4d6+18),  rock  +12/+7/+2  (2d8+12); rock  throwing,  spell-like  abilities;  rock catching, scent
# Giant, Storm 27 19d8+114199 +2 gargantuan  greatsword  +26/+21/+16 (4d6+21), gargantuan mighty composite longbow  +14/+9/+4  (2d8+14);  spelllike abilities;   electricity   immune,   rock catching,  freedom  of  movement,  water breath.
# Giant Eagle 15 4d10+4 26 +3 2  claws  +7  (1d6+4),  bite  +2  (1d8+2); evasion
# Giant Owl 15 4d10+4 26 +32  claws  +7  (1d6+4),  bite  +2  (1d8+2); superior low-light visionGirallon 16 7d10+14 52 +3 4 claws +12 (1d4+8), bite +7 (1d8+4); rend 2d4+12; scentGnoll 17 2d8+2 11 0 battleaxe +3 (1d8+2), shortbow +1 (1d6); darkvision 60 ft.
# Gnome 16 1d8+1 5 0 short sword +2 (1d6-1), light crossbow+2 (1d8); spells; low-light vision, +2 save vs illusion, +1 attacks vs kobold/goblin, +4 AC vs giant
# Gnome, Deep 21 1d84 0 short sword +2 (1d6-1), light crossbow+2 (1d8);  spells;  nondetectable,  darkvision 120  ft.,  +2  save  vs  illusion,  +1  atk  vs gobln., DR 12
# Gnome, Forest 16 1d8+1 5 0 short sword +2 (1d6-1), light crossbow+2 (1d8); pass., low-light vision, +2 save vs illusion, +1 attacks vs humanoids, +4 AC vs giant
# Goblin 15 1d8 4 +1 morningstar +1 (1d8-1), dart +3 (1d4-1); darkvision 60 ft.Golem, Flesh 18 9d10 49 -1 2 slams +10 (2d8+5); berserk; construct, magic immunity, DR 15/+1
# Golem, Clay 22 11d10 60 -1 2  slams  +14  (2d10+7);  berserk,  wound; construct,  magic  immunity,  DR  20/+1, immune to piercing/slashing, haste
# Golem, Stone 26 14d10 77 -1 2  slams  +18  (2d10+9);  slow;  construct, magic immunity, DR 30/+2
# Golem, Iron 30 18d10 99 -1 2  slams  +23  (2d10+11);  breath  (10 ft.,p);  poison  (DC17,  1d4  STR/death), construct,  magic  immunity,  DR  50/+3, rust vulnerability
# Gorgon 18 8d10+24 68 +4 gore +12 (1d8+7); breath weapon (60 ft., Fort DC17, turn to stone), trample 1d8+7; scent
# Halfling 15 1d8 4 +1 light  sword+2  (1d8-1),  heavy  crossbow +3 (1d10); +2 saves vs. fearHalfling, Tallfellow 15 1d8 4 +1light  sword+2  (1d8-1),  heavy  crossbow +3 (1d10); +2 saves vs. fearHalfling, Deep 15 1d8 4 +1 light  sword+2  (1d8-1),  heavy  crossbow +3 (1d10); +2 saves vs. fear, darkvision 60 ft., stonecunning
# Harpy 13 7d8 31 +2 club  +7/+2  (1d4),  2  claws  +2  (1d3); captivating song
# Hell Hound 16 4d8+4 22 +5 bite  +5  (1d8+1);  breath  (30  ft.,  DC13, 1d4+1); scent, fire subtype
# Hippogriff 15 3d10+9 25 +2 2 claws +5 (1d4+4), bite +0 (1d8+2)Hobgoblin 15 1d8+1 5 +1longsword  +1  (1d8),  javelin  +2  (1d6); darkvision 60 ft.
# 89Homunculus 14 2d10 11 +2 bite +2 (1d4-1 &p); poison (DC11, 1/ 5d6 min. sleep), construct
# Howler 17 6d8+12 39 +7 bite +10 (2d8+5), 1d4 quills +5 (1d4+2); quills, howl
# Hydra (5 heads) 15 5d10+25 52 +1 5 bites +4 (1d10+3); scent
# Hydra (6 heads) 15 6d10+30 63 +1 6 bites +5 (1d10+3); scent
# Hydra (7 heads) 15 7d10+35 73 +1 7 bites +7 (1d10+4); scent
# Hydra (8 heads) 15 8d10+40 84 +1 8 bites +8 (1d10+4); scent
# Hydra (9 heads) 15 9d10+45 94 +1 9 bites +9 (1d10+5); scent
# Hydra (10 heads) 15 10d10+50 105 +1 10 bites +10 (1d10+5); scent
# Hydra (11 heads) 15 11d10+55 115 +1 11 bites +12 (1d10+6); scent
# Hydra (12 heads) 15 12d10+60 126 +1 12 bites +13 (1d10+6); scent
# Invisible Stalker 17 8d8+16 52 +8 slam +10/+5 (2d6+6); elemental, natural invisibility, imp. track
# Kobold 15 1/2 d8 2 +1  h-spear  -1  (1d6-2),  light  crossbow+2 (1d8); darkvision 60, light sensivity
# Kraken 20 20d10+180 290 +4 2  tentacle  rakes  +28  (2d8+12),  6  arms +23 (1d6+6), bite +23 (4d6+6); improved grab, constrict 2d8+12 or 1d6+6; jet, ink cloud, spell-like abilities
# Kuo-Toa 18 2d8+2 11 0 spear   +3   (1d8+1),   bite   -2   (1d4); lightning   bolt,   pincer   staff;   keen sight,  slippery,  adhesive,  immunities, electricity resistance 30, light blindness, amphibiousLamia 17 9d10+9 58 +2 touch  +9  (1  permanent  MIND  drain), dagger +11/+6 (1d4); spell-like abilities, wisdom drain
# Lammasu 14 7d10+21 59 0 2 claws +12 (1d6+6); spells, pounce, rake 1d6+3;  magic  circle  against  evil,  spell-like abilities
# Lizardfolk 15 2d8+2 11 0 2 claws +2 (1d4+1), bite +0 (1d4), javelin +1 (1d6+1)Locathah 14 2d8 9 +1 longspear  +1  (1d8),  light  crossbow  +2 (1d8)Magmin 14 2d8 9 +1 burning  touch  +1  (1d8  fire  and combustion);  combustion,  fiery  aura; elemental,  fire  subtype,  melt  weapon, DR 15/+1
# Manticore 16 6d10+24 57 +2 2  claw  +9  (2d4+5),  bite  +7  (1d8+2),  6 spikes +6 (1d8+2); scent
# Medusa 15 6d8 +6 33 +2 shortbow  +8/+3  (1d6),  dagger  +6/+1 (1d4), snakes +3 (1d4 &p); poison (DC14, 1d6/2d6 Str), petrifying gaze, poison
# Mephit, Air 17 3d8 13 +7 2  claws  +4  (1d3);  breath  (15  ft.,  DC12, 1d8), spell-like abilities, summon mephit; fast healing 2, DR 5/+1
# Mephit, Dust 17 3d8 13 +7 2 claws +4(1d3); breath (10 ft., DC12, 1d4 & torment), spell-like abilities, summon mephit; fast healing 2, DR 5/+1
# 90Mephit, Earth 16 3d8+3 16 -1 2 claws +7 (1d3+3); breath (15 ft., DC12, 1d8), spell-like abilities, summon mephit; fast healing 2, DR 10/+1
# Mephit, Fire 16 3d8 13 +5 2 claws +4 (1d3 & 2 fire); breath (15 ft., DC12,  1d8),  spell-like  abils,  summon mephit;  fire  subtype,  fast  heal  2,  DR 5/+1
# Mephit, Ice 18 3d8 13 +7 2 claws +4 (1d3 & 2 cold); breath (10 ft., DC12, 1d4 & torment), spell-like abilities, summon  mephit;  cold  subtype,  fast healing 2, DR 5/+1
# Mephit, Magma 16 3d8 13 +5 2 claws +4 (1d3 & 2 fire); breath (10 ft., DC12, 1d4 & torment), spell-like abilities, summon  mephit;  fire  subtype,  fast healing 2, DR 5/+1
# Mephit, Ooze 16 3d8+3 16 0 2 claws +6 (1d3+2); breath (10 ft., DC12, 1d4  &  torment),  spell-like  abilities, summon mephit; fast healing 2, DR 5/+1
# Mephit, Salt 16 3d8+3 16 -1 2 claws +7 (1d3+3); breath (10 ft., DC12, 1d4  &  torment),  spell-like  abilities, summon  mephit;  fast  healing  2,  DR 10/+1
# Mephit, Steam163d813+52 claws +4 (1d3 & 2 fire); breath (10 ft., DC12, 1d4 & torment), spell-like abilities,  summon  mephit;  fire  subtype,  fast healing 2, DR 5/+1
# Mephit, Water163d8+31602 claws +6 (1d3+2); breath (15 ft., DC12, 1d8), spell-like abilities, summon mephit; fast healing 2, DR 5/+1
# Merfolk 13 1d8+1 5 +1  trident  +1  (1d8),  heavy  crossbow  +2 (1d10); low-light visionMimic 13 7d8+21 52 +1 slam +8 (1d8+6); adhesive; mimic shape, acid immunity
# Mind Flayer 15 8d8+8 44 +6 4 tentacles +8 (1d4+1); mind blast (-2 to hit and defend), psionics, improved grab, extract thoughts; SR 25, telepathy
# Minotaur 14 6d8+12 39 0 huge  greataxe  +9/+4  (2d8+6),  gore  +4 (1d8+2);  charge  4d6+6;  scent,  natural cunning
# Mummy 17 6d12+342 -1 slam +6 (1d6+4 and mummy rot); despair, mummy rot; undead, resistant to blows, DR 5/+1, fire vulnerability
# Naga, Water 15 7d8+28 59 +1bite  +7  (2d6+4  &p);  poison  (DC17,  1d8 Con), spells
# Naga, Spirit 16 9d8+36 76 +1bite  +9  (2d6+6  &p);  poison  (DC18,  1d8 Con), charm gaze, spells
# Naga, Dark 14 9d8+18 58 +2 sting  +7  (2d4+2  &p),  bite  +2  (1d4+1); poison  (DC16,  2d4  min.  sleep),  detect thoughts,  spells;  poison  immunity, guarded thoughts, charm resistance
# Naga, Guardian 18 11d8+44 93 +2 bite +12 (2d6+7 &p); poison (DC19, 2d8 Con), spit, spells
# Nymph 11 3d6 10 +1 dagger  +1  (1d4);  blindsight,  unearthly beauty, spell-like abilities
# Ogre 16 4d8+8 26 -1 huge greatclub +8 (2d6+7), large javelin +1 (1d8+5)
# Ogre Mage 18 5d8+15 37 +4 huge  greatsword  +7  (2d8+7),  huge longbow  +2  (2d6);  spell-like  abilities; regeneration 2, SR 18Orc 14 1d8 4 0 greataxe +3 (1d12+3), javlin +1 (1d6+2); darkvision 60 ft., light sensitivity
# Owlbear 15 5d10+20 47 +1 2  claws  +7  (1d6+5),  bite  +2  (1d8+2); improved grab; scent
# Pegasus 14 4d10+12 34 +22  hooves  +7  (1d6+4),  bite  +2  (1d3+2); scent, spell abilities
# Phase Spider 15 5d10+15 42 +7 bite +7(1d6+4 & poison); poison (DC15, 2d6 STR), ethereal jaunt
# Phasm 17 15d8+30 97 +6 2 slams +12 (1d3+1); amorphous, scent, alternate form, telepathy, tremorsense
# Rakshasa 21 7d8+21 52 +2 2  claws  +8  (1d4+1),  bite  +3  (1d6); detect  thoughts,  spells;  alternate  form, spell  immunity,  vulnerable  to  blessed crossbow bolts, DR 20/+3Roc 14 18d10+126 225 +2 2 claws +21 (2d6+12), bite +16 (2d8+6); snatch
# Satyr 15 5d6+5 22 +1 gore +2 (1d6), dagger -3 (1d4), shortbow +3 (1d6); pipes
# Sea Lion 18 6d10+18 51 +1 2 claws +7 (1d6+4), bite +2 (1d8+2); rend 2d6+6; scent
# Shadow 13 3d12 19 +2incorporeal touch +3 (1d6 Str); strength damage,   create   spawn;   undead, incorporeal, +2 turn resistance
# Skeleton, Tiny 13 1/4 d12 1 +5 2 claws +0 (1d2-2); undead, immunities
# Skeleton, Small 13 1/2 d12 3 +5 2 claws +0 (1d3-1); undead, immunities
# Skeleton, Medium 13 1d12 6 +5 2 claws +0 (1d4); undead, immunities
# Skeleton, Large 13 2d12 13 +5 2 claws +2 (1d6+2); undead, immunities
# Skeleton, Huge 13 4d12 26 +5 2 claws +4 (1d8+4); undead, immunities
# Skeleton, Gargantuan 13 16d12 104 +5 2   claws   +10   (2d6+6);   undead, immunities
# Skeleton, Colossal 13 32d12 208 +5 2   claws   +16   (2d8+8);   undead, immunities
# Slaad, Red 16 7d8+21 52 +1bite  +10  (2d8+4),  2  claws  +8  (1d4+2  & implant);  pounce,  implant  eggs  inside victim,  stunning  croak,  summon  slaad; fast healing 5, resistances
# Slaad, Blue 18 8d8+24 60 +2 4  rakes  +11  (2d6+4),  bite  +9  (2d8+2 &d);  spell-like  abilities,  disease  (DC17), summon slaad;  fast heal. 5, resistances
# Slaad, Green 20 9d8+27 67 +1 2  claws  +12  (1d6+4),  bite  +10  (2d8+2); spell-like  abilities,  summon  slaad;  fast healing 5, resistances
# Slaad, Gray 22 10d8+30 75 +1 2  claws  +14  (2d4+4),  bite  +12  (2d8+2); spell-like   abilities,   summon   slaad; fast  healing  5,  DR  10/+1,  resistances, alternate form
# Slaad, Death 26 15d8+45 112 +8 2  claws  +20  (3d6+5  and  stun),  bite +18  (2d10+2);  stun,  spell-like  abilities, summon slaad; fast healing 5, DR 20/+2, resistances, telepathy, alternate form
# Spectre 15 7d12 45 +7 incorporeal  touch  +6  (1d8  and  energy drain); energy drain (x2, remove DC15), create  spawn;  undead,  incorporeal,  +2 turn resistance, unnatural aura, sunlight powerlessness
# Sprite, Grig 18 1/2 d6+1 2 +4 diminutive  short  sword  +6  (1d3-3), composite shortbow +6 (1d4); spell-like abilities, SR 17
# Sprite, Nixie 14 1d6 3 +7 dagger  +4  (1d4-2),  light  crossbow  +4 (1d8); water breathing, charm person; SR 16
# Sprite, Pixie 16 1d6 3 +4 dagger  +5  (1d4-2),  composite  shortbow +6  (1d6);  spell-like  abilities,  special arrows; SR 16, natural invisibility
# Tarrasque 35 48d10+576 840 +7 bite +57 (4d8+17), 2 horns +52 (1d10+8), 2  claws  +52  (1d12+8),  tail  slap  +52 (3d8+8);  frightful  presence  (DC26), rush  (150  ft.),  improved  grab,  swallow whole,  augmented  criticals  (18-20/x3);  DR  25/+5,  carapace,  immunities, regeneration 40, scent, SR 32
# Treant (Ent) 20 7d8+35 66 -1 2  slams  +12  (2d6+9);  animate  trees, trample, double damage against objects; plant,  fire  vulnerability,  half  damage from piercing
# Triton 16 3d8+3 16 0 trident  +4  (1d8+1),  heavy  crossbow  +3 (1d10); spell-like abilities
# Troglodyte 15 2d8+4 13 -1longspear +1 (1d8), bite -1 (1d4), stench (30 ft., DC13, -2 morale), darkvision 90 ft.
# Troll 18 6d8+36 63 +2 2 claws +9 (1d6+6), bite +4 (1d6+3); rend 2d6+9; regeneration 5, scent, darkvision 90 ft.
# Umber Hulk 17 8d8+32 68 +1 2  claws  +11  (2d4+6),  bite  +9  (2d8+3); confusing gaze; tremorsense
# Unicorn 18 4d10+20 42 +3 horn +11 (1d8+8), 2 hooves +3 (1d4+2); magic  circle  against  evil,  spell-like abilities, immunities
# Vampire Spawn 15 4d12 26 +6 slam +5 (1d6+4 & energy drain); charm, energy  drain  (remove  DC14),  blood drain (1d4 Con/round); undead, +2 turn resist., DR 10/silver, cold and electricity resistance 10, gaseous form, spider climb, fast healing 2Will-o’-wisp 29 9d8 40 +13 shock +16 (2d8); spell immunity, natural invisibility
# Winter Wolf 15 6d10+18 51 +5 bite +9 (1d8+6); breath (15 ft, DC16, 4d6), trip; sct, cold subtypeWorg 14 4d10+8 30 +2 bite +7 (1d6+4); trip; scent
# Wraith 15 5d12 32 +7 incorporeal touch +5 (1d4 & 1d6 perm. STR); create spawn; undead, incorporeal, +2  turn  resistance,  unnatural  aura, daylight powerlessness
# Wyvern 17 7d12+14 59 +1 sting +9 (1d6+4 &p), bite +4 (2d8+2), 2 wings  +4  (1d8+2),  2  claws  +9  (1d6+4); poison (DC17, 2d6 Con), improved grab, snatch; scent
# Zombie, Tiny 11 1/2 d12+3 6 -1 slam  +2  (1d3);  undead,  partial  actions onlyZombie, Small 11 1d12+3 9 -1 slam  +1  (1d4);  undead,  partial  actions only
# Zombie, Medium 11 2d12+3 16 -1 slam +2 (1d6+1); undead, partial actions onlyZombie, Large 11 4d12+3 29 -1 slam +4 (1d8+4); undead, partial actions only
# Zombie, Huge 11 8d12+3 55 -1 slam +7 (2d6+7); undead, partial actions onlyZombie, Gargantuan 11 24d12+3 159 -1 slam  +15  (2d8+10);  undead,  partial actions only
# Zombie, Colossal 11 48d12+3 315 -2 slam  +25  (4d6+13);  undead,  partial actions only
# Ape 14 4d8+8 26 +2 2  claws  +7  (1d6+5),  bite  +2  (1d6+2); scent
# Baboon 13 1d8+1 5 +2 bite +2 (1d6+3); scent
# Badger 15 1d8+2 6 +3 2 claws +5 (1d2-1), bite +0 (1d3-1); rage; scent
# Bat 16 1/4 d8 1 +2 -; blindsight
# Bear, Black 13 3d8+6 19 +1 2  claws  +6  (1d4+4),  bite  +1  (1d6+2); scent
# Bear, Brown 15 6d8+24 51 +1 2  claws  +11  (1d8+8),  bite  +6  (2d8+4); improved grab; scent
# Bear, Polar 15 8d8+32 68 +1 2  claws  +13  (1d8+8),  bite  +8  (2d8+4); improved grab; scent
# Bison 13 5d8+15 37 0butt +6 (1d8+6); stampede; scent
# Boar 16 3d8+9 22 0 gore +4 (1d8+3); ferocity; scent
# Camel 13 3d8+6 19 +3 bite +5 (1d4+6); scent
# Cat 14 1/2 d8 2 +2 2 claws +4 (1d2-4), bite -1 (1d3-4)
# Cheetah 15 3d8+6 19 +4 bite +6 (1d6+3), 2 claws +1 (1d2+1); trip; sprint
# Crocodile 15 3d8+9 22 +1 bite  +6  (1d8+6),  tail  slap  +6  (1d12+6); improved grab
# Crocodile, Giant 16 7d8+28 59 +1bite  +11  (2d8+12),  tail  slap  +11 (1d12+12); improved grab
# Dog 15 1d8+2 6 +3 bite +2 (1d4+1); scent
# Dog, Riding 16 2d8+4 13 +2 bite +3 (1d6+3); scentDonkey 13 2d8+2 11 +1 bite +1 (1d2); scent
# Eagle 14 1d8+1 5 +2 2 claws +3 (1d3), bite -2 (1d4)
# Elephant 15 11d8+55 104 0 slam  +16  (2d6+10),  2  stamps  +11 (2d6+5),  gore  +16  (2d8+15);  trample 2d8+15; scent
# 94Hawk 17 1d8 4 +3 claws +5 (1d4-2)Horse, Heavy 13 3d8+6 19 +1 2 hooves +3} (1d6+2); scent
# Horse, Heavy War 14 4d8+12 30 +1 2  hooves  +6  (1d6+4),  bite  +1  (1d4+2); scent
# Horse, Light 13 3d8+6 19 +1 2 hooves +2 (1d4+1); scent
# Horse, Light War 14 3d8+9 22 +1 2  hooves  +4  (1d4+3),  bite  -1  (1d3+1); scent
# Leopard 15 3d8+6 19 +4 bite +6 (1d6+3), 2 claw +1 (1d3+1); pnce, rake 1d3+1; scent
# Lion 15 5d8+10 32 +3 2 claw +7 (1d4+5), bite +2 (1d8+2); pnce, rake 1d4+2; scent
# Lizard 14 1/2 d8 2 +2bite +4 (1d4-4)Lizard, Giant 15 3d8+9 22 +2bite +5 (1d8+4)
# Monkey 14 1d8 4 +2 bite +4 (1d3-4)Mule 13 3d8+9 22 +1 2 hooves +4 (1d4+3)
# Octopus 16 2d8 9 +3 arms  +5  (0),  bite  +0  (1d3);  improved grab; ink cloud, jet
# Octopus, Giant 18 8d8+8 44 +2 8 tentacles +10 (1d4+5), bite +5 (1d8+2); improved grab, constrict; ink cloud, jet
# Owl 17 1d8 4 +3 claws +5 (1d4-2)Pony 13 2d8+2 11 +1 2 hooves +2 (1d3+1); scent
# Pony, War 13 2d8+4 13 +1 2 hooves +3 (1d3+2); scentPorpoise 15 2d8+2 11 +3 butt +4 (2d4); blindsight
# Rat 14 1/4 d8 1 +2 bite +4 (1d3-4); scentRaven 14 1/4 d8 1 +2 claws +4 (1d2-5)
# Rhinoceros 16 8d8+40 76 0 gore +13 (2d6+12)Shark, Medium 15 3d8+3 16 +2 bite +4 (1d6+1); keen scent
# Shark, Large 15 7d8+7 38 +2 bite +7 (1d8+4); keen scentShark, Huge 15 10d8+20 65 +2 bite +10 (2d6+7); keen scent
# Snake, Constrictor 15 3d8+3 16 +3 bite  +5  (1d3+4);  improved  grab, constrict 1d3+4; scent
# Snake, Giant Constr. 15 11d8+11 60 +3 bite  +13  (1d8+10);  improved  grab, constrict 1d8+10; scent
# Snake, Viper, Tiny 17 1/4 d8 1 +3 bite  +5  (p);  poison  (DC11,  1d6  Con), scent
# Snake, Viper, Small 17 1d8 4 +3 bite +4 (1d2-2 &p); poison (DC11, 1d6 Con), scent
# Snake, Viper, Medium 16 2d8 9 +3 bite +4 (1d4-1 &p); poison (DC11, 1d6 Con), scent
# Snake, Viper, Large 15 3d8 13 +3 bite  +4  (1d4  &p);  poison  (DC11,  1d6 Con), scent
# Snake, Viper, Huge 15 4d8+4 22 +4 bite  +5  (1d4  &p);  poison  (DC13,  1d6 Con), scent
# Squid 16 3d8 13 +3 arms +5 (0), bite +0 (1d6+1); imp., grab; ink cloud, jet
# Squid, Giant 17 12d8+12 66 +3 10  tentacles  +15  (1d6+8),  bite  +10 (2d8+4);  improved  grab,  constrict 1d6+8; ink cloud, jet
# 95Tiger 14 6d8+18 45 +2 2 claw +9 (1d8+6), bite +4 (2d6+3); pnce, grab, rake 1d8+3Toad 15 1/4 d8 1 +1 -
# Weasel 14 1/2 d8 2 +2 bite +4 (1d3-4); attach; scentWhale, Baleen 16 12d8+72 126 +1 tail slap +17 (1d8+18); blindsight
# Whale, Cachalot 16 12d8+84 138 +1 bite +17 (4d6+12), tail slap +12 (1d8+6); blindsight
# Whale, Orca 16 9d8+45 85 +2 bite +12 (2d6+12); blindsightWolf 14 2d8+4 13 +2 bite +3 (1d6+1); trip; scent
# Wolverine 14 3d8+12 25 +2 2 claws +4 (1d4+2), bite -1 (1d6+1); rage; scent
# Giant Ant, Worker 17 2d8 9 0 bite +1 (1d6); improved grab; vermin
# Giant Ant, Soldier 17 2d8+2 11 0 bite  +3  (2d4+3);  improved  grab,  acid sting; vermin
# Giant Ant, Queen 17 4d8+4 22 -1 bite  +5  (2d6+4);  improved  grab; vermin
# Giant Bee 14 3d8 13 +2 sting +2 (1d4 &p); poison (DC13, 1d6 Con), vermin
# Giant Beetle, Bom. 16 2d8+4 13 0 bite +2 (1d4+1); acid spray; vermin
# Giant Beetle, Fire 16 1d8 40bite +1 (2d4); vermin
# Giant Beetle, Stag 19 7d8+21 52 0 bite  +10  (4d6+9);  trample  2d8+3; vermin
# Giant Pray. Mantis 14 4d8+8 26 -1 claws +6 (1d8+4), bite +1 (1d6+2); imp grab, squeeze; vrmn
# Giant Wasp 14 5d8+10 32 +1 sting +6 (1d3+6 &p); poison (DC18, 1d6 Dex), vermin
# Centipde, Tiny 14 1/4 d8 1 +2 bite  +4  (1d3-5  &p);  poison  (DC11,  1 Dex), vermin
# Centipde, Small 14 1/2 d8 2 +2 bite +3 (1d4-3 &p); poison (DC11, 1d2 Dex), vermin
# Centipde, Medium 14 1d8 4 +2 bite +2 (1d6-1 &p); poison (DC13, 1d3 Dex), vermin
# Centipde, Large 14 2d8 9 +2 bite +2 (1d8+1 &p); poison (DC16, 1d4 Dex), vermin
# Centipde, Huge 16 4d8 18 +2 bite +4 (2d6+4 &p); poison (DC18, 1d6 Dex), vermin
# Centipde, Gargantuan 18 16d8 72 +2 bite +13 (2d8+7 &p); poison (DC26, 1d8 Dex), vermin
# Centipde, Colossal 20 32d8 144 +2 bite  +23  (4d6+10  &p);  poison  (DC36, 2d6 Dex), vermin
# Scorpion, Tiny 14 1/2 d8+2 4 0 2 claws +2 (1d2-4), sting -3 (1d2-4 &p); poison (DC11, 1d2 Str), improved grab; vermin
# Scorpion, Small 14 1d8+2 6 0 2 claws +1 (1d3-1), sting -4 (1d3-1 &p); poison (DC11, 1d3 Str), improved grab, squeeze; vermin
# 96Scorpion, Medium 14 2d8+4 13 0 2 claws +2 (1d4+1), sting -3 (1d4 &p); poison (DC15, 1d4 Str), improved grab, squeeze; vermin
# Scorpion, Large 14 4d8+8 26 0 2  claws  +5  (1d6+3),  sting  +0  (1d6+1 &p); poison (DC18, 1d6 Str), improved grab, squeeze; vermin
# Scorpion, Huge 16 16d8+32 104 0
# Scorpion, Gargantuan 18 32d8+64 208 0
# Scorpion, Colossal 20 64d8+128 416 0
# Spider, Tiny 15 1/2 d8 2 +3 bite +5 (1d3-4 &p); poison (DC11, 1d2 Str), web; vermin
# Spider, Small 14 1d8 4 +3 bite +4 (1d4-2 &p); poison (DC11, 1d3 Str), web; vermin
# Spider, Medium 14 2d8+2 11 +3 bite +4 (1d6 &p); poison (DC14, 1d4 Str), web; vermin
# Spider, Large 14 4d8+4 22 +3 bite +4 (1d8+3 &p); poison (DC17, 1d6 Str), web; vermin
# Spider, Huge 16 10d8+10 55 +3 bite +9 (2d6+6 &p); poison (DC22, 1d8 Str), web; vermin
# Spider, Gargantuan 18 24d8+24 132 +3 bite +20 (2d8+9 &p); poison (DC31, 2d6 Str), web; vermin
# Spider, Colossal 20 48d8+48 264 +3 bite  +36  (4d6+12  &p);  poison  (DC35, 2d8 Str), web; vermin
#
}

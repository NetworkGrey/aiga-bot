# Age of Empires Mobile — Rings Complete Reference
## AIGA Source Document v1.0
## Source: aoem-calculator Rings Data.ts (MIT Licence, juan_jm/aoem-calculator on Codeberg)

---

## Overview

Rings are equippable items that provide passive stat bonuses and a skill effect to heroes. Each hero equips one ring. Rings unlock at Town Centre level 18 (Milestone 15).

There are 35 rings across 3 tiers. Higher tier rings have better base stats, higher max levels, and more powerful skills.

---

## Ring Tiers

| Tier | Type | Max level | Craft cost | Number available |
|---|---|---|---|---|
| 0 | Flower rings | 30 | 200 | 10 |
| 1 | Animal rings | 40 | 600 | 14 |
| 2 | Element/Special rings | 50 | 1,600 or 4,000 | 11 |

---

## Upgrade Costs Per Level

### Tier 0 rings (lv1-30) — Dust cost per level group
| Level range | Dust per level |
|---|---|
| 1-4 | 10 |
| 5-9 | 20 |
| 10 | 45 |
| 11-14 | 30 |
| 15-19 | 40 |
| 20 | 90 |
| 21-24 | 60 |
| 25-29 | 80 |
| 30 | 150 |

### Tier 1 and 2 rings (lv31-50) — Iron Meteorite required
| Level range | Meteorite per level |
|---|---|
| 40 | 15 |
| 41-50 | 12 |

---

## MGE Scoring for Rings

| Action | MGE pts |
|---|---|
| Craft 1 ring | 2,000 |
| Use 1 Copper Dust | 400 |
| Use 1 Silver Dust | 1,000 |
| Use 1 Fine Gold | 3,000 |
| Use 1 Meteor Steel | 20,000 |

---

## Tier 0 — Flower Rings (Max Level 30)

Stat formula: base + (scaling × (level-1)). At max lv30: base + (scaling × 29).

| Ring | Stat 1 | At lv30 | Stat 2 | At lv30 | Skill | Skill type |
|---|---|---|---|---|---|---|
| Ring of Clover | Troop attack | 6.8% | Troop defence | 6.8% | Armor Maintenance | Turn-based |
| Ring of Tulip | Troop attack | 6.8% | Troop defence | 6.8% | Mighty Strike | Active |
| Ring of Violet | Troop defence | 6.8% | Troop health | 3.4% | Hands of Industry | Passive |
| Ring of Daisy | Troop attack | 6.8% | Troop defence | 6.8% | Double Strike | Secondary strike |
| Ring of Iris | Troop attack | 6.8% | Troop defence | 6.8% | Critical Blade | Passive |
| Ring of Rose | Troop attack | 6.8% | Troop defence | 6.8% | Surprise Attack | Active |
| Ring of Hyacinth | Troop attack | 6.8% | Troop health | 3.4% | Battle Review | Passive |
| Ring of Lily | Troop attack | 6.8% | Troop health | 3.4% | Rest and Recover | Active |
| Ring of Laurel | Troop attack | 6.8% | Troop defence | 6.8% | Siege Tactics | Passive |
| Ring of Sunflower | Troop attack | 6.8% | Troop health | 3.4% | Bumper Harvest Omen | Passive |

**Best Tier 0 for combat:** Ring of Tulip (attack + defence + active skill trigger) or Ring of Clover (attack + defence + turn-based). Both give identical stat values at lv30 — skill type determines which is better for a specific hero.

**Note on Ring of Violet:** Musashi currently uses Ring of Tulip (lv10). Josephine uses Ring of Violet (lv1). Tier 0 rings are a starting point — upgrade to Tier 1 animal rings as resources allow.

---

## Tier 1 — Animal Rings (Max Level 40)

All Tier 1 rings cost 600 to craft.

| Ring | Stat 1 | At lv40 | Stat 2 | At lv40 | Skill | Skill type |
|---|---|---|---|---|---|---|
| Ring of Bear | Commander Might dmg | 8.8% | Troop attack | 15.4% | All Out | Passive |
| Ring of Rhino | Commander damage | 6.6% | Troop defence | 11.0% | Breach | Active |
| Ring of Steed | Troop damage | 22.0% | Troop health | 11.0% | Load Boost | Passive |
| Ring of Crow | Troop damage | 17.6% | Troop defence | 13.2% | Twist of Fate | Active |
| Ring of Seahorse | Troop damage | 17.6% | Troop health | 6.6% | Unyielding Faith | Passive |
| Ring of Shark | Skill damage | 22.8% | Troop defence | 15.4% | Punisher | Passive |
| Ring of Badger | Commander damage | 6.6% | Troop defence | 11.0% | Armor of Steel | Passive |
| Ring of Elephant | Troop damage | 17.6% | Troop health | 6.6% | Siege Master | Passive |
| Ring of Lion | Troop attack | 17.6% | Troop defence | 13.2% | Heroic Lineage | Passive |
| Ring of Serpent | Troop damage | 17.6% | Troop defence | 13.2% | Strategy and Might | Passive |
| Ring of Deer | Troop skill dmg red | 6.2% | Troop damage reduction | 6.2% | Coercion | Passive |
| Ring of Falcon | Normal attack dmg | 15.4% | Troop defence | 13.2% | Blessing of Oasis | Turn-based |
| Ring of Night Wolf | Commander Might dmg | 8.8% | Troop attack | 13.2% | Ablaze Spirit | Passive |
| Ring of Boar | Troop damage | 17.6% | Troop damage reduction | 15.1% | Burning Will | Passive |

**Best Tier 1 for attack leads:** Ring of Steed (22% troop damage) or Ring of Shark (22.8% skill damage) — highest offensive values.

**Best Tier 1 for defence/survival:** Ring of Boar (17.6% damage + 15.1% damage reduction) or Ring of Deer (double damage reduction).

**Best overall Tier 1 for combat lead:** Ring of Steed or Ring of Crow — both give strong troop damage with secondary survivability stats.

---

## Tier 2 — Element and Special Rings (Max Level 50)

Two cost tiers within Tier 2: 1,600 craft cost (standard) and 4,000 craft cost (premium).

### Standard Tier 2 (craft cost 1,600)

| Ring | Stat 1 | At lv50 | Stat 2 | At lv50 | Stat 3 | At lv50 | Skill | Type |
|---|---|---|---|---|---|---|---|---|
| Tranquil Water | Skill dmg reduction | 10.8% | Troop defence | 10.8% | Troop health | 5.4% | Light's Protection | Passive |
| Lofty Mountain | Skill dmg reduction | 10.8% | Troop defence | 21.6% | Troop health | 5.4% | Accumulating Strength | Passive |
| Scorching Flame | Skill dmg reduction | 10.8% | Rage recovery | 16.2% | Troop attack | 10.8% | Heroic Moment | Passive |
| Effulgent Sun | Skill dmg reduction | 10.8% | Troop attack | 13.5% | Troop defence | 10.8% | Firm Onslaught | Active |
| Azure Moon | Skill dmg reduction | 10.8% | Troop attack | 13.5% | Troop defence | 10.8% | Foreboding of Destruction | Active |

### Premium Tier 2 (craft cost 4,000)

| Ring | Stat 1 | At lv50 | Stat 2 | At lv50 | Stat 3 | At lv50 | Skill | Type |
|---|---|---|---|---|---|---|---|---|
| Radiant Guardian | Healing effect | 26.5% | Troop attack | 10.8% | Troop defence | 10.8% | Flurry of Blows | Turn-based |
| Lord of Eastern Heavens | Skill dmg reduction | 10.8% | Troop attack | 16.2% | Troop health | 8.1% | Decree of Victory | Passive |
| Messenger of Destruction | Skill dmg reduction | 10.8% | Troop attack | 10.8% | Troop defence | 10.8% | Perception | Passive |
| Sacred Sage | Skill dmg reduction | 10.8% | Troop defence | 10.8% | Troop health | 5.4% | Silent Oath | Passive |
| Everflame Wings | Skill dmg reduction | 10.8% | Troop attack | 10.8% | Troop defence | 10.8% | Silencing Flame | Turn-based |
| Skyward Knight | Skill dmg reduction | 10.8% | Troop attack | 16.2% | Troop defence | 16.2% | Cost of Victory | Passive |

**Best Tier 2 for attack leads:** Lord of Eastern Heavens (attack 16.2% + health 8.1%) or Skyward Knight (attack 16.2% + defence 16.2%) — both strong all-round.

**Best Tier 2 for support/recovery:** Radiant Guardian (healing 26.5% — best healing ring available, suited to Hammurabi or Tokugawa).

**Best Tier 2 overall for rally combat:** Skyward Knight — highest combined offensive and defensive values at lv50.

---

## Ring Priority Recommendations by Hero

| Hero | Current ring | Recommended upgrade path |
|---|---|---|
| Musashi | Ring of Tulip (T0 lv10) | → Ring of Steed or Ring of Crow (T1) → Lord of Eastern Heavens (T2) |
| Josephine | Ring of Violet (T0 lv1) | → Ring of Crow or Ring of Steed (T1) |
| Hammurabi | None | → Any T0 attack ring → Ring of Boar (T1) for survivability |
| Joan of Arc | None | → Ring of Tulip or Clover (T0) → Ring of Crow (T1) |
| Wu Wei | None | → Any T0 ring → Ring of Serpent (T1) |

**General rule:** Any ring is better than no ring. Equip something on every hero before worrying about which tier. Upgrade path is: T0 any → T1 best available → T2 when resources allow.

**Investment priority:** Ring heroes in march order — M1 first, then M2, then M3/M4/M5.

---

## Stat ID Reference

| Stat ID | Meaning |
|---|---|
| troop_atk | All troops attack % |
| troop_def | All troops defence % |
| troop_hp | All troops health % |
| troop_dmg | All troops damage dealt % |
| troop_dmg_red | All troops damage taken reduction % |
| troop_skill_dmg_red | All troops skill damage taken reduction % |
| comm_dmg | Commander damage % |
| comm_might_dmg | Commander Might damage % |
| normal_atk_dmg | Normal attack damage % |
| skill_dmg | All skill damage % |
| healing | Healing effect % |
| rage | Rage recovery |

---

*Source: aoem-calculator Rings Data.ts (MIT Licence). Stat values calculated from base + (scaling × (level-1)) formula. Verify skill effects in-game as detailed skill descriptions require in-game inspection.*
# AIGA — Rings Skills Addendum
## Age of Empires Mobile
### Source: Age of Empires Mobile Fandom Wiki — Signet Rings page (CC-BY-SA)
### Version: 1.0 | March 2026
### Purpose: Supplements AIGA_Rings_Reference.md with exact ring skill effect descriptions

---

## Important Notes

- Stat values in this document are at an unspecified mid-level, NOT max level
- For max-level stat values, always use AIGA_Rings_Reference.md (sourced from calculator data)
- This document adds the ring skill effect descriptions which were absent from the calculator data
- Ring of Steed is absent from the Fandom wiki — may be wiki omission. *[verify in-game]*
- Ring of Mamba and Ring of Seahorse have identical skill descriptions in the source — likely a wiki error. *[verify in-game]*

---

## Tier 0 — Plant Rings: Skill Effects

| Ring | Skill Name | Skill Effect | Skill Type |
|---|---|---|---|
| Ring of Iris | Critical Blade | Increases the hero's critical strike rate by 1.26% | Passive |
| Ring of Hyacinth | Battle Review | Increases the hero's XP obtained by 5.75% | Passive |
| Ring of Lily | Rest and Recover | Recovers your troop's units (recovery rate: 34.50%, strategy bonus) | Active |
| Ring of Daisy | Double Strike | After launching a normal attack, deals might damage to the enemy troop (damage rate: 35.65%, might bonus) | Secondary Strike |
| Ring of Tulip | Mighty Strike | Deals might damage to the enemy troop (damage rate: 28.75%, might bonus) | Active |
| Ring of Violet | Hands of Industry | Increases your troop's gathering speed by 4.60% | Passive |
| Ring of Rose | Surprise Attack | Deals strategy damage to the enemy troop (damage rate: 28.75%, strategy bonus) | Active |
| Ring of Laurel | Siege Tactics | Increases the hero's siege by 20.47 | Passive |
| Ring of Sunflower | Bumper Harvest Omen | Grants 2.76% extra resources when your troops gather resources successfully | Passive |
| Ring of Clover | Armor Maintenance | Has a 50% chance to reduce your troop's damage taken by 5.75% for 3s every 6s | Turn-based |

**Advisory notes on Tier 0 skills:**
- Ring of Hyacinth (Battle Review) — XP gain boost is only useful for early levelling. No combat value. Never equip on a maxed hero.
- Ring of Laurel (Siege Tactics) — Siege stat increase. Low value for combat heroes per AIGA principle (avoid siege stats).
- Ring of Violet (Hands of Industry) — Gathering speed boost. Only equip on gathering heroes.
- Ring of Sunflower (Bumper Harvest Omen) — Gathering bonus. Only equip on M5 gathering march heroes.
- Ring of Tulip and Ring of Clover remain best Tier 0 for combat — confirmed by both stat values and skill effects.

---

## Tier 1 — Animal Rings: Skill Effects

| Ring | Skill Name | Skill Effect | Skill Type |
|---|---|---|---|
| Ring of Mamba | Unyielding Faith | When your troop takes strategy damage more than 1% of their max units in a single attack, reduces their strategy damage taken by 4.20% for 6s | Passive |
| Ring of Boar | Burning Will | Increases the damage of your troop's passive skills by 8.82% when your troop's units fall below 60% | Passive |
| Ring of Deer | Coercion | Reduces a random enemy hero's damage by 4.62% and increases one of your heroes' damage by 4.62% | Passive |
| Ring of Rhino | Breach | Can be activated during sieges. Deals 110.25 damage to wall durability (siege bonus) | Active |
| Ring of Shark | Punisher | Every time your troop's normal attack hits the target, reduces the target's recovery effect by 0.21%, up to 50 stacks | Passive |
| Ring of Badger | Armor of Steel | For the first 18s after entering battle, reduces your troop's normal attack and secondary strike skill damage taken by 6.62% | Passive |
| Ring of Bear | All Out | Reduces all your heroes' armor by 20.00 and increases the commander's might by 22.05 | Passive |
| Ring of Seahorse | Unyielding Faith | When your troop takes strategy damage more than 1% of their max units in a single attack, reduces their strategy damage taken by 4.20% for 6s | Passive |
| Ring of Lion | Heroic Lineage | Increases the hero's might, strategy, and armor by 13.65 | Passive |
| Ring of Elephant | Siege Master | Increases the hero's siege by 21.42 | Passive |
| Ring of Falcon | Blessing of Oasis | Grants one of the following effects every 9s: 1) Recovers your troop's units (recovery rate: 44.10%). 2) Reduces your troop's damage taken by 6.72% for 3s | Turn-based |
| Ring of Night Wolf | Ablaze Spirit | After every 9 normal attacks of your troop, increases the damage of all your heroes' normal attacks and secondary strike skills by 5.25% (might bonus) and reduces their armor by 7.35 for 3s | Passive |
| Ring of Crow | Twist of Fate | Steals 11.55 might, strategy, and armor from the enemy commander (strategy bonus) for 3s | Active |

**Advisory notes on Tier 1 skills:**
- Ring of Shark (Punisher) — stacks up to 50 times reducing enemy recovery by 0.21% each. At 50 stacks = 10.5% recovery reduction on the enemy. Strong in prolonged fights against recovery-heavy builds. Pairs well against Justinian, Bushra, or any recovery-focused opponent.
- Ring of Bear (All Out) — reduces your own heroes' armor by 20 in exchange for +22.05 might on commander. High-risk, high-reward. Only viable on heavily geared commanders with strong armor gems.
- Ring of Rhino + Ring of Elephant — both give siege stat boosts. Low value for combat heroes. Siege-only use cases.
- Ring of Badger (Armor of Steel) — opening 18s damage reduction on normal attacks and secondary strikes. Situationally strong against secondary-strike heavy marches.
- Ring of Crow (Twist of Fate) — steals stats from enemy commander. Synergises well with Hannibal who also debuffs enemy commander stats.
- Ring of Falcon (Blessing of Oasis) — dual-effect every 9s. Either recovers units OR reduces damage taken. Reliable passive value for support heroes.
- Ring of Night Wolf (Ablaze Spirit) — boosts normal attack and secondary strike damage after every 9 attacks. Good for secondary-strike heavy marches (Hannibal, Hua Mulan, Lu Bu).
- Ring of Mamba and Ring of Seahorse share identical skill descriptions in wiki — confirmed data issue. *[verify which is correct in-game]*

---

## Tier 2 — Legendary Creature Rings: Skill Effects

### Standard Tier 2 (craft cost 1,600)

| Ring | Skill Name | Skill Effect | Skill Type |
|---|---|---|---|
| Tranquil Water | Light's Protection | For the first 18s after entering battle, reduces your troop's damage taken by 7.60% | Passive |
| Effulgent Sun | Firm Onslaught | Enters charging state. After 3s, deals massive might damage to the enemy troop (damage rate: 76.00%, might bonus) | Active (Charge) |
| Azure Moon | Foreboding of Destruction | Enters charging state. After 3s, deals massive strategy damage to the enemy troop (damage rate: 91.20%, strategy bonus) | Active (Charge) |
| Scorching Flame | Heroic Moment | When your commander uses a commander skill, increases all your heroes' might by 4.18% for 9s | Passive |
| Everflame Wings | Silencing Flame | Inflicts the burn effect on the enemy troop every 9s, dealing strategy damage every second (damage rate: 2.37%, strategy bonus). Increases the enemy troop's strategy damage taken by 0.95% (strategy bonus) for 9s. Has a 5.70% chance to [truncated in source] | Turn-based |
| Lofty Mountain | Accumulating Strength | For the first 18s after entering battle, reduces your troop's might damage taken by 2.85% (armor bonus). After 18s, increases your troop's damage by 2.85% (strategy bonus) | Passive |

### Premium Tier 2 (craft cost 4,000)

| Ring | Skill Name | Skill Effect | Skill Type |
|---|---|---|---|
| Radiant Guardian | Flurry of Blows | Increases the hero's secondary strike skill activation chance by 0.50% every 6s and has a 40% chance to gain double attack for 3s | Turn-based |
| Skyward Knight | Cost of Victory | The hero deals 15.00% less damage (cannot be purified). Increases your commander's damage by 3.23% (strategy bonus) and their signature active skill's activation chance by 1.90% | Passive |
| Sacred Sage | Silent Oath | All your heroes cannot use active skills (cannot be purified). Increases turn-based skills' damage by 10.45% and healing effect by 10.45% | Passive |
| Lord of the Eastern Heavens | Decree of Victory | Reduces the damage of all your heroes' active skills by 25% (cannot be purified) but increases the damage of their normal attacks by 19.00% | Passive |
| Messenger of Destruction | Perception | Reduces the damage of all your heroes' normal attacks by 20% (cannot be purified) but increases the damage of their passive skills by 14.25% | Passive |

**Advisory notes on Tier 2 skills — critical:**

- **Skyward Knight (Cost of Victory)** — hero deals 15% less damage but grants commander damage boost + signature activation boost. The penalty is significant. Best on a support hero where personal damage output matters less than triggering the commander's signature more often. NOT ideal on a damage-focused lead.

- **Sacred Sage (Silent Oath)** — blocks all heroes' active skills entirely (cannot be purified). Tradeoff: +10.45% turn-based damage and healing. Only viable in a pure turn-based build (e.g. Octavian with Coordination). Would cripple any active-skill dependent march.

- **Lord of the Eastern Heavens (Decree of Victory)** — reduces active skill damage by 25% but boosts normal attack damage by 19%. Best on normal-attack heavy heroes (Boudica, Leonidas, counterattack builds). Harmful on active/charging skill focused heroes (Sun Tzu, Suleiman).

- **Messenger of Destruction (Perception)** — reduces normal attack damage by 20% but boosts passive skill damage by 14.25%. Best on passive-skill dependent heroes. Harmful on normal-attack heavy builds.

- **Effulgent Sun and Azure Moon** — both have charge mechanics (3s delay before damage). Might vs strategy versions. Best on heroes with charging synergy (Flash of Inspiration, Maneuver) that can skip or reduce the charge time.

- **Everflame Wings (Silencing Flame)** — burn DoT + strategy damage taken debuff every 9s. Synergises with Suleiman (Magnificent Conquest gets bonus effects against burned targets) and Queen Seondeok.

- **Radiant Guardian (Flurry of Blows)** — secondary strike activation boost + 40% chance double attack every turn-based trigger. Best on secondary-strike focused support heroes. Confirms the ring is a support/recovery hero ring despite the skill name suggesting offense.

- **Tranquil Water (Light's Protection)** — flat 7.60% damage reduction for opening 18s. Straightforward defensive value. Good on any frontline hero.

- **Scorching Flame (Heroic Moment)** — every commander skill use increases all heroes' might by 4.18% for 9s. High value in commander-skill-spam marches. Stacks if the commander skill fires multiple times.

---

## Updated Best Ring Recommendations

Incorporating both stat values (from AIGA_Rings_Reference.md) and skill effects (this document):

### For M1 Attack Lead (e.g. Miyamoto Musashi)
- **Current:** Ring of Tulip lv10 — upgrade priority
- **Target Tier 1:** Ring of Crow (stat + Twist of Fate steals enemy commander stats) or Ring of Night Wolf (boosts secondary strike damage after 9 attacks)
- **Target Tier 2:** Lord of Eastern Heavens if normal-attack focused | Skyward Knight if balanced

### For M1 Secondary Support (e.g. Josephine)
- **Current:** Ring of Violet lv1 — low priority but upgrade when resources allow
- **Target Tier 1:** Ring of Boar (survival) or Ring of Falcon (dual recovery/reduction)
- **Target Tier 2:** Radiant Guardian (secondary strike activation + double attack chance)

### For Recovery Support (e.g. Hammurabi, Justinian)
- **Target Tier 1:** Ring of Falcon (Blessing of Oasis — recovery or damage reduction every 9s)
- **Target Tier 2:** Radiant Guardian (best healing ring) or Tranquil Water (opening damage reduction)

### For Counterattack Heroes (e.g. Boudica, Leonidas)
- **Target Tier 2:** Lord of Eastern Heavens — reduces active skill damage (not their primary damage source anyway) while boosting normal attack damage (their primary counter damage)

### For Turn-Based Specialists (e.g. Octavian)
- **Target Tier 2:** Sacred Sage — blocks active skills (Octavian's build already minimises active skills) while boosting turn-based damage significantly

### For Gathering Heroes (M5 — Diao Chan, Cleopatra, Darius)
- Ring of Violet (gathering speed) or Ring of Sunflower (extra resources on gather)
- Never equip a combat ring on a dedicated gathering hero

---

*Source: Age of Empires Mobile Fandom Wiki — Signet Rings page (CC-BY-SA). Skill values shown at unspecified mid-level. Use AIGA_Rings_Reference.md for max-level stat values. March 2026.*

---

## Ring Upgrade Materials — Jeweler's Marks and Hammers
*Source: Theria Games Rings Calculator (Jayson, July 2025) — migrated from Calculator_Findings_Addendum*

Six ring upgrade materials confirmed:
1. **Jeweler's Marks** ← confirmed upgrade material
2. Copper Sand
3. Silver Sand
4. Fine Gold
5. Meteor Steel
6. **Hammers** ← confirmed upgrade material

*[Exact quantities of Jeweler's Marks and Hammers required per upgrade level — verify in-game]*

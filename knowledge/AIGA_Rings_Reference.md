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

# AIGA — Calculator Findings Addendum
## Age of Empires Mobile
### Source: Theria Games calculator UI labels (Jayson, July-August 2025)
### Version: 1.0 | March 2026
### Purpose: New data points extracted from Theria Games calculator interfaces. Supplements existing references.

---

## LEGENDARY ADVENT — PACK SIZE RESOLVED

**Source: Theria Games Legendary Advent Calculator UI**

The Theria Legendary Advent Calculator explicitly shows spin breakdown as: "Spins: X **5x** & Y **1x**"

This confirms the pack size is **5 spins for 4,200 Empire Coins**, not 10.

| Option | Empire Coins | Spins | EC per spin | Saving vs singles |
|---|---|---|---|---|
| Single spin | 900 | 1 | 900 | — |
| Pack | 4,200 | 5 | 840 | 60 EC per spin / 300 EC per pack |

**Impact on AIGA advice:**
- Previous system prompt stated "10-spin pack saves 4,800 EC" — this was incorrect
- Correct statement: 5-spin pack saves 300 EC vs five singles
- The pack is still worth using but the saving is modest, not dramatic
- The core advice remains the same: use packs when spending, save for MGE Day III

**Update required in:** System prompt, AIGA_Research_Mercenary_Wheel_Reference.md

*Source: Theria Games Legendary Advent Calculator (Jayson, July 2025)*

---

## LEGENDARY ADVENT — MILESTONE REWARDS PARTLY PROBABILISTIC

**Source: Theria Games Legendary Advent Calculator UI**

The calculator shows milestone medal rewards as:
"(X guaranteed, Y on a **30% chance**)"

This means some milestone bonuses are not guaranteed — a portion of the milestone medal rewards only have a 30% probability of being awarded.

**AIGA implication:** When planning wheel spins around milestone targets, account for the fact that secondary milestone medals are probabilistic. The guaranteed portion is certain; the 30% portion is a bonus expectation only.

*[Exact breakdown of which milestones are guaranteed vs 30% — verify in-game]*

*Source: Theria Games Legendary Advent Calculator (Jayson, July 2025)*

---

## GEM RARITY TIERS — FULL PROGRESSION

**Source: Theria Games Equipment and Gems Calculator UI**

AIGA previously had no gem rarity progression documented. The calculator reveals 10 rarity levels:

| Level | Rarity name |
|---|---|
| 1 | Common |
| 2 | Advanced |
| 3 | Rare |
| 4 | Epic |
| 5 | Legendary |
| 6 | Mythic |
| 7 | Mythic I |
| 8 | Mythic II |
| 9 | Mythic III |
| 10 | Mythic IV |

Gems can also be set to **None** (empty slot).

**Gem stat types per slot (confirmed from calculator):**
- Unit health
- Unit defense
- Unit attack
- Unit capacity
- Gathering speed

**Slot unlock levels (confirmed):**
- Gem slot 1: unlocks at gear level 10
- Gem slot 2: unlocks at gear level 20
- Gem slot 3: unlocks at gear level 40

*[Costs to upgrade between gem rarity tiers — verify in-game or via calculator when running live]*

*Source: Theria Games Equipment and Gems Calculator (Jayson, August 2025)*

---

## GEAR UPGRADE MATERIALS — LIGHTNING CRYSTALS

**Source: Theria Games Equipment and Gems Calculator UI**

The calculator lists four gear upgrade materials:
1. Blueprints
2. Forging kits (forging tools)
3. Magma crystals
4. **Lightning crystals** ← not previously in AIGA knowledge base

Lightning crystals appear to be a gear upgrade material alongside Magma crystals. Based on the calculator output structure, they are likely used at higher gear levels or star upgrades.

*[Exact use of lightning crystals — which gear levels/stars require them — verify in-game]*

**Update required in:** AIGA_Gear_Gems_Reference.md, system prompt gear section

*Source: Theria Games Equipment and Gems Calculator (Jayson, August 2025)*

---

## RINGS — JEWELER'S MARKS MATERIAL

**Source: Theria Games Rings Calculator UI**

The rings calculator lists five upgrade materials:
1. Jeweler's Marks ← not previously in AIGA knowledge base
2. Copper Sand
3. Silver Sand
4. Fine Gold
5. Meteor Steel
6. Hammers ← not previously documented in AIGA

Jeweler's Marks and Hammers appear to be ring upgrade materials alongside the four already documented in AIGA.

*[Exact use of Jeweler's Marks and Hammers in the ring upgrade process — verify in-game]*

**Update required in:** AIGA_Rings_Reference.md

*Source: Theria Games Rings Calculator (Jayson, July 2025)*

---

## MEE SCORING — DAY-SPECIFIC BREAKDOWN

**Source: Theria Games Troop Training Calculator UI**

The troop training calculator outputs MEE scores broken down by specific event days:

| MEE Day | Activity scored |
|---|---|
| MEE II | Troop training |
| MEE IV | Troop training |
| MEE V | Troop training |

AIGA's existing MEE reference treats MEE training scoring as a single figure. The calculator confirms MEE has at least three separate days where troop training earns points, with potentially different scoring rates per day.

MGE troop scoring from the same calculator:
- MGE V — troop training day (confirmed, matches AIGA)
- MGE VI/VII — power gain from trained troops (confirmed, matches AIGA)

*[Full MEE day structure and training scoring rates per day — verify in-game or via Theria calculator live]*

**Update required in:** AIGA_MEE_Reference.md

*Source: Theria Games Troop Training Calculator (Jayson, July 2025)*

---

## HERO RANKS — SUB-RANKS CONFIRMED

**Source: Theria Games Hero Medals Calculator UI**

The hero medals calculator has inputs for both Rank (1-5) and Sub-rank (0-5) separately. This confirms that hero rank progression has a two-tier structure: main ranks AND sub-ranks within each rank.

AIGA's existing rank reference documents medals needed for Rank 1 through Rank 6 cumulatively. The sub-rank system suggests there is additional progression within each rank that AIGA has not captured.

*[Full sub-rank medal costs and what sub-ranks unlock — verify in-game. This may affect medal planning advice significantly]*

*Source: Theria Games Hero Medals Calculator (Jayson, June 2025)*

---

## XP TOME DENOMINATIONS — CONFIRMED

**Source: Theria Games Extra Tools Calculator UI**

Five XP tome denominations confirmed:

| Tome level | XP value |
|---|---|
| Lv. 2 | 500 XP |
| Lv. 3 | 1,000 XP |
| Lv. 4 | 10,000 XP |
| Lv. 5 | 50,000 XP |
| Lv. 6 | 100,000 XP |

These match AIGA's existing workbook exactly. Confirmed correct.

*Source: Theria Games Extra Tools Calculator (Jayson, July 2025)*

---

## MGE GEAR CALCULATION — SMITHY LEVEL MATTERS

**Source: Theria Games Equipment and Gems Calculator — MGE Mode**

The MGE mode of the gear calculator takes Smithy level as an input alongside number of Rare/Epic/Legendary pieces to calculate total meteorite cost, blueprints, time, and MGE score.

This confirms that Smithy level affects MGE Day II planning because it changes the forge time and therefore how many pieces can be crafted during the event window. A higher Smithy level = faster forging = more pieces possible = more MGE points.

Minimum Smithy level for Legendary gear: 15 (36% time reduction) — already in AIGA.
Recommended for MGE efficiency: Smithy 25 (78% time reduction).

*Source: Theria Games Equipment and Gems Calculator (Jayson, August 2025)*

---

*Sources: Theria Games calculator interfaces — Equipment & Gems, Legendary Advent, Rings, Troop Training, Hero Medals, Extra Tools, Research (Jayson, June-August 2025). Data extracted from UI labels as calculators are JavaScript-rendered. Verify all [verify in-game] items before using in player advice.*

# Age of Empires Mobile — Troop Training and Promotion Reference
## AIGA Source Document v1.0
## Source: aoem-calculator TrainingData.ts (MIT Licence, juan_jm/aoem-calculator on Codeberg)

---

## Overview

All costs and values below are **per single troop**. Multiply by your troop count to get total cost.

Time is in seconds per troop. Food/Wood/Stone/Gold are resource units per troop.

There are 7 troop tiers (T1-T7). All four troop types (Swordsmen, Archers, Pikemen, Cavalry) share identical costs and stats per tier.

---

## Per-Troop Stats by Tier — Fresh Training

| Tier | Power | MGE Day V pts | MEE pts | Train time (s) | Food | Wood | Stone | Gold |
|---|---|---|---|---|---|---|---|---|
| T1 | 1.0 | 2 | 30 | 10 | 80 | 20 | 0 | 0 |
| T2 | 1.3 | 3 | 50 | 14 | 100 | 30 | 30 | 0 |
| T3 | 1.7 | 5 | 70 | 19 | 140 | 40 | 40 | 40 |
| T4 | 2.2 | 10 | 100 | 28 | 235 | 55 | 55 | 55 |
| T5 | 2.9 | 20 | 160 | 43 | 340 | 80 | 80 | 80 |
| T6 | 4.2 | 50 | 280 | 75 | 470 | 110 | 110 | 110 |
| T7 | 6.0 | 100 | 500 | 130 | 650 | 150 | 150 | 150 |

---

## Per-Troop Promotion Costs (Difference Only)

Promotion costs = target tier values minus source tier values. You only pay the difference since you already invested in the lower tier.

| From | To | Power gain | MGE pts | Food | Wood | Stone | Gold | Time (s) |
|---|---|---|---|---|---|---|---|---|
| T1 | T2 | +0.3 | 1 | 20 | 10 | 30 | 0 | 4 |
| T2 | T3 | +0.4 | 2 | 40 | 10 | 10 | 40 | 5 |
| T3 | T4 | +0.5 | 5 | 95 | 15 | 15 | 15 | 9 |
| T4 | T5 | +0.7 | 10 | 105 | 25 | 25 | 25 | 15 |
| T5 | T6 | +1.3 | 30 | 130 | 30 | 30 | 30 | 32 |
| T6 | T7 | +1.8 | 50 | 180 | 40 | 40 | 40 | 55 |
| T1 | T4 | +1.2 | 8 | 155 | 35 | 55 | 55 | 18 |
| T3 | T5 | +1.2 | 15 | 200 | 40 | 40 | 40 | 24 |
| T1 | T7 | +5.0 | 98 | 570 | 130 | 150 | 150 | 120 |

**Critical rule:** Promotion gives ZERO MGE Day V points. Only fresh training earns MGE points. Always promote during peace, train fresh during MGE Day V.

---

## Bulk Training Reference — 10,000 Troops

| Tier | Power gained | MGE Day V pts | Food | Wood | Stone | Gold | Time |
|---|---|---|---|---|---|---|---|
| T1 | 10,000 | 20,000 | 800K | 200K | 0 | 0 | 1d 3h |
| T2 | 13,000 | 30,000 | 1.0M | 300K | 300K | 0 | 1d 15h |
| T3 | 17,000 | 50,000 | 1.4M | 400K | 400K | 400K | 2d 5h |
| T4 | 22,000 | 100,000 | 2.35M | 550K | 550K | 550K | 3d 5h |
| T5 | 29,000 | 200,000 | 3.4M | 800K | 800K | 800K | 5d |
| T6 | 42,000 | 500,000 | 4.7M | 1.1M | 1.1M | 1.1M | 8d 16h |
| T7 | 60,000 | 1,000,000 | 6.5M | 1.5M | 1.5M | 1.5M | 15d 1h |

---

## Bulk Training Reference — 100,000 Troops

| Tier | Power gained | MGE Day V pts | Food | Wood | Stone | Gold | Time |
|---|---|---|---|---|---|---|---|
| T3 | 170,000 | 500,000 | 14M | 4M | 4M | 4M | 22d |
| T4 | 220,000 | 1,000,000 | 23.5M | 5.5M | 5.5M | 5.5M | 32d 9h |
| T5 | 290,000 | 2,000,000 | 34M | 8M | 8M | 8M | 49d 18h |

---

## MGE Day V — Points per Troop by Tier

| Tier | MGE pts per troop | MGE pts per 1,000 troops | MGE pts per 10,000 troops |
|---|---|---|---|
| T1 | 2 | 2,000 | 20,000 |
| T2 | 3 | 3,000 | 30,000 |
| T3 | 5 | 5,000 | 50,000 |
| T4 | 10 | 10,000 | 100,000 |
| T5 | 20 | 20,000 | 200,000 |
| T6 | 50 | 50,000 | 500,000 |
| T7 | 100 | 100,000 | 1,000,000 |

Higher tier troops earn significantly more MGE points per troop. T7 gives 50x the points of T1 per troop. Always train the highest tier available during MGE Day V for maximum points efficiency.

---

## MEE (Mightiest Empire Event) — Points per Troop

| Tier | MEE pts per troop |
|---|---|
| T1 | 30 |
| T2 | 50 |
| T3 | 70 |
| T4 | 100 |
| T5 | 160 |
| T6 | 280 |
| T7 | 500 |

---

## Power Gain Reference

Power per troop increases significantly with tier:

| Tier | Power per troop | Power per 1,000 troops | Power per 10,000 troops |
|---|---|---|---|
| T1 | 1.0 | 1,000 | 10,000 |
| T2 | 1.3 | 1,300 | 13,000 |
| T3 | 1.7 | 1,700 | 17,000 |
| T4 | 2.2 | 2,200 | 22,000 |
| T5 | 2.9 | 2,900 | 29,000 |
| T6 | 4.2 | 4,200 | 42,000 |
| T7 | 6.0 | 6,000 | 60,000 |

Promoting 75,000 troops from T3 to T4 gives approximately 37,500 additional power (75,000 x 0.5 power gain per troop).

---

## Strategic Guidelines

### Train vs Promote decision
- **During MGE Day V:** Always train fresh troops (not promote) — promotion gives zero MGE points
- **During peace:** Promote existing lower-tier troops — cheaper than training fresh
- **During war:** Train fresh if troops are urgently needed; promote if time allows

### Resource planning for T4
Training 10,000 T4 troops costs approximately:
- 2.35M Food, 550K Wood, 550K Stone, 550K Gold
- 3 days 5 hours base training time (without speed bonuses)

### Highest ROI tier for current mid-game players (TC21-25)
T4 is the sweet spot for most mid-game players:
- Unlocked after T4 research (Advanced Swordsmen/Pike/Cavalry/Archers)
- 2.2 power per troop vs 1.7 for T3 — 29% more power per troop
- 10 MGE points vs 5 for T3 — double the MGE efficiency
- Manageable resource cost vs T5+

### Training time with speed bonuses
Base training time applies the formula: `final_time = base_time / (1 + speed_bonus%)` applied via the game's speed bonus system. Training speed research and VIP levels reduce these times significantly.

---

## Troop Load Values (Gathering Capacity per Troop)

| Tier | Load per troop |
|---|---|
| T1 | 45 |
| T2 | 60 |
| T3 | 75 |
| T4 | 90 |
| T5 | 105 |
| T6 | 120 |
| T7 | 135 |

Higher tier troops carry more resources per gathering trip. T4 troops carry exactly double what T1 troops carry per unit. For gathering marches, higher tier troops improve both combat survivability and resource haul per trip.

---

*Source: aoem-calculator TrainingData.ts (MIT Licence). Data current as of calculator development stop October 2025. All values are per-troop — multiply by troop count for totals. Verify against in-game values after any major game update.*

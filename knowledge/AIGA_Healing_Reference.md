# Age of Empires Mobile — Troop Healing Reference
## AIGA Source Document v1.0
## Source: aoem-calculator HealingData.ts (MIT Licence, juan_jm/aoem-calculator on Codeberg)

---

## Overview

Wounded troops recover in the Hospital. Healing costs resources and time per troop based on tier. Troops not healed before Hospital capacity is exceeded are permanently lost.

All values below are **per single troop**. Multiply by wounded troop count for totals.

---

## Healing Cost Per Troop by Tier

| Tier | Power | Time (min) | Food | Wood | Stone | Gold |
|---|---|---|---|---|---|---|
| T1 | 1.0 | 0.11 | 8 | 2 | 0 | 0 |
| T2 | 1.3 | 0.14 | 10 | 3 | 3 | 0 |
| T3 | 1.7 | 0.18 | 14 | 4 | 4 | 4 |
| T4 | 2.2 | 0.29 | 23 | 5 | 5 | 5 |
| T5 | 2.9 | 0.43 | 34 | 8 | 8 | 8 |
| T6 | 4.2 | 0.76 | 47 | 11 | 11 | 11 |
| T7 | 6.0 | 1.33 | 65 | 15 | 15 | 15 |

---

## Healing vs Training Cost Comparison

Healing is approximately 10% of the cost of training fresh troops. Always heal wounded troops rather than training replacements.

| Tier | Heal food cost | Train food cost | Heal is cheaper by |
|---|---|---|---|
| T3 | 14 | 140 | 90% cheaper |
| T4 | 23 | 235 | 90% cheaper |
| T5 | 34 | 340 | 90% cheaper |
| T6 | 47 | 470 | 90% cheaper |
| T7 | 65 | 650 | 90% cheaper |

**Rule:** Never let wounded troops expire unhealed. The resource cost to replace them via training is 10x the healing cost.

---

## Bulk Healing Reference — 10,000 Troops

| Tier | Food | Wood | Stone | Gold | Time |
|---|---|---|---|---|---|
| T1 | 80,000 | 20,000 | 0 | 0 | 18h 20m |
| T2 | 100,000 | 30,000 | 30,000 | 0 | 1d 0h |
| T3 | 140,000 | 40,000 | 40,000 | 40,000 | 1d 5h |
| T4 | 230,000 | 50,000 | 50,000 | 50,000 | 2d 0h |
| T5 | 340,000 | 80,000 | 80,000 | 80,000 | 3d 0h |
| T6 | 470,000 | 110,000 | 110,000 | 110,000 | 5d 6h |
| T7 | 650,000 | 150,000 | 150,000 | 150,000 | 9d 4h |

---

## Bulk Healing Reference — 50,000 Troops

| Tier | Food | Wood | Stone | Gold | Time |
|---|---|---|---|---|---|
| T3 | 700,000 | 200,000 | 200,000 | 200,000 | 6d 3h |
| T4 | 1,150,000 | 250,000 | 250,000 | 250,000 | 10d |
| T5 | 1,700,000 | 400,000 | 400,000 | 400,000 | 15d |

---

## Hospital Capacity

Hospital capacity determines the maximum number of wounded troops that can queue for healing simultaneously. Troops wounded beyond this cap are permanently lost.

**Hospital upgrade priority:**
- Hospital must scale with your total troop count
- At 500,000+ troops, Hospital capacity should comfortably exceed your largest single battle casualty estimate
- Upgrade Hospital at every TC milestone that requires it (TC11, TC16, TC21, TC28)
- Never let Hospital capacity fall behind total troop growth

**Signs your Hospital is too small:**
- Troops showing as lost (not wounded) after battles
- Hospital queue full immediately after any major rally
- Wounded troop count exceeds hospital capacity shown in city overview

---

## Strategic Healing Rules

**During war:**
- Heal continuously — keep healing queue full at all times
- Prioritise highest tier troops first (T4+ cost most to replace)
- Use healing speedups during heavy war periods to clear queue faster
- Check Hospital capacity before every major rally

**During peace:**
- Clear all wounded troops before the next war phase
- Stock up Food and Wood specifically — these are the primary healing resources
- Hospital queue running during peace means wasted capacity — keep it clear

**Resource planning for healing:**
Food is the primary healing resource at all tiers. Maintain a Food stockpile sized to heal at minimum 20-30% of your total troop count between gathering runs. At 500,000 T4 troops that means keeping ~2.3M Food in reserve as a healing buffer.

---

## Healing Speedups

Healing speedups work the same way as building and research speedups — they reduce time in the Hospital queue. Save healing speedups for:
- Post-war mass healing after major battles
- MEE event phases where power recovery speed matters
- Any situation where wounded troops are blocking march capacity

---

*Source: aoem-calculator HealingData.ts (MIT Licence). All values are per troop — multiply by wounded count for totals. Time values are in minutes per troop in source data.*

# Age of Empires Mobile — Gathering Reference
## AIGA Source Document v1.0
## Source: aoem-calculator gathering data.json (MIT Licence, juan_jm/aoem-calculator on Codeberg)

---

## Resource Node Levels

Gathering nodes on the world map have levels 1-9. Higher level nodes hold more resources and generate faster. Rich nodes (special variants) have double the speed and capacity.

### Node gathering speed (resources per hour)

| Node level | Base speed (rss/hr) | Rich node speed (rss/hr) |
|---|---|---|
| 1 | 0 | 0 |
| 2 | 250,000 | 250,000 |
| 3 | 180,000 | 180,000 |
| 4 | 180,000 | 360,000 |
| 5 | 180,000 | 360,000 |
| 6 | 190,000 | 380,000 |
| 7 | 200,000 | 400,000 |
| 8 | 210,000 | 420,000 |
| 9 | 210,000 | 420,000 |

### Node total capacity (total resources held)

| Node level | Base capacity | Rich node capacity |
|---|---|---|
| 1 | 0 | 0 |
| 2 | 800,000,000 | 800,000,000 |
| 3 | 54,000 | 54,000 |
| 4 | 216,000 | 720,000 |
| 5 | 540,000 | 1,800,000 |
| 6 | 912,000 | 3,040,000 |
| 7 | 2,160,000 | 7,200,000 |
| 8 | 3,780,000 | 12,600,000 |
| 9 | 5,292,000 | 17,640,000 |

*Note: Level 2 capacity value appears anomalous in source data (800M) — verify in-game.*

---

## Troop Load by Tier

Each troop carries this many resources per unit when gathering.

| Troop tier | Resources carried per troop |
|---|---|
| T1 | 45 |
| T2 | 60 |
| T3 | 75 |
| T4 | 90 |
| T5 | 105 |
| T6 | 120 |
| T7 | 135 |

### Practical gathering capacity examples

With a march of 50,000 troops:

| Troop tier | Total load (resources per trip) |
|---|---|
| T3 | 3,750,000 |
| T4 | 4,500,000 |
| T5 | 5,250,000 |
| T6 | 6,000,000 |
| T7 | 6,750,000 |

T4 troops carry 20% more per trip than T3. Every tier upgrade improves gathering efficiency directly.

---

## Gathering March Configuration

### Best gathering heroes
| Hero | Role | Why |
|---|---|---|
| Diao Chan | Lead | Signature skill multiplies daily resources by 1.5x — best gathering lead in game |
| Cleopatra | Support | Efficient Harvest skill + dual cavalry/sword type flexibility |
| Darius the Great | Support | Efficient Harvest skill, dual cavalry/pikemen type |
| King Derick | Support | Efficient Harvest 15, dual archer/sword type |
| Yuan Xia | Support | Pairs well with Diao Chan specifically |

### Gathering skill
The key skill on gathering heroes is **Efficient Harvest** — increases resources gathered per trip. Prioritise this skill on dedicated gathering heroes only. Never invest SP in Efficient Harvest on combat heroes.

### Talent tree for gathering heroes
- Take all gathering speed talents
- Take all resource yield talents
- Ignore combat damage and unit attack talents entirely
- Reset gathering talent tree when converting hero back to combat role (costs 100 Empire Coins)

---

## Peace Period Gathering Strategy

### M5 gathering configuration (peace mode)
| Slot | Hero | Role |
|---|---|---|
| Lead | Diao Chan | Gathering specialist — 1.5x daily resource multiplier |
| Support | Cleopatra | Efficient Harvest |
| Support | Darius | Efficient Harvest |

### Daily gathering routine
1. Send M5 gathering march to highest level node available immediately on stamina depletion
2. When M3/M4 stamina depletes from tribe grinding, redirect to resource farms
3. Warehouse protects resources from raids — upgrade Warehouse if under attack pressure
4. Diao Chan's daily resource multiplier resets every 24 hours — ensure at least one full gathering trip completes per day

### Node targeting priority
- Target the highest level node your march can reach
- Rich nodes are 2x more efficient than standard nodes at same level — always prefer rich if available
- Food and Gold are typically the bottleneck resources at TC23+ — prioritise those node types

### Gathering march troop type
Send the troop type that matches the node type if the game offers a bonus for it. Otherwise send your largest troop pool (Swordsmen at 140,000 gives the most load capacity per trip).

---

## Resources Protected by Warehouse

The Warehouse protects a set amount of each resource from being looted by attackers. Resources above the cap are vulnerable. During active war periods:
- Upgrade Warehouse to increase protected cap
- Spend resources on queued buildings/research before logging off during war
- Keep resource stockpile below protected cap when enemy attacks are likely

---

## MGE and MEE Gathering Points

From the MGE scoring data:
- Gathering 100 resources of any type = 1 MGE point
- Gathering is the lowest value MGE activity — only do it passively during Day III
- Focus gathering effort on Day III alongside Wheel spins (1,000 pts each)

MEE (Mightiest Empire Event) also rewards gathering but specific values vary by event phase — check in-game event details for current scoring.

---

*Source: aoem-calculator gathering data.json (MIT Licence). Troop load values cross-referenced with TrainingData.ts. Verify node capacity values in-game as the level 2 capacity appears anomalous in source data.*

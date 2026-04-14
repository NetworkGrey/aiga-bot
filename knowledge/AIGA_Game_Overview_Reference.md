# AIGA — Game Overview Reference
## Age of Empires Mobile
### Sources: AoE Mobile Fandom Wiki Starter Guide (Sigarme), AoE Mobile Official Discord FAQ
### Version: 1.0 | March 2026

---

## Game Identity

- **Full name:** Age of Empires Mobile (AoEM)
- **Developer:** Co-developed by TiMi Studio Group and World's Edge (Microsoft)
- **Publisher:** Level Infinite
- **Global launch:** October 17, 2023
- **Platforms:** iOS (App Store), Android (Google Play)
- **PC:** No native client. Supported emulators: BlueStacks, NOX, Thunder
- **Franchise:** Official mobile entry in the Age of Empires franchise
- **No season resets:** Player progress is permanent — no wipe between seasons. Every resource spent is a permanent investment.
- **Beta test data:** All beta test server data was fully retained at global launch

---

## Core Game Loop

Build a Citadel, train armies, develop heroes, research technologies, join an alliance, participate in events and alliance warfare. The end goal is alliance-level competition for control of the Imperial City (server throne).

Primary progression levers in order of importance:
1. Town Centre level — gates everything else
2. Hero development — determines march quality
3. Troop tier and quantity — determines combat power
4. Research — multiplies all of the above
5. Alliance strength — gates endgame content

---

## Commander Skill Auto-Levelling

Commander skills level up automatically with hero level — they do not require manual skill point investment. This is distinct from signature skills and customisable skills.

| Hero Level | Commander Skill Level |
|---|---|
| 10 | 10 |
| 20 | 15 |
| 40 | 20 |
| 60 | 25 |
| 80 | 30 |
| 100 | 35 |
| 120 | 40 (max) |

**Implication for AIGA advice:** Never recommend spending SP on commander skills. They are free progression tied entirely to hero XP level.

---

## Skill Unlock Mechanics

**Customisable skill slots:**
- Slot 1 unlocks at hero lv25
- Slot 2 unlocks at hero lv38

**At lv38, two Epic skills are automatically unlocked** — no medals or resources required.

**Legendary customisable skills must be unlocked separately** using legendary skill medals. These are obtained from:
- Bundles (real-money purchases)
- Items store (in-game currency)

**Implication for AIGA advice:** A hero at lv38 with only Epic skills in their slots is not necessarily under-invested — it may simply mean legendary skill medals have not been acquired yet. Flag this distinction when auditing hero builds.

---

## Building Strategy — Key Tips

**Production buildings (Mills, Quarries, Lumber Camps, Gold Mines):**
- Only upgrade ONE of each type to maximum level
- Keep all others at low level deliberately
- Reason: Alliance Glory and similar competitive events award points for upgrading buildings — low-level buildings are a strategic reserve of easy event points
- Exception: one production building per type must meet TC prerequisite requirements

**Priority building upgrade order:**
1. Town Centre — always the primary target
2. University — keep at max level at all times (research speed + technology unlocks)
3. Tavern — important for hero level cap and free recruitment cooldown
4. Embassy — more assists = more building/research speed reduction. Upgrade aggressively
5. Hospital — upgrade when University, Tavern and Embassy are current
6. Military Barracks (all four) — upgrade for training speed and troop tier unlocks
7. Smithy (unlocks TC15) — upgrade immediately when unlocked, significantly reduces forge time. Up to 5 forging queues at max level.
8. City Walls — upgrade whenever possible (required for TC level progression)
9. War Hall (unlocks TC12) — upgrade to increase rally capacity and daily pillage limit
10. Watchtower — upgrade only to meet TC prerequisites, nothing more
11. Market — upgrade only to meet TC prerequisites, nothing more
12. Guard Towers — upgrade last, after all critical buildings are current

**Alliance assists:** Every alliance assist received reduces building and research queue time. More embassy levels = more assists receivable. This is one of the highest-value passive accelerators in the game — always request helps and always provide them.

---

## Alliance System

**Stronghold prerequisites:** 5 alliance members + 100,000 total military power. Required to unlock Supply Depot and alliance events.

**Alliance technology trees:**
- Politics tree: increases maximum member capacity — prioritise first
- Science tree: adds territory flags for world map expansion
- Economy tree: boosts resource production and gathering for all members

**Donating resources:** Always use all donation attempts. Benefits: unlocks alliance technologies, generates alliance funds for territory buildings, rewards donor with Alliance Coins (spendable in alliance store).

**Alliance Coins** are earned by donating and through alliance events. Spend in Alliance Treasury Shop which resets every 7 days — includes skill points.

---

## Alliance Events

### Trojan Turmoil
- Frequency: every 2 days, started by alliance leader
- Duration: 30 minutes
- Mechanic: 3 waves of Trojan Horse enemies appear near Supply Depot. Each wave has a different unit type weakness and military specialty weakness. Rally against each wave.
- Wave duration: 7min 30s per wave before auto-advancing
- **Rewards: up to 2,000 Empire Coins every 2 days** + resources + War Hall blueprints
- Priority: high — Empire Coins are a scarce premium currency

### Supplies Bounty
- Mechanic: defeat increasingly difficult tribes through 80 levels
- Reward: passive storage of speedups and resources based on latest completed level (up to 12 hours capacity), claimed at Supply Depot

### Giants Roar (early game, limited duration)
- Mechanic: defeat common tribes to collect Giant's Treasure banners. Use banners to summon Giant Legion near your Citadel and rally with alliance.
- **King Derrick medal limits:** No daily cap when using your own banners. Cap of 30 legendary King Derrick medals per day when assisting other players' banners.
- This is the primary early-game source of King Derrick medals — do not miss it

---

## Hero Progression — Additional Notes

**Military specialties** unlock at hero lv50. This enables pairing combination bonuses when heroes with matching specialties are placed in the same march. Always develop hero to at least lv50 before evaluating pairing effectiveness.

**Signature skills:** Level up with SP first — no scrolls required unlike customisable skills. Prioritise signature skill levelling before investing in customisable skills.

**Hero ranks:** Each rank requires medals (exclusive or universal legendary). Rank milestones that grant new ability boosts or passives: Rank 1, Rank 3, Rank 5. Full rank table:
- Unlock: 10 medals
- Rank 0→1: 20 medals (cumulative: 30)
- Rank 1→2: 50 medals (cumulative: 80)
- Rank 2→3: 100 medals (cumulative: 180)
- Rank 3→4: 150 medals (cumulative: 330)
- Rank 4→5: 270 medals (cumulative: 600)

*Note: This table from Fandom guide matches AIGA system prompt verified data — confirmed consistent.*

---

## Expeditions

### Island Tactics
- 900 challenge stages
- Completion rewards per stage + passive Tactic Coin production
- Coins spent in Island Tactics store (gear materials, blueprints, SP items)
- **Non-negotiable daily activity** — collect coins twice daily minimum (cap at 12 hours)
- Best free source of gear crafting materials

### Military Exercise
- 50 stages
- Exclusive token rewards spendable in Military Exercise store
- Temporary boosts apply per stage (do not carry over)
- Progress left to right through battles, supply points and strategy tiles

### Apex Arena
- PvP expedition — set offensive and defensive lineups
- Rank determined by win/loss ratio
- Daily and weekly rewards based on rank
- Update lineups as account progresses

---

## Daily Activities Checklist

High-value daily habits that should become automatic:

| Activity | Why |
|---|---|
| Free Island Tactics coin collection (x2) | Coins cap at 12h — collect twice or lose production |
| Legendary Arrival tavern pull | Free hero tokens and resources |
| Free stamina supply (50 stamina) | Never let it expire |
| Alliance donation (up to 20 attempts) | Coins + alliance tech + assists |
| Alliance assists (up to 20) | Reduces all allies' queue times |
| Tribe defeats | Stamina usage, SP, event points |
| Resource gathering | Passive income, event points |
| Hospital auto-heal | Prevent troop death from overflow |
| Seaside Fishing | Free daily food bonus |
| Daily quests (200 points target) | Unlocks all daily chests |
| Legendary Advent free spins (8/day) | Always use — never skip |

**Daily quest 200-point path:**
- Legendary Arrival recruitment: 40 pts
- Gather 50k resources: 30 pts
- Defeat tribes 10 times: 30 pts
- Heal at hospital once: 10 pts
- Train 1,000 units: 20 pts
- Collect resources from world tiles 5 times: 30 pts
- Alliance donations 10 times: 20 pts
- Assist allies 20 times: 30 pts
- **Total: 210 pts — all chests unlocked**

---

## Free-to-Play Hero Acquisition Notes

**Early obtainable heroes (no spending required):**
- Josephine — given at game start
- Joan of Arc — given at game start
- Darius I + Hammurabi — log in 7 consecutive days (beginner event)
- King Derrick — Giants Roar event (early game, limited window)
- Tribhuwana — Legendary Advent (20 spins unlocks chest with 10 medals, guaranteeing summon)

**Miyamoto Musashi:** Available via VIP 1 and 2 exclusive bundles (paid). Paired with Hammurabi and King Derrick as recommended early lineup.

---

## World Map and Server

- New players are auto-assigned to a default server on first login
- Server switching: Settings > Personal Information > available after completing beginner's guide
- Switching server creates a new character and requires completing the beginner's guide again
- Friends can join existing servers through the same Settings menu

---

## Security Note (from Official Discord)

MOD and official staff have identity roles visible in the Discord server. Never trust private messages claiming prizes, asking for account details, or offering third-party recharges — these are scams. Official staff will never DM to request account information.

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | March 2026 | Initial release — commander skill table, skill unlock mechanics, building strategy, alliance events, expeditions, daily checklist |

---

*Sources: Age of Empires Mobile Fandom Wiki — Starter Guide by Sigarme (CC-BY-SA). AoE Mobile Official Discord FAQ. Community knowledge — verify any time-limited event details in-game.*

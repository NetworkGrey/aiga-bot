# AIGA — Signet Rings Reference
## Network Grey | Age of Empires Mobile
## Version: 2.2 | June 2026

---

## Revision History

| Version | Date | Changes |
|---|---|---|
| v1.0 | March 2026 | Initial rings reference. 35 rings, stats, skill types, Jeweler's Marks confirmed. |
| v2.0 | June 2026 | Full rebuild. Added FTP tier ratings, hero-role ring stacks, ring builder logic, meta overrides, allocation cascade rules. Sources: Theria Games calculator + Fandom Wiki image verification + in-game confirmation + FTP tier list video (community, credited). |
| v2.1 | June 2026 | Corrected Lu Bu's permanent T2 to Radiant Guardian (in-game verified by Gustav, overrides F2P-ignore rating for this hero specifically). Resolved Lagertha knowledge gap — Tranquil Water confirmed via AllClash. Added Divine Warrior as unverified/future ring (not in canonical set, source: AllClash + FTP video, not cross-confirmed by calculator or wiki). Added zero-combat-value T0 ranking rule (crit/damage stats over XP/gathering utility as placeholder). |
| v2.2 | June 2026 | FINAL authoritative pass for dev handoff. Corrected "King Derek" → "King Derrick" spelling throughout (matches Hero Roster v8 canonical name). Cross-referenced against Hero Roster v8's `Ring Path` field — confirmed 14 heroes have full tiered T0→T1→T2 paths (Gustav's 13-hero roster + Lu Bu), explicitly documented that the remaining 62 heroes carry only a single unverified legacy ring value inherited from pre-v2 data, not a real tiered recommendation. This gap is now the single most important entry in Known Gaps and is the primary blocker for full ring builder rollout in app.py. No legacy single-ring values were upgraded to tiered paths in this pass — doing so without per-hero skill/role verification would be fabrication, not correction, per the project's standing rule that blank gaps ship and guessed values do not. |
| v2.2 (count correction) | June 2026 | Canonical ring count confirmed as **35** (10 T0 / 14 T1 / 11 T2) — corrects v2.2's draft note that mis-stated 33 and a header typo that said "9 rings" for Tier 2. No ring of Mamba exists in the canonical set. Sacred Sage is the 11th confirmed T2 ring (Balance bracket). |

---

## Sources

| Source | Trust level | Used for |
|---|---|---|
| Theria Games calculator (HTML) | Medium-high | Ring names, stat values, skill effects, craft costs |
| Fandom Wiki image gallery | Medium | Ring name verification (image filenames as proxy) |
| In-game verification (Gustav, S371) | Highest | Canonical 35-ring set confirmed |
| FTP tier list video (community YouTube) | Medium — community | Usage tier ratings, meta overrides, hero-specific flags |
| aoem-calculator (MIT, Codeberg) | Highest | MGE scoring for ring crafting |
| AllClash hero build guides | Medium — community | Hero-specific ring pairings (e.g. Lagertha) |
| aoemobileguides.com hero guides | Medium — community | Hero skills, specialties, pairings (no ring data) |

---

## Canonical Ring Set — 35 Rings

**Tier 0 (Flower) — 10 rings | Max lv30 | Craft cost: 200 jeweler's coins**
**Tier 1 (Animal) — 14 rings | Max lv40 | Craft cost: 600 jeweler's coins**
**Tier 2 (Element) — 11 rings | Cheap: 1,600 coins (5 rings) | Balance: 4,000 coins (6 rings)**

Total: 10 + 14 + 11 = **35 rings**.

---

## Core Rules

- Rings unlock at TC18
- One ring per hero — cannot equip two rings on one hero
- One of each ring type across the entire roster — no duplicate ring names across all heroes simultaneously
- When a ring is upgraded (T0→T1), the T0 ring returns to inventory and becomes available for reassignment
- When a T1 ring is acquired, the T0 ring cascades to the next priority hero without a ring
- Every hero should have a ring — any ring beats no ring
- Allocation priority: M1 Lead → M1 Sup1 → M1 Sup2 → M2 Lead → ... → M5 Sup2
- Exception: meta-specific overrides apply regardless of march position (see hero flags below)

---

## Ring Status Tags (Ring Builder)

When advising a player on ring status, use these three tags:

- **fitted** — ring is owned and currently equipped to this hero
- **available** — ring is owned but not equipped to this hero (on another hero or in inventory)
- **not acquired** — ring not yet crafted or owned

---

## Tier 0 — Flower Rings (10 rings)

| Ring | Skill Name | Skill Type | Skill Effect (max lv30) | Combat Value | Notes |
|---|---|---|---|---|---|
| Daisy | Double Strike | Second strike | 20% chance: might dmg on normal attack (155% rate, might bonus) | High | Best T0 for DPS leads. Must-have placeholder for any warrior/might hero |
| Clover | Armor Maintenance | Turn-based | 50% chance: -25% dmg taken for 3s every 6s | High | Best T0 for survivability. Suits any support or lead needing tankiness |
| Tulip | Mighty Strike | Active | 25% chance: might dmg to enemy troop (125% rate, might bonus) | Medium-high | Good T0 for might-damage leads. PIK and SW leads |
| Rose | Surprise Attack | Active | 25% chance: strategy dmg to enemy troop (125% rate, strategy bonus) | Medium | Strategy-damage heroes only. Weak on might leads |
| Lily | Rest and Recover | Active | 25% chance: recover troop units (150% rate, strategy bonus) | Medium | Recovery/support heroes. Not for DPS leads |
| Iris | Critical Blade | Passive | +5.5% hero crit rate | Medium | Generic crit boost. Decent on any hero |
| Hyacinth | Battle Review | Passive | +25% hero XP gained | Zero combat | Levelling only — unequip before combat or events |
| Laurel | Siege Tactics | Passive | +89 hero siege | Zero combat | Siege march only (King Derrick/Josephine/Harald). No value on combat heroes |
| Violet | Hands of Industry | Passive | +20% gathering speed | Zero combat | Gathering heroes only (Diao Chan, Cleopatra, Darius) |
| Sunflower | Bumper Harvest Omen | Passive | +12% resources on successful gather | Zero combat | Gathering heroes only |

**Best T0 combat:** Daisy (DPS lead) or Clover (support/survivability)
**Gathering-only T0:** Violet, Sunflower — never equip on combat heroes
**Avoid on combat heroes:** Hyacinth, Laurel

**T0 placeholder ranking rule:** when no combat-relevant T0 is available, always prefer a ring with an active combat stat (Iris +crit rate, Tulip/Rose active damage chance) over a zero-combat-value ring (Hyacinth XP, Laurel siege, Violet/Sunflower gathering). A passive combat stat that's always active beats a utility stat that requires unequipping around fights. Example: Iris over Hyacinth as a combat-march placeholder — crit rate applies in every fight, XP gain has no battlefield value and requires manual swapping.

---

## Tier 1 — Animal Rings (14 rings)

| Ring | Skill Name | Skill Type | Skill Effect (max lv40) | FTP Rating | Notes |
|---|---|---|---|---|---|
| Night Wolf | Ablaze Spirit | Passive | Every 9 normal attacks: +25% normal/second-strike dmg (might bonus), -35 armor for 3s | Must-have | **LU BU SPECIFIC** — see meta override below |
| Falcon | Blessing of Oasis | Turn-based | Every 9s: recover units (210% rate) OR -32% dmg taken for 3s | Must-have | Best universal support ring. Suits any support slot on any march |
| Boar | Burning Will | Passive | Below 60% units: +42% passive skill dmg | Must-have | Best for PIK supports. Strong on Cyrus-type heroes |
| Bear | All Out | Passive | -20 armor on all heroes, +105 commander might | Great | CAV/SW DPS leads. Sacrifices armor for might damage |
| Serpent | Strategy and Might | Passive | +65 strategy (might bonus) | Great | Tactical SW and strategy-based heroes. Suits Sun Tzu formations |
| Deer | Coercion | Passive | -22% random enemy hero dmg, +22% one of your hero's dmg | Great | Flexible — suits support slots on any march type |
| Lion | Heroic Lineage | Passive | +65 might/strategy/armor (flat) | Good-flexible | Generic flat stat boost. Works on any hero, any march |
| Crow | Twist of Fate | Active | 30% chance: steal 55 might/strategy/armor from enemy for 3s | Flexible | Tactical formations only. Not ideal for F2P warrior lineups |
| Badger | Armor of Steel | Passive | First 18s: -31.5% normal attack and second-strike dmg taken | Flexible | Counter to Lu Bu-heavy metas. Strong on PIK |
| Seahorse | Unyielding Faith | Passive | If troop takes >1% max units strategy dmg in one hit, -20% strategy dmg taken for 6s | Flexible | Counter to strategy meta. Situational |
| Shark | Punisher | Passive | Each normal attack: -1% target recovery effect, stacks to 50 | Okay-ignore | Healing debuffer. Niche and slow to activate. Generally avoid |
| Steed | Load Boost | Passive | +20% gathering speed, +20% troop load | Gathering only | Permanent fit for gathering lead (Diao Chan). Never equip on combat hero |
| Rhino | Breach | Active | 20% chance: 525 wall durability dmg (siege bonus) | Siege only | Siege march only. No combat value |
| Elephant | Siege Master | Passive | +102 hero siege | Siege only | Siege march only. No combat value |

**Must-have T1:** Night Wolf (Lu Bu only), Falcon (any support), Boar (PIK support)
**Gathering-only T1:** Steed — never equip on combat hero
**Siege-only T1:** Rhino, Elephant — only for dedicated siege march

---

## META OVERRIDE — Night Wolf / Lu Bu

**Night Wolf is a Lu Bu-specific ring regardless of march position.**

Lu Bu's secondary strike mechanic triggers crits when combined with Night Wolf's every-9-attacks buff. This produces the 40k-50k damage spikes seen in top Lu Bu marches. Equipping Night Wolf on any other hero produces a fraction of that value.

**Rule:** Night Wolf always goes to Lu Bu first. If Lu Bu is not in the roster, Night Wolf then follows normal march priority allocation.

**Lu Bu's full confirmed ring path (in-game verified, Gustav, S371):**
Daisy → Night Wolf → Radiant Guardian

This overrides the general F2P-ignore rating on Radiant Guardian for Lu Bu specifically. Radiant Guardian's Flurry of Blows (second-strike activation + Double Attack) synergises directly with Lu Bu's crit-chain kit the same way Night Wolf does. In-game verification outranks the community FTP tier list per source hierarchy (see Sources table). Radiant Guardian remains F2P-ignore for all other heroes.

---

## META OVERRIDE — Lagertha (W.SW 3rd Slot)

**Confirmed ring path:** Daisy (T0) → Night Wolf (T1, if not claimed by Lu Bu) → Tranquil Water (T2)

Source: AllClash hero build guide lists Divine Warrior + Tranquil Water as Lagertha's pairings. Tranquil Water is in the verified 35-ring canonical set and is adopted as her confirmed T2. Divine Warrior is NOT in the canonical set (not found in Theria Games calculator or Fandom wiki) — flagged as an unverified/possible future ring, do not recommend until cross-confirmed.

Lagertha role confirmed via aoemobileguides.com: Legendary SW, specialties Warrior/Piercing/Active, secondary striker kit (Berserker's Shield Dance, Valkyrie's Edge). Pairs with Yodit, Constantine, Miyamoto Musashi.

---

## Tier 2 — Element Rings (11 rings)

### Cheap T2 (1,600 jeweler's coins) — 5 rings

| Ring | Skill Name | Skill Type | Skill Effect (max lv50) | FTP Rating | Notes |
|---|---|---|---|---|---|
| Tranquil Water | Light's Protection | Passive | First 18s of battle: -40% troop dmg taken | Must-have | Best general survivability ring in game. Suits any march lead or support |
| Lofty Mountain | Accumulating Strength | Passive | First 18s: -15% might dmg taken (armor bonus). After 18s: +15% troop dmg (strategy bonus) | Must-have | Best general DPS lead ring. Open field and rally. Suits SW/CAV leads |
| Effulgent Sun | Firm Onslaught | Active | 30% chance: charge 3s then massive might dmg (400% rate, might bonus) | Okay | Charge delay is a weakness. Not recommended as priority pick |
| Azure Moon | Foreboding of Destruction | Active | 25% chance: charge 3s then massive strategy dmg (480% rate, strategy bonus) | Okay | Charge delay is a weakness. Strategy heroes only |
| Scorching Flame | Heroic Moment | Passive | On Commander Skill use: +22% all heroes' might for 9s | Okay | Requires good rage generation. Situational |

### Balance T2 (4,000 jeweler's coins) — 6 rings

| Ring | Skill Name | Skill Type | Skill Effect (max lv50) | FTP Rating | Notes |
|---|---|---|---|---|---|
| Skyward Knight | Cost of Victory | Passive | -15% hero dmg dealt (unpurifiable), +17% commander dmg (strategy bonus), +10% sig activation | Must-have | Best support ring for tactical formations. Suits SW/ARC support slots |
| Messenger of Destruction | Perception | Passive | -20% normal attack dmg (unpurifiable), +75% passive skill dmg | Must-have | Best PIK lead ring. Non-negotiable for Cyrus-type leads |
| Everflame Wings | Silencing Flame | Turn-based | Every 9s: Burn, +5% enemy strategy dmg taken for 9s, 30% chance to Silence 3s | Late-game BIS | Best tactical formation ring. Silence mechanic is game-changing at lv30+ |
| Sacred Sage | Silent Oath | Passive | Disables active skills (unpurifiable), +55% turn-based dmg and healing effect | Late-game BIS | Turn-based formations only (Marshall PIK). Julius Caesar/Octavian type heroes |
| Radiant Guardian | Flurry of Blows | Turn-based | Every 6s: +5% second-strike activation, 100% Double Attack for 3s | F2P ignore* | Mulan/Belisarius specific. No F2P formation needs this ring. *Exception: confirmed BIS for Lu Bu (see meta override) |
| Lord of Eastern Heavens | Decree of Victory | Passive | -25% active skill dmg (unpurifiable), +100% normal attack dmg | Ignore | Explicitly rated ignore by community. Even spenders regret this purchase. Avoid |

**Must-have T2 (cheap):** Tranquil Water, Lofty Mountain
**Must-have T2 (balance):** Skyward Knight, Messenger of Destruction
**Late-game BIS:** Everflame Wings, Sacred Sage
**Avoid:** Lord of Eastern Heavens (ignore tier regardless of cost), Radiant Guardian (F2P ignore, except Lu Bu)

### Unverified / Possible Future Rings — DO NOT RECOMMEND

| Ring | Source | Status |
|---|---|---|
| Divine Warrior | AllClash (Lagertha pairing), FTP tier video | NOT in canonical 35-ring set. Not found in Theria Games calculator or Fandom wiki gallery. Possible future ring or AllClash error. *[verify in-game before use]* |
| Celestial Spark | FTP tier video only | Same status — unverified, not in canonical set |
| Radiant Thunder | FTP tier video only | Same status — unverified, not in canonical set |
| Siege of Judgment / Sacred Siege | FTP tier video only | Likely mistranscription of Sacred Sage — do not treat as separate ring |

---

## Hero Ring Stacks — Best T0 / T1 / T2 Per Hero Role

Used by ring builder to answer "what is the best ring for [hero]?" regardless of player inventory.
Status tags (fitted / available / not acquired) are applied when player context is provided.

### M1 — Swordsmen Rally March

| Hero | Role | Best T0 | Best T1 | Best T2 |
|---|---|---|---|---|
| Musashi | SW DPS Lead | Daisy | Night Wolf | Lofty Mountain |
| Yodit | SW DPS Support | Clover | Falcon | Skyward Knight |
| Hammurabi | SW Buff Support | Clover | Lion | Tranquil Water |
| Lagertha | SW Secondary Striker (3rd slot) | Daisy | Night Wolf (if available) | Tranquil Water *(confirmed, AllClash)* |

### M2 — Pikemen Rally March

| Hero | Role | Best T0 | Best T1 | Best T2 |
|---|---|---|---|---|
| Cyrus | PIK Lead | Tulip | Boar | Messenger of Destruction |
| Joan | PIK Counterattack Support | Clover | Falcon | Tranquil Water |
| Boudica | PIK Damage Support | Tulip | Bear | Everflame Wings |

### M3 — Cavalry March

| Hero | Role | Best T0 | Best T1 | Best T2 |
|---|---|---|---|---|
| Lu Bu | CAV DPS Lead | Daisy | Night Wolf *(meta override)* | Radiant Guardian *(in-game verified override)* |
| Guan Yu | CAV Support | Tulip | Bear | Scorching Flame |
| Timur | CAV/ARC Support | Lily | Deer | Azure Moon |

### M4 — Archer March

| Hero | Role | Best T0 | Best T1 | Best T2 |
|---|---|---|---|---|
| Yi Sun-Shin | ARC Lead | Daisy | Falcon | Tranquil Water |
| Bellevue | ARC Support | Clover | Falcon | Everflame Wings |
| Henry V | ARC Support | Iris | Badger | Skyward Knight |

### M5 — Gathering March (Peace Config)

| Hero | Role | Best T0 | Best T1 | Best T2 |
|---|---|---|---|---|
| Diao Chan | Gathering Lead | Violet | Steed | — (no T2 gathering ring) |
| Cleopatra | Gathering Support | Sunflower | Steed* | — |
| Darius | Gathering/PIK Support | Laurel | Steed* | — |

*Steed — only one exists. Diao Chan (M5 Lead) gets priority. Cleopatra and Darius use T0 gathering rings as permanent ceiling until second Steed is crafted.

---

## Ring Allocation Cascade Rules

1. Assign permanent ring (best T2) to each hero in M1 Lead → M5 Sup2 priority order, no duplicates
2. Meta overrides apply before march priority (Night Wolf → Lu Bu regardless of march)
3. When player owns a ring, check cascade: does this hero already have a better ring? If yes, pass it down
4. When a hero upgrades T0 → T1: T0 ring returns to pool, assign to next ringless hero in priority order
5. When a hero upgrades T1 → T2: T1 ring replaces T0 on the next hero in the cascade, T0 continues down
6. Gathering rings (Violet, Sunflower, Steed) never enter the combat cascade — they stay in the M5 pool
7. Siege rings (Laurel, Rhino, Elephant) never enter the combat cascade — they stay in the dedicated siege march pool
8. Ignore-tier rings (Lord of Eastern Heavens, Radiant Guardian for F2P) — flag if player has them equipped, suggest reassignment

---

## Gathering Sub-Pool

These rings never enter the general combat cascade — they are allocated only within the M5 gathering march:

| Ring | Tier | Effect |
|---|---|---|
| Violet | T0 | +20% gathering speed |
| Sunflower | T0 | +12% resources on successful gather |
| Steed | T1 | +20% gathering speed, +20% troop load |

Diao Chan (M5 Lead) gets priority on Steed since only one exists per the current ring economy. Cleopatra and Darius hold T0 gathering rings as their ceiling until a second Steed is crafted.

---

## Siege Sub-Pool

These rings never enter the general combat cascade — they are allocated only within a dedicated siege march:

| Ring | Tier | Effect |
|---|---|---|
| Laurel | T0 | +89 hero siege |
| Rhino | T1 | 20% chance: 525 wall durability dmg (siege bonus) |
| Elephant | T1 | +102 hero siege |

No combat value on a standard march — only relevant for heroes dedicated to siege duty (e.g. King Derrick, Josephine, Harald in a siege-specific assignment).

---

## MGE Ring Scoring

| Activity | MGE Points |
|---|---|
| Craft 1 ring | 2,000 |
| Copper Dust | 400 |
| Silver Dust | 1,000 |
| Fine Gold | 3,000 |
| Meteor Steel | 20,000 |

Save ring crafting for MGE Day II (Hero Growth day) for maximum point efficiency.

---

## Full Roster Ring Coverage Status — 76 Heroes

This section is the authoritative status check against `AIGA_Hero_Roster_v8.md`'s `Ring Path` field, cross-referenced for this handoff.

### Tier 1 — Fully Verified Tiered Paths (14 heroes)

These heroes have a confirmed T0 → T1 → T2 progression, sourced either from Gustav's in-game roster (this session) or from community hero-build guides (AllClash, aoemobileguides.com):

| Hero | Confirmed Path | Source |
|---|---|---|
| Lu Bu | Daisy → Night Wolf → Radiant Guardian | In-game verified, Gustav S371 |
| Musashi | Daisy → Night Wolf → Lofty Mountain | Gustav's 15-hero lineup, this session |
| Yodit | Clover → Falcon → Skyward Knight | Gustav's 15-hero lineup, this session |
| Hammurabi | Clover → Lion → Tranquil Water | Gustav's 15-hero lineup, this session |
| Cyrus | Tulip → Boar → Messenger of Destruction | Gustav's 15-hero lineup, this session |
| Joan of Arc | Clover → Falcon → Tranquil Water | Gustav's 15-hero lineup, this session |
| Boudica | Tulip → Bear → Everflame Wings | Gustav's 15-hero lineup, this session |
| Guan Yu | Tulip → Bear → Scorching Flame | Gustav's 15-hero lineup, this session |
| Timur | Lily → Deer → Azure Moon | Gustav's 15-hero lineup, this session |
| Yi Sun-Shin | Daisy → Falcon → Tranquil Water | Gustav's 15-hero lineup, this session |
| Bellevue | Clover → Falcon → Everflame Wings | Gustav's 15-hero lineup, this session |
| Henry V | Iris → Badger → Skyward Knight | Gustav's 15-hero lineup, this session |
| Diao Chan | Violet → Steed → (no T2 gathering ring) | Gustav's 15-hero lineup, this session |
| Lagertha | Daisy → Night Wolf (if available) → Tranquil Water | AllClash hero build guide, this session |

Note: Cleopatra and Darius the Great are documented in the M5 stack table above (Sunflower/Laurel → Steed* → none) but share the contested single Steed ring with Diao Chan — see M5 table footnote.

### Tier 2 — Single Unverified Legacy Value Only (62 heroes)

These heroes carry exactly one ring name in the roster's `Ring Path` field (e.g. "Ring of Steed," "Ring of Shark," "Ring of Clover") with no tier progression, no role-based reasoning documented, and no source citation. This is inherited legacy data from before the ring system was properly tiered. **Do not treat these as verified recommendations.** They are placeholders only.

Examples from this category: Hua Mulan (Ring of Steed), Attila the Hun (Ring of Clover), Josephine (Ring of Tulip), Tribhuwana (Ring of Steed), Sun Tzu (Ring of Shark), Charlemagne (Ring of Shark), Ramesses II (Skyward Knight), Mehmed II (Ring of Steed), Zhuge Liang (Ring of Shark), Theodora (Skyward Knight), Suleiman (Everflame Wings), Leonidas I (Ring of Boar), Richard I (Ring of Boar), Ram Khamhaeng (Ring of Steed), Octavian (Ring of Steed), Julius Caesar (Ring of Steed), El Cid (Ring of Night Wolf), Robin Hood (Ring of Falcon), Rani Durgavati (Ring of Steed), Ashoka (Ring of Steed), Frederick Barbarossa (Ring of Boar), Philip IV (Ring of Shark), King Arthur (Skyward Knight), and approximately 40 more — full list in `AIGA_Hero_Roster_v8.md`.

**Two flagged conflicts within this legacy set:**
- El Cid's legacy value is "Ring of Night Wolf" — this directly conflicts with the Lu Bu meta override (Night Wolf is Lu Bu-specific). El Cid's legacy entry needs review and is almost certainly wrong as written.
- King Arthur's legacy value is Skyward Knight on a DPS Lead role — Skyward Knight is a support-oriented ring (reduces own hero damage to boost commander damage). Flagged by Rings thread as "worth a second look" but not yet corrected.

### Tier 3 — Pending / No Data (remaining heroes)

A small number of heroes (e.g. King Derrick, Queen Dido, Queen Seondeok) show `PENDING (Rings/Mounts thread)` rather than even a legacy guess — these are honestly blank rather than carrying bad inherited data, which is the safer state.

---

## Known Gaps

| Item | Issue | Priority |
|---|---|---|
| **62 heroes with legacy single-ring values only** | No tiered T0→T1→T2 path, no role-based reasoning, no source citation. These are NOT verified ring builder recommendations — see Full Roster Ring Coverage Status above. | **Critical — blocks full ring builder rollout in app.py** |
| El Cid's "Ring of Night Wolf" legacy value | Conflicts directly with Lu Bu meta override. Needs review, likely incorrect as written. | High |
| King Arthur's Skyward Knight on DPS Lead role | Flagged as questionable fit (Skyward Knight is support-oriented). Not yet corrected. | Medium |
| Jeweler's Marks exact quantities per upgrade level | Confirmed as upgrade material, quantities unknown | Medium |
| Lord of Eastern Heavens | Ignore tier confirmed by community — monitor if meta shifts | Low |
| Radiant Guardian | F2P ignore confirmed except Lu Bu override — only relevant for Mulan/Belisarius/Lu Bu formations | Low |
| T2 ring stat scaling lv1-50 | Max lv50 values documented, intermediate levels incomplete | Medium |
| Divine Warrior, Celestial Spark, Radiant Thunder | Appear in community sources, not cross-confirmed against calculator or wiki — do not recommend until verified | Medium |

---

## Dev Handoff Notes (app.py / Ring Builder)

**What this file delivers as dev-ready:**
- Complete, verified mechanics for all 35 canonical rings (stats, skill effects, costs, FTP tiers) — ready to hard-code as a ring database
- Ring builder logic (status tags, cascade rules, allocation priority) — ready to implement as the recommendation engine
- 14 heroes with fully verified tiered paths — ready to ship as ring builder output for those heroes specifically
- Confirmed meta overrides (Lu Bu/Night Wolf, Lu Bu/Radiant Guardian, Lagertha/Tranquil Water) — ready to hard-code as exceptions to the general role-matching logic

**What this file does NOT deliver:**
- A complete 76-hero ring recommendation set. 62 heroes only have a single legacy ring value with no tier path or sourcing — treating these as ring builder output would surface unverified guesses as confident recommendations to end users, which violates the project's core "never fabricate named game data" rule.

**Recommended app.py behaviour for the 62 unverified heroes:** if a player queries one of these heroes, return the legacy single value labelled clearly as `[unverified legacy data — community tier list cross-check recommended]` rather than presenting it as a confirmed T0/T1/T2 stack. Do not silently upgrade these to the same display format as the 14 verified heroes.

**Next step for full rollout:** Rings thread to work through the 62-hero backlog using the same method applied this session — confirm hero type/role/skills first (cross-check Hero Roster v8), then apply the role-to-ring-tier logic documented in this file, citing AllClash/aoemobileguides.com/in-game verification per hero. El Cid and King Arthur should be prioritised given the flagged conflicts.

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

---

*AIGA Rings Reference v2.2 | Network Grey | June 2026*
*Sources: Theria Games calculator, Fandom Wiki, in-game verification (S371), FTP tier list (community YouTube), AllClash, aoemobileguides.com*
*Not affiliated with TiMi Studio Group, Level Infinite, Proxima Beta Pte. Limited, Microsoft, or Xbox Game Studios.*

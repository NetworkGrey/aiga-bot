# Age of Empires Mobile — Mount System
## AIGA Knowledge Base | heroes/AIGA_Mount_System.md
## Status: DEFINITIVE — trait roster, temperament mapping, breeding mechanics, adornment data model, and roster schema requirements confirmed in-game
## Version: 6.0 | Supersedes all prior mount KB versions | Prepared for Dev Thread incorporation into app.py
## Sources hierarchy: in-game verification (Gustav, S371 N3W) > AIGA_Hero_Roster_v7.md (live roster cross-check) > Magedd breeding guide (aoem.vercel.app/guide) > community video transcripts (Mr Sneaky, Timmy, Karmani, Sam Wise, Titobods) > aoem-calculator (MIT) > community guide V2
## v6.0 changes: Cyrus the Great corrected to Warbred/Valor (was stale Fearless/Tidebreaker in some exports); King Arthur confirmed Warbred/Overpower; Lagertha explicitly flagged as KNOWLEDGE GAP (no temperament/trait confirmed anywhere — do not infer or guess); `mount_trait_2` schema requirement formalized as a first-class data model rule (Section 4a) for confirmed dual-trait-required heroes (Josephine, Bellevue); Timur and Henry V resolved to single-trait Lifesaver (cross-pool chase abandoned, not a compromise)
## v5.0 changes: adornment data model corrected (form/orientation/special-effect are 3 separate fields, not one); hero role → orientation lookup table added; M5 gathering-adornment exception added; practical breeding decision framework added (real-world inventory triage, not just theoretical target builds)

---

## 1. Base Attributes

Every mount carries base attributes that stack directly with hero attributes. There are 4 attribute types:

| Attribute | Effect |
|---|---|
| Might | Increases troop physical damage |
| Strategy | Increases troop tactical damage |
| Armor | Increases mounted troops' damage resistance |
| Siege | Increases siege effectiveness |

**Critical compatibility rule:** a trait must match an attribute the mount has to fully apply. A Might-damage trait on a mount with no Might attribute loses the attribute-scaling component of its bonus. Always verify attribute/trait compatibility before committing a mount to a hero.

---

## 2. Mount Quality Tiers

| Quality | Rarity | Colour | Base attributes | Attribute range (in-game) |
|---|---|---|---|---|
| Courser | Common | Blue | 2 | +2 to +5 |
| Destrier | Epic | Purple | 2 | +5 to +10 |
| Skywing | Legendary | Gold | 2 | +10 to +18 |
| Celestial Charger | Mythical | Orange/Red | 3 | +18 to +25 |

**Key rules:**
- Offspring never exceed the attribute range ceiling of their quality tier
- Epic mounts require hero lv40+ to equip. Common mounts can be equipped at any hero level
- No mount equipped is always worse than any mount, even with temperament or trait mismatch
- **Trait value is independent of mount quality.** A Common mount can roll a maximum-value trait; a Mythical mount can roll a minimum-value trait. Quality only gates the attribute range, not trait quality
- Up to 3 traits possible on a single mount (single/double/triple — see Section 5)

---

## 3. Temperament System — 7 Confirmed Temperaments

Temperament controls two independent things: (a) the inheritance-vs-mutation ratio, and (b) for the 4 specialized temperaments, which trait pool a mutation is biased toward.

| Temperament | Type | Inheritance / Mutation rate | Trait pool bias |
|---|---|---|---|
| Warbred | Specialized | Standard | 80.19% chance of landing in the Might Damage pool on mutation |
| Alert | Specialized | Standard | 80.18% chance of landing in the Strategy Damage pool on mutation |
| Fearless | Specialized | Standard | 78.95% chance of landing in the Universal pool on mutation |
| Protective | Specialized | Standard | 80.17% chance of landing in the Healing pool on mutation |
| Spirited | Control | 45% inheritance / 55% mutation | None — generates new random traits from any pool |
| Docile | Control | 55% inheritance / 45% mutation | None — favours preserving existing parent traits |
| Mischievous | Control | 50% inheritance / 50% mutation | None — neutral, no strategic bias |

**Important naming note:** "Fearless" is both a temperament name AND one specific trait within the Universal pool. These are not the same thing — the temperament gives a 78.95% chance of landing somewhere in the 15-trait Universal pool; the Fearless trait itself (solo battle damage reduction) is just one member of that pool.

**Temperament inheritance odds (same-temperament breeding):**
- 30% offspring inherits father's temperament
- 30% offspring inherits mother's temperament
- 40% random temperament

**Different-temperament breeding:** higher probability of a fully random offspring temperament (exact split not numerically confirmed — treat as worse odds than same-temperament breeding for targeting a specific outcome).

**Never mix temperaments when targeting a specific specialized trait pool.** Same x same is the only reliable way to bias toward Warbred/Alert/Fearless/Protective trait pools.

**Control temperament usage:**
- Spirited: use to generate a trait you don't currently have anywhere in your mount roster (Strategy 1, Section 8)
- Docile: use to preserve and lock in a trait you already have (Strategy 2, Section 8)
- Mischievous: no specific strategic use — breed out or use as filler when no other pairing is available

---

## 4. The 30 Confirmed Traits

All 30 traits below are confirmed via direct in-game screenshot (Gustav, S371). This is the canonical list — supersedes all community guide naming.

### Might Damage Traits (5) — Warbred pool

| Trait | Range | Effect |
|---|---|---|
| Overpower | 2%–10% | +Might damage from active skills |
| Gallant | 2%–10% | +Might damage from secondary strike skills |
| Valor | 2%–10% | +Might damage from passive skills |
| Phalanx Breaker | 2%–10% | +Might damage from turn-based skills |
| Fierce | 4.5%–22.5% | +Normal attack damage |

### Strategy Damage Traits (4) — Alert pool

| Trait | Range | Effect |
|---|---|---|
| Spiritbond | 2%–10% | +Strategy damage from active skills |
| Stratagem | 2%–10% | +Strategy damage from secondary strike skills |
| Cunning | 2%–10% | +Strategy damage from passive skills |
| Battlemaster | 2%–10% | +Strategy damage from turn-based skills |

*Cunning and Battlemaster currently have no heroes using passive/turn-based Strategy damage in the active meta — treat as breeding fodder until new heroes release. [verify as new heroes launch]*

---

## 4a. Data Model Requirement — Single Trait Field Is Insufficient For Some Heroes

**For Dev Thread:** `app.py` and any roster schema (including `AIGA_Hero_Roster_v7.md`) must support an optional second trait field per hero — `mount_trait_2` — in addition to the primary `mount_trait`. This is not a nice-to-have; a small but confirmed set of heroes have two traits that are both mandatory simultaneously, drawn from two different temperament pools, and a single-value field cannot represent their correct build without silently dropping half of it.

**Confirmed heroes requiring `mount_trait_2`:**

| Hero | mount_temp (primary) | mount_trait | mount_trait_2 | Why both are mandatory |
|---|---|---|---|---|
| Josephine | Warbred | Gallant | Lifesaver | Gallant supplies offense (secondary strike Might damage), Lifesaver supplies defense (recovery-triggered damage reduction). Neither alone represents her confirmed build. |
| Bellevue | Warbred | Gallant | Lifesaver | Identical combo and reasoning to Josephine. |

**Heroes where a cross-pool double was considered but explicitly resolved to a single trait (do NOT add `mount_trait_2` for these):**

| Hero | Resolution |
|---|---|
| Timur | Lifesaver alone. Fierce (Warbred) was a theoretical secondary want, but his negligible damage output means it adds no real value — chasing it is not recommended. |
| Henry V | Lifesaver alone. Same reasoning — low-priority hero, single trait is the complete, correct answer for him. |

**Gathering heroes are a related but separate case** — they need two traits (Swift + Abundance, optionally + Full Stores) but from a pool with no temperament bias at all, not a cross-pool conflict. See Section 12, M5 table, and the dedicated handling note below. Recommend representing gathering heroes with `mount_temp = "GATHERING"` (a literal flag value, not a real temperament) rather than forcing Spirited or Docile into that field, since neither is the hero's permanent state — it's a two-phase breeding process, not a static property.

**Implementation guidance:** `mount_trait_2` should default to null/empty for all heroes except the confirmed list above. Do not populate it speculatively for heroes with two "good" traits unless this KB explicitly documents both as mandatory — most heroes have one primary trait and several lower-priority alternatives, which belong in the existing trait-priority arrow notation (e.g., "Overpower → Army Sunder"), not in a second mandatory field.

### Universal Traits (15) — Fearless pool

These work regardless of Might/Strategy attribute, making them the most versatile and valuable trait category.

| Trait | Range | Effect |
|---|---|---|
| Thunderbolt | 2.7%–13.5% | +Critical strike damage |
| Army Sunder | 1.8%–9% | +All damage dealt (active, passive, secondary strike, turn-based, normal attack — everything) |
| Dustbane | 2%–10% | +Solo battle damage (PvP, not effective vs PvE/tribes) |
| Tidebreaker | 2%–10% | +Group/rally battle damage (PvP) |
| Fearless (trait) | 0.7%–3.5% | −Solo battle damage received (PvP) |
| Bastion | 0.7%–3.5% | −Group/rally battle damage received (PvP) |
| Iron Ridge | 0.6%–3% | −Might damage received |
| Tactician | 0.6%–3% | −Strategy damage received |
| Bedrock | 0.48%–2.4% | −All damage received |
| Peacemaker | 1%–3% | −Active skill damage received |
| Blade Sever | 0.6%–3% | −Secondary strike damage received |
| Entrenchment | 0.6%–3% | −Passive skill damage received |
| Stalwart | 1%–3% | −Turn-based skill damage received |
| Perseverance | 1.2%–6% | −Normal attack damage received |
| Siege | 3%–10% | +Mounted hero siege effectiveness (siege battles only) |

**Offence/defence trait mirror** — every offensive skill-type trait has a matching defensive counterpart:

| Skill type | Offence trait (damage dealt) | Defence trait (damage received) |
|---|---|---|
| Active skill | Overpower (Warbred) | Peacemaker |
| Secondary strike | Gallant (Warbred) | Blade Sever |
| Passive skill | Valor (Warbred) | Entrenchment |
| Turn-based skill | Phalanx Breaker (Warbred) | Stalwart |
| Normal attack | Fierce (Warbred) | Perseverance |
| All damage | Army Sunder | Bedrock |
| Solo battle | Dustbane | Fearless (trait) |
| Rally/group battle | Tidebreaker | Bastion |
| Might only | — | Iron Ridge |
| Strategy only | — | Tactician |

### Healing Traits (3) — Protective pool

| Trait | Range | Effect |
|---|---|---|
| Lifesaver | 0.96%–4.8% | −Damage taken for 3s after the mounted hero causes a recovery effect |
| Renewal | 2.3%–11.5% | +Healing effect from the mounted hero |
| Healing Armor | 0.8%–4% | +Healing received by your troop |

### Resource Gathering Traits (3) — separate pool, no temperament bias

| Trait | Range | Effect |
|---|---|---|
| Swift | 1%–10% | +Gathering speed from mounted hero's troop |
| Abundance | 1%–10% | +Resources gathered by mounted hero's troop |
| Full Stores | 2%–8% | +Mounted troop's resource load capacity |

**Gathering traits do not mix with combat traits** — confirmed they sit in a separate mutation pool from the 27 combat traits. None of the 7 named temperaments bias toward this pool specifically; use Spirited to generate, Docile to preserve, same as any other trait-hunting process.

---

## 5. Inheritance Mechanics

### Three ways offspring acquire characteristics

| Mode | Base rate | Modified rate |
|---|---|---|
| Inheritance | 50% | 55% with Docile parent(s) |
| Mutation | 50% | 55% with Spirited parent(s) |
| Lineage Ascension (quality upgrade) | 10–50% depending on combination | See Section 6 |

### Number of traits in offspring (base rates)

| Outcome | Base probability |
|---|---|
| 1 trait | 40% |
| 2 traits | 60% |

These base rates shift significantly based on parent trait count and quality:

| Parent configuration | Single trait % | Double trait % | Triple trait % |
|---|---|---|---|
| Both parents 0 traits | 100% | 0% | 0% |
| One parent has a trait, other has none | 100% (single only — double impossible) | 0% | 0% |
| Both parents 1 trait | 90% | 10% | 0% |
| One parent 1 trait + one parent 2 traits | 40% | 60% | 0% |
| Both parents 2 traits (lower quality) | 44% | 51% | 5% |
| Both parents 2 traits (higher quality) | 25% | 70% | 5% |

Triple trait chance appears fixed at 5% regardless of parent configuration once both parents carry 2 traits. Up to 3 traits per mount is the confirmed maximum (requires Orange/Mythical quality for the 3rd attribute slot, though traits and attributes are tracked separately).

### Factors influencing inheritance outcomes

- **Parent temperament:** Docile increases inheritance, Spirited increases mutation, specialized temperaments (Warbred/Alert/Fearless/Protective) bias mutation toward their pool
- **Parent attributes:** offspring attributes correlate with parents — if no parent has Might, offspring will not have Might
- **Parent traits:** only traits possessed by at least one parent can be inherited (you cannot inherit a trait neither parent has — only mutation can introduce a wholly new trait)
- **Parent quality:** higher quality parents give better odds of quality-ascending offspring (see Section 6)

### Trait value scaling

Trait percentage values are randomly rolled within their range at the moment of mutation/inheritance, and can improve across generations. A 2% Overpower roll can become 10% Overpower through repeated breeding of mounts that already carry it, particularly using Docile to lock in inheritance while re-rolling the value upward.

---

## 6. Quality (Lineage) Ascension

Breeding two mounts has a chance to produce offspring of higher quality than either parent.

| Parent pairing | Ascension chance | Possible outcomes |
|---|---|---|
| Common x Common | 20% | Ascend to Epic |
| Common x Epic | 50% | Either Common or Epic |
| Epic x Epic | 10% | Ascend to Legendary |
| Epic x Legendary | 50% | Either Epic or Legendary |
| Legendary x Legendary | 1% | Ascend to Mythical (Celestial Charger) |
| Mythical x Legendary | 100% | Mythical retained |

**Epic x Epic cannot skip to Legendary directly except via the 10% ascension roll — there is no guaranteed path.** Mythical (Celestial Charger) can only be produced from two Legendary parents, at a 1% rate per breed.

---

## 7. Breeding Mechanics — Core Rules

- Both parent mounts are consumed in breeding — there is no way to breed without losing both parents
- Always keep 2–3 backup copies of any mount carrying a valuable trait before using it to breed, since the original is destroyed regardless of outcome
- Maximum 100 breedings per mass-breeding session
- Mass breeding consumes Common mounts first when seeking ascension — lock any mount you want to keep before running mass breeding
- Breeding any pair (even two traitless mounts) earns Insight Points, spent in the Animal Research tree

### Quality matching for breeding eligibility

Mounts can only breed with mounts of identical quality going into the breed (the ascension chance above determines what comes OUT, not what goes in). Common x Common, Epic x Epic, Legendary x Legendary, Mythical x Legendary are all valid input pairings.

---

## 7a. Practical Decision Framework — Working With an Existing Mount Pool

Sections 5–8 describe breeding mechanics and idealized target builds. In practice, most players are reconfiguring an existing, accumulated mount inventory rather than breeding from zero toward a theoretical ideal. This section codifies the decision rules used to triage a real inventory against target builds — this is the logic the webapp should run when a user says "here's what I have, what should I equip."

### Rule 1 — Always check existing inventory before recommending a fresh breed

Before suggesting any breeding ladder, ask whether the user already has a mount matching or partially matching the target trait, anywhere in their pool, on any hero or unequipped. A spare mount sitting unused is always faster than breeding one from scratch, regardless of how "clean" the breeding path looks on paper.

### Rule 2 — Temperament is irrelevant for equipping; only Trait and Attribute matter

Temperament only influences breeding *outcomes* (which trait pool a mutation is biased toward). It has zero effect on what an already-finished mount does once equipped. A mount with the correct trait and attribute is fully functional regardless of whether it is Warbred, Spirited, Docile, Mischievous, or any other temperament. Do not reject or downgrade a candidate mount on temperament grounds — only check Trait (does it match the hero's needs) and Attribute (does it correlate, where the trait requires it).

This rule resolves a common false flag: a user reporting "I have Overpower but it's not Warbred" is not a problem requiring a re-breed — it's a ready-to-equip mount.

### Rule 3 — Double trait with one irrelevant trait beats single trait with the relevant trait, in essentially all cases

If Trait A is what the hero needs and Trait B is unrelated/inert for that hero's kit, a mount carrying (Trait A + Trait B) is equal-or-better than a mount carrying (Trait A) alone — the irrelevant second trait costs nothing, it simply does not contribute. Always prefer the double-trait option in a side-by-side comparison unless the second trait is actively counter-productive (rare — most traits are neutral-or-better even when off-theme; no traits in the confirmed roster currently have a documented negative side effect).

### Rule 4 — Cross-pool double traits are a known hard case; do not force them

Some heroes have confirmed builds requiring two traits from two different specialized temperament pools (example: Timur and Henry want Lifesaver [Protective] but their Fierce-adjacent Warbred stock is the wrong pool; Bellevue wants Gallant [Warbred] + Lifesaver [Protective] together). These cross-pool double traits take meaningfully longer to breed than same-pool double traits, because there is no single temperament that biases toward both pools simultaneously.

When a hero needs a cross-pool double trait:
1. Default recommendation: accept a single-trait mount with whichever trait matters most for that hero's actual kit usage (commonly the Protective/recovery trait for low-damage support heroes, since the combat trait contributes little to a hero who barely deals damage).
2. Only pursue the full cross-pool double trait if the hero is high enough priority (march lead) to justify the extra breeding investment, or if a partial match already exists in inventory (Rule 1).
3. Do not block other, higher-priority breeding lines to chase a cross-pool double trait on a low-priority hero.

### Rule 5 — Breeding two mounts that already share the same trait biases toward keeping that trait, not generating a new one

If the goal is to **change** a mount's trait (e.g., it currently has Fierce, the target is Overpower), breeding it against another mount that also has Fierce increases the odds of inheriting Fierce again, working against the goal. To mutate toward a new trait, pair the mount with a different trait (or a traitless mount) of the same temperament instead.

If the goal is to **lock in or upgrade the value of an existing trait** (not change it), breeding two mounts that already share that trait is correct — same-trait pairing maximizes inheritance odds for that specific trait and can push its rolled percentage value upward across generations.

### Rule 6 — Breeding always consumes both parents; weigh the downside before committing valuable duplicates

When a user has two mounts that are both already valuable (e.g., two double-trait mounts with the exact same two traits), breeding them together is a genuine gamble: best case is a quality-ascended or value-optimized upgrade, worst case is losing both in exchange for a worse single-trait result. This is a reasonable gamble for low-priority heroes (low cost if it goes wrong) and a riskier one for a march lead's only good mount (where losing the trait entirely has real cost). Always flag this trade-off explicitly rather than recommending the breed unconditionally — let the user decide based on the hero's priority and their risk tolerance.

### Rule 7 — Attribute correlation matters for damage-type traits, not for proc-based traits

Damage-percentage traits (Overpower, Valor, Fierce, Thunderbolt, Army Sunder, etc.) scale off the mount's base attribute (Might or Strategy) — equipping one without the matching attribute still applies the trait's flat percentage bonus, but loses the attribute-stacking component. Proc/trigger-based traits like Lifesaver do not require attribute correlation at all, since they trigger off an event (a recovery effect) rather than scaling a stat — this gives much more flexibility in which mount to use for support-trait hunts.

### Rule 8 — Priority order for triage across a full roster

When working through multiple heroes/marches in one session: fix march leads first (highest combat impact), then march supports, then defer cross-pool hard cases (Rule 4) and gathering-role heroes (Section 10a — lower stakes since adornment/mount investment there caps out earlier) to last.

---

## 8. Breeding Strategies

### Strategy 1 — Generate a specific trait you don't have (mutation-led)

1. Use Spirited temperament parents — 55% mutation probability to generate a new random trait
2. Once you've generated something in roughly the right pool, switch to the matching specialized temperament (Warbred for Might, Alert for Strategy, Fearless for Universal, Protective for Healing)
3. Breed specialized x specialized until the specific desired trait lands — at 80%+ pool bias, this converges in a handful of attempts
4. **Critical check before starting:** ensure parent attributes match the trait type you're hunting. Don't chase a Might trait if no parent in the line carries the Might attribute.

### Strategy 2 — Preserve and improve an existing trait (inheritance-led)

1. Use Docile temperament — 55% inheritance probability locks in parent traits more reliably
2. Breed the trait-carrying mount with another Docile mount (ideally also carrying the same trait, to push toward double-trait consolidation)
3. Repeat to push the trait's rolled value upward across generations
4. Always keep backup copies before using a good mount in this process — it will be consumed

### Strategy 3 — Build a perfect mount (long-term, multi-generation)

1. **Generations 1–2:** Spirited + specialized temperament combo to generate the traits you need (Strategy 1)
2. **Generations 3–4:** Switch to Docile to consolidate multiple good traits onto fewer mounts, combining mounts that each carry one good trait
3. **Generation 5+:** Breed your best mounts together, push for lineage ascension, maximise both attribute and trait values
4. This process realistically takes 1–3 weeks and 15–25+ breeds for a fully optimised double-trait Legendary/Mythical mount with maxed trait values

### Worked example — Universal damage mount (Fearless / Thunderbolt + Army Sunder)

| Phase | Goal | Method | Estimated breeds | Estimated time |
|---|---|---|---|---|
| Phase 1 | Obtain Thunderbolt | Fearless x Fearless mutation | 2–5 | 1–2 days |
| Phase 2 | Add Army Sunder (double trait) | Fearless x Fearless with one Thunderbolt parent | 3–6 | 1–3 days |
| Phase 3 | Optimise values to max range | Breed best mounts together repeatedly | 10+ | 1–2 weeks |
| Total | — | — | 15–21 | 1–3 weeks |

**Optional Phase 4 — third trait (requires Mythical/Orange quality, 3-attribute slot):** add a defensive Universal trait like Bedrock or Iron Ridge for additional resilience. Very difficult, multiple weeks, marginal additional gain (2–3% additional damage reduction).

---

## 9. Animal Research Centre

### Tree structure

Two sides, funded by Insight Points earned from every breeding action (junk breeds included).

**Left side (breeding efficiency):**
- Keen Eye for Steeds / Natural Advantage — higher chance of superior base attributes per breed
- Legacy Inheritance — inherited traits more likely to roll high values
- Exceptional Talent — mutated traits more likely to roll high values
- Bloodline Stability — unlocks the Adornment Workshop, plus Insight Point gain bonus per breed
- Insight Advancement — Insight Point gain bonus per breed

**Right side (permanent combat stats):**
- Per troop type column (SW/PIK/CAV/ARC): attack %, defence %, health %
- Stats are permanent and passive once unlocked — apply to any hero of that troop type with any mount equipped, regardless of mount quality
- Example: 5/10 Cavalry column gives +7.5% attack, +7.5% defence, +2.25% health per mounted Cavalry hero
- With 3 heroes mounted on that troop type: effectively ~22% attack and ~22% defence bonus over an unmounted formation

### Optimal research path

**Phase 1 — minimums (always do first):**

| Milestone | Why |
|---|---|
| Bloodline Stability lv1 | Unlocks adornment slots — non-negotiable |
| Bloodline Stability lv3 | +Insight Point gain per breed |
| Insight Advancement lv3 | +Insight Point gain per breed |
| Remaining left-side nodes lv1 | Minimum unlock requirement to access deeper nodes |

**Phase 2 — right side push (after Phase 1):** focus on primary march troop type first — unlock 1/10 on secondary troop types to open deeper nodes, then push the primary troop type to 5/10+ before spreading further investment.

**Why right side over left side after minimums:** the left side only improves breeding odds — breeding outcomes remain probabilistic regardless of investment. The right side gives guaranteed, permanent stats the moment any mount is equipped, irrespective of quality. A Common mount still triggers full right-side bonuses. The cumulative effect across 3 mounted heroes (~22% attack/defence) outweighs marginal breeding-odds improvements at this stage of investment.

### Key rules

- Breed junk/traitless mounts deliberately to farm Insight Points — never let a breeding pair go to waste
- Mass breeding Common mounts toward Epic ascension is a valid simultaneous Insight-farming + ascension method (lock anything you want to keep first)
- Right-side stats apply per mounted hero of that troop type — they scale with how many heroes of that type you have mounted, not a flat once-per-account bonus

---

## 10. Adornment System

Unlocked via Animal Research (Bloodline Stability). Each mount can equip one adornment, chosen as either the Attack or Defense form for that troop type. Cannot equip both simultaneously on one mount.

### Adornment forms by troop type

| Troop | Attack form | Base stats | Defense form | Base stats |
|---|---|---|---|---|
| Swordsmen | Swift Blade | SW attack, SW health, hero skill damage | Mystic Mirror | SW defence, SW health, troop damage taken reduction |
| Pikemen | Guiding Star | PIK attack, PIK health, hero skill damage | Stalwart Shield | PIK defence, PIK health, troop damage taken reduction |
| Cavalry | Unyielding Iron | CAV attack, CAV health, hero skill damage | Sacred Lily | CAV defence, CAV health, troop damage taken reduction |
| Archers | Piercing Arrow | ARC attack, ARC health, hero skill damage | Eagle's Blessing | ARC defence, ARC health, troop damage taken reduction |

Both forms of the same troop type draw special effects from the same shared pool — the form choice only affects base stats, not which special effects are available.

### 10a. Gathering Heroes (M5) — Adornment Exception

**The "any equipment beats no equipment" principle does NOT extend to adornments on gathering heroes, and this is a deliberate exception, not an oversight.**

The "no mount is always worse than any mount" rule (Section 2) applies to mounts because mount base attributes and traits (specifically Swift, Abundance, Full Stores) are confirmed gathering-relevant. Adornments are a different equipment slot layered on top, and their value proposition does not carry over:

- The base stats on every adornment form (attack/health or defence/health/damage-taken-reduction) are combat stats. Gathering heroes are not in combat during their gathering role — these stats are inert for that role.
- Every confirmed special effect in the current pool (Resistance, Natural Selection, Thunder, Wavebreaker, Boiling Blood, Lightning Strike, Resourcefulness, etc. — see Section 11) is combat-triggered: battle start, skill activation, critical strike, double attack state. None reference gathering speed, resource yield, or node interaction.
- Conclusion: an adornment on a gathering hero is closer to **neutral** than beneficial. It does not actively harm the hero, but it also does not meaningfully improve gathering performance the way an equipped mount with the right trait does.

**Practical guidance:** do not prioritize Meteorite Steel, Chalcedony, or Raw Iron spend on M5 adornments. If resources are genuinely surplus with nothing better to use them on, there's no harm in equipping one — but it should never compete against M1–M4 adornment investment, where base stats and special effects are doing real work. If a hero rotates between gathering (M5) and combat duty (e.g., Darius rotating to M3 during peace config), reassess the adornment as a combat decision only during the combat-assigned period.

### Crafting, dismantling, upgrading

- Craft cost: 10 Meteorite Steel per adornment
- **First special effect re-roll after crafting is free** — always use it before spending Chalcedony on further re-rolls
- Dismantle returns: 5 Meteorite Steel (50% recovery)
- Resetting an adornment (unequip, then reset) fully refunds Raw Iron spent on intensification
- Upgrade levels 1–60 using Raw Iron for levels 1–20, then **Refined Iron** for levels 21–60 *[two-tier material system — verify exact level breakpoint in-game]*

### Adornment upgrade level bonus thresholds

| Level range | Attack adornments | Defence adornments |
|---|---|---|
| 1–20 | Attack bonus 1%+ | Defence bonus 1%+ |
| 20–40 | Health bonus 0.5%+ | Health bonus 0.5%+ |
| 40–60 | Skill damage increase 0.5%+ | Skill damage taken reduction 0.5%+ |

### Special effect re-roll / rarity system

- Special effects upgrade through rarity tiers: Common → Uncommon → Rare → Epic (purple) → Legendary (gold) → Mythical (red)
- First tier upgrade is 100% success
- Higher tiers have increasing failure chance, **and confirmed downgrade risk** — a special effect can roll backward to a lower tier on a failed upgrade attempt
- At Mythical tier, a special effect's value is substantially higher than base (example observed: a skill damage special effect rose from ~7% at base to ~18% at Mythical)

### Data Model — Three Separate Fields, Not One

**Critical correction (confirmed this session against live builder data):** adornments are commonly mis-modelled as a single flat field. They are actually three independent fields that must be tracked separately:

| Field | What it is | Values |
|---|---|---|
| Troop Type | Fixed by the hero's current march assignment | SW / PIK / CAV / ARC |
| Form | The physical item equipped — determines base stats and locks orientation | One of 8 confirmed names (see table below) |
| Special Effect | The rolled bonus on that item — independent of form, shared pool per troop type | Resistance, Natural Selection, Thunder, etc. |
| Effect Rarity/Level | Affects the magnitude of the special effect | Common → Uncommon → Rare → Epic → Legendary → Mythical |

**A Form is never itself an orientation choice and a Special Effect simultaneously** — these are different slots on the same item, not alternative selections. A live builder UI that offers a single dropdown mixing form names (Swift Blade, Guiding Star) with special effect names (Thunder, Resistance) is structurally incorrect and will silently fail to ever offer Resistance as an option if Resistance isn't in that merged list — this exact bug was identified and confirmed in the existing AIGA builder.

### Form Reference — Troop Type and Orientation (confirmed in-game)

| Troop Type | Attack Form | Defense Form |
|---|---|---|
| Swordsmen | Swift Blade | Mystic Mirror |
| Pikemen | Guiding Star | Stalwart Shield |
| Cavalry | Unyielding Iron | Sacred Lily |
| Archers | Piercing Arrow | Eagle's Blessing |

Orientation is fixed by which Form is chosen — a hero cannot equip a Cavalry-only form on a Pikemen hero, and the Attack/Defense status is a fixed property of each Form name, not a separate toggle.

### Which Orientation to Use — Hero Role Lookup

**Precedence order (apply top to bottom, first match wins):**

1. **Archer, any role → always Defense.** Overrides all other logic. Archers carry the highest attack stat in the game and the least inherent damage reduction — survival outweighs further offence regardless of whether the hero deals damage.
2. **Pure support / no meaningful damage output → Defense.**
3. **Damage-dealing lead or damage-dealing support → Attack.**
4. **Gathering hero (M5 role) → see Section 10a, adornments are low-value here regardless of orientation.**

| Hero type | Recommended form | Reason |
|---|---|---|
| SW DPS lead (Miyamoto, Lagertha, Yodit) | Swift Blade (Attack) | Hero skill damage increase directly benefits them |
| SW support (Tribhuwana, Scipio) | Mystic Mirror (Defense) | No damage to boost — pure march-wide stats |
| PIK DPS lead (Cyrus, Boudica, Leonidas) | Guiding Star (Attack) | Hero skill damage boost |
| PIK support (Mansa Musa, Barbarossa, Joan of Arc) | Stalwart Shield (Defense) | Support role, already tanky march |
| CAV DPS (Lu Bu, Zhao Yun, El Cid, Guan Yu) | Unyielding Iron (Attack) | Primary damage dealers |
| CAV support (Timur, Attila) | Sacred Lily (Defense) | Support role — little/no damage in kit |
| ARC, any role (Yi Sun-Shin, Bellevue, Mulan, Henry) | Eagle's Blessing (Defense) | Archer override — applies even to active damage leads |

**Dual-troop-type hero caveat:** heroes with two valid troop types (e.g., Josephine [ARC/SW], Saladin [CAV/ARC], Ramesses II [SW/ARC]) do not have a fixed orientation — it depends entirely on which troop type they are *currently* deployed as in the active march. The builder must read the hero's current march assignment's troop type before applying this lookup, not assume a static value from the hero's name alone. A wrong default here (assuming one troop type without checking) will misclassify any hero with multiple valid types.

**Heroes with unconfirmed role classification** (no KB-confirmed damage/support profile as of this version): Sejong the Great, Harald III, Constantine, Otto, and newer/lower-tier roster additions (Gao Meng, Wu Wei, Kaso, Yuan Xia, Axel, Narses, Nino, Luki, Leo). The builder should flag these as "unclassified — verify role before recommending orientation" rather than guessing a default, since a false-confidence wrong answer is worse than an honest gap.

---

## 11. Adornment Special Effects

Special effects are rolled separately from the base adornment form, via the Chalcedony re-roll system. The same pool of special effects is shared between the Attack and Defense form of a given troop type.

**Core ranking principle:** consistent, unconditional effects beat one-time or hard-to-trigger conditional effects. Resistance and Natural Selection rate highest across nearly every source because they trigger automatically with no precondition.

**75% damage reduction cap applies to special effects too** *[exact cap unverified in-game — community estimates range 65–75%]*. Once a march's total damage reduction (rings + traits + adornments + skills combined) approaches this cap, further damage-reduction effects give diminishing or zero return — switch slot allocation to damage-increase effects instead.

### Universal special effects

| Special effect | Trigger | Effect | Rating |
|---|---|---|---|
| Resistance | Battle start, 18s window | First 3 instances of skill damage taken reduced ~12.5% each; troop damage taken reduced ~8.5% for 18s; halves after 18s; resets each new engagement | Must-have on every march, every troop type |
| Natural Selection | Every 9s, 75% chance (independent rolls) | 75% chance to reduce commander damage taken AND 75% chance to increase commander damage dealt — both can trigger simultaneously | Must-have for support-form (defensive) Swordsmen adornments |

### Swordsmen special effects

| Special effect | Rarity | Trigger | Effect | Rating | Best on |
|---|---|---|---|---|---|
| Natural Selection | Common | Every 9s | See universal | Must-have | Mystic Mirror — Tribhuwana, Scipio |
| Resistance | Common | Battle start | See universal | Must-have | Any SW adornment |
| Wavebreaker | Common | Hero activates signature active skill | +flat Might per stack (up to 3 stacks), +10% active skill damage at full stack | High | Swift Blade — SW Might active leads |
| Calculation | Common | Same as Wavebreaker | Same mechanic, Strategy stat | High | Swift Blade — SW Strategy active leads |
| Blazing Edge | Rare | Hero activates signature active skill, 45% chance | High burst damage on first hit, once every 3s | Good | Swift Blade — Miyamoto, Lagertha |
| Starlink | Rare | Same trigger | Same mechanic, Strategy damage | Good | Swift Blade — Ramesses, Sun Tzu |
| Radiance | Rare | King Arthur specific | 1.45x multiplicative damage | Situational | King Arthur only |
| Mutual Aid | Common | After recovery | +healing effect, requires heal to trigger | Below average | — |
| Charge | Common | First 3 signature active skill uses only | Damage increase | Poor | One-time-effective heroes use skills far more than 3 times per fight |

### Pikemen special effects

| Special effect | Rarity | Trigger | Effect | Rating | Best on |
|---|---|---|---|---|---|
| Resistance | Common | Battle start | See universal | Must-have | Any PIK adornment |
| Resourcefulness | Common | Every 6s, 60% chance (independent) | +flat Strategy AND +Strategy skill damage — both can trigger | Must-have for strategy PIK | Belisarius, A-Shocker, Elizabeth I |
| Secondary Strike | Rare | Hero deals counterattack damage, 65% chance | Extra damage, once every 3s | Must-have for Warrior PIK | Cyrus, Boudica — counterattack passive leads |
| Insight | Common | Troop takes skill damage | Reduces subsequent damage from that skill | High | Counters skill-heavy cavalry spam |
| Stacked Armor | Common | Battle start, every 3s, 3 stacks max | ~2.5% troop damage reduction per stack | Good | Alternative to Resistance |
| Gambit | Rare | Hero deals skill damage, 65% chance | Extra damage OR strategy attribute bonus | Average | Resourcefulness is generally better |
| Blood Debt | Common | Condition-based | Damage effect | Situational | — |
| Guard Formation | Common | Allied troops in range | +allied armor | Poor | — |

### Cavalry special effects

| Special effect | Rarity | Trigger | Effect | Rating | Best on |
|---|---|---|---|---|---|
| Resistance | Common | Battle start | See universal | Must-have | All CAV |
| Boiling Blood | Rare | Hero deals critical strike, on trigger | Recover units + secondary strike skill damage boost | Must-have | Lu Bu |
| Rally | Common | After 12 normal attacks | Reduces caster's skill damage, boosts other heroes' skill damage, stacks | High | Non-damage supports (Timur, Attila) buffing a damage lead |
| Chain Slayer | Rare | After 3 customisable secondary strike/active skills | Boosts next hero's skill damage, stacks | High | Belisarius, Hannibal |
| Lone Valor | Rare | Only one combat target present | Reduce damage taken + increase commander damage every 9s | Situational — untested for rally validity | Potential S-tier for Lu Bu if rally counts as single target |
| Cloud Piercer | Common | Every 9s | Bonus damage if target commander has lower Might | Niche | Whale-level play |
| Shadow Chaser | Common | Skill trigger | Damage effect | Below average | Tested — does not beat Resistance |
| Intimidation | Common | One target only | Damage increase | Below average | — |

### Archer special effects

| Special effect | Rarity | Trigger | Effect | Rating | Best on |
|---|---|---|---|---|---|
| Resistance | Common | Battle start | See universal | Must-have | All ARC |
| Lightning Strike | Rare | While in double attack state | +normal attack and secondary strike damage | Must-have | Mulan, Bellevue |
| Power Accumulation | Common | First 18s | Reduce damage taken + rage recovery | High | Active-skill heroes wanting faster rage (Napoleon support) |
| Eye of the Storm | Rare | After secondary strike skill | Additional damage, every 3s | Good | Alternative to Lightning Strike outside double attack state |
| Slaughter | Common | Enemy below 20% units | Increase commander skill damage | Niche | Napoleon — AoE commander skill |
| Strike Soul | Rare | Commander skill hits single target | Extra strategy damage | Below average | Solo open-field only |
| Strike Weakness | Rare | Target has any debuff | Increase damage per debuff stack | Niche | Debuff-stacking heroes (Suleiman) |
| Deceptive Words | Common | Every 9s | Inflict debuff on target | Niche | Pairs with Strike Weakness |
| Blood Rage | Common | Conditional | Rage generation | Below average | — |
| Risk Aversion | Common | After commander skill | +movement speed, −damage taken | Situational | — |

---

## 12. Hero Build Reference

Names and pool assignments use the in-game-confirmed trait roster from Section 4. Temperament listed first is the primary breeding target.

### M1 — Swordsmen

| Hero | Role | Temperament | Trait priority | Adornment form | Notes |
|---|---|---|---|---|---|
| Miyamoto Musashi | Active lead | Warbred | Overpower → Army Sunder → Bedrock | Swift Blade | Active skill Might damage |
| Yodit | Active lead | Warbred | Overpower → Army Sunder → Bedrock | Swift Blade | Same kit profile as Miyamoto |
| Hammurabi | Active support | Warbred | Overpower → Army Sunder | Swift Blade | Active skill Might damage |
| Lagertha | Active lead | **KNOWLEDGE GAP** | **KNOWLEDGE GAP** | Swift Blade *(form only — orientation confirmed, trait not)* | Her ring (Lord of Eastern Heavens) is independently confirmed wrong/Ignore-tier with no replacement assigned. No mount temperament or trait has been confirmed for her by any source. Her skill kit (Crashing Boulder, Peerless Strike, High Spirit, Bloodthirst, Shield Slam, Raging Bloodline) reads as active-skill Might damage, the same general pattern as Miyamoto — **this is an unverified inference, not a confirmed value, and must not be entered into the roster as fact.** Requires dedicated verification pass. |
| King Arthur | Active lead | Warbred | Overpower → Army Sunder | Swift Blade | **Confirmed (June 2026):** sword/cavalry commander with piercing/active skills, same archetype as Miyamoto and other active-skill leads. Previously misassigned Fearless/Tidebreaker in some roster exports — Warbred/Overpower is the corrected, locked-in value. |
| Scipio | Support | Fearless/Protective | Lifesaver → Bedrock | Mystic Mirror | Small recovery, benefits from Lifesaver |
| Tribhuwana | Support, never lead | Protective | Lifesaver → Bedrock | Mystic Mirror | |
| Josephine | Secondary strike support | Warbred (primary) + Protective (secondary) | **Confirmed dual-trait requirement: Gallant (Warbred) + Lifesaver (Protective), both required simultaneously** | Mystic Mirror | Not a primary/fallback choice — Gallant supplies offense (secondary strike Might damage), Lifesaver supplies defense (recovery-triggered damage reduction). Roster schema needs a `mount_trait_2` field to represent this correctly; do not collapse to a single trait. |
| Oda Nobunaga | Turn-based lead | Warbred | Phalanx Breaker → Army Sunder | Swift Blade | |

### M2 — Pikemen

| Hero | Role | Temperament | Trait priority | Adornment form | Notes |
|---|---|---|---|---|---|
| Cyrus the Great | Passive lead | Warbred | Valor → Army Sunder → Dustbane | Guiding Star | All Warrior PIK deal passive Might damage — Valor non-negotiable. **Confirmed correction (June 2026): previously misassigned Fearless/Tidebreaker in some roster exports — Warbred/Valor is the locked-in correct value, confirmed by name in this KB, not inferred from similar heroes.** |
| Vlad III | Passive lead | Warbred | Valor → Army Sunder → Dustbane | Guiding Star | Same profile as Cyrus |
| Boudica | Passive support | Warbred | Valor → Army Sunder → Bedrock | Guiding Star | |
| Leonidas | Passive lead | Warbred | Valor → Army Sunder → Dustbane | Guiding Star | |
| Richard I | Passive lead | Warbred | Valor → Army Sunder → Dustbane | Guiding Star | |
| Joan of Arc | Passive support, rally lead | Protective | Lifesaver → Bedrock | Stalwart Shield | |
| Mansa Musa | Support | Protective | Lifesaver → Bedrock | Stalwart Shield | Valor alternative if running DPS build |
| Barbarossa | Super support/tank | Protective | Lifesaver → Bedrock | Stalwart Shield | Cyrus + Barbarossa march is extremely tanky |
| Belisarius | Strategy secondary strike | Alert | Stratagem → Army Sunder | Guiding Star | |
| Elizabeth I | Healing conversion | Protective | Lifesaver → Renewal/Healing Armor | Stalwart Shield | More healing = more lifesteal via conversion mechanic |

### M3 — Cavalry

| Hero | Role | Temperament | Trait priority | Adornment form | Notes |
|---|---|---|---|---|---|
| **Lu Bu** | Crit lead | **Fearless** | **Thunderbolt** → Gallant *(cross-pool)* → Army Sunder | Unyielding Iron | **Confirmed correction:** Thunderbolt is Fearless/Universal, not Warbred. Lu Bu's primary breeding target is Fearless. Gallant (Warbred) is a secondary want only achievable via double-trait roll or separate breeding line |
| Zhao Yun | Passive + crit | Fearless or Warbred | Thunderbolt + (Valor/Fierce/Army Sunder) | Unyielding Iron | Three valid builds — see note below |
| Guan Yu | Secondary strike | Warbred | Gallant → Fierce → Army Sunder | Unyielding Iron | Both core traits cleanly Warbred — no cross-pool issue |
| El Cid | Secondary strike lead | Warbred | Gallant → Army Sunder/Fierce | Unyielding Iron | |
| Timur | Support, no damage | Protective | Lifesaver (single trait — sole priority) | Sacred Lily | **Resolved:** Fierce (Warbred) was the theoretical secondary want, but with negligible damage output in his kit, the confirmed recommendation is Lifesaver alone, not a forced cross-pool double trait. Do not chase Fierce for him. |
| Attila the Hun | Support | Protective | Lifesaver → Bedrock | Sacred Lily | |
| Saladin | Secondary strike passive | Warbred | Fierce → Bedrock | Sacred Lily | |
| Tomyris | Double attack state | Warbred | Fierce → Bedrock | Sacred Lily | |

**Zhao Yun's three valid builds:**
1. Thunderbolt + Valor — crit amplification + passive damage (recommended, his signature skill is his main damage source)
2. Thunderbolt + Fierce — crit + normal attack
3. Thunderbolt + Army Sunder — crit + universal damage (best for secondary-strike-heavy builds)
All three pair Thunderbolt (Fearless) with a second trait from a different pool — accept this as a deliberate double-trait target via the cross-pool breeding process, not a single clean temperament.

### M4 — Archers

| Hero | Role | Temperament | Trait priority | Adornment form | Notes |
|---|---|---|---|---|---|
| Yi Sun-Shin | Strategy active lead | Alert | Spiritbond → Army Sunder | Perfect Piercing Arrow / Eagle's Blessing | Archers default to Eagle's Blessing (defensive) regardless of role |
| Napoleon | Strategy active, AoE commander | Alert | Spiritbond → Army Sunder | Eagle's Blessing | Slaughter adornment effect is Napoleon-specific niche pick |
| Mulan | Active lead | Warbred | Gallant → Army Sunder | Eagle's Blessing | Lightning Strike adornment effect priority |
| Bellevue | Secondary strike support | Warbred (primary) + Protective (secondary) | **Confirmed dual-trait requirement: Gallant (Warbred) + Lifesaver (Protective), both required simultaneously** | Eagle's Blessing | Same combo as Josephine — Gallant supplies offense, Lifesaver supplies defense. Roster schema needs `mount_trait_2` field; do not collapse to a single trait. |
| Henry V | Support, low priority | Protective | Lifesaver (single trait — sole priority) | Eagle's Blessing | Low-value hero — don't invest in chasing a cross-pool double trait. Single Lifesaver is sufficient. |
| Alp Arslan | Active skill damage | Warbred | Overpower → Army Sunder → Dustbane | Eagle's Blessing | |
| Queen Seondeok | Strategy | Alert | Spiritbond | Eagle's Blessing | |

### M5 — Gathering

| Hero | Role | Temperament | Trait priority | Notes |
|---|---|---|---|---|
| Diao Chan | Gathering lead | Spirited (to generate) → Docile (to preserve) | Swift + Abundance + Full Stores | Best gathering lead — target all 3 gathering traits across generations if possible, minimum Swift + Abundance on one mount |
| Cleopatra | Gathering support | Same process | Swift + Abundance | |
| Darius | Gathering support (peace config) | Same process | Swift + Abundance | When rotated to M3 for tribe grinding, gathering mount becomes suboptimal — consider a reserve combat mount for this rotation |
| King Derek | Gathering role | Same process | Swift + Abundance | Never combat traits on a dedicated gathering hero |

---

## 13. Mount Resource Sources

| Resource | Primary sources |
|---|---|
| Mount Whistles | Desolate Desert, Rally Against Tribes, Alliance Treasury, Mall/VIP Store, Merits Store, Empire Horse Range |
| Meteorite Steel | Desolate Desert, Mall, Rally Against Tribes, Merits Store |
| Raw Iron | Desolate Desert, Mall, Rally Against Tribes, Merits Store |
| Refined Iron | Same sources as Raw Iron *[verify exact source breakdown in-game]* |
| Chalcedony | Desolate Desert, Mall, Rally Against Tribes, Merits Store |

Mount search proficiency increases odds of higher-rarity mount whistles pulls (Epic/Legendary). Base Legendary pull rate is extremely low (~0.03%), rising to ~0.11% at high proficiency (~200,000). Best free source for all mount materials: Desolate Desert and alliance events, completed consistently.

---

## 14. Key Rules Summary

- 7 temperaments total: Warbred, Alert, Fearless, Protective (specialized — bias mutation toward a trait pool), Spirited, Docile, Mischievous (control — adjust inheritance/mutation ratio only, no pool bias)
- 30 confirmed traits: 5 Warbred, 4 Alert, 15 Fearless/Universal, 3 Protective, 3 Gathering
- Trait value is independent of mount quality — a Common mount can roll a max-value trait
- Both parent mounts are always consumed in breeding — keep backups of anything valuable before breeding it
- Quality ascension: Common x Common 20%, Epic x Epic 10%, Legendary x Legendary 1% (Mythical), Mythical retained 100% when bred with Legendary
- Lu Bu's primary breeding target is **Fearless** (for Thunderbolt), not Warbred
- Gathering traits (Swift, Abundance, Full Stores) form their own pool, separate from all 7 combat temperaments — no temperament biases toward them
- Cross-pool hero builds (Timur, Bellevue, Henry V) require accepting either a single-trait compromise or a harder double-trait breed across two different specialized temperaments
- Epic mounts require hero lv40+ to equip
- 75% damage reduction is the likely cap across rings/traits/adornments/skills combined *[unverified exact threshold]* — stop stacking reduction near this point and shift to damage traits
- Resistance is the best universal adornment special effect — suits any march, any troop type, always
- First adornment special-effect re-roll after crafting is free — always use it
- Animal Research: unlock Bloodline Stability first (adornments), then push left-side minimums (lv3 Bloodline Stability + lv3 Insight Advancement), then focus right-side combat stats on primary troop type
- Right-side Animal Research stats are permanent, guaranteed, and apply per mounted hero of that troop type — not a one-time account bonus
- **Adornments are 3 separate fields, not 1:** Troop Type (fixed by march assignment), Form (Attack or Defense variant, 8 confirmed names), Special Effect (rolled bonus, shared pool per troop type). A UI or KB entry merging Form names and Special Effect names into one list is structurally wrong and will hide options like Resistance
- Adornment orientation rule, in precedence order: Archer (any role) → always Defense; pure support → Defense; damage dealer → Attack. Dual-troop-type heroes must be evaluated by their *current* march troop type, not a static per-hero default
- Adornments on M5 gathering heroes are low-value (combat base stats and combat-triggered special effects do not apply to a non-combat role) — never prioritize adornment resources for M5 over M1–M4
- When triaging an existing mount pool (not breeding from zero): always check inventory before recommending a fresh breed; temperament is irrelevant for equipping (only Trait + Attribute matter); a double trait with one irrelevant trait beats a single trait with the relevant one in nearly all cases; breeding same-trait parents locks in that trait rather than generating a new one — pair different traits to mutate toward something new
- **Schema requirement for Dev Thread:** roster data model needs an optional `mount_trait_2` field for confirmed dual-trait-required heroes (currently Josephine, Bellevue only — see Section 4a). Do not populate this field speculatively for other heroes.
- **Lagertha has no confirmed mount temperament or trait anywhere in any source.** This is a genuine, flagged knowledge gap, not an oversight — do not infer from similar-archetype heroes (e.g., Miyamoto) and enter as fact. Requires dedicated in-game verification.
- Cyrus the Great and King Arthur are both confirmed Warbred — Cyrus/Valor, King Arthur/Overpower. Both were previously stale (Fearless/Tidebreaker) in some roster exports; this is now corrected at source in this KB.

---

*Sources: in-game verification screenshots (Gustav, S371 N3W) — definitive for trait roster and exact percentage values. AIGA_Hero_Roster_v7.md cross-check (June 2026) — confirmed Cyrus the Great and King Arthur corrections, surfaced Lagertha as a genuine unverified gap, confirmed the dual-trait schema requirement for Josephine and Bellevue. Live AIGA builder data audit (aiga.networkgrey.co.za) — confirmed adornment dropdown structural bug, validated the 8 confirmed Form names and full hero-build roster against Gustav's actual equipped mounts. Magedd breeding guide (aoem.vercel.app/guide) — definitive for breeding probability mechanics, inheritance formulas, and strategy framework, though some trait names in that guide were machine-translation artifacts and have been corrected against in-game screenshots. Community video transcripts (Mr Sneaky, Timmy, Karmani, Sam Wise, Titobods) — used for hero-specific build recommendations and adornment special effect ratings, flagged as community-sourced opinion where it diverges from confirmed mechanics. aoem-calculator (MIT licence, Codeberg) — original numerical baseline, largely superseded by in-game confirmation in this version. All remaining [verify in-game] flags and explicit KNOWLEDGE GAP markers represent genuine open gaps, not low-confidence guesses — they must not be filled with inferred values without dedicated verification.*

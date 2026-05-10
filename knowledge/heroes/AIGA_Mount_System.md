# Age of Empires Mobile — Mount System Reference
## AIGA Source Document v1.0

---

## Mount Quality Tiers

| Quality | Rarity | Colour | Base attributes | Attribute range |
|---|---|---|---|---|
| Courser | Common | Blue | 2 | +2 to +4 |
| Destrier | Epic | Purple | 2 | +5 to +9 |
| Skywing | Legendary | Gold | 2 | +10 to +16 |
| Celestial Charger | Mythical | Red | 3 | +18 to +25 |

**Key rule:** Base attributes (Might/Armor/Strategy/Siege) stack directly with hero attributes. Higher quality = stronger base stats. Offspring never exceed the attribute range ceiling of their quality tier.

**Mythical rule:** Celestial Charger (Red) can only be obtained by breeding two Skywing (Legendary/Gold) mounts together.

**Minimum retention rule in mass breeding:** Destrier (Epic/Purple) is the minimum quality retained. Courser (Common/Blue) mounts with high-value traits will be consumed during mass breeding. Always assign and lock hero mounts before running mass breeding sessions.

---

## Epic mounts require hero level 40+ to equip.
## Rare mounts can be equipped at any hero level.
## No mount equipped is always worse than any mount regardless of temperament mismatch.

---

## Temperament System

Temperament determines what traits offspring are likely to inherit or mutate toward. Never mix temperaments when breeding — always breed same temperament x same temperament.

| Temperament | Speciality | Mutation/inheritance chance | Best used on |
|---|---|---|---|
| Warbred | Might damage traits | 80.19% mutation to Might traits | Attack leads and damage supports |
| Alert | Strategy damage traits | 80.18% mutation to Strategy traits | Strategy-based heroes |
| Fearless | Universal traits | 78.95% mutation to universal traits | March leads, rally-focused heroes |
| Protective | Healing and recovery traits | 80.17% mutation to healing traits | Support and recovery heroes |
| Docile | Trait preservation | 55% inheritance chance | Preserving specific valuable traits |
| Spirited | New trait generation | 55% mutation to random new traits | Generating new trait combinations |
| Mischievous | None | No impact on inheritance or mutation | Limited breeding value |

**Temperament inheritance rule:** Offspring are more likely to inherit the temperament shared by both parents. Breeding same x same temperament gives the highest chance of desired offspring temperament.

---

## Traits by Temperament

### Warbred — Might Damage Traits

| Trait | Effect (min/max) | Skill type buffed |
|---|---|---|
| Overpower | Active skill Might damage +2%/+10% | Active skills |
| Gallant | Secondary strike Might damage +2%/+10% | Secondary strike |
| Valor | Passive skill Might damage +2%/+10% | Passive skills |
| Phalanx Breaker | Turn-based skill Might damage +2%/+10% | Turn-based skills |
| Fierce | Normal attack damage +4.5%/+22.5% | Normal attacks |

**Best Warbred trait by hero role:**
- Musashi (active skill lead): Overpower (+10% active skill Might damage)
- Toyotomi (active skill lead): Overpower or Fierce
- Guan Yu (critical strike): Fierce (+22.5% normal attack damage)
- Josephine (attack support): Overpower or Valor

---

### Alert — Strategy Damage Traits

| Trait | Effect (min/max) | Skill type buffed |
|---|---|---|
| Spiritbond | Active skill Strategy damage +2%/+10% | Active skills |
| Stratagem | Secondary strike Strategy damage +2%/+10% | Secondary strike |
| Cunning | Passive skill Strategy damage +2%/+10% | Passive skills |
| Battlemaster | Turn-based skill Strategy damage +2%/+10% | Turn-based skills |

**Best Alert trait by hero role:**
- Yi Sun-Shin (Strategy primary stat): Spiritbond or Battlemaster
- Strategy-based support heroes: Stratagem or Cunning

---

### Fearless — Universal Traits

| Trait | Effect (min/max) | Notes |
|---|---|---|
| Thunderbolt | Critical strike damage +2.7%/+13.5% | Offensive |
| Army Sunder | All damage types +1.8%/+9% | Universal offensive |
| Dustbane | Solo battle damage +2%/+10% | Solo PVP only |
| Tidebreaker | Rally battle damage +2%/+10% (effectively +9% max) | Rally focused — highest priority for rally players |
| Bastion | Defensive — reduces incoming damage | Defensive, good for march leads |

**Rally player priority:** Tidebreaker is the most valuable Fearless trait for alliance rally-focused gameplay. Joan of Arc (pike lead, rally march) should target Tidebreaker long term.

---

### Protective — Healing Traits

| Trait | Effect (min/max) | Notes |
|---|---|---|
| Lifesaver | After recovery effects, damage taken -0.96%/-4.8% for 3s | Best for recovery support heroes |
| Renewal | Healing effect +2.3%/+11.5% | General healing boost |
| Healing Armor | Received healing effect +0.8%/+4% | Received healing boost |

**Best Protective trait:** Lifesaver for supports with recovery skills. Renewal for general support heroes.

---

## Mount Assignment Rules by Hero Role

| Hero role | Correct temperament | Target trait |
|---|---|---|
| Attack lead (Sword) | Warbred | Overpower or Fierce |
| Attack lead (Cavalry) | Warbred | Fierce or Valor |
| Attack lead (Archer) | Alert or Warbred | Spiritbond (Alert) or Overpower (Warbred) |
| March lead (Pike, counterattack) | Fearless | Tidebreaker (rally) or Bastion (defensive) |
| Attack support | Warbred | Match primary skill type |
| Buff support | Warbred | Any combat trait |
| Recovery support | Protective | Lifesaver or Renewal |
| Gathering hero | Protective | Any — trait less critical for gathering |

---

## Breeding Mechanics

### How breeding works
- Combine two mounts to produce one offspring
- Both parent mounts are consumed in the process
- Offspring quality, temperament and traits are influenced by parents
- Results contain a random element — repeat breeding may be needed for desired outcome

### Skill inheritance rules
- If both parents have no skills: offspring gains one random skill (mutation)
- If both parents have skills: chance to add second or third skill
- Repeatedly breeding same temperament strengthens bloodline and improves inheritance odds

### Breeding session limits
- Maximum 100 breedings per session
- Session stops when limits exceeded or insufficient parents remain

### Quality matching rule
- Mounts can only breed with others of identical quality
- Common x Common, Epic x Epic, Legendary x Legendary
- Mixed quality breeding is not permitted

---

## Breeding Programme Management

### Naming convention
Offspring are named using parent IDs and generation letter:
- Format: [ParentA_ID]-[ParentB_ID][generation]
- Example: W9 x W11 produces W9-11a (first attempt), W9-11b (second attempt)
- Once assigned to a hero the ID is permanent

### Mount ID system by temperament group
| Prefix | Temperament |
|---|---|
| W | Warbred |
| F | Fearless |
| P | Protective |
| A | Alert |
| D | Docile |
| S | Spirited |
| M | Mischievous |

### Lock status rules
| Status | Applies to |
|---|---|
| Lock immediately | All assigned mounts, all breeding pairs, all breeding reserves |
| Unlock to discard | Wrong temperament mounts with no breeding value |
| Never discard | Legendary mounts regardless of temperament, any mount with exceptional traits |

### Discard criteria
Discard (unlock and release) mounts that are:
- Docile with no valuable traits (low combat breeding value)
- Mischievous (no mutation/inheritance benefit)
- Alert (unless strategy heroes are present in active marches)
- Spirited with no traits (unless specifically needed for mutation breeding)
- Any temperament that does not match any hero's needs and has no breeding pair available

---

## Mount Adornment System

Each mount can equip one adornment. Adornments provide additional combat bonuses beyond the mount's base attributes and traits.

### Crafting
- Cost: 10 Meteorite Steel per adornment
- Dismantling returns 5 Meteorite Steel (50% recovery)
- Choose attack or defence variant per military specialty
- Cannot equip both attack and defence simultaneously

### Upgrade system
Upgrade adornments using Raw Iron. Levels 1-60 with bonus thresholds:

**Attack adornments:**
| Level range | Bonus type |
|---|---|
| 1-20 | Attack bonus 1%+ |
| 20-40 | Health bonus 0.5%+ |
| 40-60 | Skill damage increase 0.5%+ |

**Defence adornments:**
| Level range | Bonus type |
|---|---|
| 1-20 | Defence bonus 1%+ |
| 20-40 | Health bonus 0.5%+ |
| 40-60 | Skill damage taken reduction 0.5%+ |

### Adornment upgrade materials
- Raw Iron: 20-800 units per level (increases with level)
- Chalcedony: 1 per re-roll attempt (for effect rarity upgrades)

### Re-roll system
Adornment effects can be upgraded through rarity tiers (Common through Mythical) using Chalcedony + Raw Iron. First tier upgrade is 100% success rate. Higher tiers have increasing failure chance and potential downgrades.

### Priority for adornment investment
1. M1 heroes first (Musashi, Josephine, Hammurabi)
2. M2 heroes (Joan, Wu Wei, Gatos)
3. M3/M4/M5 heroes after primary marches equipped

### Best adornment types by hero
| Hero type | Recommended adornment |
|---|---|
| Sword lead (Musashi) | Attack — Swordsmen — Thunder or Wavebreaker |
| Pike lead (Joan) | Attack or Defence — Pikemen — Secondary Strike (rare) or Resistance |
| Pike support (Wu Wei) | Attack — Pikemen — Thunder or Blood Debt |
| Pike support (Gatos) | Attack — Pikemen — Secondary Strike (1% drop, rare) |
| Cavalry lead (Guan Yu) | Attack — Cavalry — Chain Slayer or Boiling Blood |
| Archer lead (Yi Sun-Shin) | Attack — Archers — War Prep or Lightning Strike |

---

## Mount Resource Sources

| Resource | Primary sources |
|---|---|
| Mount Whistles | Desolate Desert, Rally Against Tribes, Alliance Treasury, Mall/VIP Store, Merits Store, Empire Horse Range |
| Breeding materials | Consumed mounts, events |
| Meteorite Steel | Desolate Desert, Mall, Rally Against Tribes events, Merits Store |
| Raw Iron | Desolate Desert, Mall, Rally Against Tribes, Merits Store |
| Chalcedony | Desolate Desert, Mall, Rally Against Tribes, Merits Store |

**Best free source:** Desolate Desert and alliance events. Complete these consistently for steady mount material income.

---

## Skill Tree — Breeding Research (Animal Research)

Upgrading Animal Research improves breeding outcomes.

| Research | Effect |
|---|---|
| Keen Eye for Steeds | Increases search proficiency — better mount discovery rates |
| Natural Advantage | Higher chance of superior base attributes through breeding |
| Legacy Inheritance | Inherited traits more likely to have high values |
| Exceptional Talent | Mutated traits acquire higher values more frequently |
| Bloodline Stability | Unlocks Adornment Workshop, increases fusion insight points |

**Priority:** Green path first (search proficiency and Prophecy gain) before red path (combat stats). Troop type paths — focus on your primary march troop type first.

---

*Source: Mount System Guide V2 (community guide), aoem-calculator.com, AIGA session data. Verify current values in-game as game updates may affect breeding rates and adornment costs.*

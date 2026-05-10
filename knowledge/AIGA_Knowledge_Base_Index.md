# AIGA — Knowledge Base Master Index

## Network Grey | Age of Empires Mobile

## Version: 1.5 | Last updated: 9 May 2026

---

## Revision History

| Version | Date | Changes |
| :---- | :---- | :---- |
| v1.0 | March 2026 | Initial index. 12 core documents, system prompt, web designer guide, todo list, workbook. |
| v1.1 | 30 March 2026 | Added legal compliance documents. Microsoft flagged as second IP holder. SA minimum age 18 confirmed. |
| v1.2 | 30 March 2026 | Added AIGA\_Game\_Mechanics\_Reference.md. Updated Events\_Index from Batch 2 zip (28 HTML files). |
| v1.3 | 30 March 2026 | Index updated to reflect v1.1 and v1.2 additions. Total 38 documents. |
| v1.4 | 9 May 2026 | Added 13 new files. Hero reference chain updated (v1 and v2 superseded by v3). AIGA\_Legal\_AoEMobileGuides\_Reference.md flagged missing. Total 51 documents. |
| v1.5 | 9 May 2026 | Full folder restructure into 8 categories. 51 flat files consolidated to 35 (23 bot-facing). 2 superseded hero files deleted. 19 files absorbed into 9 consolidated documents. KEYWORD\_MAP paths and recursive glob requirement flagged for bot.py. |

---

## Purpose and Architecture

This file is the single source of truth for the AIGA knowledge base. It serves two audiences:

**Claude Code (primary):** Reads this index to locate files, execute restructures, merge content, and update `bot.py`. All file paths in this document are relative to the repository `/knowledge/` root.

**AIGA bot (secondary):** Does not read this file directly. The bot uses `KEYWORD_MAP` in `bot.py` to inject the top 2-3 matching documents per query. File paths in `KEYWORD_MAP` must match this index exactly.

**Rule:** Never add a file to the repository without a corresponding index entry. Never update a path on GitHub without updating `KEYWORD_MAP` in `bot.py` simultaneously.

---

## Folder Structure

/knowledge/

|

|-- AIGA\_Knowledge\_Base\_Index.md          ROOT — this file

|

|-- /heroes/                              Hero data, builds, skills, XP costs, mounts

|-- /gear/                                Gear crafting, forging, gems, rings

|-- /march/                               March lineups, formations, rally compositions

|-- /combat/                              PvP, open field, world map, civilisations

|-- /events/                              MGE, MEE, all competitive events

|-- /base/                                Buildings, TC, research, troops, healing

|-- /economy/                             Gathering, coins, store, VIP

|-- /system/                              Ops files, prompts, legal — not bot-facing

    |-- /source/                          Raw source PDFs — archived, not bot-facing

---

## Document Registry

### /heroes/ — 6 files

| File | Description | Source | Status | Known gaps |
| :---- | :---- | :---- | :---- | :---- |
| heroes/AIGA\_Hero\_Complete\_Reference.md | All heroes — base stats, skills, specialties, pairings. Merged from v3 \+ Hero\_Data\_Verified. | aoemobileguides.com \+ Network Grey | Current | Post-Oct 2025 heroes. Guan Yu, Yi Sun-Shin, Harald, Yodit, Tribhuwana, Toyotomi, Otto missing. Maya Mutuala, Yellet missing. |
| heroes/AIGA\_Hero\_Builds\_Reference.md | S-tier hero builds, skill selections, Lu Bu mercenary analysis. Merged from S\_Tiers \+ LuBu\_Comparison PDF. | aoemobileguides.com \+ community \+ Network Grey | Current | Post-Oct 2025 heroes |
| heroes/AIGA\_Hero\_Skills\_Library.md | Full skill catalogue — rarity, type, values, eligible heroes, fragment unlock costs. | aoemobileguides.com | Current | Post-Oct 2025 skills |
| heroes/AIGA\_Hero\_Tier\_List.md | S+ through D tier ratings and notes per hero. | aoemobileguides.com | Current | Maya Mutuala, Yellet, post-Oct 2025 heroes |
| heroes/AIGA\_Hero\_XP\_Skills.md | XP costs lv1-140, SP costs per skill level, rank medals, scroll costs, XP tome denominations, hero sub-rank data. Calculator-verified. | aoem-calculator (MIT) \+ Theria Games | Current | Sub-rank medal costs per sub-rank unknown |
| heroes/AIGA\_Mount\_System.md | Temperaments, traits, breeding rules, rarity chain (Epic x Epic \= Epic only, Legendary x Legendary \= Celestial Charger), adornments. | Community / Network Grey | Current | Exact trait values for all mounts |

---

### /gear/ — 2 files

| File | Description | Source | Status | Known gaps |
| :---- | :---- | :---- | :---- | :---- |
| gear/AIGA\_Gear\_Reference.md | Gear names by troop type, craft costs, forge kit costs (lv20-30 verified at 2,340-2,548 kits), star upgrades, gem slots, gem rarity tiers (10 levels: Common through Mythic IV), lightning crystal requirements, gem stat types per slot. Merged from Gear\_Gems \+ Gear\_Stats\_Addendum \+ Calculator\_Findings gear sections. | aoem-calculator \+ Theria Games | Current | Lightning crystal exact level thresholds. Full cumulative forge kit table unverified beyond lv20-30. |
| gear/AIGA\_Rings\_Reference.md | All 35 rings — stats at max level, skill types, Jeweler's Marks as confirmed upgrade material. Merged from Rings\_Reference \+ Rings\_Skills\_Addendum \+ Calculator\_Findings rings section. | aoem-calculator \+ Theria Games | Current | Jeweler's Marks exact quantities per upgrade level |

---

### /march/ — 1 file

| File | Description | Source | Status | Known gaps |
| :---- | :---- | :---- | :---- | :---- |
| march/AIGA\_March\_Reference.md | March build guides, rally compositions, hero formation mechanics, positioning rules. Merged from March\_Compositions \+ Hero\_Formation\_Reference. | Community | Current | None documented |

---

### /combat/ — 2 files

| File | Description | Source | Status | Known gaps |
| :---- | :---- | :---- | :---- | :---- |
| combat/AIGA\_Game\_Mechanics\_Reference.md | Core game mechanics, combat system, auto battler, stamina, open field PvP, world map, territory, passes, hive strategy, game modes. Merged from Game\_Mechanics \+ Combat\_PvP\_Addendum \+ WorldMap\_Addendum \+ Game\_Modes\_Addendum. | Theria Games \+ Fandom Wiki \+ Van (YouTube) \+ Official AoEM | Current | Holy Sites mechanics |
| combat/AIGA\_Civilizations\_Reference.md | 8 documented civilisations, landmarks, territory bonuses. Arabs (9th civ) confirmed but not documented. | Fandom wiki \+ community | Current | Arabs full stat bonuses. Julius Caesar civ suspected wiki error. |

---

### /events/ — 3 files

| File | Description | Source | Status | Known gaps |
| :---- | :---- | :---- | :---- | :---- |
| events/AIGA\_MGE\_Reference.md | MGE Day I-VII scoring, tribe scores, gear scores, Smithy level dependency on gear MGE pts, event strategy. Smithy data migrated from Calculator\_Findings. | aoem-calculator \+ Theria Games | Current | None |
| events/AIGA\_MEE\_Reference.md | Complete MEE guide — scoring all activities, day-specific breakdown (Days II/IV/V confirmed as training days), strategy, vs MGE comparison. Merged from MEE\_Guide\_v1 \+ MEE\_Guide\_v1\_1 \+ MEE\_Reference \+ Calculator\_Findings MEE section. | aoem-calculator \+ Network Grey \+ Theria Games | Current | T5 MEE pts conflict unresolved: multiplier implies 200, troop table shows 160 — verify in-game |
| events/AIGA\_Events\_Reference.md | All competitive events — overview, Legendary Advent wheel (5-spin/4,200 IC confirmed, token mechanic: 1 per spin, 60 \= 15 medals, secondary milestones 30% probabilistic), Battle of Dawn, Wonder Contest, Starfall Vein, Frontline Escort stub. Merged from Events\_Index \+ Battle\_of\_Dawn\_Reference \+ Wonder\_Contest \+ Starfall\_Vein PDF \+ Calculator\_Findings wheel sections. | Theria Games \+ AoE Mobile Guides \+ Fandom Wiki \+ Network Grey | Current | Frontline Escort full scoring. Golden Expedition full rules. |

---

### /base/ — 5 files

| File | Description | Source | Status | Known gaps |
| :---- | :---- | :---- | :---- | :---- |
| base/AIGA\_Buildings\_Reference.md | All 24 buildings lv1-30 — full costs, prerequisites, power values. | aoem-calculator (buildings.json) | Current | Smithy building costs missing from source |
| base/AIGA\_Town\_Centre\_Reference.md | TC upgrade prerequisites lv6-30 and key milestones. | aoem-calculator | Current | None |
| base/AIGA\_Research\_Reference.md | University military and economy research trees, Mercenary Camp T1 and T2 costs (48 technologies), Legendary Advent wheel MGE scoring. Merged from Research\_Mercenary\_Wheel \+ Research\_Technology. | aoem-calculator \+ community | Current | University military tree node unlock levels incomplete |
| base/AIGA\_Troop\_Training\_Reference.md | Training costs T1-T7, promotion costs, MGE/MEE pts per troop, gather load. | aoem-calculator (MIT) | Current | None |
| base/AIGA\_Healing\_Reference.md | Healing costs T1-T7, heal vs retrain comparison. | aoem-calculator (MIT) | Current | None |

---

### /economy/ — 4 files

| File | Description | Source | Status | Known gaps |
| :---- | :---- | :---- | :---- | :---- |
| economy/AIGA\_Gathering\_Reference.md | Resource nodes lv1-9, speed and capacity, troop load by tier, optimal hero lineup. | aoem-calculator | Current | Node lv2 capacity appears anomalous — verify |
| economy/AIGA\_Free\_Coins\_Reference.md | Free Empire Coin sources, farming methods, priority spend guide. | Community / Network Grey | Current | None documented |
| economy/AIGA\_Items\_Store\_Reference.md | In-game items, store inventory, recommended purchases. | Community | Current | None documented |
| economy/AIGA\_VIP\_Reference.md | VIP levels, benefits, point costs. | Community | Current | Verify current VIP tier caps in-game |

---

### /system/ — 9 files (not bot-facing)

| File | Description | Version | Status |
| :---- | :---- | :---- | :---- |
| system/AIGA\_System\_Prompt\_v3\_FINAL.md | Master system prompt — identity, rules, condensed game data for bot context | v3.0 FINAL | Current |
| system/AIGA\_Onboarding\_KYC\_Reference.md | Player onboarding flow, KYC tiers, response depth rules | v1.0 | Current |
| system/AIGA\_Game\_Overview\_Reference.md | Game introduction and core mechanics overview — onboarding context only, not a query target | v1.0 | Current |
| system/AIGA\_Legal\_ProximaBeta\_Reference.md | Official AoEM Privacy Policy (Jan 2026\) and EULA — IP ownership, 18+ restriction, required disclaimer | v1.0 | Current |
| system/AIGA\_Web\_Designer\_Guide.docx | WordPress/PayFast setup guide for web designer | v1.0 | Current |
| system/AIGA\_Thread\_Handoff.docx | Internal development session handoff notes | v1.0 | Current |
| system/AIGA\_Todo\_List.html | Interactive project task tracker | v2 | Active |
| system/AIGA\_March\_Analyser.html | Interactive march analysis tool | — | Active |
| system/AIGA\_Workbook\_v2.xlsx | War Chest player workbook template | v2 | Active — full template pending |

### /system/source/ — 2 files (archived PDFs, not bot-facing)

| File | Description | Status |
| :---- | :---- | :---- |
| system/source/Battle\_of\_Dawn\_Decree.pdf | Official Battle of Dawn decree — source material. Content extracted into events/AIGA\_Events\_Reference.md. | Archived |
| system/source/LuBu\_Mercenary\_Comparison.pdf | Lu Bu mercenary comparison — source material. Content extracted into heroes/AIGA\_Hero\_Builds\_Reference.md. | Archived |

---

## Document Count Summary

| Folder | Files | Bot-facing |
| :---- | :---- | :---- |
| /heroes/ | 6 | Yes |
| /gear/ | 2 | Yes |
| /march/ | 1 | Yes |
| /combat/ | 2 | Yes |
| /events/ | 3 | Yes |
| /base/ | 5 | Yes |
| /economy/ | 4 | Yes |
| /system/ | 9 | No |
| /system/source/ | 2 | No |
| Root (this file) | 1 | No |
| **Total** | **35** | **23 bot-facing** |

---

## Claude Code Implementation Instructions

### Step 1 — Delete (superseded, zero content value)

| File | Reason |
| :---- | :---- |
| AIGA\_Hero\_Complete\_Reference.md (v1) | Superseded by v3 |
| AIGA\_Hero\_Complete\_Reference\_v2.md | Superseded by v3 |

### Step 2 — Content merges then delete source file

| Source file | Merge target | Action |
| :---- | :---- | :---- |
| AIGA\_Hero\_Complete\_Reference\_v3.md | heroes/AIGA\_Hero\_Complete\_Reference.md | Rename — base file |
| AIGA\_Hero\_Data\_Verified.md | heroes/AIGA\_Hero\_Complete\_Reference.md | Append verified data section |
| AIGA\_Hero\_Builds\_Reference\_S\_Tiers.md | heroes/AIGA\_Hero\_Builds\_Reference.md | Rename — base file |
| LuBu\_Mercenary\_Comparison.pdf | heroes/AIGA\_Hero\_Builds\_Reference.md | Extract and append — move PDF to system/source/ |
| AIGA\_Hero\_Formation\_Reference.md | march/AIGA\_March\_Reference.md | Append formation section |
| AIGA\_March\_Compositions\_Reference.md | march/AIGA\_March\_Reference.md | Rename — base file |
| AIGA\_Gear\_Gems\_Reference.md | gear/AIGA\_Gear\_Reference.md | Rename — base file |
| AIGA\_Gear\_Stats\_Addendum.md | gear/AIGA\_Gear\_Reference.md | Append stats section |
| AIGA\_Rings\_Reference.md | gear/AIGA\_Rings\_Reference.md | Rename — base file |
| AIGA\_Rings\_Skills\_Addendum.md | gear/AIGA\_Rings\_Reference.md | Append skills section |
| AIGA\_Research\_Mercenary\_Wheel\_Reference.md | base/AIGA\_Research\_Reference.md | Rename — base file |
| AIGA\_Research\_Technology\_Reference.md | base/AIGA\_Research\_Reference.md | Append technology section |
| AIGA\_Game\_Mechanics\_Reference.md | combat/AIGA\_Game\_Mechanics\_Reference.md | Move to folder — base file |
| AIGA\_Combat\_PvP\_Addendum.md | combat/AIGA\_Game\_Mechanics\_Reference.md | Append PvP section |
| AIGA\_WorldMap\_Mechanics\_Addendum.md | combat/AIGA\_Game\_Mechanics\_Reference.md | Append world map section |
| AIGA\_Game\_Modes\_Addendum.md | combat/AIGA\_Game\_Mechanics\_Reference.md | Append game modes section |
| AIGA\_MEE\_Reference.md | events/AIGA\_MEE\_Reference.md | Rename — base file |
| AIGA\_MEE\_Guide\_v1.md | events/AIGA\_MEE\_Reference.md | Append guide content |
| AIGA\_MEE\_Guide\_v1\_1.pdf | events/AIGA\_MEE\_Reference.md | Extract and append — delete PDF after |
| AIGA\_Events\_Index\_Reference.md | events/AIGA\_Events\_Reference.md | Rename — base file |
| AIGA\_Battle\_of\_Dawn\_Reference.md | events/AIGA\_Events\_Reference.md | Append Battle of Dawn section |
| AIGA\_Wonder\_Contest\_Reference.md | events/AIGA\_Events\_Reference.md | Append Wonder Contest section |
| AIGA\_Starfall\_Vein\_Reference.pdf | events/AIGA\_Events\_Reference.md | Extract and append — delete PDF after |
| Battle\_of\_Dawn\_Decree.pdf | system/source/ | Move only — no content extraction needed |
| AIGA\_Calculator\_Findings\_Addendum.md | Multiple (see Step 2a) | Migrate then delete |

### Step 2a — Calculator Findings data migration targets

| Data | Destination |
| :---- | :---- |
| Gem rarity tiers (10 levels confirmed, Common through Mythic IV) | gear/AIGA\_Gear\_Reference.md |
| Lightning crystals as confirmed upgrade material | gear/AIGA\_Gear\_Reference.md |
| Gem stat types per slot confirmed | gear/AIGA\_Gear\_Reference.md |
| Jeweler's Marks as confirmed ring upgrade material | gear/AIGA\_Rings\_Reference.md |
| Advent Wheel secondary milestone medals — 30% probabilistic | events/AIGA\_Events\_Reference.md |
| MEE training days — Days II, IV, V confirmed | events/AIGA\_MEE\_Reference.md |
| Hero sub-rank structure data | heroes/AIGA\_Hero\_XP\_Skills.md |
| XP tome denominations (lv2=500, lv3=1,000, lv4=10,000, lv5=50,000, lv6=100,000) | heroes/AIGA\_Hero\_XP\_Skills.md |
| MGE gear calculation — Smithy level dependency confirmed | events/AIGA\_MGE\_Reference.md |

### Step 3 — Update bot.py

**3a — Recursive glob (required — current glob misses all subfolders)**

\# Before

knowledge\_dir.glob("\*.md")

\# After

knowledge\_dir.glob("\*\*/\*.md")

**3b — KEYWORD\_MAP with updated subfolder paths**

KEYWORD\_MAP \= {

    \# Heroes

    "hero":             "heroes/AIGA\_Hero\_Complete\_Reference.md",

    "heroes":           "heroes/AIGA\_Hero\_Complete\_Reference.md",

    "build":            "heroes/AIGA\_Hero\_Builds\_Reference.md",

    "builds":           "heroes/AIGA\_Hero\_Builds\_Reference.md",

    "skill":            "heroes/AIGA\_Hero\_Skills\_Library.md",

    "skills":           "heroes/AIGA\_Hero\_Skills\_Library.md",

    "fragment":         "heroes/AIGA\_Hero\_Skills\_Library.md",

    "tier":             "heroes/AIGA\_Hero\_Tier\_List.md",

    "xp":               "heroes/AIGA\_Hero\_XP\_Skills.md",

    "level":            "heroes/AIGA\_Hero\_XP\_Skills.md",

    "medal":            "heroes/AIGA\_Hero\_XP\_Skills.md",

    "rank":             "heroes/AIGA\_Hero\_XP\_Skills.md",

    "tome":             "heroes/AIGA\_Hero\_XP\_Skills.md",

    "mount":            "heroes/AIGA\_Mount\_System.md",

    "breed":            "heroes/AIGA\_Mount\_System.md",

    "breeding":         "heroes/AIGA\_Mount\_System.md",

    "temperament":      "heroes/AIGA\_Mount\_System.md",

    "adornment":        "heroes/AIGA\_Mount\_System.md",

    \# Gear

    "gear":             "gear/AIGA\_Gear\_Reference.md",

    "forge":            "gear/AIGA\_Gear\_Reference.md",

    "gem":              "gear/AIGA\_Gear\_Reference.md",

    "gems":             "gear/AIGA\_Gear\_Reference.md",

    "meteorite":        "gear/AIGA\_Gear\_Reference.md",

    "ring":             "gear/AIGA\_Rings\_Reference.md",

    "rings":            "gear/AIGA\_Rings\_Reference.md",

    \# March

    "march":            "march/AIGA\_March\_Reference.md",

    "formation":        "march/AIGA\_March\_Reference.md",

    "lineup":           "march/AIGA\_March\_Reference.md",

    "composition":      "march/AIGA\_March\_Reference.md",

    "rally":            "march/AIGA\_March\_Reference.md",

    \# Combat

    "combat":           "combat/AIGA\_Game\_Mechanics\_Reference.md",

    "attack":           "combat/AIGA\_Game\_Mechanics\_Reference.md",

    "battle":           "combat/AIGA\_Game\_Mechanics\_Reference.md",

    "map":              "combat/AIGA\_Game\_Mechanics\_Reference.md",

    "pvp":              "combat/AIGA\_Game\_Mechanics\_Reference.md",

    "stamina":          "combat/AIGA\_Game\_Mechanics\_Reference.md",

    "territory":        "combat/AIGA\_Game\_Mechanics\_Reference.md",

    "civ":              "combat/AIGA\_Civilizations\_Reference.md",

    "civilization":     "combat/AIGA\_Civilizations\_Reference.md",

    "civilisation":     "combat/AIGA\_Civilizations\_Reference.md",

    "landmark":         "combat/AIGA\_Civilizations\_Reference.md",

    \# Events

    "mge":              "events/AIGA\_MGE\_Reference.md",

    "governor":         "events/AIGA\_MGE\_Reference.md",

    "mee":              "events/AIGA\_MEE\_Reference.md",

    "empire":           "events/AIGA\_MEE\_Reference.md",

    "event":            "events/AIGA\_Events\_Reference.md",

    "events":           "events/AIGA\_Events\_Reference.md",

    "wheel":            "events/AIGA\_Events\_Reference.md",

    "advent":           "events/AIGA\_Events\_Reference.md",

    "spin":             "events/AIGA\_Events\_Reference.md",

    "starfall":         "events/AIGA\_Events\_Reference.md",

    "wonder":           "events/AIGA\_Events\_Reference.md",

    "dawn":             "events/AIGA\_Events\_Reference.md",

    "token":            "events/AIGA\_Events\_Reference.md",

    \# Base

    "building":         "base/AIGA\_Buildings\_Reference.md",

    "buildings":        "base/AIGA\_Buildings\_Reference.md",

    "barracks":         "base/AIGA\_Buildings\_Reference.md",

    "tc":               "base/AIGA\_Town\_Centre\_Reference.md",

    "town":             "base/AIGA\_Town\_Centre\_Reference.md",

    "prerequisite":     "base/AIGA\_Town\_Centre\_Reference.md",

    "research":         "base/AIGA\_Research\_Reference.md",

    "university":       "base/AIGA\_Research\_Reference.md",

    "mercenary":        "base/AIGA\_Research\_Reference.md",

    "technology":       "base/AIGA\_Research\_Reference.md",

    "troop":            "base/AIGA\_Troop\_Training\_Reference.md",

    "troops":           "base/AIGA\_Troop\_Training\_Reference.md",

    "training":         "base/AIGA\_Troop\_Training\_Reference.md",

    "t4":               "base/AIGA\_Troop\_Training\_Reference.md",

    "t5":               "base/AIGA\_Troop\_Training\_Reference.md",

    "heal":             "base/AIGA\_Healing\_Reference.md",

    "healing":          "base/AIGA\_Healing\_Reference.md",

    "hospital":         "base/AIGA\_Healing\_Reference.md",

    \# Economy

    "gather":           "economy/AIGA\_Gathering\_Reference.md",

    "gathering":        "economy/AIGA\_Gathering\_Reference.md",

    "resources":        "economy/AIGA\_Gathering\_Reference.md",

    "node":             "economy/AIGA\_Gathering\_Reference.md",

    "coins":            "economy/AIGA\_Free\_Coins\_Reference.md",

    "currency":         "economy/AIGA\_Free\_Coins\_Reference.md",

    "free":             "economy/AIGA\_Free\_Coins\_Reference.md",

    "store":            "economy/AIGA\_Items\_Store\_Reference.md",

    "shop":             "economy/AIGA\_Items\_Store\_Reference.md",

    "items":            "economy/AIGA\_Items\_Store\_Reference.md",

    "vip":              "economy/AIGA\_VIP\_Reference.md",

}

---

## Source Hierarchy

When data conflicts between sources, apply this priority order:

| Priority | Source | Trust level |
| :---- | :---- | :---- |
| 1 | aoem-calculator (MIT Licence, Codeberg) | Highest — open source, verifiable |
| 2 | Official AoEM YouTube / aoemobile.com (TiMi Studio Group) | High — developer content |
| 3 | Official AoEM Dev Columns | High — developer content |
| 4 | Theria Games (theriagames.com) | Medium-high — detailed, generally accurate |
| 5 | aoemobileguides.com | Medium — community, disclaim accuracy |
| 6 | Van (YouTube) | Medium — community, credit by name |
| 7 | Fandom Wiki | Low-medium — frequently outdated or incorrect |
| 8 | General community / unattributed | Low — flag as unverified |

---

## Known Gaps — Priority Order

### Critical

- Arabs civilisation full stat bonuses — confirmed 9th civ, not yet documented  
- TiMi / Level Infinite explicit fan content policy — not yet located  
- Hero sub-rank medal costs — 5 sub-ranks per rank confirmed, costs unknown  
- AIGA\_Legal\_AoEMobileGuides\_Reference.md — missing from project, needs recreation

### High

- Maya Mutuala and Yellet hero pages — post-Oct 2025  
- Missing heroes: Guan Yu, Yi Sun-Shin, Harald, Yodit, Tribhuwana, Toyotomi, Otto  
- Frontline Escort event — full mechanics and scoring  
- Golden Expedition — full scoring and rules

### Medium

- Gem upgrade costs — 10 tiers now named, upgrade material costs unknown  
- Jeweler's Marks exact quantities per ring upgrade level  
- Lightning crystals exact gear level thresholds  
- Holy Sites mechanics  
- Smithy building costs

### Resolved since v1.4

- Starfall Vein scoring — now in events/AIGA\_Events\_Reference.md  
- Wonder Contest mechanics — now in events/AIGA\_Events\_Reference.md  
- Gem rarity tier names — 10 levels confirmed  
- Advent Wheel token mechanic — documented  
- MEE day-specific training days — Days II, IV, V confirmed  
- XP tome denominations — confirmed  
- Advent wheel pack size — 5-spin at 4,200 IC confirmed

---

## Data Verification Queue

| Item | Issue | Priority |
| :---- | :---- | :---- |
| T5 MEE training pts | Multiplier implies 200 pts, troop table shows 160 — verify in-game | High |
| Legendary gear MGE pts | Source says 30,000 — conflicting community report of 15,000 | High |
| Arabs civilisation buffs | 9th civ confirmed — exact bonuses not documented | High |
| Unit promotion MGE pts | Source confirms 0 — community guide says 1 | Medium |
| Mercenary Camp T2 lv5 cost | Source data shows same as lv3 — likely error | Medium |
| Tariq vs Khalid hero name | Theria lists Tariq, AIGA has Khalid — one is wrong | Medium |
| Forge kit cumulative totals | lv20-30 verified at 2,340-2,548 kits — full table unverified | Medium |
| Gathering node lv2 capacity | Source shows 800,000,000 — appears anomalous | Low |
| Julius Caesar civilisation | Fandom wiki lists Byzantium — suspected error | Low |
| T3 troop defence stat | Wiki shows 50, lower than T2's 66 — suspected wiki error | Low |

---

## Compliance Reminders

Required disclaimer for all AIGA product surfaces (Discord, web app, documents):

"AIGA is an independent fan advisory service created by Network Grey. Not affiliated with, endorsed by, or associated with TiMi Studio Group, Level Infinite, Proxima Beta Pte. Limited, Microsoft, or Xbox Game Studios. Age of Empires and Age of Empires Mobile are trademarks of Microsoft Corporation."

South Africa minimum age per official Privacy Policy: **18+** — must be displayed on Discord server and web app.

---

*Maintained by Network Grey. Update this index at the end of every knowledge base session. Version and date every revision in the revision history table.*  

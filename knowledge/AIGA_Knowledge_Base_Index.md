# AIGA — Knowledge Base Master Index
## Network Grey | Age of Empires Mobile
## Version: 1.6 | Last updated: June 2026

---

## Revision History

| Version | Date | Changes |
|---|---|---|
| v1.0 | March 2026 | Initial index. 12 core documents, system prompt, web designer guide, todo list, workbook. |
| v1.1 | 30 March 2026 | Added legal compliance documents. Microsoft flagged as second IP holder. SA minimum age 18 confirmed. |
| v1.2 | 30 March 2026 | Added AIGA_Game_Mechanics_Reference.md. Updated Events_Index from Batch 2 zip (28 HTML files). |
| v1.3 | 30 March 2026 | Index updated to reflect v1.1 and v1.2 additions. Total 38 documents. |
| v1.4 | 9 May 2026 | Added 13 new files. Hero reference chain updated (v1 and v2 superseded by v3). AIGA_Legal_AoEMobileGuides_Reference.md flagged missing. Total 51 documents. |
| v1.5 | 9 May 2026 | Full folder restructure into 8 categories. 51 flat files consolidated to 35 (23 bot-facing). 2 superseded hero files deleted. 19 files absorbed into 9 consolidated documents. KEYWORD_MAP paths and recursive glob requirement flagged for bot.py. |
| v1.6 | June 2026 | Mount System replaced with v6 DEV HANDOFF (30 confirmed traits, full adornments, corrected hero assignments). Rings Reference corrected to 35 rings (10 T0 / 14 T1 / 11 T2 — Sacred Sage confirmed 11th T2, Mamba absent). KEYWORD_MAP verified — no mismatches. Commit 72e676f. |

---

## Purpose and Architecture

This file is the single source of truth for the AIGA knowledge base. It serves two audiences:

**Claude Code (primary):** Reads this index to locate files, execute restructures, merge content, and update `bot.py`. All file paths in this document are relative to the repository `/knowledge/` root.

**AIGA bot (secondary):** Does not read this file directly. The bot uses `KEYWORD_MAP` in `bot.py` to inject the top 2-3 matching documents per query. File paths in `KEYWORD_MAP` must match this index exactly.

**Rule:** Never add a file to the repository without a corresponding index entry. Never update a path on GitHub without updating `KEYWORD_MAP` in `bot.py` simultaneously.

---

## Folder Structure

```
/knowledge/
|
|-- AIGA_Knowledge_Base_Index.md          ROOT — this file
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
```

---

## Document Registry

### /heroes/ — 6 files

| File | Description | Source | Status | Known gaps |
|---|---|---|---|---|
| heroes/AIGA_Hero_Complete_Reference.md | All heroes — base stats, skills, specialties, pairings. Merged from v3 + Hero_Data_Verified. | aoemobileguides.com + Network Grey | Current | Post-Oct 2025 heroes. Guan Yu, Yi Sun-Shin, Harald, Yodit, Tribhuwana, Toyotomi, Otto missing. Maya Mutuala, Yellet missing. |
| heroes/AIGA_Hero_Builds_Reference.md | S-tier hero builds, skill selections, Lu Bu mercenary analysis. Merged from S_Tiers + LuBu_Comparison PDF. | aoemobileguides.com + community + Network Grey | Current | Post-Oct 2025 heroes |
| heroes/AIGA_Hero_Skills_Library.md | Full skill catalogue — rarity, type, values, eligible heroes, fragment unlock costs. | aoemobileguides.com | Current | Post-Oct 2025 skills |
| heroes/AIGA_Hero_Tier_List.md | S+ through D tier ratings and notes per hero. | aoemobileguides.com | Current | Maya Mutuala, Yellet, post-Oct 2025 heroes |
| heroes/AIGA_Hero_XP_Skills.md | XP costs lv1-140, SP costs per skill level, rank medals, scroll costs, XP tome denominations, hero sub-rank data. Calculator-verified. | aoem-calculator (MIT) + Theria Games | Current | Sub-rank medal costs per sub-rank unknown |
| heroes/AIGA_Mount_System.md | Temperaments, traits, breeding rules, rarity chain (Epic x Epic = Epic only, Legendary x Legendary = Celestial Charger), adornments. | Community / Network Grey | Current | ~30 heroes with no mount data (Hannibal, Justinian, Harald III, Sejong, Wu Wei, Kaso, Gao Meng, Axel, Yuan Xia, Leo, Luki, Narses, Nino and others). Lagertha: permanent knowledge gap — do not infer. |

### /gear/ — 2 files

| File | Description | Source | Status | Known gaps |
|---|---|---|---|---|
| gear/AIGA_Gear_Reference.md | Gear names by troop type, craft costs, forge kit costs (lv20-30 verified at 2,340-2,548 kits), star upgrades, gem slots, gem rarity tiers (10 levels: Common through Mythic IV), lightning crystal requirements, gem stat types per slot. Merged from Gear_Gems + Gear_Stats_Addendum + Calculator_Findings gear sections. | aoem-calculator + Theria Games | Current | Lightning crystal exact level thresholds. Full cumulative forge kit table unverified beyond lv20-30. |
| gear/AIGA_Rings_Reference.md | All 35 rings — stats at max level, skill types, Jeweler's Marks as confirmed upgrade material. Merged from Rings_Reference + Rings_Skills_Addendum + Calculator_Findings rings section. | aoem-calculator + Theria Games | Current | Jeweler's Marks exact quantities per upgrade level. T2 count: v2.2 had 9 (error) — confirmed 11 in-game June 2026. |

### /march/ — 1 file

| File | Description | Source | Status | Known gaps |
|---|---|---|---|---|
| march/AIGA_March_Reference.md | March build guides, rally compositions, hero formation mechanics, positioning rules. Merged from March_Compositions + Hero_Formation_Reference. | Community | Current | None documented |

### /combat/ — 2 files

| File | Description | Source | Status | Known gaps |
|---|---|---|---|---|
| combat/AIGA_Game_Mechanics_Reference.md | Core game mechanics, combat system, auto battler, stamina, open field PvP, world map, territory, passes, hive strategy, game modes. Merged from Game_Mechanics + Combat_PvP_Addendum + WorldMap_Addendum + Game_Modes_Addendum. | Theria Games + Fandom Wiki + Van (YouTube) + Official AoEM | Current | Holy Sites mechanics |
| combat/AIGA_Civilizations_Reference.md | 8 documented civilisations, landmarks, territory bonuses. Arabs (9th civ) confirmed but not documented. | Fandom wiki + community | Current | Arabs full stat bonuses. Julius Caesar civ suspected wiki error. |

### /events/ — 3 files

| File | Description | Source | Status | Known gaps |
|---|---|---|---|---|
| events/AIGA_MGE_Reference.md | MGE Day I-VII scoring, tribe scores, gear scores, Smithy level dependency on gear MGE pts, event strategy. Smithy data migrated from Calculator_Findings. | aoem-calculator + Theria Games | Current | None |
| events/AIGA_MEE_Reference.md | Complete MEE guide — scoring all activities, day-specific breakdown (Days II/IV/V confirmed as training days), strategy, vs MGE comparison. Merged from MEE_Guide_v1 + MEE_Guide_v1_1 + MEE_Reference + Calculator_Findings MEE section. | aoem-calculator + Network Grey + Theria Games | Current | T5 MEE pts conflict unresolved: multiplier implies 200, troop table shows 160 — verify in-game |
| events/AIGA_Events_Reference.md | All competitive events — overview, Legendary Advent wheel (5-spin/4,200 IC confirmed, token mechanic: 1 per spin, 60 = 15 medals, secondary milestones 30% probabilistic), Battle of Dawn, Wonder Contest, Starfall Vein, Frontline Escort stub. Merged from Events_Index + Battle_of_Dawn_Reference + Wonder_Contest + Starfall_Vein PDF + Calculator_Findings wheel sections. | Theria Games + AoE Mobile Guides + Fandom Wiki + Network Grey | Current | Frontline Escort full scoring. Golden Expedition full rules. |

### /base/ — 5 files

| File | Description | Source | Status | Known gaps |
|---|---|---|---|---|
| base/AIGA_Buildings_Reference.md | All 24 buildings lv1-30 — full costs, prerequisites, power values. | aoem-calculator (buildings.json) | Current | Smithy building costs missing from source |
| base/AIGA_Town_Centre_Reference.md | TC upgrade prerequisites lv6-30 and key milestones. | aoem-calculator | Current | None |
| base/AIGA_Research_Reference.md | University military and economy research trees, Mercenary Camp T1 and T2 costs (48 technologies), Legendary Advent wheel MGE scoring. Merged from Research_Mercenary_Wheel + Research_Technology. | aoem-calculator + community | Current | University military tree node unlock levels incomplete |
| base/AIGA_Troop_Training_Reference.md | Training costs T1-T7, promotion costs, MGE/MEE pts per troop, gather load. | aoem-calculator (MIT) | Current | None |
| base/AIGA_Healing_Reference.md | Healing costs T1-T7, heal vs retrain comparison. | aoem-calculator (MIT) | Current | None |

### /economy/ — 4 files

| File | Description | Source | Status | Known gaps |
|---|---|---|---|---|
| economy/AIGA_Gathering_Reference.md | Resource nodes lv1-9, speed and capacity, troop load by tier, optimal hero lineup. | aoem-calculator | Current | Node lv2 capacity appears anomalous — verify |
| economy/AIGA_Free_Coins_Reference.md | Free Empire Coin sources, farming methods, priority spend guide. | Community / Network Grey | Current | None documented |
| economy/AIGA_Items_Store_Reference.md | In-game items, store inventory, recommended purchases. | Community | Current | None documented |
| economy/AIGA_VIP_Reference.md | VIP levels, benefits, point costs. | Community | Current | Verify current VIP tier caps in-game |

### /system/ — 9 files (not bot-facing)

| File | Description | Version | Status |
|---|---|---|---|
| system/AIGA_System_Prompt_v3_FINAL.md | Master system prompt — identity, rules, condensed game data for bot context | v3.0 FINAL | Current |
| system/AIGA_Onboarding_KYC_Reference.md | Player onboarding flow, KYC tiers, response depth rules | v1.0 | Current |
| system/AIGA_Game_Overview_Reference.md | Game introduction and core mechanics overview — onboarding context only, not a query target | v1.0 | Current |
| system/AIGA_Legal_ProximaBeta_Reference.md | Official AoEM Privacy Policy (Jan 2026) and EULA — IP ownership, 18+ restriction, required disclaimer | v1.0 | Current |
| system/AIGA_Web_Designer_Guide.docx | WordPress/PayFast setup guide for web designer | v1.0 | Current |
| system/AIGA_Thread_Handoff.docx | Internal development session handoff notes | v1.0 | Current |
| system/AIGA_Todo_List.html | Interactive project task tracker | v2 | Active |
| system/AIGA_March_Analyser.html | Interactive march analysis tool | — | Active |
| system/AIGA_Workbook_v2.xlsx | War Chest player workbook template | v2 | Active — full template pending |

### /system/source/ — 2 files (archived PDFs, not bot-facing)

| File | Description | Status |
|---|---|---|
| system/source/Battle_of_Dawn_Decree.pdf | Official Battle of Dawn decree — source material. Content extracted into events/AIGA_Events_Reference.md. | Archived |
| system/source/LuBu_Mercenary_Comparison.pdf | Lu Bu mercenary comparison — source material. Content extracted into heroes/AIGA_Hero_Builds_Reference.md. | Archived |

---

## Document Count Summary

| Folder | Files | Bot-facing |
|---|---|---|
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
|---|---|
| AIGA_Hero_Complete_Reference.md (v1) | Superseded by v3 |
| AIGA_Hero_Complete_Reference_v2.md | Superseded by v3 |

### Step 2 — Content merges then delete source file

| Source file | Merge target | Action |
|---|---|---|
| AIGA_Hero_Complete_Reference_v3.md | heroes/AIGA_Hero_Complete_Reference.md | Rename — base file |
| AIGA_Hero_Data_Verified.md | heroes/AIGA_Hero_Complete_Reference.md | Append verified data section |
| AIGA_Hero_Builds_Reference_S_Tiers.md | heroes/AIGA_Hero_Builds_Reference.md | Rename — base file |
| LuBu_Mercenary_Comparison.pdf | heroes/AIGA_Hero_Builds_Reference.md | Extract and append — move PDF to system/source/ |
| AIGA_Hero_Formation_Reference.md | march/AIGA_March_Reference.md | Append formation section |
| AIGA_March_Compositions_Reference.md | march/AIGA_March_Reference.md | Rename — base file |
| AIGA_Gear_Gems_Reference.md | gear/AIGA_Gear_Reference.md | Rename — base file |
| AIGA_Gear_Stats_Addendum.md | gear/AIGA_Gear_Reference.md | Append stats section |
| AIGA_Rings_Reference.md | gear/AIGA_Rings_Reference.md | Rename — base file |
| AIGA_Rings_Skills_Addendum.md | gear/AIGA_Rings_Reference.md | Append skills section |
| AIGA_Research_Mercenary_Wheel_Reference.md | base/AIGA_Research_Reference.md | Rename — base file |
| AIGA_Research_Technology_Reference.md | base/AIGA_Research_Reference.md | Append technology section |
| AIGA_Game_Mechanics_Reference.md | combat/AIGA_Game_Mechanics_Reference.md | Move to folder — base file |
| AIGA_Combat_PvP_Addendum.md | combat/AIGA_Game_Mechanics_Reference.md | Append PvP section |
| AIGA_WorldMap_Mechanics_Addendum.md | combat/AIGA_Game_Mechanics_Reference.md | Append world map section |
| AIGA_Game_Modes_Addendum.md | combat/AIGA_Game_Mechanics_Reference.md | Append game modes section |
| AIGA_MEE_Reference.md | events/AIGA_MEE_Reference.md | Rename — base file |
| AIGA_MEE_Guide_v1.md | events/AIGA_MEE_Reference.md | Append guide content |
| AIGA_MEE_Guide_v1_1.pdf | events/AIGA_MEE_Reference.md | Extract and append — delete PDF after |
| AIGA_Events_Index_Reference.md | events/AIGA_Events_Reference.md | Rename — base file |
| AIGA_Battle_of_Dawn_Reference.md | events/AIGA_Events_Reference.md | Append Battle of Dawn section |
| AIGA_Wonder_Contest_Reference.md | events/AIGA_Events_Reference.md | Append Wonder Contest section |
| AIGA_Starfall_Vein_Reference.pdf | events/AIGA_Events_Reference.md | Extract and append — delete PDF after |
| Battle_of_Dawn_Decree.pdf | system/source/ | Move only — no content extraction needed |
| AIGA_Calculator_Findings_Addendum.md | Multiple (see Step 2a) | Migrate then delete |

### Step 2a — Calculator Findings data migration targets

| Data | Destination |
|---|---|
| Gem rarity tiers (10 levels confirmed, Common through Mythic IV) | gear/AIGA_Gear_Reference.md |
| Lightning crystals as confirmed upgrade material | gear/AIGA_Gear_Reference.md |
| Gem stat types per slot confirmed | gear/AIGA_Gear_Reference.md |
| Jeweler's Marks as confirmed ring upgrade material | gear/AIGA_Rings_Reference.md |
| Advent Wheel secondary milestone medals — 30% probabilistic | events/AIGA_Events_Reference.md |
| MEE training days — Days II, IV, V confirmed | events/AIGA_MEE_Reference.md |
| Hero sub-rank structure data | heroes/AIGA_Hero_XP_Skills.md |
| XP tome denominations (lv2=500, lv3=1,000, lv4=10,000, lv5=50,000, lv6=100,000) | heroes/AIGA_Hero_XP_Skills.md |
| MGE gear calculation — Smithy level dependency confirmed | events/AIGA_MGE_Reference.md |

### Step 3 — Update bot.py

**3a — Recursive glob (required — current glob misses all subfolders)**

```python
# Before
knowledge_dir.glob("*.md")

# After
knowledge_dir.glob("**/*.md")
```

**3b — KEYWORD_MAP with updated subfolder paths**

```python
KEYWORD_MAP = {
    # Heroes
    "hero":             "heroes/AIGA_Hero_Complete_Reference.md",
    "heroes":           "heroes/AIGA_Hero_Complete_Reference.md",
    "build":            "heroes/AIGA_Hero_Builds_Reference.md",
    "builds":           "heroes/AIGA_Hero_Builds_Reference.md",
    "skill":            "heroes/AIGA_Hero_Skills_Library.md",
    "skills":           "heroes/AIGA_Hero_Skills_Library.md",
    "fragment":         "heroes/AIGA_Hero_Skills_Library.md",
    "tier":             "heroes/AIGA_Hero_Tier_List.md",
    "xp":               "heroes/AIGA_Hero_XP_Skills.md",
    "level":            "heroes/AIGA_Hero_XP_Skills.md",
    "medal":            "heroes/AIGA_Hero_XP_Skills.md",
    "rank":             "heroes/AIGA_Hero_XP_Skills.md",
    "tome":             "heroes/AIGA_Hero_XP_Skills.md",
    "mount":            "heroes/AIGA_Mount_System.md",
    "breed":            "heroes/AIGA_Mount_System.md",
    "breeding":         "heroes/AIGA_Mount_System.md",
    "temperament":      "heroes/AIGA_Mount_System.md",
    "adornment":        "heroes/AIGA_Mount_System.md",
    # Gear
    "gear":             "gear/AIGA_Gear_Reference.md",
    "forge":            "gear/AIGA_Gear_Reference.md",
    "gem":              "gear/AIGA_Gear_Reference.md",
    "gems":             "gear/AIGA_Gear_Reference.md",
    "meteorite":        "gear/AIGA_Gear_Reference.md",
    "ring":             "gear/AIGA_Rings_Reference.md",
    "rings":            "gear/AIGA_Rings_Reference.md",
    # March
    "march":            "march/AIGA_March_Reference.md",
    "formation":        "march/AIGA_March_Reference.md",
    "lineup":           "march/AIGA_March_Reference.md",
    "composition":      "march/AIGA_March_Reference.md",
    "rally":            "march/AIGA_March_Reference.md",
    # Combat
    "combat":           "combat/AIGA_Game_Mechanics_Reference.md",
    "attack":           "combat/AIGA_Game_Mechanics_Reference.md",
    "battle":           "combat/AIGA_Game_Mechanics_Reference.md",
    "map":              "combat/AIGA_Game_Mechanics_Reference.md",
    "pvp":              "combat/AIGA_Game_Mechanics_Reference.md",
    "stamina":          "combat/AIGA_Game_Mechanics_Reference.md",
    "territory":        "combat/AIGA_Game_Mechanics_Reference.md",
    "civ":              "combat/AIGA_Civilizations_Reference.md",
    "civilization":     "combat/AIGA_Civilizations_Reference.md",
    "civilisation":     "combat/AIGA_Civilizations_Reference.md",
    "landmark":         "combat/AIGA_Civilizations_Reference.md",
    # Events
    "mge":              "events/AIGA_MGE_Reference.md",
    "governor":         "events/AIGA_MGE_Reference.md",
    "mee":              "events/AIGA_MEE_Reference.md",
    "empire":           "events/AIGA_MEE_Reference.md",
    "event":            "events/AIGA_Events_Reference.md",
    "events":           "events/AIGA_Events_Reference.md",
    "wheel":            "events/AIGA_Events_Reference.md",
    "advent":           "events/AIGA_Events_Reference.md",
    "spin":             "events/AIGA_Events_Reference.md",
    "starfall":         "events/AIGA_Events_Reference.md",
    "wonder":           "events/AIGA_Events_Reference.md",
    "dawn":             "events/AIGA_Events_Reference.md",
    "token":            "events/AIGA_Events_Reference.md",
    # Base
    "building":         "base/AIGA_Buildings_Reference.md",
    "buildings":        "base/AIGA_Buildings_Reference.md",
    "barracks":         "base/AIGA_Buildings_Reference.md",
    "tc":               "base/AIGA_Town_Centre_Reference.md",
    "town":             "base/AIGA_Town_Centre_Reference.md",
    "prerequisite":     "base/AIGA_Town_Centre_Reference.md",
    "research":         "base/AIGA_Research_Reference.md",
    "university":       "base/AIGA_Research_Reference.md",
    "mercenary":        "base/AIGA_Research_Reference.md",
    "technology":       "base/AIGA_Research_Reference.md",
    "troop":            "base/AIGA_Troop_Training_Reference.md",
    "troops":           "base/AIGA_Troop_Training_Reference.md",
    "training":         "base/AIGA_Troop_Training_Reference.md",
    "t4":               "base/AIGA_Troop_Training_Reference.md",
    "t5":               "base/AIGA_Troop_Training_Reference.md",
    "heal":             "base/AIGA_Healing_Reference.md",
    "healing":          "base/AIGA_Healing_Reference.md",
    "hospital":         "base/AIGA_Healing_Reference.md",
    # Economy
    "gather":           "economy/AIGA_Gathering_Reference.md",
    "gathering":        "economy/AIGA_Gathering_Reference.md",
    "resources":        "economy/AIGA_Gathering_Reference.md",
    "node":             "economy/AIGA_Gathering_Reference.md",
    "coins":            "economy/AIGA_Free_Coins_Reference.md",
    "currency":         "economy/AIGA_Free_Coins_Reference.md",
    "free":             "economy/AIGA_Free_Coins_Reference.md",
    "store":            "economy/AIGA_Items_Store_Reference.md",
    "shop":             "economy/AIGA_Items_Store_Reference.md",
    "items":            "economy/AIGA_Items_Store_Reference.md",
    "vip":              "economy/AIGA_VIP_Reference.md",
}
```

---

## Source Hierarchy

When data conflicts between sources, apply this priority order:

| Priority | Source | Trust level |
|---|---|---|
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
- AIGA_Legal_AoEMobileGuides_Reference.md — missing from project, needs recreation

### High
- Maya Mutuala and Yellet — post-Oct 2025, not yet in any KB file
- Skill3/skill4 recommendations — pending AT data entry for majority of heroes
- Hero pairings — flagged KNOWLEDGE GAP in v8 for most heroes
- Frontline Escort event — full mechanics and scoring
- Golden Expedition — full scoring and rules

### Medium
- Gem upgrade costs — 10 tiers now named, upgrade material costs unknown
- Jeweler's Marks exact quantities per ring upgrade level
- Lightning crystals exact gear level thresholds
- Holy Sites mechanics
- Smithy building costs

### Resolved since v1.4
- Starfall Vein scoring — now in events/AIGA_Events_Reference.md
- Wonder Contest mechanics — now in events/AIGA_Events_Reference.md
- Gem rarity tier names — 10 levels confirmed
- Advent Wheel token mechanic — documented
- MEE day-specific training days — Days II, IV, V confirmed
- XP tome denominations — confirmed
- Advent wheel pack size — 5-spin at 4,200 IC confirmed
- Exact trait values for all mounts — 30 traits confirmed in-game (Gustav, S371 June 2026), full catalogue with effect ranges now in heroes/AIGA_Mount_System.md
- Ring canonical count — confirmed 35 in-game (10 T0 / 14 T1 / 11 T2). Ring of Mamba absent. Sacred Sage is 11th T2. v2.2 T2 count error corrected in gear/AIGA_Rings_Reference.md

---

## Data Verification Queue

| Item | Issue | Priority |
|---|---|---|
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

> "AIGA is an independent fan advisory service created by Network Grey. Not affiliated with, endorsed by, or associated with TiMi Studio Group, Level Infinite, Proxima Beta Pte. Limited, Microsoft, or Xbox Game Studios. Age of Empires and Age of Empires Mobile are trademarks of Microsoft Corporation."

South Africa minimum age per official Privacy Policy: **18+** — must be displayed on Discord server and web app.

---

*Maintained by Network Grey. Update this index at the end of every knowledge base session. Version and date every revision in the revision history table.*

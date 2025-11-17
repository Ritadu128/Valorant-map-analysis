**### Overview**
This project combines user research and basic data analysis to understand how Valorant players experience different maps, how map design influences performance, and what factors shape player satisfaction.
The goal is to connect player behavior, map-level performance data, and self-reported experience to generate insights that can inform product or map improvements in gaming environments.

**### Data Sources**
- Player Survey Data (`data/survey_data.xlsx`):
  - Map preference (favorite / least favorite)
  - Player roles (Duelist, Controller, Initiator, Sentinel)
  - Gameplay style, communication habits, emotional experience
  - Pain points like coordination issues or map unfamiliarity
- Match Performance Dataset (`data/player_stats.csv`):
  - Kill, Death, ADR, KAST, Headshot %
  - Cleaned & anonymized for analysis

**### Methods**
Mixed-method approach
Quantitative:
- Grouped performance metrics by map (e.g., average K/D, win rate)
- Compared performance patterns based on different maps

Qualitative:
- Processed survey responses to identify common motivations, preferred roles, and gameplay styles.  
- Highlighted frustration points, such as coordination challenges, map design, or team behavior issues.  


**### Result**
- There was no clear performance difference between liked maps and disliked maps.
- All five players showed stable performance regardless of which map they played.
- Even on maps that survey participants frequently complained about, the selected players maintained consistent K/D, ADR, and KAST.

**### Project Files**
- `image/` – full EDA and visualization
- map_analysis.py – main analysis script + data cleaning
- `data/` – raw & survey datasets
- `survey/` – questionnaire and methodology

**### How to Run**
map_analysis.py

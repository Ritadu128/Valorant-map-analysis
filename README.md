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

**### Methods(Mixed-method approach)**
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

**### Interpretation**
1. Map preference is mostly psychological
Players may “dislike” a map because:
- They feel less comfortable
- They get frustrated by certain layouts
- They have negative memory associated with a map
...But this emotional dislike does not necessarily reduce performance, especially for experienced players.

2. Skill level moderates the impact of map differences
For highly skilled players (like the official player in the dataset):
- Strong fundamentals
- Adaptability
- Team coordination
...allow them to perform consistently across all maps.
This reduces the performance gap that casual players feel they experience.

3. Map design may shape user sentiment more than actual gameplay ability
Maps with unique layouts or more complex rotations tend to generate stronger psychological reactions.
Even if performance doesn’t drop, players feel they might play worse because:
- The map design feels uncomfortable
- They get more frustrated during the match
That frustration then becomes a user experience issue, not necessarily a performance issue.

4. This matches how Valorant intentionally designs maps(Note: These categories are inferred from player experience and community discussions, not officially labeled by Riot Games.)
Valorant’s map pool has:
- Comfort maps
- High friction maps
This variety:
- Keeps gameplay fresh
- Encourages players to improve
- Gives the community things to love/hate
- Prevents gameplay fatigue
So the emotional "preference gap" between maps may actually help player retention because it keeps the game interesting.


**### Project Files**
- `image/` – full EDA and visualization
- map_analysis.py – main analysis script + data cleaning
- `data/` – raw & survey datasets
- `survey/` – questionnaire and methodology

**### How to Run**
map_analysis.py

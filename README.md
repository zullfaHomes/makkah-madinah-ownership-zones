# Makkah and Madinah non-Saudi ownership zones

The 22 designated zones in which non-Saudis may buy property in Makkah (12 zones) and Madinah
(10 zones), as reusable data. Each zone has its boundary, its official code and names in English
and Arabic, its area, and three measured distances to the Grand Mosque or the Prophet's Mosque,
with who may buy there and what may be held.

The Real Estate General Authority (REGA) publishes these boundaries only on an interactive map, the
[Saudi Properties portal](https://saudiproperties.rega.gov.sa/zones). This dataset puts them in a
form a researcher, a journalist, a developer or a mapping tool can use directly. It is compiled and
kept current by [Zullfa](https://zullfa.com), the independent guide for Muslims abroad buying
property in Makkah and Madinah.

- **Files:** [`data/zones.geojson`](data/zones.geojson) (boundaries and every field) and
  [`data/zones.csv`](data/zones.csv) (one row per zone, no geometry)
- **Boundaries retrieved:** 2 November 2026 from the Saudi Properties portal
- **Live version:** <https://zullfa.com/data/zones.geojson>, rebuilt with every update to the site
- **Licence:** [CC BY 4.0](LICENSE). Credit "Zullfa — https://zullfa.com" (see [Cite](#cite))

## The zones

Sorted by distance from the mosque, nearest first. Each name links to the zone's page on Zullfa,
with its map, what is being built there and what a buyer should check.

| City | Zone | Code | Area (m²) | Nearest edge to the mosque (m) | On foot |
|---|---|---|---:|---:|---|
| Makkah | [Burj Ajyad](https://zullfa.com/makkah/zones/burj-ajyad) | `L197` | 5,578 | 314 | 5–6 min |
| Makkah | [Abraj Makkah](https://zullfa.com/makkah/zones/abraj-makkah) | `L1048` | 13,021 | 321 | 5–6 min |
| Makkah | [Jabal Omar](https://zullfa.com/makkah/zones/jabal-omar) | `L008` | 235,869 | 452 | 7–8 min |
| Madinah | [Rua Al-Madinah](https://zullfa.com/madinah/zones/rua-al-madinah) | `L048` | 1,381,869 | 652 | 10–11 min |
| Makkah | [King Salman Gate](https://zullfa.com/makkah/zones/king-salman-gate) | `L062` | 964,021 | 685 | 10–12 min |
| Madinah | [Madinah Zone 1](https://zullfa.com/madinah/zones/madinah-zone-1) | `L354` | 587,409 | 713 | 10–12 min |
| Makkah | [Masar](https://zullfa.com/makkah/zones/masar) | `L051` | 1,388,213 | 819 | 12–14 min |
| Makkah | [Makkah Zone 2](https://zullfa.com/makkah/zones/makkah-zone-2) | `L056` | 686,060 | 1,283 | 18–22 min |
| Makkah | [Thakher Makkah](https://zullfa.com/makkah/zones/thakher-makkah) | `L052` | 303,959 | 1,973 | 28–33 min |
| Makkah | [Makkah Zone 1](https://zullfa.com/makkah/zones/makkah-zone-1) | `L055` | 698,929 | 2,449 | 35–41 min |
| Madinah | [Downtown Madinah](https://zullfa.com/madinah/zones/downtown-madinah) | `L200` | 414,878 | 3,024 | 42–51 min |
| Madinah | [Madinah Zone 2](https://zullfa.com/madinah/zones/madinah-zone-2) | `L300` | 580,884 | 3,123 | 44–53 min |
| Madinah | [Darat Al-Hijra](https://zullfa.com/madinah/zones/darat-al-hijra) | `L011` | 1,129,279 | 3,165 | 44–53 min |
| Makkah | [Makkah Zone 3](https://zullfa.com/makkah/zones/makkah-zone-3) | `L337` | 1,293,389 | 3,697 | 52–62 min |
| Madinah | [Knowledge Economic City](https://zullfa.com/madinah/zones/knowledge-economic-city) | `L023` | 6,816,148 | 4,814 | over an hour |
| Makkah | [Tilal Village](https://zullfa.com/makkah/zones/tilal-village) | `L360` | 336,700 | 6,365 | over an hour |
| Madinah | [Al-Mahwa](https://zullfa.com/madinah/zones/al-mahwa) | `L316` | 300,084 | 8,313 | over an hour |
| Madinah | [Mishraf](https://zullfa.com/madinah/zones/mishraf) | `L211` | 469,033 | 8,943 | over an hour |
| Madinah | [Al-Ghurra](https://zullfa.com/madinah/zones/al-ghurra) | `L311` | 2,377,318 | 10,834 | over an hour |
| Madinah | [Diyar Al-Maqar](https://zullfa.com/madinah/zones/diyar-al-maqar) | `L312` | 191,983 | 12,386 | over an hour |
| Makkah | [Al-Manar](https://zullfa.com/makkah/zones/al-manar) | `L053` | 566,095 | 14,625 | over an hour |
| Makkah | [Dahiyat Sumou](https://zullfa.com/makkah/zones/dahiyat-sumou) | `L054` | 1,672,001 | 16,711 | over an hour |

## Fields

| Field | Meaning |
|---|---|
| `zone_code` | The register's own code for the zone, as shown on the portal |
| `name`, `name_official`, `name_ar` | Zullfa's English name, the portal's English name, and the Arabic name |
| `city` | `makkah` or `madinah` |
| `area_m2` | Area of the published boundary, in square metres |
| `distance_to_haram_m.boundary` | Straight line from the zone's nearest boundary point to the mosque |
| `distance_to_haram_m.farthest` | Straight line from the zone's farthest boundary point |
| `distance_to_haram_m.centroid` | Straight line from the zone's area-weighted centre |
| `walk_minutes_min`, `walk_minutes_max` | The nearest distance at 1.2 and 1.0 m/s; empty when it is over an hour |
| `within_an_hour_on_foot` | Whether the nearest edge is within an hour's walk |
| `eligible_buyers` | Who the portal lists as able to buy in the zone |
| `ownership_pct`, `usufruct_max_years` | The ownership share and the longest usufruct the portal shows |
| `permitted_uses`, `excluded_uses` | Property uses the portal lists for the zone |
| `permitted_rights` | Real rights that may be held there, in the portal's words |
| `gazetted_on` | The date the portal gives for the zone's designation, where it gives one |
| `url` | The zone's page on Zullfa |
| `source_url`, `retrieved` | Where and when the boundary was taken |

In the CSV, the distances are split into three columns, and list fields are joined with `;`.

## Method

- **Boundaries** come from the Saudi Properties portal's own geometry, not traced from a picture.
- **Distances** are haversine straight lines to the Grand Mosque (21.422487, 39.826206) or the
  Prophet's Mosque (24.467667, 39.611111). They are measured on the full published boundary, before
  the boundary is simplified.
- **The geometry in this file** is that boundary simplified to about 10 metres for drawing, with rings
  kept separate so holes render. A distance computed from this geometry will differ slightly from
  the published figure.
- **Walking times** are a floor, not a route: the straight-line distance at a steady pace. Real
  streets, tunnels and crowds add time.

## Updating

```
python3 scripts/build.py            # take the current file from zullfa.com and rebuild the CSV
python3 scripts/build.py --offline  # rebuild the CSV only
```

Zullfa re-reads the portal when REGA changes a zone. Each change here is a commit and a release, so
any earlier version can still be cited.

## Cite

> Zullfa (2026). *Makkah and Madinah non-Saudi ownership zones* [Data set]. https://zullfa.com/data/zones.geojson

GitHub's "Cite this repository" button gives this in other formats from [`CITATION.cff`](CITATION.cff).
Each release is also archived with a DOI on Zenodo.

## Not legal advice

This is a reference dataset, not legal advice. Zone boundaries and rules can change. Before a
purchase, check the zone on the Saudi Properties portal and with a REGA-licensed broker or a lawyer.
Zullfa's [law tracker](https://zullfa.com/law-tracker) follows the rules, and its
[figures page](https://zullfa.com/figures) has more data on the same terms.

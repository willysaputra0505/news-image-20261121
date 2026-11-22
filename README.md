# The World in One Image — Saturday, 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/willysaputra0505/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/willysaputra0505/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A single 1024×1024 poster summing up the world's news of **Saturday, 21 November 2026** — generated deterministically with Python (PIL) and delivered by a small Node program.

## The day in six stories

1. **Iran hits US bases in Bahrain** — the IRGC claims missile and drone strikes on al-Riffa and Awali; Bahrain says a civilian industrial site burned, with no injuries. *(Reuters / Euronews)*
2. **Mexico captures 'El Chapo Isidro'** — FBI most-wanted cartel boss Fausto Isidro Meza Flores seized in Sinaloa; the cartel violence that followed left at least 11 dead. *(AP / Reuters)*
3. **Russian strike hits Zelenskyy's hometown** — a triple-tap attack on Kryvyi Rih kills a boy, 7, and a paramedic; 60 wounded, including children. *(AP / CNN)*
4. **COP31 talks run into overtime** — the Antalya summit passes its deadline with no deal as nearly 200 nations split over fossil fuels. *(AP)*
5. **AI sell-off drags stocks into correction** — the S&P 500 falls 3.7%; the Nasdaq erases its 2026 gains and the Nikkei drops 5.06%. *(One Turn)*
6. **Trump defends Putin ties; Zelenskyy hits back** — "For us, he is a killer," Zelenskyy says after the Shenzhen summit with Trump and Xi. *(CNN)*

Also today: the EU unveils a €1.78 trillion budget for 2028–2034; Argentina approves a $50bn LNG export project; Wolbachia mosquitoes cut dengue 69% in a Brazil trial; the EU sends Ukraine a record €7.9bn aid payment.

## Run it

```bash
# regenerate the poster (requires Python 3 + Pillow, DejaVu fonts)
python3 generate.py

# deliver it to the output directory (Node 22, stdlib only)
MAKEFUN_OUTPUT_DIR=/tmp/out node --experimental-strip-types main.ts
```

`main.ts` reads `entry.png` next to itself, checks it is within the 1 MiB limit, creates the output directory (`MAKEFUN_OUTPUT_DIR`, default `/output`) and copies the poster there.

## Files

- `generate.py` — the poster generator (PIL primitives only, no external assets)
- `entry.png` — the finished 1024×1024 poster
- `main.ts` — the delivery program

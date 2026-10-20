# Learned

What Market-Nana took from the facts and from research. Dated.

## 2026-10-19

- Every channel the product bots have used reaches a few dozen people at most,
  and none has produced a paid customer. The one sale came from Google search.
  (TRIED.md)
- The doors that closed are mostly about AI: Roll20, DriveThruRPG, TTRPG
  communities, Pinterest, the KDP forum's regulars. Any channel that runs
  through a community's goodwill should be expected to reject AI-made work.
- "AI agents run a business" is a crowded press story in 2026 (Andon Labs'
  store, Project Vend, a podcast season on an AI-agent startup). What the
  studio has that they don't: the bots built fine, and the internet wouldn't let
  them sell. (adversary, 10-19)
- A reporter's first question will be cost and hours, and the numbers page
  doesn't answer it yet.
- Halloween is too late for KDP sellers (vibe-cider: 3–4 week low-content
  reviews). The Trace Press printables are free with no mark, so parents and
  teachers are reach, not sales. Christmas is the KDP window.
- Sizecurve's own kill criterion is judged at the end of 10-20 UTC (48 of 50
  qualifying views on 10-19). If it fires, cider2 stops new work on it.

## 2026-10-19, later

- Correction: KDP's help page says puzzle and coloring books are generally not
  low-content, so the 3–4 week low-content review (above) probably doesn't
  apply to Puzzle Press books. The Halloween line stands for Trace Press
  worksheets.
- At least five KDP puzzle generators advertise free, no-watermark output.
  Puzzle Press's $19 has to buy something they don't give, or no comparison
  favours it. (round 2, killed)
- KDP educators mostly earn from Book Bolt's 25% recurring affiliate cut. A
  one-time $19 tool gives them almost nothing to recommend it for.
- Christmas submit-by dates (vibe-cider's count from KDP's timelines, 10-19):
  a puzzle book not marked low-content, about 19 November for Black Friday; a
  tracing book marked low-content, 30 October. On the Christmas pages now.
- Sizecurve's kill criterion is engaged views on its own site (at least 50) and
  10 stranger checks, window now ending 10-27 (cider2). Checks are met; views
  48. A trade piece that sends two real readers to the study page passes it.
  Installs are not the criterion.
- vibe-cider tested the five "free" KDP puzzle generators (10-19, no accounts,
  T = seen in the file): only PuzzleForge and kdpbook.io's single pages give a
  clean free file with no sign-up, and neither makes a cover, a page-count
  gutter or page numbers. Three of the five stamp a diagonal watermark on free
  output. Where Puzzle Press is behind: PuzzleForge's free interior is cleaner.
  Line every cell supports: "the whole KDP paperback, cover and gutter included,
  with no sign-up, for $19 once rather than a monthly plan."
- The 10-16 cross-promotion footer's `?from=` tags are unreadable: Cloudflare
  on the VibeCider zone gives paths and hosts, no query strings, no referrers
  (vibecider4). A tracked link only counts if it's a distinct path or the
  product's own counter (cider2's study-page counter, for example).

## 2026-10-19, traffic (Cloudflare, the boss's token)

- Two sources, and only one counts people. The zone's request counts
  (`httpRequests1dGroups`) are mostly our own bots: on 09-21, the biggest
  page-view day (11,169), the top senders were `node` and HeadlessChrome on
  Puzzle Press and Bulkhead, i.e. the bots' own tests. The "uniques" highs of
  10-15 to 10-19 are crawlers, link previews and the new subdomains. Don't quote
  either as visitors.
- The account's browser beacon (`rumPageloadEventsAdaptiveGroups`, sampled
  about 1 in 10 until mid-October) counts real page loads in a browser and
  gives the referrer host. It does not give query strings. Filter it to our
  hosts and drop ChromeHeadless and Unknown. This corrects the line above: a
  referrer host is readable. The `?from=` value still isn't.
- Human peak, by far: **09-29 to 10-01**, about 400, 330 and 150 page loads.
  Nearly all on the studio home page, landing on `/` with no referrer, from the
  US, Germany, the UK and Canada, desktop and phone alike, starting about 09:00
  UTC on 09-29. Then they read the zoo (/zoo, vibe-cider, the numbers, cider3's
  log) and some went on to Puzzle Press, Bulkhead and Trace Press. On 09-29 and
  09-30, Google sent about 50 more to the home page: people searching the name.
- What came before it: no bot log or TRIED line explains it. The one sale (from
  Google) was at 03:08 UTC, before the surge began. A no-referrer landing on
  `/`, followed by people searching the name, looks like a mention where the
  link couldn't be clicked: a chat, an email, a video or a spoken mention. Asked
  the boss whether he shared it.
- The next human days are far smaller: 09-18 (Puzzle Press, about 120), 09-21
  (about 120: Bulkhead from the r/battlemaps post and the Reddit app, Puzzle
  Press from r/KDP), 10-15 (about 100: Close of Day's reviewer through Shopify
  admin, plus the r/SideProject day). Every outside source on record (Reddit,
  Owlbear, Google, Shopify admin, t.co, Facebook, ChatGPT) sent 10 to 50 page
  loads in total, ever.
- The 10-16 cross-promotion footer: from 10-16 to 10-19, none of about 83 human page
  loads on Puzzle Press, Trace Press and Bulkhead led to a recorded VibeCider
  page load. Our own pages have too few people for a link between them to send
  anyone.
- Blind spots: Sizecurve's pages block the beacon (`script-src 'self'`) and
  send `referrer-policy: no-referrer`, so Sizecurve is measured only by
  cider2's own counter. Visitors who block the beacon aren't counted anywhere,
  so every beacon figure is a floor. Sampling is about 1 in 10 before mid-October
  and about 1 in 1 after.

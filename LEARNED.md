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
  09-30, Google sent about 50 more to the home page: people searching the name,
  or clicks in Gmail on the web, which also show up as Google.
- **Solved (the boss's screenshot, 10-19): it was him.** On the night of 09-28 he
  commented in an r/ClaudeCode thread about someone else's AI-run business
  that made $0: "Bananafest-destiny.com one of my 3 app developer bots just
  made its first sale tonight". 15,637 views, 29 upvotes, plus his replies
  further down (3.5k to 8.3k views each). See TRIED and FACTS. The paragraph
  below was written before he said so.
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
- Link-preview fetches show where a link was pasted. For the 09-29 crowd:
  WhatsApp (09-29 14:00Z), X (15:00Z), Discord and Telegram (09-30), and
  LinkedIn (10-01 02:00Z, the boss's launch post for Sizecurve). All of them come after the
  surge began at about 09:00Z, so they're people passing it on, not the
  start. Many of the crowd's browsers were the kind that strip referrers
  (Brave, the DuckDuckGo browser, Firefox for Android). Their pages: the home
  page, /team, the numbers, the zoo, and the first-sale story.
- Why the boss's comment worked when the bots' posts didn't. About 1 in 40 of
  its viewers came to look. vibecider4's r/SideProject post got about 1 in 270,
  and cider3's r/OwlbearRodeo post about 1 in 400. The comment was:
  - a person, not a bot, speaking as himself;
  - in a thread already about the exact subject (an AI running a business);
  - carrying news (a first sale, that night) against the thread's $0;
  - in a crowd that wants the experiment (Claude Code users), not the product.
  - The domain was plain text, not a link. Nothing came in from a Reddit
    referrer, so people typed it or searched for it.
- What it didn't do: sell. The crowd read the story and left, because no product
  then was for Claude Code users. The VibeCider bot came 10-16, and the site's
  free "check my slop" security check is aimed at people who build apps with
  AI.
- So the story spreads best when the boss himself tells it, where people are
  already arguing about whether AI can run a business. A bot can't do this for
  him: it was his voice that worked.

## 2026-10-19, what the story can sell, and when

From the boss's answers (FACTS, "Reddit, the long game, kits") and round 5's
market-gate and adversary:

- **The story sells on results, and we don't have one yet.** The boss: "Kits
  would sell if the apps were making money." Market-gate's own killer said the
  same thing: a studio that made $18 can't sell a money machine. A kit, a
  course, an agent sold as a file: each asks the buyer to believe it works,
  and $18.09 is the proof on offer. So the story becomes money after an app
  does, not instead of one.
- **Until then, the story builds an audience.** The boss calls it "the long
  game", "SEO or social media… just not quick". What that game keeps is the
  people: an email list, plus his name in r/ClaudeCode. When an app does make
  money, those are the first people to tell, and the same story then sells.
  Market-gate's line: 1,000 or more emails reopens a paid newsletter and
  sponsors.
- **So the apps aren't off the hook.** The quickest way to monetize the story
  is still to get one product to a few paying customers. The story rounds
  should keep the crowd (the signup) and point it at what fits it. Rounds 1,
  3 and 4 still count.
- **Sequence:** the next r/ClaudeCode comment goes up only once the site can
  keep a visitor. Otherwise it's 09-29 again: 400 visits, nobody kept.

## 2026-10-19, money

- **There is no money to spend.** The boss: "I technically don't even have one
  dollar" (FACTS). Every test I plan costs $0. The only costs are the studio's
  Claude usage and the boss's hour, and both are already tight.
- **So I don't put paid options in front of him**, even as "your call". That
  covers buying a product, paid ads, sponsorships and paid tools. ~~Anything
  with a fee, such as a store's listing fee, is named in the plan as a blocker,
  not as a choice.~~ Wrong, the same night. The boss: "An id check isn't a
  kill. A small fee isn't a kill." A store's small fee or an ID check is an ask
  for him, with the cost in rough terms (§5). He decides; I don't drop the
  shelf for it. "No money" still rules out anything bigger than a small,
  one-time fee.
- **A first paying customer is worth more than any metric.** It's the first
  money the studio can spend. Rounds closest to a sale come first in the daily
  list: round 3 (Sizecurve, whose window ends 10-27) before the story rounds.

## 2026-10-19, the first bite

- **The boss is right that the studio pushes**, so "no outside push" was the
  wrong test. The question is whether a small push, our kind, turns into
  installs on the shelf, and then reviews.
- **On Shopify, the target is the first one or two merchants per app.** The
  boss: "nothing happens until you get some reviews". His reading fits
  cider2's count: 83% of 2026 ops-app launches have no review at all. So
  "eventually" doesn't come by itself for most apps. It comes when a push
  lands the first installs. That's my job, and it's narrow enough to aim at.
- **Push and spray pull opposite ways.** Our push is small: the boss's hour, a
  few emails, one comment. It works best on a few products, so spraying many
  new ones dilutes it. With three Shopify apps waiting for a first bite, the
  next pushes go to them, not to new products.
- **14 days asks for a first bite: one outside install.** I'd hoped it could
  measure being seen in search, but nobody can read listing views or search
  impressions (cider2, 10-19). The bar is cider2's: at least one install by a
  store that isn't ours or the reviewer's, with no ad money. Sizecurve got 0,
  so one already beats the only baseline we have.
- **Never buy or trade for a review.** Shopify's app store rules forbid it, and
  a removed review or a delisting costs more than waiting.

## 2026-10-19, podcasts

- **No podcast pitches until a product pays off.** That's from the boss (FACTS
  10-19). Any podcast booking puts him on air, and he won't do that before the
  bots make money. Dropped: round 1 items 6 (Shell Game) and 11 (How I AI), and
  round 3 item 5 (the Shopify podcast form).
- Round 1 items 4 and 5 (two podcasts) were sent before this. If either offers
  a slot, I draft him a short "not yet, maybe later".

## 2026-10-20, a Facebook referrer isn't a person

- I read 23 beacon page loads with a Facebook referrer (10-14 to 10-20) as
  people, and called them "the first pull any product has shown". vibe-cider's
  request log showed they were Meta's own servers drawing link previews. Each
  burst fell in the same minute as a facebookexternalhit fetch. One or two
  requests from Meta's network ran the page as plain Chrome, with no robot in
  the name, so they fired the beacon with a Facebook referrer. Cloudflare's
  bot filter let them through.
- vibe-cider wrote down the same trap on 09-29: "a same-minute fetch by a
  social crawler is not an arrival". I didn't apply it.
- **Before naming a social site as a source, check it against a request log:**
  a burst in the same minute as that site's preview fetcher, with no request
  from outside its network, is a preview. The beacon can't show the network;
  the product bot's request log can. Every beacon "human" count, the 10-16
  footer's 83 included, may hold a few of these.
- Pasting a link into Facebook or Messenger builds a preview even if no one
  clicks it. So these bursts show that someone shared the link, not that
  anyone read it.


## 2026-10-20, short video: the wall is the tap, not the schedule

From the boss's answer (FACTS, 10-20) and the round 7 research
(plan/2026-10-20-video-schedule.md):
- The house TikTok has a Website field that takes one link. The boss: "It
  allows me to put in one link." So TikTok can carry a tappable route out
  today, without 1,000 followers.
- Inference: "I had the links in bio before" most likely means links typed
  into the bio text. cider2 logged on 09-18 that the bio URL was plain text,
  not tappable. If so, until the Website field, no route off TikTok could be
  tapped, and its near-zero arrivals don't yet say what a tappable link would
  bring.
- Inference: one link per platform means each platform needs its own path
  (such as /tt), or its arrivals can't be told apart. In-app browsers often
  send no referrer.
- Inference: no evidence says posting often cuts views per post. What a clip
  gets depends on its opening and how long people watch, so the effort goes
  into the first 3 seconds and the tappable route, not the cadence.

## 2026-10-20, a Shopify listing costs the boss about an hour

From the boss's answer (FACTS, 10-20):
- Flatdesk and Close of Day took "maybe 2 hours" in all, spread "in between
  work and stuff". The screencast took the longest, and he automated
  Flatdesk's.
- Inference: about an hour of his per Shopify listing, and less when the
  screencast is scripted. His hours aren't what limits how many apps go up.
  Shopify's review queue and caps are.
- Inference: the Etsy option's guess was about 3 hours of his, so on his hours
  alone Etsy costs more than a Shopify listing, before its fee and ID check.

## 2026-10-20, on X the community has the readers, not the account

From the boss's screenshot (FACTS, 10-20) and the beacon:
- The account's plain posts got about 0 impressions. Its one post in X's Vibe
  Coding community (10-15) got 43 impressions and 1 link click in 5 days.
- The beacon has exactly 1 t.co load in 10-13 to 10-20: VibeCider's home page,
  10-16 at 12:02 CDT. So the click was a real page load, a day after the
  post. Whose, I can't tell.
- Inference: an account with almost no followers reaches people on X only
  through a community, whose members see the post. That's RULES §2.1 at small
  scale. One click doesn't make a rate, so the next post is a test, not a
  schedule.
- Inference: the community's rules (one introduction, then "only major
  feature updates", as r/vibecoding describes them) cap how often any one
  product can post. A story post should lead with a finding and link to the
  log, not a pay page.

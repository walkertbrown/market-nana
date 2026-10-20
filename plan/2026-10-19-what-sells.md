# Plan 2026-10-19 — find what would sell, before anyone builds it

Move: a new one, not in RULES §2 ("invent others"). **Choose the shelf before
the product.** Product: whatever each product bot builds next. The bots decide
what to build (§7). This round hands them evidence, not orders.

Why: the boss, 10-19 (FACTS): "So it all just goes back to how do we make apps
that sell. How do we find out what would sell". Also "Kits would sell if the
apps were making money". The story can't be monetized until a product works.

## What the record says (TRIED, LEARNED, the zoo log)

- **Building isn't the hard part.** Four bots shipped five products in 40 days.
- **Getting found is.** Every push channel failed or was shut: forums called
  it spam, Pinterest banned the domain, Roll20 and DriveThruRPG ban AI work, and
  60 cold emails got 0 replies.
- **The one sale came from search.** A KDP seller searched Google for a tool and
  paid 26 minutes later. The buyer already had the problem, already spent money
  on it, and found us by looking.
- ~~**The zoo log shows no demand test before a build.**~~ **Wrong** (the
  adversary). I searched for two words instead of reading what the bots did.
  Since 10-02, cider2's rules say no app starts without a written case: who
  buys, linked demand, reach, worth. cider2 ran shelf-first research on 10-02
  to 10-05, and Close of Day and Flatdesk came out of it. Sizecurve (09-13) had
  no such evidence. Puzzle Press's evidence was that rivals charge, and five
  free generators turned out to compete with it.
- **The boss's test for an idea** (zoo log): "something broad", with "a wide
  buyer pool and a thing people already pay for". Restaurant apps are out.

So, for bots that can build almost anything cheaply, the question isn't
"what's a good app". It's "**which shelf puts a new, small product in front of
buyers who already pay, and what's missing on that shelf?**"

## The method

1. **Our own shelves first.** From the zoo log: which store or search sent
   strangers to each product, and how many. That's Google for Puzzle Press, the
   Shopify App Store for Sizecurve, the Owlbear manifest and itch for Bulkhead,
   and so on.
2. **A shelf survey.** Six to eight stores where buyers search inside the
   store, a new entrant can get found without outside marketing, buyers
   already pay, AI-built work is allowed, and a bot can ship with no human in
   the loop. Each claim gets a number and a URL.
3. **The gaps on the best two or three:**
   - what buyers there search for and pay for;
   - what the top sellers' 1- and 2-star reviews say is missing;
   - where people say "I'd pay for…".
   The complaint is the spec.
4. **Market-gate on each candidate** before it reaches a product bot.
5. **Hand it over:** the candidates go to the product bots by mail and to the
   boss in this conversation. Each bot decides, and its reason goes in this log.

## Who it reaches

The product bots and the boss. Nothing here reaches a stranger. A product built
from it will reach its shelf's buyers.

## The cheapest real test

The research costs no money and none of the boss's time. It does use the
studio's Claude usage, which is the one real cost; the boss has hit the limit
before. For each candidate, the test is whatever market-gate names. For a bot,
shipping the smallest version on the right shelf may be the cheapest test
there is, because building is cheap. If so, the number is the shelf's own
count of impressions and installs in the first 14 days.

## The number that says it worked

(Changed after the adversary; see below.)

**Leading:** Close of Day's and Flatdesk's first 14 days, against cider2's
bars (10-19, before either was approved). Day 0 is the day of approval.
- **Pass:** at least 1 install, within 14 days, by a store that isn't ours or
  the reviewer's, with no ad money spent on that app.
- **Strong pass:** that store also accepts the subscription and is still
  installed on day 14.
- **Fail:** 0 outside installs.
- **Baseline:** Sizecurve, 0 outside installs by its day 14, and still 0.
- **Read from:** the Partner Dashboard's installs list (the boss) and each app's
  own install records (cider2). ~~Listing views and search impressions can't be
  read by anyone.~~ They can, with a GA4 tag on the listing (log, 10-19 late).
- **Changed 10-19 late:** the boss expects 0 installs in 14 days even from a
  good app, so the install bar moves to the scoreboard (11-30). The 14-day
  number becomes search views and "Add app" clicks, if the tag goes on. See the
  log.

Also: how many new candidates carry a buyer-side fact that exists today.

**Scoreboard:** a paid customer of a product chosen this way.

## Judged

- 10-23: the brief (shelves cider2 didn't read, push before pain).
- 14 days after Close of Day goes live, and 14 days after Flatdesk does.
- 11-30: a paid customer, or not.

## Adversary

Run 2026-10-19. Verdict: **change it. This round has already been run**, by
cider2, and its result isn't in yet.

- **cider2's lessons, which the plan ignored:**
  - Of about 2,200 Shopify apps launched in 2026 in 16 ops categories, 83% have
    no review. The five fastest-growing follow a law, a platform tool ending,
    or one outside network.
  - Each 2026 regulation had a full page of apps before merchants finished
    complaining.
  - A rival with few reviews after a year in front of the people asking means
    the pain doesn't convert to paying. So a complaint isn't a spec.
- **The shelves are saturated:**
  - Chrome Web Store listings 0–2 months old have a median of 4 users, and 74%
    have no rating
    ([exstats](https://exstats.com/blog/published-first-chrome-extension-now-what)).
  - The Shopify App Store has 22.5k apps, 6k+ of them added in a year, and 51%
    have no reviews
    ([Revenue Hunt](https://revenuehunt.com/state-of-the-shopify-app-economy/)).
  - Gumroad reportedly lists a product on Discover only after it has sales.
  - "A new entrant gets found without outside marketing" probably passes no
    shelf. Don't let the research lower the bar.
- **A shelf brings impressions, not buyers.** Sizecurve ranks about #20 for
  "size run". Its ad got 601 impressions, 2 clicks and 0 installs.
- **Other ways to find out first:**
  - Fake doors and pre-sales need traffic, which we lack.
  - The $50 commission has had one abandoned checkout and no sale.
  - Copying a proven product is what Puzzle Press was.
  - Buying a small product that already has traffic is the only way to buy
    distribution directly. A small one is a few thousand dollars; that's the
    boss's call, rough terms only (§5).
  - The bots' real edge is speed. Openings come from a law, a platform tool
    ending, or a new network, and those shelves fill within weeks. Bots build
    in days.
- **The numbers were wrong:**
  - "A bot takes up a candidate" measures how persuasive I am, not demand.
  - "A paid customer by 11-30" can't tell a bad method from a slow shelf
    (build, then review, then a median of 4 users).
  - "No human in the loop" is false on Shopify: Flatdesk needed the boss's
    screencast.
- **The deciding question:** once Close of Day and Flatdesk, both picked by
  this method, have been live 14 days, has App Store search brought them
  installs that Sizecurve never got? If yes, scale the method. If no, more
  shelves won't fix it.

What I changed:

1. **Judge the method that already ran.** I asked cider2 to write down, before
   each goes live, what Close of Day's and Flatdesk's first 14 days must show
   (listing views from search, installs, a paid shop), and which counts it can
   read. Judged 14 days after each goes live.
2. **Survey only the shelves cider2 didn't read.** That's the Chrome Web Store
   first, then the others. Entry test: three 2026 launches that reached paying
   users within 60 days with no outside push, with URLs. Otherwise the shelf is
   dropped. The research agent was redirected to this.
3. **Push before pain, not review mining.** Watch for laws taking effect,
   platform tools or APIs being retired, and new networks with no app yet.
   Score each opening by how soon a bot could be listed. If it earns its place,
   this becomes a standing weekly watch, handed to the product bots.
4. **Numbers:** every candidate carries one buyer-side fact that exists today
   (a store-suggested search phrase, dated threads of people asking, or a 2026
   entrant whose installs are growing), or it isn't passed on. The boss's hours
   per listing are counted.
5. ~~**Buying a product with traffic** goes to the boss as an option, not a plan.~~
   Struck 10-19: there's no money for it (FACTS).

## Log

**10-19, 21:00 CDT.** Planned. Research and adversary running in parallel.

**10-19, 21:05 CDT.** Adversary done; plan changed (above). My claim that no
bot tested demand was wrong, and I've corrected it to the boss. Mailed cider2
for the 14-day bars. Redirected the research.

**10-19, 21:08 CDT.** The boss: "I technically don't even have one dollar"
(FACTS). Buying a product is struck. Every test in this round, and in every
round, costs $0. The only spend is the studio's Claude usage and the boss's
hour.

**10-19, 21:11 CDT.** The boss asked: "Is there a scenario where 'throwing a
bunch of shit at the wall to see what sticks' is the best option that might
work?" My answer: yes, but only on a shelf that passes all four of these:
1. It shows a brand-new listing to people searching, with no outside push.
2. A listing takes none of the boss's hours and costs nothing.
3. It doesn't punish volume. Pinterest already flagged our domain, and KDP
   caps daily titles.
4. It shows impressions per listing within 14 days, so a dud is killed fast.

The studio's past throws mostly went where the wall can't be seen. Spraying
multiplies a shelf's hit rate; it can't create one. The 10-23 brief now says
which shelf, if any, passes all four. The research agents were asked for these
fields.

**10-19, 21:16 CDT.** The boss: "we will and have been pushing… it's all about
waiting for that one or two people to actually bite" (FACTS). What changes:
1. **The entry test drops "with no outside push".** A shelf qualifies if a
   small push of our kind (a few emails, one comment, one cite) can turn into
   installs there, and the shelf then shows the app to searchers on the
   strength of its reviews.
2. **The 14-day bars measure being seen** (listing views from search), not
   sales. Bites are judged on 11-30.
3. **The first bite comes before new products.** The Shopify apps need their
   first one or two merchants. The pushes aimed at them come before any new
   product: round 3 now (Sizecurve, with the boss), then Close of Day and
   Flatdesk once each is live. That's a round of its own; I'll plan it when
   Close of Day is approved.

**10-19, 21:22 CDT** (from `date`). **Log times corrected.** I had written
clock times from a guess, and some were later than the commits that hold them
(this log said 22:10 when the clock read 21:16). Every log time in plan/ is
now the time of the commit that first holds the line. The exceptions are
times a mail carries, which were already right. From now on a log time comes
from `date`.

**10-19, 21:30 CDT.** One of three shelf surveys is in (digital goods, finished
21:11). The other two (developer tools, app stores) are still running.
- **Closed to a new AI-built product:** Canva, Figma, Envato (AI banned or
  sellers not approved), Notion (paid selling has a waitlist of months),
  Gumroad Discover (needs about $100 of sales brought in first).
- **Etsy:** 86.5M buyers and a listing API. But there's a fee per listing, a
  photo-ID check, and some new shops pay a setup fee. With no money, that's
  a blocker.
- **KDP (selling books, not the tool):** first. Buyers' complaints on puzzle
  books are errors a program can check: words in word searches that aren't in
  the grid, "easy" crosswords full of rare words, sudoku with two solutions,
  memory books pitched at the wrong level. Puzzle Press already makes these
  books. The catches: new titles mostly get found through Amazon ads, the boss
  holds the account, and ~~3 titles a day is the cap~~ the cap is 2 new titles
  per format per week, since 09-21 (the boss's correction, below). Whether to publish is
  vibe-cider's call (§7).
- **Caveats:** Amazon now needs a sign-in to filter reviews by star, so the
  quotes can't be confirmed as 1- or 2-star. Etsy blocked the machine. Its one
  no-socials success story sells a course. No 2026 launch on any of these
  shelves passed the entry test cleanly.

**10-19, 21:38 CDT.** The coordinating research agent is done (finished 21:31).
- **Our own shelves:** no store's own search has ever brought a sale or a
  merchant install. Puzzle Press's one sale came from Google search.
- **Shelf survey:** every shelf but KDP is dropped.
  - Chrome: a registration fee, at most two published extensions, and no
    paying users found.
  - Etsy: fees and an ID check.
  - Gumroad, Notion, WordPress.org, VS Code, Raycast, Figma, Google Workspace,
    Atlassian, Wix: gated, unpaid, or company checks.
  - KDP "passes, weakly": three paperbacks published 10-02 to 10-16 already
    show a sales rank with no reviews and no Sponsored tag.
- **Spraying:** every shelf caps or bans near-duplicates, and KDP needs the
  boss's hands for each upload. With $0 and an hour a day, it isn't possible.
- **Push before pain:**
  - The no-tax-on-tips deduction (2025–2028): a tip log, with demand peaking
    January to April 2027. About 10 already listed.
  - Medicaid's work-hours rule from 2027-01-01: a log. None listed, but
    unproven demand.
  - Publisher's retirement: low.
- **Its top three, all KDP:**
  - a large-print, no-writing activity book for adults with memory loss;
  - a tip and overtime deduction log;
  - an error-free "easy" large-print Christmas word search for seniors.

**The boss, same hour** (FACTS): the cap is 2 a week, not 3 a day. He's right:
KDP's notice says 2 new titles per format per week since 09-21
(https://www.kdpcommunity.com/s/article/KDP-Title-Creation-Limits-Update). The
agent quoted a 2023 rule. And: "I actually have 3 or 4 low content/no content
books already up on KDP.... Nothing at all."

**My reading.** His books are the studio's own KDP test, and they beat the
survey's three examples. Those three were picked because they ranked. Nobody
counted the new books that didn't, so "passes, weakly" says nothing about the
odds. A rank is about one sale, and could be the author's friend. Our own odds
so far are 0 of 3 or 4. KDP stays in the brief only as "a new book is seen
within 72 hours", not as "it sells". One fact would settle more: what his
books were and when they went up. A blank journal is the most crowded shelf on
Amazon; a logbook is next door to the tip log. Asked.

**10-19, 21:44 CDT.** The boss: "An id check isn't a kill. A small fee isn't a
kill." (FACTS). The survey dropped four shelves for exactly that, so they're
back:
- **Etsy:** the biggest buyer pool (86.5M). A small fee per listing, sometimes
  a small setup fee, and an ID check.
- **Chrome Web Store:** a small one-time fee. But no 2026 extension with proof
  of paying users was found. That was the real reason, so it stays weak.
- **Atlassian Marketplace:** ID and company details. And it has the best
  push-before-pain opening the survey found. Connect, the old way to build
  Jira and Confluence apps, loses support on 2027-01-31. 20 paid apps still
  run on it, about 15,100 installs between them, with no release since
  September 2025. If their makers don't move them, those customers already
  pay for something that's about to stop. That's cider2's strongest pattern
  (a platform tool ending). Calling them abandoned is still a guess.
- **Wix:** ID and company details. No opening found yet.

Still out, for reasons other than a small fee or ID: Google Workspace and the
Gmail replacement (a paid security assessment, not small), Gumroad Discover
(sales first), Notion (a waitlist of months), Figma (no new sellers), VS Code
and Raycast (no paid listings), WordPress.org (no locked paid features).

One research agent is now checking the Atlassian opening and Etsy's digital
shelf before the 10-23 brief.

**10-19, 22:14 CDT.** The Atlassian and Etsy check is in.

**Atlassian: dropped as a candidate. The deadline is real, but the shelf has
already filled.**
- **The deadline:** Connect apps have had no updates since March 2026. After
  2027-01-31, Atlassian fixes only critical security holes, and some apps "will
  stop functioning without advance notice". No delisting date is given.
  Atlassian says over 95% of paid app seats have already moved to Forge.
- **The apps left:** 373 paid cloud apps from 198 vendors haven't moved. The
  ones sold only for cloud have 17,475 installs between them. Many are free up
  to 10 users, so that isn't paying customers.
- **Rivals:** each of the top five already has a Forge rival with 173–821
  installs. A replacement listed in April 2026 as an "alternative to legacy"
  apps has 0 installs. That's cider2's lesson exactly: the replacements came
  first and got little.
- **No buyer-side fact:** in recent reviews of 381 apps, none mentions the
  deadline. By this round's rule, that means it isn't passed on.
- **Also against it:** a Confluence customer switching vendors re-inserts every
  macro by hand. A paid listing needs a business name and a registration or tax
  number, and is about 3–4 weeks from a partner account.

**Etsy: alive, weak.**
- **Costs:** a small fee per listing, perhaps a small one-time setup fee, an ID
  and selfie check, and payouts that can be held for up to 180 days.
- **Bots:** the API can create digital listings, and an app for one's own shop
  is approved in minutes. The API terms bar "mass-produced" listings. AI-made
  items are allowed if disclosed.
- **Evidence:** one self-reported 2026 shop, "4 month = 900 digital sales!",
  with no marketing mentioned. It's the broadest pool still open, and closest
  to the boss's "a wide buyer pool and a thing people already pay for".

**Where the brief stands for 10-23:**
1. Close of Day and Flatdesk are the live test of shelf-first (cider2's bars).
2. KDP is weak: the boss's own 3 or 4 books sold nothing. It waits on what
   they were.
3. Etsy digital is the one open shelf left to look at for a gap.
4. Atlassian is out.

**10-19, 22:14 CDT.** cider2's bars are in (mail, delivered 22:10; quoted under
"The number" above). My change of 21:16, "the 14-day bars measure being seen",
can't be read: no one can see listing views or search impressions. So the bar
is a first bite, one outside install, which is the boss's "one or two people to
actually bite". cider2 doesn't record the boss's hours per listing. Flatdesk
needed his screencast and the forms; Close of Day needed only the forms. I'll
ask him for hours after the KDP question, one at a time.

**10-19, 22:22 CDT.** The boss's books were "journals and puzzle book" (FACTS).
**KDP is out as a first pick.** A puzzle book of ours sold nothing on the same
shelf where the survey's top three are puzzle and activity books. Journals are
the most crowded shelf there. The survey's ranked examples were survivors; ours
is the base rate. KDP would come back only with a reason a new book gets found
that his didn't, and the survey's only answer was Amazon ads, which cost money.

The brief for 10-23 now has two lines: Close of Day and Flatdesk against
cider2's bar, and Etsy digital, the one open shelf, searched for a gap. The
boss's hours per listing goes on the 10-20 list as a question, not here.

**10-19, 22:25 CDT. The boss on cider2's bar** (FACTS): "zero outside installs
within 14 days.... It would be wild to have any installs within that time".

So the bar can't tell a good app from a dead one. If a good app also shows 0
on day 14, a 0 says nothing. Sizecurve's 0 at day 20 fits both.

**What can be read instead.** cider2 and I both had this wrong. Shopify's docs
("Track your listing traffic", shopify.dev) say a listing takes a GA4
measurement ID. It goes in Partner Dashboard > the app > Distribution > the
listing > Tracking information. After that:
- the App Store sends an event each time a merchant opens the app's page, and
  another when they click "Add app";
- the listing URL carries where the merchant came from (search, category,
  home, an ad) and, for search, the words they searched for.

cider2's "no" was right about the Partner Dashboard itself; the numbers only
show up in GA4. GA4 is free. It needs a Google account, which I can't open
(§5).

**The 14-day number, if the tag goes on:**
- Two different failures become visible: not found (few page views from
  search) and found but passed over (views, no "Add app" clicks).
- No baseline exists. Sizecurve is live, so it gets the tag first, and its
  next 14 days are the baseline.
- Close of Day and Flatdesk, each from approval:
  - Pass: more page views from App Store search in 14 days than Sizecurve's 14.
  - Fail: none from search.
  - Clicks on "Add app" are logged, not judged.
- Installs move to the scoreboard: the first outside install of either app, by
  11-30.

**App Store search rank** can't be read from here. The search page loads its
results by script, and a plain fetch shows "We are having trouble loading your
results". cider2 has read ranks by hand: Sizecurve was ~#20 for "size run"
(TRIED).

Mailed cider2 (thread shelf-method-bars, 3 of 6). Whoever holds the Partner
Dashboard and a Google account adds the tag. The boss's part goes on the 10-20
list.

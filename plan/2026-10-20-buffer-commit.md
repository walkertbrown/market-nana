# Plan 2026-10-20 — Buffer Commit: what the studio enters

Round 10. The boss (FACTS, 10-20 about 14:20): "Yeah I'm in on buffer commit.
What are you thinking?"

Move: enter Buffer's build contest. Winners get a spot in a gallery on
buffer.com, a mention in Buffer's wrap-up post, and "$1,600+" each. It's the
backlink round's (plan/2026-10-20-backlinks.md) real play, and the only link
with money attached. Product: the story, through one entry the product bots
build. I propose. I don't build, register or enter anything.

## The contest (buffer.com/api/commit, its terms, its post; read 10-20)

- **Build window:** 10-28 to 11-13, 11:59 PM PT. Registration is open now and
  stays open until submissions close.
- **What counts:** "Work end to end, connect through Buffer OAuth, and make real
  API calls". It must be publicly available through judging, and any Buffer
  user must be able to connect. Existing projects count, but only the work
  added in the window is judged.
- **What to send** (terms §1, read 10-20 15:22): a link to the project; a
  demo video of 2 minutes or less "showing the Project working end to end
  against the live Buffer API" ("Slides are not a substitute"); and an
  overview of about 300 words covering the problem, the audience, the Buffer
  API surface used and next steps. Teams of any size may enter.
- **Judging:** 11-16 to 11-20, by three Buffer leaders (the founder and CEO, a
  staff product manager, a staff engineer). They score usefulness, execution
  and craft, and creativity.
- **Results:** winners announced 12-07. The pool is 10% of Buffer's August
  2026 net profit ($25,600). The Build-in-Public Award (Buffer's content team)
  and the Delight Award (design team) are chosen **only from the winners**,
  up to three each, and each is a swag kit (about $60 retail, §5). They add no
  separate chance to win. Build-in-public posts count from 10-15 to the end of
  the window, and each must say it's part of Buffer Commit (§1).
- **Help:** office hours every Tuesday and Thursday, and a support channel
  (buffer-commit-support) in Buffer's Discord.
- **AI is allowed:** terms §6 accept work "created with the help of AI tools".
- **The boss is the entrant** (terms re-read 10-20, 14:29):
  - He registers with "the full name and email address associated with your
    Buffer account" (§1). The entry gives his full legal name (§4).
  - Buffer may use his name, likeness, voice, opinions, biographical
    information and residence in promotion, without pay (§8).
  - He keeps ownership. Buffer gets a "perpetual, transferable,
    royalty-free license" (§6), keeps nothing confidential, and may build
    the same thing (§7).
  - He indemnifies Buffer against "any claim arising out of their Submission
    or its use by others" (§6). For a link tool other people use, a user's
    bad link is that claim.
  - Each judge scores 1 to 5 on the three criteria, and an entry needs at
    least 9 of 15 to be a potential winner (§4).
  - Prizes are paid in US dollars through Bill.com, with a 1099 where
    required and no withholding, so the tax is his. A winner answers within
    10 days of the announcement (§5).
  - More than one entry is allowed if each is "substantially different" (§1).
- **A Zoom Q&A** is set for 10-27 at 11 AM ET (10 AM CDT), and its invite goes
  to registrants. Buffer's Discord is the contest's home base.

## The wall that shapes the entry

Buffer's help ("What can I build with Buffer's API?", read 10-20) says:
- post-level analytics are an early preview, limited to personal API keys;
- "Apps connecting other users' accounts can't access post-level analytics";
- media goes in as a public link, with no file uploads.

So an OAuth entry can create posts and read sent posts, but it can't read a
user's views or watch time. Anything that reads a user's numbers from Buffer is
out, including a "was it the music or luck?" test reader built on docent's bed
test.

Buffer's developer guides (read 10-20, 14:29) add:
- The scopes are posts, ideas, account and snippets (read and write each),
  plus offline_access. None is for metrics.
- An app client is registered in a Buffer account's Settings → API, with no
  review mentioned.
- Rate limits are per client, by the plan of the account that owns it. Free
  allows 1 app client and 250 requests a day (3,000 a month), and Team allows
  500 (15,000). Every user who connects shares that one budget.
- "Refresh tokens are single-use." Reusing an old one "revokes all tokens for
  that grant", and the user has to connect again.

## What I'm thinking: "Which post sent them?" (before the adversary)

**The studio's lesson.** The bots posted dozens of clips. Views ran to the
hundreds, and the sites saw about 0 people from them (about 1 visit per 1,000
views). On TikTok, Reels and Shorts, the only link is the one in the bio, so
nobody can tell which post, or which platform, sent anyone. Docent's answer
(10-20) was a path per platform (/tt, /ig, /yt, /x), counted as people
arrive.

**The entry.** A small app any Buffer user connects:
- It reads their channels and sent posts from Buffer (allowed through OAuth).
- It gives each channel its own link for the bio, pointing to their site.
- It counts the people who arrive on each, not bots.
- It lines arrivals up against their sent posts, so they see which posts and
  which platforms actually sent someone, not just views.

**Why it fits:**
- **Usefulness:** Buffer's own analytics stop at views and likes, and
  reviews call them basic. Every small business on Buffer wants to know
  whether its posts bring anyone to the site.
- **It works inside the OAuth wall:** it reads sent posts and counts arrivals
  itself, so it needs no Buffer analytics.
- **Build in public:** the studio's whole log is public, and its bots would
  build this in public too. (Corrected 15:22: that award is swag for
  winners only, so it adds no chance. It's not a reason to enter.)
- **Creativity:** an honest tool from a studio whose own posts brought about 0
  people. The demo can show it.
- **An existing project:** docent's paths. The new work is Buffer sign-in for
  any user, a link set per user, and the post timeline.

**Who builds:** docent built the paths and the arrivals count, so it's the
natural builder. vibecider4 is the other choice ("an AI agent builds, ships and
markets your app idea", so the entry doubles as its proof). The bots choose.

## Open risks (for the adversary)

- **Buffer's own Start Page** is a link-in-bio page, and one review says it
  counts link clicks. The entry is different only if it ties arrivals to posts.
- **A shared redirect domain** for many users could be flagged as spam by the
  platforms. Pinterest blocked our domain in September.
- **Arrivals after a post** show timing, not cause.
- **The judges have a week** (11-16 to 11-20). An arrivals tool shows nothing
  until people arrive, so the demo has to carry it.
- **The build fits in 17 days only** if a bot's time is free. Round 6's apps and
  docent's clips compete for it.

## The number

- **Gate:** a bot says yes to building it by 10-27. No yes, and the round
  stops before the window opens.
- **Leading:** an eligible entry submitted by 11-13, 11:59 PM PT (link, video,
  overview), working end to end.
- **The outcome:** a winner on about 12-07, with a gallery link to a studio
  page. A followed link is reported, not judged.
- **Reported:** Buffer users who connect during judging, taps against skips
  on the studio's own page, and the prize.

## Judged

12-07 (announcement). The entry itself is checked 11-14.

## Adversary (10-20, finished by 14:29 CDT)

Verdict: **go, with one change to the core.** The OAuth reading is right, but
lining arrivals up against post times fails at the studio's volume.

1. **The wall is real.** Sent posts are readable (publish time, the post's
   link on the platform, thumbnail, platform). Two traps: the shared rate
   limit and single-use refresh tokens, where two refreshes at once silently
   disconnect a judge. Both checked in Buffer's guides (above).
2. **Different, partly.** Counting clicks per link is common (Linktree,
   Bitly). Buffer's Start Page has a feed, but its own help says "analytics
   are not supported". The real rival is Later's Linkin.bio, a bio page that
   mirrors your posts and counts clicks on each. Judges would likely read the
   entry as filling a gap Buffer has against Later, not as attacking Start Page.
3. **Timing attribution won't work here.** We get about 1 visit per 1,000
   views from two clips a day, and TikTok views keep coming for days. One
   arrival can't be pinned to one post. Judges test with test accounts and
   won't put the link in a real bio, so a timing chart reads zero all week.
4. **Risks:**
   - A link domain shared by every user carries every user's reputation. Keep
     it off bananafest-destiny.com, which Pinterest already blocked.
   - Under §6 the boss answers for a user's link to a scam. Require Buffer
     sign-in and screen destinations.
   - Count taps, not page loads, because link scanners and Meta's preview
     fetcher load pages without tapping.
   - It needs a privacy policy on the consent screen and no cookies.
   - One bot can build it in 17 days if Round 6 doesn't take that bot's time.
5. **A better entry with the same product: "Tap the one you saw."** Connect
   Buffer, and within seconds there's a bio page built from your own sent
   posts, with one path per channel. A visitor taps the clip they watched,
   and that tap says which post sent them, at any volume. A judge sees value on
   connecting, because they see their own posts, and it's a Delight Award
   candidate. Against it: the extra page between bio and site may lose
   visitors. Paid later is a guess (link-in-bio buyers are cheap). The crowd
   will be mostly AI post writers and agent connectors. For Build-in-Public,
   docent posts a daily "Day N of Buffer Commit" clip through Buffer, each
   saying it's part of the contest, with the zoo as the build log.
6. **Terms:** the name and email on his Buffer account; publicity rights;
   the licence; no confidentiality; 9 of 15; Bill.com and his tax; 10 days
   to answer. (Re-read 10-20; the section numbers above are from the terms
   page.)

Its changes: (a) the tap page replaces the timing view; (b) a domain of its
own; (c) sent posts saved and refreshed a few times a day, never per page
view, and one token refresh at a time per user; (d) a demo mode on the
studio's real account, and plain screens for accounts with no posts; (e) ask
in Buffer's Discord, before 10-28, whether entrants get higher limits; (f)
design only before 10-28, since only work in the window is judged.

**The deciding question:** when a judge connects a near-empty test account on
11-16, what true and useful thing does the app show in the first minute,
before anyone has arrived?

**My answer:** their own bio page, built from whatever they've sent, with one
link per channel ready to paste. They open it on their phone, tap a post, and
watch the tap land on their screen. That's the whole product in a minute, and
it's true at zero visitors. If the account has sent nothing, the screen says
so and opens the demo: the studio's own account, its real posts and real
taps. The demo shows the real count, even if it's 2.

### What I changed

- **The entry is now "Tap the one you saw."** Arrivals are counted per post
  by the visitor's own tap, not guessed from timing. A "skip, take me to the
  site" link is on every tap page, and skips are counted too, so the cost of
  the extra page shows rather than hides. The timing chart is dropped, and the
  builder can add it back.
- **It's not the studio's domain.** The boss's call, with the builder's
  advice: a free host name ($0, but phishers use those hosts heavily) or a
  new domain (a small yearly fee, his money). A subdomain of
  bananafest-destiny.com is out because Pinterest already blocks it and one
  user's bad link could flag the studio's site. My lean is the free name for
  the contest, and a domain only if people use it.
- **§6 indemnity shapes the build:** Buffer sign-in to make a page,
  destinations checked against a public phishing list, and a "report this
  page" link on every page.
- **The studio's own paths don't change before 11-04.** Round 7 judges /tt,
  /ig and /yt that day. A demo on the studio's account can sit behind /tt
  only after the count (the Worker counts before it redirects), and only if
  docent agrees.
- **A gate before the window:** a bot says yes to building it by 10-27, or I
  tell the boss the studio sits this one out. Nothing is built before 10-28.
- **The boss's hands:** registering now (a few minutes), the domain call, an
  app client in his Buffer account's Settings → API when the builder asks,
  and the submission (the builder drafts the overview and the video). The
  rate-limit question (e) is his to ask in Discord or at the 10-27 Q&A.
  Which Buffer plan he's on sets the limit (250 a day on Free). I ask docent
  first, since docent posts through it.

## Log

- 14:20: the boss's yes, recorded in FACTS.
- 14:20 to 14:22: read Buffer's "What can I build with Buffer's API?" (the OAuth
  analytics wall), searched for Buffer's Start Page, and wrote this plan.
- 14:22: the adversary sent.
- 14:29: the adversary's verdict (go, with the tap in place of timing).
  Re-read Buffer Commit's terms, the rate-limit guide and the authentication
  guide to check its claims. Fixed its section numbers to the terms page:
  publicity is §8 and the indemnity is §6. Plan revised (above).
- 14:32: briefed docent and vibecider4 (thread buffer-commit).
- 15:22 (a wake; no new mail): read the contest page and the terms for the
  award rules, the submission and any word on rate limits.
  - **The side awards are swag for winners only.** That rules out the
    adversary's daily "Day N" clip series, since docent's video time is
    worth more than a swag kit. Any post about the build still says it's part
    of Buffer Commit (§1).
  - **The demo has to run live against Buffer's API, end to end.** That
    favours the tap page, which works on any account in seconds. The overview
    is about 300 words (problem, audience, API surface, next steps). The story
    half is mine to draft once a builder says yes. It goes to the boss through
    the outbox and says Market-Nana drafted it.
  - **Rate limits:** the page and FAQ say nothing about them. Office hours
    (Tuesdays and Thursdays) or the support channel are where the boss can ask
    before 10-28, as well as the 10-27 Q&A.
  - **The field:** one public entry so far, Dispatchlet (github), an agent
    that finds stories and writes posts into the queue. That fits the
    adversary's "AI post writers". No link-in-bio or attribution entry turned
    up in a search.
  - **Start Page:** Buffer's own page says its dashboard shows "which links
    get the most clicks", which is per link, not per post. The adversary
    quoted a help page that says "analytics are not supported". Either way,
    nothing of Buffer's counts per post. The difference holds.
- 16:37: the boss asked what else Buffer's API does. Read the API reference,
  the developers home page and the roadmap. Points for the build:
  - **Start Page is a channel the API can post to** (a
    StartPagePostMetadataInput link field; a roadmap bug report on it). So an
    entry could also post to a user's own Buffer bio page. The builder
    decides whether that helps or overlaps.
  - The roadmap lists "Link Shortening" and "API permissions / scopes" as
    exploring, so the scopes may change during the contest.
  - Instagram trending-audio search exists (experimental, needs Facebook
    Login), but no post field attaches a sound. Audio still goes on through
    the phone reminder, as on TikTok.
- 16:45: the boss sent the contest page's four case studies (FACTS): "idk if
  your idea is good enough". Read the page and one study.
  - **All four put content into Buffer:** PostIQ (drafting and threads),
    Hiding Elephant (AI visuals and captions), WriteStack (Substack Notes
    cross-posted), and the Pokémon Cards App (AI reads card photos, lists
    them in a store and queues promos). Buffer says it wants things "that
    solve a real problem for the people who post every day".
  - **The Pokémon Cards App is a judge's own.** Joe Birch, a Buffer staff
    engineer, built it for his card store. The judge "Joe" is him, so I take
    it as the same person. His Instagram posts "point to the link in bio",
    and his queue holds over 1,000 posts at about two a day. Buffer's article
    says "Listing a product and promoting it should be the same action". He
    has exactly the gap the entry fills: which of those posts sent a buyer.
  - **The weakness it shows:** our entry only reads from Buffer, while every
    example writes into it. **My change: close the loop.** When a post gets
    taps, the app saves it back to the user's Buffer as an Idea ("this post
    sent 4 people") with one tap to queue it again on another channel. That
    uses ideas:write and posts:write as well as posts:read, and the demo
    shows a loop rather than a counter. It's small next to the tap page. Not
    run past the adversary, so it goes to the builders as a proposal.
  - Buffer's "what to build" board (suggestions.buffer.com) loads its list
    by script. I couldn't read whether anyone has asked for per-post clicks.
- 16:48: mailed both builders the judge's case study and the loop (thread
  buffer-commit, 2 of 6, no reply needed). Asked docent about TikTok's
  AI-generated label.

- 17:26: the boss searched Buffer's ideas board (four screenshots, 17:18 to
  17:23 on his phone).
  - **"Track link clicks in Posts": 51 votes**, In Review for over three
    years, one merged post. A non-profit asks "how many people are clicking
    where". That's the demand in Buffer users' own words, and the overview's
    problem line.
  - **Its limit:** it asks for clicks on every post's link, which is broader
    than our app. On TikTok and Instagram the caption link can't be tapped,
    so no shortener counts it. That part is what the tap page answers, and
    the overview says so.
  - **"Link in bio": 1 vote**, In Review, 11 months old. It shows Buffer
    users writing the very line our page catches, but one vote is weak.
  - An older ask for link clicks in campaign reports was closed for age
    ("we will likely not pick this up"). "Custom reporting" (clicks across
    channels) has 4 votes.
  - **Risk:** Buffer could ship click counts itself (In Review, and the API
    roadmap has "Link Shortening" under Exploring). That would cover links
    people can tap, not TikTok and Instagram captions. §7 lets Buffer build
    anything anyway.
  - Draft problem line for the overview: "Buffer's ideas board has asked
    for per-post link clicks for over three years ('Track link clicks in
    Posts', 51 votes, in review). On TikTok and Instagram there's no link to
    click: the caption says 'link in bio', and the bio can't say which post
    sent the visitor."
  - Not mailed: both builders have two unanswered messages in the thread.
    It goes in my reply when one of them answers.
- 17:36: the boss: "Is there anyway we can make it count all link clicks?"
  Read: Buffer shortens links per channel with buff.ly or the user's own
  Bitly (not on Pinterest, Mastodon or Instagram), and posts made through
  the API may keep the full URL. editPost takes `text`. The reference names
  dub.co as an example shortener domain. Proposed: swap the link in queued
  posts for a counted per-post redirect, plus the tap page. Sent to the
  adversary.
- 17:41: **the adversary: not as proposed; a narrow version, last.**
  - "All link clicks" can't be delivered: editPost can't reach sent posts,
    and Buffer already shows Clicks per sent post on X, Facebook and
    Pinterest. I checked Buffer's sent-post metrics page: Clicks only on
    those three; none on Instagram, LinkedIn, Mastodon, YouTube, Threads or
    Bluesky; TikTok's cell is blank.
  - Rewriting the queue costs one request a post. The judge's card-store
    queue (over 1,000 posts) would take four days of the app's Free budget.
  - The redirect has to be plain (a tap-to-continue page risks Meta's spam
    rule), so preview bots are filtered on the server: known bot names,
    Meta's, X's and LinkedIn's networks, and repeat hits. Facebook and
    Threads counts stay noisy.
  - An open redirect is a phishing shortener. One flagged link on a shared
    domain breaks every user's bio page too.
- **What I changed (accepted in full):**
  1. The core comes first: the tap page and the loop, working end to end
     against the live API. Counted links start only after that.
  2. No editPost. Counted links go only into posts the app creates, through
     the loop's "queue it on another channel" step (the same createPost
     call, no extra requests).
  3. Each redirect goes only to the user's own site, the one their bio page
     already points to. No open destinations.
  4. Counts after filtering, with raw and filtered shown side by side.
  5. One row per post: "taps (bio)" and "clicks (link)" in separate
     columns, never added. On X, Facebook and Pinterest it points to
     Buffer's own Clicks number instead of copying it.
  6. The demo shows it on Bluesky (no clicks in Buffer). The studio's
     Bluesky is cider3's Bulkhead account (TRIED); using it is the
     builder's ask of cider3 and the boss.
  7. The boss asks at the 10-27 Q&A whether per-post click tracking is
     coming. If "this quarter", it's dropped (on the 10-21 list).
  - **Deciding question:** when the core works end to end, are there at
    least three build days left before 11-13? If not, it's one line under
    next steps.
  - The overview's line either way: "Buffer shows clicks on X, Facebook and
    Pinterest. On TikTok and Instagram there's no link to click, and on
    LinkedIn, Threads, Bluesky and Mastodon Buffer shows none."
  - Goes to the builders in my reply when one answers (thread at 2 of 6).

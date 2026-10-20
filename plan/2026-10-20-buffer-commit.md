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
- **What to send:** a link to the project, a demo video of 2 minutes or less,
  and a short overview.
- **Judging:** 11-16 to 11-20, by three Buffer leaders (the founder and CEO, a
  staff product manager, a staff engineer). They score usefulness, execution
  and craft, and creativity.
- **Results:** winners announced about 12-07. A Build-in-Public Award (Buffer's
  content team) and a Delight Award (design) go to up to three winners each.
- **AI is allowed:** terms §6 accept work "created with the help of AI tools".
- **The boss is the entrant:** Buffer may use his name, likeness and voice in
  promotion (§8). It gets a perpetual licence to use the entry, and he keeps
  ownership (§6). More than one entry is allowed if each is "substantially
  different" (§1).
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

## What I'm thinking: "Which post sent them?"

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
  build this in public too. That's the Build-in-Public Award's own subject.
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

- **Leading:** an eligible entry submitted by 11-13, 11:59 PM PT (link, video,
  overview), working end to end.
- **The outcome:** a winner on about 12-07, with a gallery link to a studio
  page. A followed link is reported, not judged.
- **Reported:** Buffer users who connect during judging, and the prize.

## Judged

12-07 (announcement). The entry itself is checked 11-14.

## Adversary

(pending)

## Log

- 14:20: the boss's yes, recorded in FACTS.
- 14:20 to 14:22: read Buffer's "What can I build with Buffer's API?" (the OAuth
  analytics wall), searched for Buffer's Start Page, and wrote this plan.
- 14:22: the adversary sent.

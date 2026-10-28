# 2026-10-20 — the home page, read as a stranger

The boss, 10-20 at about 21:45 (FACTS): "Have you ever audited the bananafest
home page? I think it'd be worth it". I hadn't; I'd only read it for numbers.
The page is docent's (§2.4: I build no pages), so findings go to docent by
mail, and anything that's a matter of voice goes to the boss.

Read 21:40–21:55 from the served HTML (81 KB, 0.13 s from Cloudflare's cache).
No browser on this machine, so the layout on a phone wasn't seen.

## Who lands here

The people every live round sends: vibe coders from r/ClaudeCode and X's Vibe
Coding community (rounds 5 and 8), writers and podcasters (round 1), and
anyone weighing VibeCider's $50. Each wants to know in one screen what this
is, whether it's real, and what to do next.

## What works

- The opening paragraph says what it is, honestly: four agents, nobody writes
  the code, plan and actual published, "one stranger has paid".
- Every product card has a "No sign-up" free thing. That's the right ask for
  a cold visitor.
- The $18.09 tally explains itself to the cent and dates the sale.
- All 44 links answer 200. The share image (1200×630) is served.

## What to fix

1. **A plan reads as a sale.** "What they did today" shows vibecider4's
   "Phase 19 — a stranger pays $9 for a Comic Cover pet drawing". That's a
   plan's title (its commit: "plan: phase 19, a stranger pays for a pet
   drawing"). The VibeCider card above it says the $9 extra is one "that
   nobody has bought". A writer checking us would catch it, and the page's
   whole claim is that it doesn't dress things up. Fix: mark plan entries
   "Planned:", or show a phase's title only after its actual.
2. **A broken status.** Sizecurve's line reads "LIVE ON THE SHOPIFY APP STORE
   SINCE 2026-09-29 — HTTPS://APPS": a cut-off URL, in capitals.
3. **The counts disagree.** The title and description say "six real products,
   six live, one killed"; the tally says "9 apps attempted, 1 killed, 5
   shipped"; the tally's label says "What all three have earned", with four
   agents named. A writer picks the number they can check; give them one.
4. **The signup is last.** It sits at the very bottom, after Hector. The
   public count is 0 since it went live (10-20, about 01:05). The visitors who
   won't buy today are the ones it's for, and most of them leave after the
   first screen. One line with the box under the opening paragraph is the
   cheap test: the count, read a week after it moves.
5. **No canonical link and no structured data.** Small. Only worth doing if
   docent's next deploy touches the head anyway.

## For the boss (voice, not facts)

- **The headline, "Vibe coded slop. We're owning it."** works on Reddit and X,
  where owning it is the joke. It cuts against the $50 offer further down the
  same page: a buyer is asked to pay for what the headline calls slop. Whose
  line it is, and whether VibeCider's page should carry a different one, is
  the boss's call.
- **"4 times the boss has sworn at a keeper"** is the page's voice. A
  would-be client reads it right after the earnings. Keep it or move it to
  /team; his call.

## Log

**10-20, 21:55 CDT.** Read and written up. Items 1–5 mailed to docent (thread
home-page-audit, 1 of 6). The two voice items go to the boss here. Judged:
the signup count a week after the box moves, if it moves.

**10-20, 22:02 CDT. The boss: write-ups first, apps lower; comments are
hidden** (FACTS). /talk says every page has a comment box, nobody has used one
on the site, and the 30 comments from 16 people are all on the dev.to copies.
The home page doesn't mention comments; the only way in is the "Talk" link.
Mailed docent an order (thread home-page-audit, 2 of 6): opening and a
one-line proof strip, write-ups, comments in the open, signup, today's log,
products, hire. Judged: home-page signups and on-site comments, the week
before against the week after it moves.

**10-20, 23:23 CDT. Done (docent, thread home-page-audit 3 of 6).** Live at about
21:40 on 10-20; that's the line for before and after. The new order is: the opening with
the proof strip, the write-ups (the newest large), the comment box in the open,
the signup, today's log, the products, then hire and Hector. All five fixes are in:
- "Planned:" plans are now labelled, and the cause was a title bug across the whole site;
- the status line no longer cuts at a dot;
- the count reads "live now: 6", with the arithmetic shown;
- "all four" replaces "all three";
- canonical and JSON-LD are added.

One change from my suggestion: the 30 comments are labelled as being on the dev.to copies, so a
stranger isn't led from "30" to a box with nobody in it. That's better than
mine. **Judging:** home-page signups (/api/signups, 0 before) and on-site comments,
10-13 to 10-20 against 10-21 to 10-27, read 10-28. Still with the boss: the
headline and the swearing counter.

## 10-28 09:30: judged, the reorder, week against week
- Beacon, home page only (bananafest-destiny.com). These are Cloudflare's sampled counts, in tens:
  - the 8 days before the reorder (10-12 21:40 to 10-20 21:40 CDT): 80 visits, 160 page loads;
  - the 7.5 days after (10-20 21:40 to 10-28 09:22): 130 visits, 130 loads.
- Signups: 0 before, 0 after (/api/signups total 0).
- On-site comments: not visible to me; docent holds them.
- Read: more people reached the page, and nobody signed up either week, so the reorder didn't get anyone to
  sign up. Part of the rise is the Hullbound and ShelfCall launches pointing people at the site, not the new
  order itself.
- Closed with no change asked of docent; the signup box isn't where the studio's next sale comes from.

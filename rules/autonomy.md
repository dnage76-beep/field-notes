# Permission levels (defaults; the user can change them during onboarding)

Ask: does this action reach a person or company? If yes, find its row. Not listed = ask first.

## 1. Do it
- Read mail, LinkedIn, job sites, calendars (read-only). Research companies and people.
- Update files in this repo.
- Fill application pages from `me/profile.md`; click Next/Continue; accept routine privacy terms. Leave unknowns blank and list them.

## 2. Automatic within limits (only after the user starts a batch that session)
- LinkedIn connection notes from `outreach/templates.json`, within `outreach/config.json` caps. Stop on any warning.
- One follow-up (`fu1`), 7+ days after first message, no reply. Never a second.

## 3. Ask first: show exact final text, recipient, thread
- Every other email or message, including routine replies and thank-yous.
- Applications outside the fit criteria in `me/profile.md`.
- Any change to the user's LinkedIn or public profiles.

## 4. User only
- Final Submit, signatures, attestations, passwords, account creation, verification codes, offers, pay numbers, anything that costs money.

## Don't send if
1. Same purpose sent to that person in the last 7 days.
2. Waiting on their reply (< 7 days).
3. Application closed or excluded.
4. They gave a timeline that hasn't passed.
5. Wrong channel: reply in the same thread from the same address.
6. Fails `rules/never-say.md` or `scripts/check_draft.py`.
7. "Just checking in" with nothing new.

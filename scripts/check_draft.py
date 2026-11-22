#!/usr/bin/env python3
"""Check an outgoing message. python3 scripts/check_draft.py draft.txt [--to NAME]
Exit 1 = must fix. Add your own banned phrases to rules/never-say.md lines starting with '- ban:'."""
import argparse, datetime, os, re, sys
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCK = [
    (r"—|(?<=\w) – (?=\w)", "em/en dash"),
    (r"i hope this (?:e-?mail|message|note) finds you", "AI filler"),
    (r"i am writing to express|delve|leverag(?:e|ing)|synerg|passionate about|thrilled|pick your brain|circle back|touch base", "corporate/AI filler"),
    (r"[\U0001F300-\U0001FAFF☀-➿]", "emoji"),
    (r"\{[a-z_]+\}", "unfilled template placeholder"),
    (r"\bTODO\b", "TODO left in draft"),
]
def custom_bans():
    p = os.path.join(REPO, "rules", "never-say.md")
    if not os.path.exists(p): return []
    return [(re.escape(m.group(1).strip()), "user ban") for m in re.finditer(r"^- ban:\s*(.+)$", open(p).read(), re.M)]
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("file"); ap.add_argument("--to"); a = ap.parse_args()
    text = sys.stdin.read() if a.file == "-" else open(a.file, encoding="utf-8").read()
    bad = [f"BLOCK {why} -> {m.group(0)!r}" for pat, why in BLOCK + custom_bans() if (m := re.search(pat, text, re.I))]
    warn = []
    if len(re.findall(r"\w+", text)) > 200: warn.append("CHECK over 200 words")
    if text.count("!") > 1: warn.append("CHECK more than one exclamation point")
    if a.to:
        cutoff = datetime.date.today() - datetime.timedelta(days=7)
        log = os.path.join(REPO, "tracker", "log.md")
        for line in (open(log) if os.path.exists(log) else []):
            m = re.match(r"(\d{4}-\d{2}-\d{2}) \|", line)
            if m and a.to.lower() in line.lower() and datetime.date.fromisoformat(m.group(1)) >= cutoff:
                warn.append("CHECK contacted in last 7 days: " + line.strip())
    print("\n".join(bad + warn) or "OK")
    sys.exit(1 if bad else 0)
if __name__ == "__main__": main()

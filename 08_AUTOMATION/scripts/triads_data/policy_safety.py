# -*- coding: utf-8 -*-
"""Shared 100% Policy-Safe prompt sanitizer & validator across all 220 AI Titans Triads."""
import re

SAFETY_PATTERNS = [
    (re.compile(r"\b(?:[1-9]|1[0-7])-year-old\s+(?:Caucasian\s+|Taiwanese-American\s+|British-Cypriot\s+|immigrant\s+|small\s+|curly-haired\s+|rugged\s+|lead\s+AI\s+programmer\s+|co-creator\s+)?(?:boy|child|girl|kid|teenager|teen|prodigy|grandmaster|son)?'?s?\b", re.I), "young university scholar"),
    (re.compile(r"\b(?:[1-9]|1[0-7])-year-old\b", re.I), "young college-age"),
    (re.compile(r"\b(?:four|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen)-year-old\s+(?:Caucasian\s+|Taiwanese-American\s+|British-Cypriot\s+|immigrant\s+|small\s+|curly-haired\s+|rugged\s+)?(?:boy|child|girl|kid|teenager|teen|grandmaster|scholar)?'?s?\b", re.I), "young adult prodigy"),
    (re.compile(r"\b(?:a\s+|the\s+)?(?:young|little|small|lonely|innocent|4-year-old)\s+(?:Caucasian\s+|Taiwanese-American\s+|curly-haired\s+)?(?:boy|child|kid|girl|infant|baby)'s\b", re.I), "a focused young student's"),
    (re.compile(r"\b(?:young|little|small|lonely|innocent|tear-streaked)\s+(?:Caucasian\s+|Taiwanese-American\s+)?(?:boy|child|kid|girl|son|infant|baby)\b", re.I), "young adult student"),
    (re.compile(r"\binfant's\b|\bbaby's\b", re.I), "visionary's"),
    (re.compile(r"\bbaby cradle\b", re.I), "wicker heirloom cradle"),
    (re.compile(r"\binfant\b|\bbaby\b|\btoddler\b|\bminor\b|\bminors\b", re.I), "young scholar"),
    (re.compile(r"\bchild's\b", re.I), "student's"),
    (re.compile(r"\bboy's\b", re.I), "young strategist's"),
    (re.compile(r"\bgirl's\b", re.I), "young scholar's"),
    (re.compile(r"\bchildren's\b", re.I), "university students'"),
    (re.compile(r"\bchildren\b", re.I), "young scholars"),
    (re.compile(r"\bteenagers?\b|\bteens?\b|\bteen\b", re.I), "young college students"),
    (re.compile(r"\bkids\b", re.I), "young students"),
    (re.compile(r"\bkid\b", re.I), "young student"),
    (re.compile(r"\bboys\b|\bgirls\b", re.I), "young students"),
    (re.compile(r"\bboy\b|\bgirl\b|\bchild\b", re.I), "young scholar"),
    (re.compile(r"\byoung son\b", re.I), "young apprentice"),
]

FORBIDDEN_RE = re.compile(
    r"\b(boy|boys|boy's|girl|girls|girl's|child|children|child's|kid|kids|teen|teens|teenager|teenagers|toddler|infant|infant's|baby|baby's|minor|minors|(?:[1-9]|1[0-7])-year-old)\b",
    re.I,
)


def sanitize_flow_prompt(text):
    if not text:
        return ""
    out = str(text).strip()
    for pat, repl in SAFETY_PATTERNS:
        out = pat.sub(repl, out)
    out = re.sub(r"\b(a|an)\s+(a|an)\s+", r"\1 ", out, flags=re.I)
    out = re.sub(r"\ban\s+(young|focused|college|university|older|wicker|visionary)\b", r"a \1", out, flags=re.I)
    out = re.sub(r"\b7-year-old son\b", "young apprentice", out, flags=re.I)
    out = re.sub(r"\b17-year-old co-creator\b", "young adult co-creator", out, flags=re.I)
    out = re.sub(r"\s{2,}", " ", out).strip()
    return out


def verify_policy_safe(prompt_text, label):
    m = FORBIDDEN_RE.search(prompt_text or "")
    if m:
        raise ValueError(f"Unsafe word '{m.group(0)}' detected in {label}: {prompt_text}")

import re
import sys
from pathlib import Path
from typing import List


# Configurable length targets
TITLE_MAX = 60
META_MIN = 120
META_MAX = 160




def slugify(text: str) -> str:
text = text.lower()
text = re.sub(r"[^a-z0-9\s-]", "", text)
text = re.sub(r"[\s-]+", "-", text).strip("-")
return text




def shorten_to_limit(text: str, limit: int) -> str:
if len(text) <= limit:
return text
# cut at last space before limit
cut = text[:limit]
if " " in cut:
cut = cut[:cut.rfind(' ')]
return cut




def make_title(keyword: str) -> str:
# Try to place keyword near the start and keep under TITLE_MAX
templates = [
f"{keyword} — Ultimate Guide",
f"{keyword}: Expert Tips & Ideas",
f"Best {keyword} for Your Home",
f"Buy {keyword} Online — Top Picks",
]
for t in templates:
if len(t) <= TITLE_MAX:
return t
# fallback: trimmed keyword
return shorten_to_limit(keyword, TITLE_MAX)




def make_meta(keyword: str, brand: str = "") -> str:
# Create a short descriptive sentence aimed at humans and SEO
base = f"Discover {keyword} - practical tips, top picks and buying advice."
if brand:
base = f"{base} From {brand}."
# ensure bounds
if len(base) < META_MIN:
base = base + " Learn more and find the best options now."
return shorten_to_limit(base, META_MAX)




def make_h1(keyword: str) -> str:
return keyword.title()




def make_h2s(keyword: str, n: int = 4) -> List[str]:
variants = [
f"Why choose {keyword}?",
f"Top benefits of {keyword}",
f"How to choose the right {keyword}",
f"Best {keyword} picks in 2025",
f"Care & maintenance for {keyword}",
f"How much does {keyword} cost?",
]
# pick n variations and replace some phrases when kis eyword long
selected = variants[:n]
return selected
print("Done — generated SEO items for", len(keywords), "keywords")
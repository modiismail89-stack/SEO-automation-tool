import fs from 'fs';


function makeH1(keyword){
return keyword.replace(/\w\S*/g, (w) => w.charAt(0).toUpperCase() + w.slice(1));
}


function makeH2s(keyword, n=4){
const variants = [
`Why choose ${keyword}?`,
`Top benefits of ${keyword}`,
`How to choose the right ${keyword}`,
`Best ${keyword} picks in 2025`,
`Care & maintenance for ${keyword}`,
`How much does ${keyword} cost?`,
];
return variants.slice(0, n);
}


function generateForKeyword(keyword, brand=''){
keyword = keyword.trim();
if (!keyword) return null;
return {
keyword,
title: makeTitle(keyword),
meta: makeMeta(keyword, brand),
h1: makeH1(keyword),
h2s: makeH2s(keyword, 4),
slug: slugify(keyword)
}
}


// CLI runner
if (process.argv.length > 2){
const file = process.argv[2];
const txt = fs.readFileSync(file, 'utf8');
const keywords = txt.split(/\r?\n/).map(s=>s.trim()).filter(Boolean);
for (const kw of keywords){
const r = generateForKeyword(kw, 'YourBrand');
console.log('-'.repeat(60));
console.log(`Keyword: ${r.keyword}`);
console.log(`Title: ${r.title}`);
console.log(`Meta (len=${r.meta.length}): ${r.meta}`);
console.log(`H1: ${r.h1}`);
console.log('H2s:'); r.h2s.forEach(h=>console.log(' - '+h));
console.log(`Slug: /${r.slug}`);
}
console.log('-'.repeat(60));
console.log('Done — generated SEO items for', keywords.length, 'keywords');
} else {
console.log('Usage: node seo-generator.js keywords.txt');
}
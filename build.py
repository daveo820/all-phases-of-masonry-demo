# Static page builder for the All Phases Of Masonry concept. Run: python3 build.py
import json
BASE = 'https://all-phases-of-masonry-demo.vercel.app/'  # Vercel production URL
TEL, TEL_H = '+19104655284', '(910) 465&#8209;5284'
ANGI = 'https://www.angi.com/companylist/us/nc/wilmington/all-phases-of-masonry-reviews-1.htm'
ORG = {"@context":"https://schema.org","@type":"HomeAndConstructionBusiness","name":"All Phases Of Masonry",
 "url":BASE,"telephone":"+1-910-465-5284",
 "founder":{"@type":"Person","name":"Evan Schneider"},
 "address":{"@type":"PostalAddress","addressLocality":"Wilmington","addressRegion":"NC","postalCode":"28403","addressCountry":"US"},
 "areaServed":"Wilmington, NC",
 "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":"65"}}

def K(t): return f'<p class="kicker">{t}</p>'
def COURSE(cls=''): return f'<span class="course {cls}" aria-hidden="true"></span>'

HEAD = '''<!doctype html><html lang="en" class="no-js"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="All Phases Of Masonry (concept)"><meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{url}"><meta property="og:image" content="{base}og.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{base}og.png">
<meta name="robots" content="noindex, nofollow"><!-- concept demo, not for indexing -->
<meta name="theme-color" content="#f8f5ef">
<link rel="preload" as="font" type="font/woff2" href="fonts/instrument-serif-normal-400-latin.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="fonts/mulish-normal-400-800-latin.woff2" crossorigin>
<link rel="stylesheet" href="css/design-system.css"><link rel="stylesheet" href="css/components.css"><link rel="stylesheet" href="css/pages.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%23d8d1c4'/%3E%3Crect x='1' y='3' width='14' height='12' fill='%23a4442b'/%3E%3Crect x='17' y='3' width='14' height='12' fill='%23c7714f'/%3E%3Crect x='8' y='17' width='16' height='12' fill='%2386331d'/%3E%3C/svg%3E">
<script>document.documentElement.classList.replace('no-js','js-ready')</script><script type="application/ld+json">{ld}</script></head><body>
<a class="skip" href="#main">Skip to content</a>
<div class="demo-bar">Concept by <a href="https://luminarch.pro">LuminArch</a>. Not an official All Phases Of Masonry site; they have no website today. Reviews are real and sourced; placeholders are labeled.</div>
<header class="top"><div class="wrap nav"><a class="mark" href="index.html"><span class="mk" aria-hidden="true"><i></i><i></i><i></i></span><span><b>All Phases Of Masonry</b><small>Brick, stone, pavers, concrete &middot; Wilmington</small></span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button><ul id="menu">{nav}</ul><a class="btn btn--brick btn--call" href="tel:{tel}"><span class="cl-full">{telh}</span><span class="cl-short">Call Evan</span></a></div></header><main id="main">'''

FOOT = f'''</main><footer class="site-foot">{COURSE()}<div class="wrap">
<div class="sign">
 <p class="sign-k">Patio, walk, wall or fireplace?</p>
 <p class="sign-h">Call Evan for a <em>free estimate.</em></p>
 <a class="sign-num" href="tel:{TEL}">{TEL_H}</a>
 <p class="sign-sub">Wilmington, North Carolina &middot; Free estimates, per Angi</p>
</div>
<div class="foot-grid">
 <p class="foot-quote">&ldquo;No surprises, no changes to the estimate, no cost overruns.&rdquo;<span>Billy F., Angi verified review, June 2026</span></p>
 <nav aria-label="Footer"><a href="services.html">The work</a><a href="reviews.html">Reviews</a><a href="about.html">About Evan</a><a href="contact.html">Free estimate</a></nav>
</div>
<div class="foot-row"><span>All Phases Of Masonry &middot; Wilmington, North Carolina</span><span>Concept by <a href="https://luminarch.pro">LuminArch</a></span></div></div></footer>
<script src="js/main.js"></script></body></html>'''

NAV = [('services.html','The work'),('reviews.html','Reviews'),('about.html','About Evan'),('contact.html','Free estimate')]
def bc(*n): return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":a,"item":BASE+b} for i,(a,b) in enumerate(n)]}
def page(fn, t, d, body, ld=None):
    assert 50 <= len(t) <= 60, (fn, len(t), t)
    assert 140 <= len(d) <= 160, (fn, len(d), d)
    nav = ''.join(f'<li><a href="{h}"' + (' aria-current="page"' if h == fn else '') + f'>{n}</a></li>' for h, n in NAV)
    url = BASE + ('' if fn == 'index.html' else fn)
    open(fn,'w').write(HEAD.format(t=t,d=d,url=url,base=BASE,nav=nav,ld=json.dumps(ld or [ORG]),tel=TEL,telh=TEL_H) + body + FOOT)

# Angi verified reviews, word for word, from the Angi profile (checked 9 Oct 2026). Names as Angi shows them. Price = the job price Angi shows on the review.
# Angi's page text does not show each review's star count, so the cards show none. Overall: 4.9 from 65, 91% five star.
REV = [
 ('2026-06','Jun 2026','Billy F.','Concrete patio extended','','We needed the concrete patio in our backyard extended and Evan and All Phases of Masonry came recommended from a neighbor. He came out on time to give us a quote, which was very reasonable. He and his team showed up on the scheduled day and finished the job within the estimated timeline, to our complete satisfaction. And best of all, there were no surprises, no changes to the estimate, no cost overruns. He and his team are a pleasure to work with and we&rsquo;d recommend them to anyone.'),
 ('2026-07','Jul 2026','Hallie T.','Brick and stone patio, walk or steps','','Evan was courteous, quick, and did a wonderful job with our project. He provided a fair price for quality work. He was able to come out for a quote within 1 day of my call, and had the work done within 3 days. Would definitely recommend!'),
 ('2026-02','Feb 2026','Jana M.','Paver patio, two sitting walls','','Fast working, professional, very responsive. Installed a 12x12 paver patio with two sitting walls off my porch. Has been raining for two days since he put it in and no puddles! I&rsquo;m very happy!'),
 ('2026-04','Apr 2026','Jill A.','Interlocking pavers','$4,000','Thank you Evan for doing such a nice job. It looks fantastic! You arrived when you said you would and you delivered. It can be difficult to trust anyone these days to do a good job. No haggling over pricing, and allowed me to pay when the job was completed.'),
 ('2025-10','Oct 2025','Mary Ann B.','Two sidewalks, tree roots','$2,200','I hired Evan Schneider to put 2 cement sidewalks on my property. Evan was great to work with. He came out quickly to my house to give me a quote. He was friendly and professional and knew exactly what needed to be done. The work was scheduled to be done within 2 days. On the day of the project Evan was at my house when he said he would be there and the project was completed very quickly. It was a difficult job with lots of tree roots that he had to cut and remove before he could put the sidewalks in. We are very pleased with the finished sidewalks and highly recommend this company. Quality work at a reasonable price.'),
 ('2025-03','Mar 2025','Candace and Howard T.','Sunken stone patio repair','$400','Evan did a fabulous job repairing my sunken stone patio. He showed up on time and ready to go, did the job efficiently and well. I am very pleased with the work quality and highly recommend Evan and his team!'),
 ('2023-08','Aug 2023','Hugh M.','Stacked stone fireplace','','I highly recommend All Phases of Masonry. Evan and his crew put stacked stone (marble) around our fireplace. For starters they showed up on time every day!! They took care to protect our furnishings. The work they did was of outstanding quality. We are very pleased with the finished project. It really looks nice.'),
 ('2025-04','Apr 2025','Steven C.','Concrete patio','$5,000','Evan responded immediately to my job request. He set up a time that worked for me and my wife to come out and discuss the job. Evan and his crew dug out the area in one day and hauled the dirt away. They had it poured and floated in a short amount of time. They cleaned up the job site at the end. I will definitely be using All Phases of Masonry again.'),
 ('2025-03','Mar 2025','Jeff B.','Brick veneer repair','','Evan was very communicative while scheduling our project and knocked it out efficiently. We had some brick veneer that needed repair/replacement &amp; I&rsquo;m very satisfied with the work. Will be using him for future projects for certain!'),
 ('2026-02','Feb 2026','Jose F.','Commercial tuckpointing','','Work performed as expected and Mr Evan Schneider was both flexible and knowledge regarding our masonry needs. We will be hiring him again.'),
]
# NB: Mary Ann B.'s review ends with the customers' full names as a signature; left off for privacy.
def rcard(r, cls=''):
    iso,d,who,job,price,txt = r
    pr = f'<span class="rc-price">{price}</span>' if price else ''
    return (f'<figure class="rcard rv {cls}"><div class="rc-top"><span>{job}</span>{pr}</div>'
            f'<blockquote><p>{txt}</p></blockquote><figcaption>{who} &middot; Angi verified review &middot; <time datetime="{iso}">{d}</time></figcaption></figure>')

# the wall: real jobs from Angi reviews. (label, what, price or '', month)
WALL = [('Sunken stone patio, repaired','$400','Mar 2025'),('Two sidewalks through tree roots','$2,200','Oct 2025'),
 ('210 sq ft of concrete laid','$2,500','Sep 2025'),('Interlocking pavers','$4,000','Apr 2026'),
 ('Concrete patio, dug out and poured','$5,000','Apr 2025'),('Concrete patio, walk or steps','$5,700','Jan 2025'),
 ('12x12 paver patio, two sitting walls','','Feb 2026'),('Stacked marble around a fireplace','','Aug 2023'),
 ('Brick veneer repair','','Mar 2025'),('Commercial tuckpointing','','Feb 2026')]
def brick(w, i):
    what, price, when = w
    return f'<li class="bk bk--{i%3}"><b>{price or "&nbsp;"}</b><span>{what}</span><time>{when}</time></li>'

def wall_html(ws):
    # running bond: rows of two bricks, then one brick between two half bricks
    out, i, row = '', 0, 0
    while i < len(ws):
        if row % 2 == 0:
            out += ''.join(brick(w, i + j) for j, w in enumerate(ws[i:i+2])); i += 2
        else:
            out += '<li class="bk-half" aria-hidden="true"></li>' + brick(ws[i], i) + '<li class="bk-half" aria-hidden="true"></li>'; i += 1
        row += 1
    return out

# ---------- HOME ----------
page('index.html','All Phases Of Masonry | Brick, Pavers, Concrete, Wilmington',
 'Evan Schneider and his crew build and repair brick, stone and paver patios, walks, walls and fireplaces in Wilmington, NC. 4.9 on Angi from 65 reviews.', f'''
<section class="hero"><div class="wrap hero-grid">
 <div class="hero-copy">{K('Masonry and hardscape &middot; Wilmington, NC')}
  <h1>Patios, walks, walls and fireplaces. <em>Priced up front.</em></h1>
  <p class="lede">All Phases Of Masonry is Evan Schneider and his crew. Angi lists 36 years of experience and a 4.9 rating from 65 reviews, and customers keep saying the same thing: <q>no changes to the estimate.</q></p>
  <div class="cta"><a class="btn btn--brick" href="tel:{TEL}">Call Evan {TEL_H}</a><a class="btn btn--line" href="contact.html">Free estimate</a></div>
 </div>
 <figure class="wall" aria-labelledby="wall-h">
  <figcaption id="wall-h" class="wall-h">Real jobs, real prices, from Angi reviews</figcaption>
  <ul class="wall-list">{wall_html(WALL[:8])}</ul>
 </figure>
</div>{COURSE('course--hero')}</section>

<section class="stats wrap" aria-label="Angi record">
 <div class="stat rv"><b>4.9</b><span>Angi rating, 65 reviews</span></div>
 <div class="stat rv"><b>91%</b><span>of those reviews are five star</span></div>
 <div class="stat rv"><b>36</b><span>years of experience, per Angi</span></div>
 <div class="stat rv"><b>$0</b><span>for an estimate. Angi lists free estimates.</span></div>
</section>

<section class="kinds on-dark" aria-labelledby="kd-h"><div class="wrap">
 <div class="kinds-head rv">{K('The work')}<h2 id="kd-h">From one sunken stone to a whole backyard.</h2></div>
 <div class="kinds-grid">
  <a class="kind rv" href="services.html#patios"><span class="kind-n">01</span><b>Paver and stone patios</b><span>Interlocking pavers, stone, sitting walls.</span></a>
  <a class="kind rv" href="services.html#concrete"><span class="kind-n">02</span><b>Concrete patios, walks and steps</b><span>The most common job in the reviews.</span></a>
  <a class="kind rv" href="services.html#walls"><span class="kind-n">03</span><b>Brick, stone and block walls</b><span>New walls and veneer repair.</span></a>
  <a class="kind rv" href="services.html#fireplaces"><span class="kind-n">04</span><b>Fireplaces</b><span>Brick or stone, including stacked marble.</span></a>
  <a class="kind rv" href="services.html#tuckpointing"><span class="kind-n">05</span><b>Tuckpointing</b><span>Homes and businesses.</span></a>
  <a class="kind rv" href="services.html#repair"><span class="kind-n">06</span><b>Repairs</b><span>Sunken pavers, cracked flatwork, failing brick.</span></a>
 </div>
</div>{COURSE('course--thin')}</section>

<section class="voices wrap" aria-labelledby="vo-h">
 <div class="rv">{K('What customers say')}<h2 id="vo-h">Quoted on time. Done on time. Cleaned up.</h2></div>
 <div class="voices-grid">{rcard(REV[0],'rcard--lead')}{rcard(REV[1])}{rcard(REV[2])}</div>
 <a class="btn btn--line rv" href="reviews.html">Read ten reviews</a>
</section>

<section class="photos wrap" aria-labelledby="ph-h">
 <div class="rv">{K('Finished work')}<h2 id="ph-h">The photos go here.</h2></div>
 <div class="ph-grid">
  <div class="phbox rv"><p><span class="ph">Placeholder</span> A finished paver patio. One Angi reviewer attached a photo of theirs.</p></div>
  <div class="phbox rv"><p><span class="ph">Placeholder</span> The stacked marble fireplace from August 2023.</p></div>
  <div class="phbox rv"><p><span class="ph">Placeholder</span> A sidewalk poured around tree roots.</p></div>
 </div>
</section>
''', ld=[ORG, bc(('Home',''))])

# ---------- SERVICES ----------
SV = [('patios','Paver and stone patios, walks and steps','Interlocking pavers for patios, walks, steps and driveways, plus brick and stone. A February 2026 job: a 12x12 paver patio with two sitting walls off a porch.',REV[2]),
 ('concrete','Concrete patios, walks and steps','Most of the Angi reviews are concrete jobs: patios dug out, poured and floated, a patio extended, two sidewalks cut through tree roots.',REV[4]),
 ('walls','Brick, stone and block walls','Install and repair. A March 2025 customer had brick veneer repaired and replaced.',REV[8]),
 ('fireplaces','Brick and stone fireplaces','Non gas fireplace installs, per Angi. Evan&rsquo;s crew put stacked marble around one in August 2023.',REV[6]),
 ('tuckpointing','Tuckpointing','For homes and for businesses. A commercial customer in February 2026 plans to hire him again.',REV[9]),
 ('repair','Flatwork repair','Brick and stone flatwork repair, from a $400 sunken stone patio up.',REV[5])]
def sv(i,s):
    k,n,d,r = s
    short = r[5] if len(r[5]) < 260 else r[5][:250].rsplit(' ',1)[0] + '...'
    return (f'<article id="{k}" class="sv rv"><span class="sv-n">{i+1:02d}</span><div class="sv-body"><h2>{n}</h2><p>{d}</p>'
            f'<p class="note"><span class="ph">Placeholder</span> Two photos of this kind of job.</p></div>'
            f'<blockquote class="sv-q"><p>{short}</p><footer>{r[2]}, Angi, {r[1]}{(" &middot; " + r[4]) if r[4] else ""}</footer></blockquote></article>')
page('services.html','Patios, Walls, Fireplaces, Tuckpointing | All Phases Masonry',
 'Paver and stone patios, concrete walks and steps, brick and block walls, fireplaces, tuckpointing and repairs by All Phases Of Masonry in Wilmington, NC.', f'''
<section class="sub"><div class="wrap">{K('The work')}<h1>Brick, stone, pavers, concrete.</h1><p class="lede">Every service here is on the company&rsquo;s Angi profile. Every quote is from an Angi verified review.</p></div>{COURSE()}</section>
<section class="wrap svs">{''.join(sv(i,s) for i,s in enumerate(SV))}</section>
<section class="wrap band rv"><h2>Have a project in mind?</h2><p>Estimates are free, per Angi. Evan comes out, looks, and gives you a number.</p><a class="btn btn--brick" href="contact.html">Free estimate</a></section>
''', ld=[ORG, bc(('Home',''),('The work','services.html'))])

# ---------- REVIEWS ----------
page('reviews.html','Reviews | All Phases Of Masonry, Mason in Wilmington NC',
 'Angi verified reviews for All Phases Of Masonry in Wilmington, NC, quoted word for word with dates and job prices. 4.9 from 65 reviews, 91 percent five star.', f'''
<section class="sub"><div class="wrap">{K('Reviews')}<h1>4.9 on Angi, from 65 reviews.</h1><p class="lede">Ten of them, word for word, with the month and the job price where Angi shows one.</p></div>{COURSE()}</section>
<section class="wrap rv-list">{''.join(rcard(r) for r in REV)}</section>
<section class="wrap"><p class="note rv"><span class="ph">Placeholder</span> On the real site, a link to the full Angi profile and any Google reviews once Evan sets up a Google Business Profile. Source: <a href="{ANGI}" rel="noopener">Angi</a>.</p></section>
''', ld=[ORG, bc(('Home',''),('Reviews','reviews.html'))])

# ---------- ABOUT ----------
page('about.html','About Evan Schneider | All Phases Of Masonry, Wilmington NC',
 'All Phases Of Masonry is Evan Schneider and his crew in Wilmington, NC. Angi lists 36 years of experience, free estimates and a 4.9 rating from 65 reviews.', f'''
<section class="sub"><div class="wrap">{K('About')}<h1>Evan Schneider and his crew.</h1><p class="lede">Angi lists 36 years of experience. Customers mostly talk about how he shows up.</p></div>{COURSE()}</section>
<section class="wrap about">
 <div class="phbox rv"><p><span class="ph">Placeholder</span> Evan on a job site, trowel in hand.</p></div>
 <div class="about-copy rv">
  <h2>What customers notice.</h2>
  <ul class="notice">
   <li><b>He calls back.</b> &ldquo;Called within an hour of requesting service.&rdquo; Ron S., Nov 2023</li>
   <li><b>He comes to quote fast.</b> &ldquo;Within 1 day of my call.&rdquo; Hallie T., Jul 2026</li>
   <li><b>The price holds.</b> &ldquo;The price was exactly what we agreed on.&rdquo; Joe L., Jul 2024</li>
   <li><b>He cleans up.</b> &ldquo;Friendly, fast, good cleanup: A+ all around!&rdquo; Peter C., Nov 2023</li>
   <li><b>Pay at the end.</b> &ldquo;Allowed me to pay when the job was completed.&rdquo; Jill A., Apr 2026</li>
  </ul>
  <p class="note"><span class="ph">Placeholder</span> Evan&rsquo;s story in his own words: where he learned the trade, how long in Wilmington, what kind of job he likes best.</p>
 </div>
</section>
<section class="wrap facts rv"><h2 class="sr">Company facts</h2><dl>
 <div><dt>Owner</dt><dd>Evan Schneider</dd></div>
 <div><dt>Based in</dt><dd>Wilmington, NC</dd></div>
 <div><dt>Experience</dt><dd>36 years, per Angi</dd></div>
 <div><dt>Estimates</dt><dd>Free, per Angi</dd></div>
</dl></section>
''', ld=[ORG, bc(('Home',''),('About Evan','about.html'))])

# ---------- CONTACT ----------
page('contact.html','Free Masonry Estimate | All Phases Of Masonry, Wilmington NC',
 'Ask All Phases Of Masonry for a free estimate on a patio, walk, wall, fireplace or repair. Call Evan Schneider at (910) 465-5284. Based in Wilmington, NC.', f'''
<section class="sub"><div class="wrap">{K('Free estimate')}<h1>Tell Evan about the project.</h1><p class="lede">Calling is fastest. The form shows how a project request could work.</p></div>{COURSE()}</section>
<section class="wrap contact">
 <div class="c-info rv">
  <h2>Call Evan</h2>
  <a class="c-big" href="tel:{TEL}">{TEL_H}</a>
  <p>Based in Wilmington, NC.</p>
  <p class="note"><span class="ph">Placeholder</span> Service area and hours, from Evan.</p>
 </div>
 <form id="qform" class="form rv" novalidate>
  <p class="note"><span class="ph">Demo form</span> Nothing is sent. On a real site this would reach Evan.</p>
  <fieldset><legend class="sr">Your project</legend>
   <div class="two"><label>Name<input name="n" autocomplete="name"></label><label>Phone<input name="p" type="tel" autocomplete="tel"></label></div>
   <div class="two"><label>Project type<select name="t"><option>Paver or stone patio</option><option>Concrete patio, walk or steps</option><option>Wall or veneer</option><option>Fireplace</option><option>Tuckpointing</option><option>Repair</option><option>Something else</option></select></label><label>Neighborhood or ZIP<input name="z" autocomplete="postal-code"></label></div>
   <label>Rough size and what you have in mind<textarea name="m"></textarea></label>
   <label>Photos of the area<input name="f" type="file" accept="image/*" multiple></label>
  </fieldset>
  <button class="btn btn--brick" type="submit">Send request</button>
  <p id="qmsg" role="status"></p>
 </form>
</section>
''', ld=[ORG, bc(('Home',''),('Free estimate','contact.html'))])

page('404.html','Page Not Found | All Phases Of Masonry, Wilmington NC Masons',
 'That page is not here. Head back to the All Phases Of Masonry home page, or call Evan Schneider at (910) 465-5284 for brick, stone and paver work in Wilmington.', f'''
<section class="sub"><div class="wrap">{K('404')}<h1>That page is not here.</h1><p class="lede">Try the home page, or call Evan.</p><div class="cta"><a class="btn btn--brick" href="index.html">Home</a><a class="btn btn--line" href="tel:{TEL}">Call {TEL_H}</a></div></div>{COURSE()}</section>
''')
print('built')

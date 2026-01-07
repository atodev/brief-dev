# Alternative Data Sources & Analysis

## Overview

Brief leverages **alternative data** - unconventional data sources that provide unique market insights before traditional data reflects them. This gives Brief users an informational edge that institutional investors pay millions for.

---

## Core Concept: Information Asymmetry

**Traditional Data** (everyone has access):

- Price and volume
- Company earnings reports
- News articles
- Analyst ratings

**Alternative Data** (Brief's edge):

- Satellite imagery analysis
- Real-time foot traffic
- Supply chain tracking
- Social engagement metrics
- Job posting trends

---

## Satellite Imagery Analysis

### 1. Oil Storage Tank Analysis

**Your Example: Shadow Length Analysis**

```
PROBLEM: Oil inventory reports come out weekly (Wednesdays)
SOLUTION: Satellite images show real-time storage levels

HOW IT WORKS:
┌─────────────────────────────────────────────────────────┐
│                                                           │
│  Satellite Image → Computer Vision → Volume Estimation   │
│                                                           │
│  ☀️ Sun angle = Known                                    │
│  📏 Shadow length = Measurable                            │
│  🛢️ Tank height = Known (public data)                    │
│                                                           │
│  Shadow Math:                                             │
│  - Long shadows = Empty tanks (shadow reaches far)       │
│  - Short shadows = Full tanks (liquid fills to rim)      │
│  - Floating roof visible = Can measure fill level        │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

**Analysis Process**:

```python
def analyze_oil_storage(satellite_image, location, timestamp):
    """
    Analyze oil storage tanks from satellite imagery
    """
    # 1. Identify tanks (circular structures)
    tanks = detect_storage_tanks(satellite_image)

    # 2. Measure shadows
    for tank in tanks:
        shadow_length = measure_shadow(tank, sun_angle)
        tank_height = get_tank_specs(location, tank.id)

        # 3. Calculate fill level
        # Empty tank: floating roof at bottom, long shadow
        # Full tank: floating roof at top, short shadow
        fill_percentage = calculate_fill_level(
            shadow_length,
            tank_height,
            sun_angle
        )

        # 4. Estimate volume
        volume_barrels = tank.capacity * fill_percentage

    # 5. Aggregate across facility
    total_inventory = sum(volume for tank in tanks)

    # 6. Compare to previous week
    change = total_inventory - last_week_inventory

    # 7. Predict price movement
    if change < -5_000_000:  # 5M barrel draw
        prediction = "Bullish - Low inventory"
        confidence = 0.85
    elif change > 5_000_000:  # 5M barrel build
        prediction = "Bearish - High inventory"
        confidence = 0.85
    else:
        prediction = "Neutral"
        confidence = 0.60

    return {
        'current_inventory': total_inventory,
        'change_vs_last_week': change,
        'prediction': prediction,
        'confidence': confidence,
        'report_date': next_wednesday  # Official report
    }
```

**Real Example**:

```
🛢️ Crude Oil Alternative Data Alert

📡 Satellite Analysis (Cushing, OK):
Current Inventory: 23.4M barrels (↓ 6.2M from last week)

Shadow Analysis:
- 47 tanks analyzed
- Average fill level: 58% (down from 71%)
- Confidence: 88%

🎯 PREDICTION:
Official EIA report (Wednesday): Will show large draw
Historical accuracy when change > 5M barrels: 82%

📊 TRADING SIGNAL:
Crude Oil (WTI): BULLISH
Entry: $72.50 | Target: $76.00 | Timeframe: 3 days
Catalyst: EIA report expected to confirm low inventory

⚠️ Risk: Weather could delay report, geopolitical events
```

---

### 2. Retail Parking Lot Analysis

**Use Case**: Predict retail earnings before they're announced

```
TARGET: Apple Store, Fifth Avenue, NYC
ANALYSIS: Parking lot fullness + foot traffic

┌─────────────────────────────────────────────────────────┐
│ Satellite Image Sequence (Hourly, 7 days)                │
│                                                           │
│ Monday 10 AM:    ████████░░ 80% full (peak shopping)     │
│ Monday 2 PM:     ██████░░░░ 60% full                     │
│ Monday 6 PM:     ████░░░░░░ 40% full                     │
│                                                           │
│ Compare to last year same week:                          │
│ Last Year:       ████░░░░░░ 40% full (average)           │
│ This Year:       ████████░░ 80% full (↑100%)            │
│                                                           │
│ INSIGHT: Foot traffic doubled YoY                        │
│ IMPLICATION: Strong iPhone sales likely                  │
│ CONFIDENCE: 75% (correlated 8/10 times historically)     │
└─────────────────────────────────────────────────────────┘
```

**Brief Alert**:

```
🏪 Alternative Data: Apple Retail Surge

📡 Parking lot analysis shows foot traffic up 95% YoY at
flagship stores across 15 locations.

Historical pattern: When parking lots are 80%+ full during
non-launch periods, Apple beats earnings by avg 8%.

🎯 OPPORTUNITY:
Apple (AAPL): Add to watchlist
Earnings: Jan 28 (21 days away)
Expected Beat: 5-10% above consensus

📍 Local Edge: You're 5 km from Apple HQ - you might notice
increased activity at their Cupertino campus.

Community: 23 Auckland members reported seeing more Apple
bags at shopping centers this week 🛍️
```

---

### 3. Manufacturing Activity

**Use Case**: Tesla production tracking

```
🏭 TESLA GIGAFACTORY (Shanghai)

Satellite Analysis:
- Parking lot: 94% full (production shift in progress)
- Trucks at loading dock: 47 (↑ from avg 32)
- Outdoor vehicle storage: 1,243 cars (ready for delivery)

Change vs. last month:
- Vehicles produced: +18%
- Trucks loading: +47%
- Employee parking: +12% (hiring surge)

🎯 PREDICTION:
Tesla China deliveries will beat expectations
Delivery report: Jan 10 (3 days)
Expected beat: 15-20% above analyst estimates

TRADE SETUP:
Tesla (TSLA): Entry $245, Target $265
Catalyst: Delivery numbers announcement
```

---

## Ship Tracking & Supply Chain

### Use Case: Commodity Supply Analysis

```
🚢 SHIPPING INTELLIGENCE

OIL TANKERS (Global Fleet Tracking):

Current Data (Real-time):
- Tankers en route to US: 47 ships
- Average speed: 12 knots (normal)
- Estimated arrival: 5-7 days
- Total cargo: 8.2M barrels

Change vs. last month:
- Ships en route: -23% (↓ 14 ships)
- Cargo volume: -28%
- Delays: +3 days (Red Sea tensions)

🎯 IMPLICATION:
Oil supply to US refineries decreasing
Gasoline prices likely to rise
Refinery stocks will drop

OPPORTUNITY:
Energy stocks (XLE ETF): BULLISH
Timeframe: 2-3 weeks
```

**Data Sources**:

- **MarineTraffic**: Real-time ship positions (AIS data)
- **FleetMon**: Shipping routes and cargo
- **VesselsValue**: Fleet capacity and utilization

**Example Alert**:

```
⛴️ Supply Chain Alert: Copper Shortage Incoming

📊 Data:
- 18 copper cargo ships delayed at Chinese ports (COVID restrictions)
- Normal: 3-5 day delays
- Current: 12-18 day delays
- Affected cargo: 150,000 tonnes

🏭 Impact:
Manufacturing slowdown expected in 2-3 weeks
Electronics, construction sectors affected

💰 TRADE OPPORTUNITIES:
1. Copper futures (HG): Long position
2. Freeport-McMoRan (FCX): Mining stock, BULLISH
3. Tesla (TSLA): SHORT (needs copper for EVs)

Confidence: 72% (supply chain data reliable)
```

---

## Foot Traffic & Consumer Behavior

### Data Source: SafeGraph, Placer.ai

**Use Case**: Restaurant chain performance

```
📍 MCDONALD'S FOOT TRAFFIC ANALYSIS

Locations analyzed: 500 US stores
Period: Last 30 days vs. last year

Findings:
┌────────────────────┬─────────┬──────────┐
│ Region             │ YoY     │ Trend    │
├────────────────────┼─────────┼──────────┤
│ Northeast          │ +8%     │ ↗️ Up    │
│ Southeast          │ +12%    │ ↗️ Up    │
│ Midwest            │ -2%     │ ↘️ Down  │
│ West Coast         │ +5%     │ ↗️ Up    │
│ Southwest          │ +15%    │ ↗️↗️ Strong │
└────────────────────┴─────────┴──────────┘

Average visit duration: 18 min (↑ from 15 min)
Peak hours: 12-1 PM (lunch rush ↑ 22%)
Weekend traffic: +9% YoY

🎯 PREDICTION:
McDonald's Q4 earnings will beat by 6-8%
Same-store sales growth: 8-10% (vs 5% consensus)

Earnings Date: Jan 29
Current Price: $285
Target: $305 (+7%)

⚠️ RISK: Labor costs rising may offset revenue gains
```

---

## Web Scraping & Online Signals

### 1. Job Posting Analysis

```
💼 HIRING TRENDS = BUSINESS GROWTH

Company: a2 Milk Company (ATM.NZ)
Your Distance: 8 km (Auckland)

LinkedIn Job Postings (Last 30 days):
┌─────────────────────────┬───────┬─────────┐
│ Department              │ Posts │ Change  │
├─────────────────────────┼───────┼─────────┤
│ Sales (China)           │ 12    │ ↑ +300% │
│ Marketing               │ 8     │ ↑ +150% │
│ Supply Chain            │ 5     │ ↑ +100% │
│ R&D                     │ 3     │ ↑ +50%  │
│ Total                   │ 28    │ ↑ +180% │
└─────────────────────────┴───────┴─────────┘

Historical Pattern:
When job postings > 20/month:
- Revenue grows 15%+ next quarter (9/10 times)
- Stock price rises 12% avg over 90 days

🎯 SIGNAL: Strong Growth Expected
a2 Milk is rapidly expanding, especially in China market

YOUR EDGE: Drive by their Auckland HQ and see the hiring
activity firsthand. Parking lot filling up? More people
at lunch spots nearby? These are leading indicators!
```

### 2. App Download Rankings

```
📱 APP STORE INTELLIGENCE

Tracking: Uber (UBER)
Region: United States

App Store Rankings (Transportation Category):
Today: #3 (↑ 2 spots from last week)
Downloads: +45% WoW
Reviews: 4.8 stars (↑ from 4.6)

User Reviews (Sentiment Analysis):
"Wait times way down" - mentioned 2,340 times
"Cheaper than last month" - 1,892 mentions
"More drivers available" - 1,234 mentions

🎯 INSIGHT:
Supply-demand balance improving
Driver recruitment working
User satisfaction increasing

PREDICTION:
Uber Q1 guidance will be raised
Rides per day up ~40-50%

OPPORTUNITY: UBER stock - BULLISH
Entry: $72 | Target: $82 | Timeframe: 30 days
```

### 3. Product Availability Scraping

```
🛒 E-COMMERCE SIGNALS

Company: Apple (AAPL)
Product: iPhone 15 Pro Max

Availability Tracking (50 stores globally):
In Stock: 92% (↑ from 45% last month)
Delivery: 1-3 days (↓ from 4-6 weeks)
Discount: None (full price maintained)

🎯 INTERPRETATION:
- Supply chain issues resolved ✅
- Demand remains strong (no discounts) ✅
- Inventory accumulation (either good or bad)

TWO SCENARIOS:

Bullish Case (65% probability):
- Apple solved production issues
- Meeting strong demand efficiently
- Margins will improve

Bearish Case (35% probability):
- Demand is slowing (excess inventory)
- May need to discount soon
- Revenue miss possible

WAIT FOR: Next week's data
If discounts appear → BEARISH
If still full price → BULLISH
```

---

## Credit Card Transaction Data

### Data Source: Second Measure, Facteus

```
💳 CONSUMER SPENDING PATTERNS

Sector: Quick Service Restaurants (QSR)
Period: December 2025 (Holiday season)

Transaction Volume ($ millions):
McDonald's: $1,240M (↑ 8% YoY)
Starbucks: $890M (↑ 12% YoY)
Chipotle: $620M (↑ 18% YoY)
Subway: $410M (↓ 3% YoY)

Average Transaction Size:
McDonald's: $12.50 (↑ $1.20)
Starbucks: $8.90 (↑ $0.80)
Chipotle: $18.20 (↑ $2.10)

Unique Customers:
Starbucks: +5% (customer growth)
Chipotle: +7% (customer growth)

🎯 RANKINGS FOR BRIEF:

1. Chipotle (CMG): Score 88/100
   - Volume: +18% ✅
   - Avg ticket: +13% ✅
   - Customers: +7% ✅
   - VERDICT: STRONG BUY before earnings

2. Starbucks (SBUX): Score 82/100
   - Solid growth across metrics
   - VERDICT: BUY

3. McDonald's (MCD): Score 75/100
   - Decent growth but slowing
   - VERDICT: HOLD
```

---

## Social Media Engagement

### Beyond Sentiment: Engagement Quality

```
📊 SOCIAL MEDIA INTELLIGENCE

Brand: Tesla
Platform: Twitter/X

Metrics (Last 7 days):
- Mentions: 2.4M (↑ 340%)
- Engagement: 45M interactions
- Sentiment: 89% positive

DEEP ANALYSIS:
Quality of Engagement:
- Verified accounts: 23,000 mentions (institutional interest)
- Influencers (>100K followers): 450 mentions
- Average retweets per post: 2,400 (viral content)

Content Analysis:
"Cybertruck" mentions: 450K (new product buzz)
"Self-driving" mentions: 280K (technology focus)
"Elon Musk" mentions: 1.2M (CEO brand strong)

🎯 INSIGHT:
- Product excitement (Cybertruck)
- Not just CEO hype (tech discussion strong)
- Institutional attention (verified accounts)

HISTORICAL PATTERN:
When verified account mentions > 20K in 7 days:
- Stock rises 8% avg over next 14 days (7/9 times)

RECOMMENDATION: Tesla (TSLA) - BULLISH
Confidence: 74%
```

---

## Briefing Integration

### How Alternative Data Appears in Your Brief

**Voice Briefing**:

```
"In second place today, we have Crude Oil with a score of 85.
Now, here's where it gets interesting: Our satellite analysis
of oil storage facilities shows inventory levels are down 26%
from last week. We're seeing long shadows over the tanks at
Cushing, Oklahoma, which means they're running low on supply.

The official government report comes out Wednesday, but we're
giving you this insight 3 days early. Historically, when our
satellite data shows drops this large, the official numbers
confirm it 82% of the time, and oil prices rise an average
of 5% within a week.

This is exactly the kind of alternative data edge that
institutions pay millions for - and you're getting it in
your morning brief."
```

**Email Report**:

```
┌─────────────────────────────────────────────────────────┐
│ 🥈 #2 RANKED: Crude Oil (WTI)              Score: 85/100│
│                                                           │
│ 🛢️ Alternative Data Alert: Satellite Imagery Analysis    │
│                                                           │
│ WHY #2? Unique Data Signals                              │
│                                                           │
│ 📡 SATELLITE INTELLIGENCE [Impact: Very High]            │
│    • Shadow analysis shows 26% inventory draw             │
│    • 47 storage tanks analyzed at Cushing, OK            │
│    • Average fill level: 58% (↓ from 71%)                │
│    • Confidence: 88%                                     │
│    Weight: 40% of ranking                                │
│                                                           │
│ 📊 BEFORE THE HEADLINES                                  │
│    • Official EIA report: Wednesday (3 days away)         │
│    • Our data gives you 72-hour head start               │
│    • Historical accuracy: 82% when change >5M barrels    │
│                                                           │
│ 🎯 OPPORTUNITY TYPE: Short-term momentum play            │
│    Entry: $72.50 | Target: $76.00 (+5%)                 │
│    Timeframe: 3-7 days                                   │
│    Catalyst: EIA report confirmation                     │
│                                                           │
│ [Satellite Images →] [Historical Accuracy →]             │
└─────────────────────────────────────────────────────────┘
```

---

## Data Provider Costs

### Pricing (Approximate)

| Data Source                   | Cost/Month   | Value                  |
| ----------------------------- | ------------ | ---------------------- |
| Planet Labs (Satellite)       | $10,000      | High - Daily imagery   |
| Maxar (High-res satellite)    | $25,000      | Very High - Detailed   |
| MarineTraffic (Ships)         | $500         | Medium - Supply chain  |
| SafeGraph (Foot traffic)      | $5,000       | High - Consumer trends |
| Second Measure (Credit cards) | $15,000      | Very High - Spending   |
| App Annie (App data)          | $1,000       | Medium - Downloads     |
| **Total**                     | **~$56,500** | **Institutional Edge** |

**Brief's Advantage**:

- Small players can't afford this
- Brief spreads cost across user base
- Each user pays $10-30/month subscription
- Democratizes institutional-grade data! 💎

---

## Community Contributions

**Users Can Share Alternative Data**:

```
👤 User Post in #auckland-investors:

"Just drove past a2 Milk HQ. Parking lot is PACKED at 7 PM.
Usually empty by 6. Something big happening? 👀"

🤖 Brief AI Response:
"Excellent observation! This aligns with our data:
- Job postings: +180% this month
- LinkedIn shows 28 open positions
- Our satellite data confirms increased activity

Combined with your real-time ground intel, this strengthens
our bullish thesis on a2 Milk. You just contributed
alternative data! 🎯"

⬆️ 45 upvotes | Added to Brief's analysis engine
```

---

This alternative data system gives Brief users the **same edge that hedge funds pay millions for** - democratizing alpha! 🚀

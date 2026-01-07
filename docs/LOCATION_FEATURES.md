# Location-Based Investment Prioritization

## Feature Overview

Brief's unique selling point is **geographic-aware investment recommendations**. The app prioritizes investment opportunities based on proximity to the user, creating a "home field advantage" for local market awareness.

---

## Core Concept

### The Local Advantage Theory

**Hypothesis**: Investors have informational advantages for companies and markets in their geographic proximity due to:

1. **Real-time Local Knowledge**

   - Observe company operations firsthand
   - Notice hiring trends, store traffic, construction activity
   - Hear local news and gossip before it goes national
   - Understand local economic conditions viscerally

2. **Time Zone Alignment**

   - Market hours overlap with your waking hours
   - Can react quickly to market movements
   - Less need to wake up early or stay up late to trade

3. **Cultural Understanding**

   - Better grasp of local consumer preferences
   - Understand regional business practices
   - Recognize local competitive dynamics

4. **Economic Impact Awareness**
   - Companies that employ your neighbors
   - Businesses that impact your local economy
   - Regional supply chain relationships

---

## Geographic Tiers

### Tier 1: Hyper-Local (0-100 km)

**Examples**:

- User in Cupertino, CA → Apple HQ (5 km)
- User in Seattle, WA → Amazon HQ (10 km)
- User in Austin, TX → Tesla Gigafactory (20 km)

**Weight**: 100% location score
**Rationale**: Maximum local awareness, drive-by observation possible

**User Experience**:

```
🏢 Apple (AAPL) - 5 km away
"Headquartered in your backyard! You're in the best
position to spot trends others might miss."
```

---

### Tier 2: Regional (100-500 km)

**Examples**:

- User in San Francisco → Los Angeles companies (560 km)
- User in Boston → New York companies (350 km)
- User in Dallas → Houston companies (400 km)

**Weight**: 75% location score
**Rationale**: Same regional economy, similar weather/culture

**User Experience**:

```
🌉 Netflix (NFLX) - 450 km away (Los Angeles)
"West Coast neighbor. Same state economy and tech ecosystem."
```

---

### Tier 3: National (500-2000 km)

**Examples**:

- User in San Francisco → New York companies (4,200 km)
- User in Miami → Chicago companies (2,000 km)
- User in Los Angeles → Boston companies (4,200 km)

**Weight**: 50% location score
**Rationale**: Same country, but different regional dynamics

**User Experience**:

```
🗽 JPMorgan Chase (JPM) - 4,200 km away (New York)
"East Coast presence. Different time zone but same national economy."
```

---

### Tier 4: International (2000+ km)

**Examples**:

- User in USA → London companies (8,000 km)
- User in USA → Tokyo companies (10,000 km)
- User in USA → Sydney companies (12,000 km)

**Weight**: 25% location score
**Rationale**: Limited local advantage, different time zones

**User Experience**:

```
🌍 HSBC Holdings - 8,500 km away (London)
"International opportunity. Consider time zone for active trading."
```

---

## Location Scoring Algorithm

### Input Data

1. **User Location**

   ```json
   {
     "latitude": 37.7749,
     "longitude": -122.4194,
     "city": "San Francisco",
     "state": "CA",
     "country": "USA",
     "timezone": "America/Los_Angeles"
   }
   ```

2. **Company Location**
   ```json
   {
     "asset_id": "AAPL",
     "hq_location": {
       "latitude": 37.3349,
       "longitude": -122.009,
       "city": "Cupertino",
       "state": "CA"
     },
     "primary_exchange": {
       "name": "NASDAQ",
       "location": {
         "latitude": 40.7128,
         "longitude": -74.006,
         "timezone": "America/New_York"
       }
     }
   }
   ```

### Calculation Steps

#### Step 1: Distance Calculation

```python
distance = haversine(user_lat, user_lon, company_lat, company_lon)
# Result: 55 km
```

#### Step 2: Tier Assignment

```python
if distance < 100:
    tier = "Hyper-Local"
    base_score = 100
elif distance < 500:
    tier = "Regional"
    base_score = 75
elif distance < 2000:
    tier = "National"
    base_score = 50
else:
    tier = "International"
    base_score = 25
```

#### Step 3: Market Hours Overlap

```python
# User awake: 6 AM - 11 PM PST
# NASDAQ hours: 6:30 AM - 1 PM PST (converted from 9:30 AM - 4 PM EST)
overlap_hours = 6.5  # Full market hours overlap
overlap_score = (6.5 / 6.5) * 100 = 100
```

#### Step 4: Local Economic Impact

```python
local_impact = 0

# Major employer check
if company_employees_in_region > 1000:
    local_impact += 10

# Regional operations check
if company_has_offices_nearby:
    local_impact += 5

# Economic correlation
if regional_gdp_correlation > 0.7:
    local_impact += 5

# Total: 20 points possible
```

#### Step 5: Final Location Score

```python
location_score = (
    base_score * 0.40 +           # 40% tier weight (100)
    overlap_score * 0.30 +        # 30% market hours (100)
    local_impact * 0.20 +         # 20% economic impact (20)
    familiarity_bonus * 0.10      # 10% familiarity (0)
)

# Result:
# (100 * 0.40) + (100 * 0.30) + (20 * 0.20) + (0 * 0.10) = 74
```

### Integration with AI Score

```python
# AI predicted return: 8.5% (score: 85/100)
# Location score: 74/100
# Sentiment score: 80/100
# Technical score: 75/100

final_score = (
    ai_score * 0.35 +          # 35%: 85 * 0.35 = 29.75
    location_score * 0.25 +    # 25%: 74 * 0.25 = 18.50
    sentiment_score * 0.20 +   # 20%: 80 * 0.20 = 16.00
    technical_score * 0.15 +   # 15%: 75 * 0.15 = 11.25
    risk_adjusted * 0.05       #  5%: 70 * 0.05 =  3.50
)

# Final: 79.0 / 100
```

---

## User Controls

### Location Preference Slider

Users can adjust how much weight is given to location:

```
[Local Focus] ←----------●----------→ [Global Focus]
     40%              25%                   0%
  (Heavy Local)    (Balanced)      (Ignore Location)
```

**Heavy Local Focus** (40% location weight):

- Reduce AI score to 25%
- Best for: Local market enthusiasts, real estate investors
- Example: "I only want to invest in Bay Area companies"

**Balanced** (25% location weight - Default):

- Standard weighting
- Best for: Most users

**Global Focus** (0% location weight):

- Distribute location weight to AI score (becomes 60%)
- Best for: Users who travel frequently, institutional investors
- Example: "I don't care where the company is, just best returns"

---

## Location-Based Features

### 1. Geographic Heatmap

Visual representation of opportunities by location:

```
    [Map of United States]

    🔴 San Francisco Bay Area (5 opportunities)
    🟠 Seattle (2 opportunities)
    🟡 Los Angeles (3 opportunities)
    🟢 Austin (1 opportunity)
    🔵 New York (2 opportunities)
```

Users can tap regions to see local opportunities.

---

### 2. "Nearby Companies" Feed

Real-time feed of companies within 50 km:

```
📍 Nearby Opportunities

Apple Inc. (AAPL)               5 km → Score: 87
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
↗ Price up 2.3% today
💬 2 positive analyst ratings this week

Google (GOOGL)                  15 km → Score: 82
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Breaking resistance level
📰 New AI product launch announced

Tesla (TSLA)                    35 km → Score: 78
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ High volatility alert
🏭 Fremont factory hiring surge
```

---

### 3. Commute Insights (Premium Feature)

Track companies along user's commute route:

```
🚗 Along Your Commute (Home → Office)

You pass 12 company headquarters daily:
• Apple HQ (exit 12A)
• Meta Campus (exit 14)
• Stanford Shopping Center (retail analytics)

💡 Tip: Notice parking lot activity, construction,
employee mood. These are leading indicators!
```

---

### 4. Local Economic Dashboard

Show regional economic health:

```
📊 Bay Area Economic Indicators

Employment: ●●●●○ (8.2% growth)
Housing: ●●○○○ (Prices up 15%)
Tech Hiring: ●●●●● (Record highs)
VC Funding: ●●●●○ ($12B last quarter)

💡 Strong local economy suggests local tech
stocks may outperform.
```

---

### 5. Location-Based Alerts

Push notifications for local events:

```
🔔 Local Market Alert

Tesla is hosting an investor day at their
Fremont factory tomorrow (40 km from you).

Consider attending or watching the livestream
for investment insights before the market reacts.

[Add to Calendar] [View Details]
```

---

## Special Cases

### Cryptocurrency

**Challenge**: No physical headquarters for decentralized assets

**Solution**:

- Use location of primary development team
- Use location of largest mining/staking operations
- Use location of primary exchange listing
- Default to user's location (neutral score) if no clear location

**Example**:

```
Bitcoin (BTC)
Location: Decentralized
Exchange: Coinbase (San Francisco, 0 km)
Score: Based on exchange proximity
```

---

### Forex

**Challenge**: Currency pairs don't have a "location"

**Solution**:

- Use location of central bank
- Weight by economic ties between countries
- Consider time zone for active trading

**Example**:

```
EUR/USD
ECB: Frankfurt, Germany (9,200 km)
Federal Reserve: Washington DC, USA (3,900 km)
Combined Score: Weighted by user's country
```

---

### Commodities

**Challenge**: Commodities are global

**Solution**:

- Use primary production location
- Use primary futures exchange location
- Consider local demand factors

**Example**:

```
Crude Oil (WTI)
Production: Texas, USA (2,500 km)
Exchange: NYMEX, New York (4,200 km)
Local Impact: High (major US industry)
```

---

## Privacy Considerations

### Location Data Handling

**What We Store**:

- User's city and state (not exact address)
- Approximate coordinates (rounded to 0.1° precision ~11 km)
- Timezone

**What We DON'T Store**:

- Exact home address
- Real-time GPS tracking
- Location history

**User Controls**:

- Manual location entry option
- Choose city instead of GPS detection
- Disable location features entirely
- Delete location data anytime

**Compliance**:

- GDPR compliant
- CCPA compliant
- Location data encrypted at rest
- Not shared with third parties

---

## Competitive Advantages

### What Makes This Unique?

1. **No Other App Does This**: Traditional investment apps ignore geography
2. **Behavioral Edge**: Users are more engaged with local companies
3. **Information Advantage**: Real-world observation supplements data
4. **Community Building**: Connect with local investors
5. **Educational**: Learn about companies in your area

### Marketing Angle

**Tagline**: "Invest in What You Know, Start With What's Near"

**Key Messages**:

- "You're already an expert on your local economy"
- "Your daily commute is market research"
- "Home field advantage for your investments"
- "Know your neighbors, invest in their success"

---

## Success Metrics

### Location Feature Engagement

**Track**:

- % of users who enable location features
- Average distance of selected investments
- Correlation between proximity and investment success
- User satisfaction with location-based recommendations

**Hypothesis to Test**:

- Do local investments perform better for users?
- Are users more likely to act on local recommendations?
- Does location awareness improve portfolio diversification?

**Expected Results**:

- 70%+ users enable location features
- 40% of investments within 500 km of user
- Higher user engagement with local opportunities
- Improved user retention

---

## Future Enhancements

### Phase 1 (Current)

- ✅ Basic distance calculation
- ✅ 4-tier geographic system
- ✅ Location-weighted scoring

### Phase 2 (Next 6 months)

- 🔄 Commute route analysis
- 🔄 Real-time location updates
- 🔄 Local event integration

### Phase 3 (Next 12 months)

- 📅 AR features (point phone at building, see stock info)
- 📅 Social: Connect with nearby investors
- 📅 Local investor meetups
- 📅 Company visit scheduling

### Phase 4 (Future)

- 💡 Satellite imagery analysis (parking lot fullness)
- 💡 Foot traffic data integration
- 💡 Local employment trend analysis
- 💡 Regional supply chain mapping

---

## Technical Implementation

### Database Schema

```sql
-- User locations
CREATE TABLE user_locations (
    user_id UUID PRIMARY KEY,
    location GEOGRAPHY(POINT, 4326),  -- PostGIS
    city VARCHAR(100),
    state VARCHAR(50),
    country VARCHAR(50),
    timezone VARCHAR(50),
    updated_at TIMESTAMP
);

-- Company locations
CREATE TABLE company_locations (
    company_id VARCHAR(20) PRIMARY KEY,
    hq_location GEOGRAPHY(POINT, 4326),
    hq_address TEXT,
    primary_exchange_id VARCHAR(20),
    updated_at TIMESTAMP
);

-- Exchange locations
CREATE TABLE exchange_locations (
    exchange_id VARCHAR(20) PRIMARY KEY,
    location GEOGRAPHY(POINT, 4326),
    timezone VARCHAR(50),
    market_open TIME,
    market_close TIME
);

-- Spatial index for fast proximity queries
CREATE INDEX idx_company_location ON company_locations
    USING GIST (hq_location);
```

### API Endpoints

```typescript
// Get nearby opportunities
GET /api/v1/opportunities/nearby
Query params:
  - radius_km: number (default: 100)
  - asset_type: 'all' | 'stocks' | 'crypto' | 'forex'
  - min_score: number (default: 60)

// Update user location
PUT /api/v1/user/location
Body: {
  latitude: number,
  longitude: number,
  manual: boolean  // true if user manually entered
}

// Get location-based briefing
GET /api/v1/briefing/location-aware
Query params:
  - location_weight: number (0-40, default: 25)
  - max_distance_km: number (default: unlimited)
```

---

This location-based approach is Brief's **killer feature** that differentiates it from every other investment app on the market! 🚀

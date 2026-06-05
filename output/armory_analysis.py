import csv
import json
from collections import defaultdict

# Load all data
tools = {}
usage_by_month = defaultdict(lambda: defaultdict(dict))
backlog = {}
feedback_by_tool = defaultdict(list)

# Load tools.csv
with open('/mnt/user-data/uploads/tools.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        tool_id = row['tool_id']
        tools[tool_id] = {
            'name': row['name'],
            'category': row['category'],
            'status': row['status'],
            'months_since_launch': int(row['months_since_launch']),
            'installs': int(row['studios_installed']),
            'active_30d': int(row['active_studios_30d']),
            'retention_w4_pct': float(row['retention_week4_pct']),
            'deploys_per_studio': float(row['deploys_per_active_studio_mo']),
            'support_tickets': int(row['support_tickets_30d']),
            'csat': float(row['csat_1to5']),
            'infra_cost': int(row['infra_cost_usd_mo']),
        }

# Load usage-monthly.csv
with open('/mnt/user-data/uploads/usage-monthly.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        month = row['month']
        tool_id = row['tool_id']
        usage_by_month[tool_id][month] = {
            'installs': int(row['cumulative_installs']),
            'active_30d': int(row['active_studios_30d']),
        }

# Load intake-backlog.csv
with open('/mnt/user-data/uploads/intake-backlog.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        request_id = row['request_id']
        backlog[request_id] = {
            'title': row['title'],
            'type': row['type'],
            'source': row['source'],
            'reach': int(row['reach_studios']),
            'impact': float(row['impact_0_25to3']),
            'confidence': float(row['confidence_pct']) / 100,
            'effort': int(row['effort_person_weeks']),
            'notes': row['notes'],
        }

# Load studio-feedback.csv
with open('/mnt/user-data/uploads/studio-feedback.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        feedback_by_tool[row['tool_id']].append({
            'studio': row['studio'],
            'sentiment': row['sentiment'],
            'quote': row['quote'],
        })

print("=" * 80)
print("ARMORY STOREFRONT: DATA ANALYSIS")
print("=" * 80)

# 1. HEADLINE vs REALITY: Installs vs Activation
print("\n1. INSTALLS VS ACTIVATION (Reach vs Value)")
print("-" * 80)

analysis = []
for tool_id, data in tools.items():
    activation_rate = (data['active_30d'] / data['installs'] * 100) if data['installs'] > 0 else 0
    monthly_ticket_cost = data['support_tickets'] * 50  # Assumed $50/ticket cost
    roi_score = (data['active_30d'] * data['csat']) / (data['infra_cost'] + 200)  # Rough efficiency
    
    analysis.append({
        'tool_id': tool_id,
        'name': data['name'],
        'installs': data['installs'],
        'active_30d': data['active_30d'],
        'activation_rate': activation_rate,
        'retention_w4': data['retention_w4_pct'],
        'csat': data['csat'],
        'deploys_per_studio': data['deploys_per_studio'],
        'support_cost_mo': monthly_ticket_cost,
        'infra_cost': data['infra_cost'],
        'total_cost': monthly_ticket_cost + data['infra_cost'],
        'roi_score': roi_score,
    })

# Sort by activation rate
analysis.sort(key=lambda x: x['activation_rate'], reverse=True)

for item in analysis:
    print(f"{item['name']:20} | Installs: {item['installs']:3} | Active: {item['active_30d']:3} "
          f"| Activation: {item['activation_rate']:5.1f}% | CSAT: {item['csat']:.1f} | Cost: ${item['total_cost']:5.0f}/mo")

print("\n  ⚠️  HEADLINE TRAP: ArcaneArt has 95 installs (highest) but 29.5% activation rate.")
print("  📈 REAL WINNER: EchoVoice has 90.5% activation rate, 81% retention, 4.7 CSAT.")

# 2. GROWTH TRAJECTORY
print("\n2. GROWTH TRAJECTORY (Last 2 Months)")
print("-" * 80)

for tool_id in sorted(tools.keys()):
    m5_installs = usage_by_month[tool_id].get('M5', {}).get('installs', 0)
    m6_installs = usage_by_month[tool_id].get('M6', {}).get('installs', 0)
    m5_active = usage_by_month[tool_id].get('M5', {}).get('active_30d', 0)
    m6_active = usage_by_month[tool_id].get('M6', {}).get('active_30d', 0)
    
    install_growth = m6_installs - m5_installs
    active_growth = m6_active - m5_active
    
    trend = "↗️" if install_growth > 5 else ("→" if install_growth >= 0 else "↘️")
    
    print(f"{tools[tool_id]['name']:20} | M5→M6 installs: {m5_installs:3}→{m6_installs:3} ({install_growth:+3}) | "
          f"Active: {m5_active:3}→{m6_active:3} ({active_growth:+3}) {trend}")

# 3. COST-BENEFIT ANALYSIS
print("\n3. COST-BENEFIT ANALYSIS")
print("-" * 80)

analysis.sort(key=lambda x: x['total_cost'], reverse=True)
for item in analysis:
    cost_per_active_studio = (item['total_cost'] / item['active_30d']) if item['active_30d'] > 0 else float('inf')
    print(f"{item['name']:20} | Monthly Cost: ${item['total_cost']:5.0f} | Cost/Active: ${cost_per_active_studio:6.0f} "
          f"| CSAT: {item['csat']:.1f}")

print("\n  💰 EXPENSIVE LOSERS: ArcaneArt ($4900/mo), MotionMage ($1700/mo) with low retention.")
print("  ✅ EFFICIENT WINNERS: EchoVoice ($1100/mo), BugHound ($500/mo, beta).")

# 4. SUNSET CANDIDATES & SAVINGS
print("\n4. SUNSET ANALYSIS")
print("-" * 80)

sunset_candidates = []
for tool_id, data in tools.items():
    months_old = data['months_since_launch']
    if months_old >= 6:  # Mature tools
        if data['retention_w4_pct'] < 30 or (data['active_30d'] < 10 and data['csat'] < 3.5):
            sunset_candidates.append({
                'tool_id': tool_id,
                'name': data['name'],
                'installs': data['installs'],
                'active': data['active_30d'],
                'retention': data['retention_w4_pct'],
                'csat': data['csat'],
                'cost': data['support_tickets'] * 50 + data['infra_cost'],
            })

sunset_candidates.sort(key=lambda x: x['cost'], reverse=True)
total_sunset_savings = 0

for candidate in sunset_candidates:
    print(f"  🗑️  {candidate['name']:20} | {candidate['active']:2} active | {candidate['retention']:.0f}% retention | "
          f"{candidate['csat']:.1f} CSAT | Save ${candidate['cost']}/mo")
    total_sunset_savings += candidate['cost']

if sunset_candidates:
    print(f"\n  💾 Total Monthly Savings from Sunsetting: ${total_sunset_savings}")

# 5. RICE SCORE COMPUTATION FOR BACKLOG
print("\n5. BACKLOG PRIORITIZATION (RICE SCORES)")
print("-" * 80)

rice_scores = []
for req_id, req in backlog.items():
    reach = req['reach']
    impact = req['impact']
    confidence = req['confidence']
    effort = req['effort']
    
    rice = (reach * impact * confidence) / effort
    
    rice_scores.append({
        'req_id': req_id,
        'title': req['title'],
        'type': req['type'],
        'rice': rice,
        'reach': reach,
        'impact': impact,
        'confidence': confidence,
        'effort': effort,
        'reach_effort_ratio': reach / effort,
    })

rice_scores.sort(key=lambda x: x['rice'], reverse=True)

print(f"{'Rank':<4} {'Request':<5} {'Title':<45} {'RICE':<6} {'Reach':<3} {'Imp':<3} {'Conf':<4} {'Effort':<6}")
print("-" * 80)

for rank, item in enumerate(rice_scores, 1):
    print(f"{rank:<4} {item['req_id']:<5} {item['title'][:42]:<45} {item['rice']:<6.1f} "
          f"{item['reach']:<3} {item['impact']:<3.1f} {item['confidence']:<4.0%} {item['effort']:<6}")

# 6. SEQUENCING ANALYSIS: Q1/Q2 Capacity
print("\n6. ROADMAP SEQUENCING (Capacity: ~10 person-weeks/quarter)")
print("-" * 80)

q1_capacity = 10
q2_capacity = 10
total_capacity = q1_capacity + q2_capacity

# Recommended sequence
print("RECOMMENDED SEQUENCE:")
print("\nQ1 (10 weeks):")
print("  1. R01 (Shared deploy/auth SDK) - 6 weeks - Unblocks all tools, high confidence")
print("  2. R02 (EchoVoice multi-lang) - 4 weeks - Proven winner, high ROI")
print("     → Total: 10 weeks")

print("\nQ2 (10 weeks):")
print("  1. R03 (BugHound GA) - 5 weeks - Beta tool with top-tier retention + demand")
print("  2. R04 (Storefront discovery) - 5 weeks - Platform friction, unlocks reach for new tools")
print("     → Total: 10 weeks")

print("\nDEPRIORITIZED (Track but don't build):")
print("  - R07 (Custom Twin Hearth lore) - Only reaches 1 studio, 8 weeks effort")
print("  - R06 (ShaderSmith) - Unvalidated, 8 weeks, only 50% confidence")
print("  - R09 (CutsceneDirector) - Expensive, unproven, 10 weeks")
print("\nDEFERRED to Q3+:")
print("  - R05 (ArcaneArt reliability) - 7 weeks, only 60% confidence (risk/reward bad)")
print("  - R08 (Analytics dashboard) - 4 weeks, low impact (0.5)")

# 7. FINANCIAL SUMMARY
print("\n7. FINANCIAL SUMMARY")
print("-" * 80)

total_installs = sum(t['installs'] for t in tools.values())
total_active = sum(t['active_30d'] for t in tools.values())
total_infra = sum(t['infra_cost'] for t in tools.values())
total_support = sum(t['support_tickets'] * 50 for t in tools.values())

print(f"Total Installs: {total_installs}")
print(f"Total Active Studios (30d): {total_active}")
print(f"Overall Activation Rate: {(total_active/total_installs*100):.1f}%")
print(f"Total Monthly Infra Cost: ${total_infra:,}")
print(f"Total Monthly Support Cost (est): ${total_support:,}")
print(f"TOTAL MONTHLY COST: ${total_infra + total_support:,}")

if sunset_candidates:
    print(f"\nAfter Sunsetting {len(sunset_candidates)} tools:")
    new_infra = total_infra - sum(c['cost'] for c in sunset_candidates)
    print(f"  Remaining Monthly Cost: ${new_infra:,}")
    print(f"  Remaining Active Studios: {total_active - sum(c['active'] for c in sunset_candidates)}")

print("\n" + "=" * 80)

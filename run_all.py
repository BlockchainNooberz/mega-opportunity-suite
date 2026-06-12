"""
Mega Opportunity Suite — Run All Analyzers
Author: Andrew Elston | github.com/BlockchainNooberz
"""
import subprocess, sys, os

analyzers = [
    ("blackrock-opportunity-analyzer", "blackrock_analyzer.py"),
    ("palantir-opportunity-analyzer", "palantir_analyzer.py"),
    ("paypal-fintech-analyzer", "paypal_analyzer.py"),
    ("wef-global-opportunity-analyzer", "wef_analyzer.py"),
    ("who-global-health-analyzer", "who_analyzer.py"),
    ("us-government-opportunity-analyzer", "us_gov_analyzer.py"),
    ("airbnb-opportunity-analyzer", "airbnb_analyzer.py"),
    ("real-estate-tokenization", "tokenization_analyzer.py"),
]

print("=" * 65)
print("MEGA OPPORTUNITY SUITE — FULL ANALYSIS RUN")
print("=" * 65)

for folder, script in analyzers:
    path = os.path.join("..", folder, script)
    if os.path.exists(path):
        print(f"\n>>> Running {script}...")
        subprocess.run([sys.executable, path])
    else:
        print(f"\n⚠️  Not found: {path} — clone the repo first")

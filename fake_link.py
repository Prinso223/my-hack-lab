link = input("Paste link to check: ")

suspicious = ["free", "giveaway", "win", "urgent", "verify", "login", "bit.ly", "tinyurl", "gift", "claim"]

score = 0
for word in suspicious:
    if word in link.lower():
        print(f"⚠️ Found suspicious word: {word}")
        score += 1

if "https://" not in link:
    print("⚠️ No https - Not secure!")
    score += 1

if score == 0:
    print("✅ Looks CLEAN")
elif score <= 2:
    print("🟡 MEDIUM RISK - Be careful")
else:
    print("🔴 HIGH RISK - Don't click!")

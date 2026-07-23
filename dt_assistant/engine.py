import js

# Complete production-grade store database map node
STORE_MAP = {
    "hbc": ["shampoo", "conditioner", "body wash", "toothpaste", "oral care", "deodorant", "soap", "lotion", "medicine", "eyewear", "makeup", "bandages"],
    "chemical": ["bleach", "sprays", "dish soap", "sponges", "trash bags", "laundry detergent", "wipes", "brooms", "mops", "foil", "tissues"],
    "grocery": ["canned goods", "candy", "peg bag chocolate", "snacks", "drinks", "chips", "cookies", "juice", "soda", "bread", "cereal", "condiments"],
    "party": ["balloons", "gift bags", "plates", "streamers", "cards", "ribbon", "tablecloths", "bows", "catering", "invitations"],
    "variety": ["kitchenware", "textiles", "home decor", "books", "apparel", "stationery", "craft supplies", "hardware", "tools", "automotive"],
    "seasonal": ["toys", "lawn and garden", "floral", "electronics", "batteries", "halloween", "christmas", "easter", "summer toys", "back to school"],
    "pet_supplies": ["dog food", "cat food", "pet treats", "pet toys", "leashes", "bowls"]
}

def process_runtime_input(mode: str, entry: str) -> str:
    """Consolidated orchestration core mapping inputs safely to logic blocks."""
    clean_entry = entry.strip().lower()
    if not clean_entry:
        return "❌ Input cannot be blank. Please enter active operational metrics."
        
    # Module 1: Aisle Finder Map Lookups
    if mode == "1":
        for sector, items in STORE_MAP.items():
            if clean_entry in sector or any(item in clean_entry or clean_entry in item for item in items):
                return f"✅ CATEGORY MATCH:\nSector: {sector.upper()}\nItems: {', '.join(items)}"
        return f"⚠️ '{entry}' not indexed. Match general sector markings on perimeter panels."
        
    # Module 2: Compute Till ID Offset Matrix
    elif mode == "2":
        try:
            parts = [p.strip() for p in clean_entry.split(",") if p.strip()]
            if len(parts) != 2: raise ValueError
            prox, patt = int(parts[0]), int(parts[1])
            return f"🎯 TILL IDENTIFIER MATCH:\nAssign Till ID String: {(prox * 10) + patt}\n\nRule: Maintain active POS login state."
        except ValueError:
            return "❌ Format Error.\nEnter parameters exactly as: Proximity,Pattern\nExample: 1,3"
            
    # Module 3: Monitor Cash Drops ($400 Drop Alarm)
    elif mode == "3":
        try:
            parts = [int(p.strip()) for p in clean_entry.split(",") if p.strip()]
            if len(parts) != 4: raise ValueError
            drawer_total = (parts[0]*1) + (parts[1]*5) + (parts[2]*10) + (parts[3]*20)
            if drawer_total >= 400.00:
                return f"🚨 DROP ALARM: ${drawer_total:.2f}\nAction: Pull ${drawer_total - 75.00:.2f} right now.\nLeave safe balance of $75.00 in drawer."
            return f"✅ COMPLIANT: Total ${drawer_total:.2f}.\nDrawer variance holds ${400.00 - drawer_total:.2f} of headroom."
        except ValueError:
            return "❌ Format Error.\nEnter bill item breakdowns: 1s,5s,10s,20s\nExample: 20,10,5,8"
            
    # Module 4: Audit Line Voids (3% Loss Prevention Filter)
    elif mode == "4":
        try:
            parts = [int(p.strip()) for p in clean_entry.split(",") if p.strip()]
            if len(parts) != 2: raise ValueError
            voids, cc = parts[0], parts[1]
            if cc <= 0: return "❌ Safeguard: Transactions must be 1 or higher to compute ratio."
            rate = (voids / cc) * 100.0
            status = "🚨 EXCEEDS 3% POLICY!" if rate >= 3.0 else "✅ COMPLIANT TRANSACTION RATIO"
            return f"📊 VOID METRIC AUDIT:\nRatio: {rate:.2f}%\nStatus: {status}"
        except ValueError:
            return "❌ Format Error.\nEnter values exactly as: Voids,Transactions\nExample: 5,160"
            
    # Module 5: Check Daily Sales Pace Against $3M Target
    elif mode == "5":
        try:
            sales = float(clean_entry)
            target = 3000000.00 / 365.0
            diff = sales - target
            perf = f"🎉 Ahead of baseline by +${diff:.2f}" if diff >= 0 else f"📉 Lagging baseline by -${abs(diff):.2f}"
            return f"📈 REVENUE MATRIX (Store #6228):\nTarget Daily Pace: ${target:.2f}\nActual Revenue: ${sales:.2f}\nPerformance: {perf}"
        except ValueError:
            return "❌ Format Error. Enter raw numeric sales value without currency tags (Example: 8450.25)"
            
    return "Operational baseline active. Select dashboard component options."

# Bind our unified engine routing hook directly to the browser view framework
current_mode = "MENU"
def ui_gateway_input(user_entry):
    global current_mode
    if current_mode == "MENU":
        js.document.getElementById("terminal").innerText = "Please select an operational module button from the upper menu grid panel."
        return
    output = process_runtime_input(current_mode, user_entry)
    js.document.getElementById("terminal").innerText = str(output)
    current_mode = "MENU"

js.window.pipeInputToPython = ui_gateway_input

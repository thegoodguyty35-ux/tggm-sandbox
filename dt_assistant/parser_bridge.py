import json
import js
import calculations
import auditor

try:
    with open("map.json", "r") as f:
        STORE_MAP = json.load(f)
except Exception:
    STORE_MAP = {}

def process_runtime_input(mode: str, entry: str) -> str:
    """Routes and thoroughly sanitizes browser input entries against runtime edge cases."""
    clean_entry = entry.strip().lower()
    if not clean_entry:
        return "❌ Input cannot be blank. Please enter active operational metrics."
        
    if mode == "1":  # Aisle Map / Go-Back Finder (Handles case, plurals, and partial keywords)
        for sector, items in STORE_MAP.items():
            if clean_entry in sector or any(item in clean_entry or clean_entry in item for item in items):
                return f"✅ CATEGORY MATCH:\nSector: {sector.upper()}\nItems: {', '.join(items)}"
        return f"⚠️ '{entry}' not indexed. Match general sector markings on perimeter layout panels."
        
    elif mode == "2":  # Compute Register Till ID
        try:
            parts = [p.strip() for p in clean_entry.split(",") if p.strip()]
            if len(parts) != 2: raise ValueError
            return calculations.get_till_id(int(parts[0]), int(parts[1]))
        except ValueError:
            return "❌ Format Error.\nEnter parameters exactly as: Proximity,Pattern\nExample: 1,3"
            
    elif mode == "3":  # Monitor Till Pickups (Safely unpacks bill array parameters)
        try:
            parts = [p.strip() for p in clean_entry.split(",") if p.strip()]
            if len(parts) != 4: raise ValueError
            return auditor.monitor_cash_drop(int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3]))
        except ValueError:
            return "❌ Format Error.\nEnter exact bill item breakdowns: 1s,5s,10s,20s\nExample: 20,10,5,8"
            
    elif mode == "4":  # Audit Line Voids (Guards against division-by-zero errors)
        try:
            parts = [p.strip() for p in clean_entry.split(",") if p.strip()]
            if len(parts) != 2: raise ValueError
            voids, cc = int(parts[0]), int(parts[1])
            if cc <= 0: return "❌ System Safeguard: Transaction count must be 1 or higher to compute ratio."
            return auditor.audit_line_voids(voids, cc)
        except ValueError:
            return "❌ Format Error.\nEnter values exactly as: Voids,Transactions\nExample: 5,160"
            
    elif mode == "5":  # Check Daily Sales Pace
        try:
            return calculations.evaluate_sales_pace(float(clean_entry))
        except ValueError:
            return "❌ Format Error. Enter raw numeric sales value without currency tags (Example: 8450.25)"
            
    return "Operational tracking baseline initialized. Select menu feature matrix button panels."

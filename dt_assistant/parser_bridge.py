import json
import js
import calculations
import auditor

# Load local store map into script memory
try:
    with open("map.json", "r") as f:
        STORE_MAP = json.load(f)
except Exception:
    STORE_MAP = {}

def process_runtime_input(mode: str, entry: str) -> str:
    """Routes active browser terminal selections to specialized logic scripts."""
    clean_entry = entry.strip().lower()
    
    if mode == "1":  # Aisle Map / Go-Back Finder
        for sector, items in STORE_MAP.items():
            if clean_entry == sector or any(item in clean_entry for item in items):
                return f"✅ CATEGORY MATCH:\nSector: {sector.upper()}\nItems: {', '.join(items)}"
        return f"⚠️ '{entry}' not indexed in current store planogram layout mappings."
        
    elif mode == "2":  # Compute Register Till ID
        try:
            prox, patt = map(int, clean_entry.split(","))
            return calculations.get_till_id(prox, patt)
        except ValueError:
            return "❌ Format Error. Enter data as: Proximity,Pattern (Example: 1,3)"
            
    elif mode == "3":  # Monitor Till Pickups ($400 Cap)
        try:
            vals = list(map(int, clean_entry.split(",")))
            return auditor.monitor_cash_drop(vals[0], vals[1], vals[2], vals[3])
        except Exception:
            return "❌ Format Error. Enter breakdown: 1s,5s,10s,20s (Example: 20,10,5,8)"
            
    elif mode == "4":  # Audit Line Voids (3% Limit)
        try:
            voids, cc = map(int, clean_entry.split(","))
            return auditor.audit_line_voids(voids, cc)
        except ValueError:
            return "❌ Format Error. Enter values: Voids,Transactions (Example: 5,160)"
            
    elif mode == "5":  # Check Daily Sales Pace ($3M Goal)
        try:
            return calculations.evaluate_sales_pace(float(clean_entry))
        except ValueError:
            return "❌ Format Error. Enter raw numeric sales value (Example: 8450.25)"
            
    return "Please select an operational module button from the upper menu grid panel."

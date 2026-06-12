import os
import sys

# CONFIGURATION
# We look for the Massive 5MB Index you just created
INDEX_FILE = "tggm_universal_index.txt"

def build_war_room():
    print("="*70)
    print("       TGGM TOROIDAL HUB // WAR ROOM ARCHITECT")
    print("       STATUS: SCANNING 5MB FORENSIC INDEX...")
    print("="*70)

    # 1. VERIFY THE BRAIN EXISTS
    if not os.path.exists(INDEX_FILE):
        print(f"[ERROR] Could not find {INDEX_FILE}.")
        print("DID YOU RUN 'universal_deep_dive.py' AND UPLOAD THE RESULT?")
        return

    # 2. DEFINE THE TARGETS (The Enemy List)
    
    # TRACK A: THE AMAZON CONFLICT (Civil/Labor)
    amazon_targets = [
        "Jasmine", "Drew", "Bathroom", "Candace", "Safety", "Meth", 
        "SOP", "Generation 9", "ACRD", "Harassment", "Line Loader", 
        "Preservation of Evidence", "Write up", "Coaching", "TUS2"
    ]
    
    # TRACK B: THE LEGAL WARFARE (Criminal/Defense)
    legal_targets = [
        "Zarzycki", "Jeremy", "Plea", "Probation", "Martin Grant", 
        "Grand Jury", "Norton", "Restrictions", "PO", "PTSD", 
        "Defense", "Thomas Macewicz", "Schnittker"
    ]

    # 3. EXECUTE THE DEEP SCAN
    amazon_conflict = []
    legal_defense = []
    count = 0
    
    try:
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            # We read line by line to handle the massive file size safely
            for line in f:
                line_clean = line.strip()
                line_lower = line_clean.lower()
                
                # Filter out short/empty lines
                if len(line_clean) < 50: continue

                # CHECK FOR AMAZON MATCHES
                if any(t.lower() in line_lower for t in amazon_targets):
                    # Format it to look like a confidential log
                    formatted = f">> [EVIDENCE LOG]: {line_clean[:300]}..." 
                    amazon_conflict.append(formatted)
                    count += 1

                # CHECK FOR LEGAL MATCHES
                elif any(t.lower() in line_lower for t in legal_targets):
                    formatted = f">> [COURT DOC]: {line_clean[:300]}..."
                    legal_defense.append(formatted)
                    count += 1
                
    except Exception as e:
        print(f"[CRITICAL ERROR] Reading Index: {e}")
        return

    # 4. GENERATE THE REPORT (The Artifact)
    
    # --- REPORT SECTION A ---
    print(f"\n\n--- TRACK A: AMAZON OPS CONFLICT ({len(amazon_conflict)} Records) ---")
    print("OBJECTIVE: Establish Wreckless Indifference & Harassment")
    print("-" * 70)
    if len(amazon_conflict) == 0:
        print("[!] No records found. Check spelling in 'tggm_universal_index.txt'")
    else:
        for i, item in enumerate(amazon_conflict[:20]): # Show top 20 matches
            print(f"{i+1}. {item}")
    print(f"... and {len(amazon_conflict)-20} more records in database.")


    # --- REPORT SECTION B ---
    print(f"\n\n--- TRACK B: ZARZYCKI LEGAL DEFENSE ({len(legal_defense)} Records) ---")
    print("OBJECTIVE: Timeline of Plea Deal & Coercion")
    print("-" * 70)
    if len(legal_defense) == 0:
        print("[!] No records found. Check spelling in 'tggm_universal_index.txt'")
    else:
        for i, item in enumerate(legal_defense[:20]):
            print(f"{i+1}. {item}")
    print(f"... and {len(legal_defense)-20} more records in database.")

    # 5. FINAL STATUS
    print("\n" + "="*70)
    print(f"[SUCCESS] WAR ROOM NODE CONSTRUCTED.")
    print(f"[METRICS] {count} TOTAL ENTITIES LINKED.")
    print(f"[ACTION] THIS REPORT IS READY FOR YOUR DEFENSE ATTORNEY.")
    print("="*70)

if __name__ == "__main__":
    build_war_room()

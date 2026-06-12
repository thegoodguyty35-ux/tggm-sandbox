import os

# CONFIGURATION
INDEX_FILE = "tggm_universal_index.txt"
OUTPUT_BLUEPRINT = "tggm_visual_blueprint.txt"

def mine_vision():
    print("="*70)
    print("       TGGM VISUAL ARCHITECT // DEEP VISION MINING")
    print("       STATUS: HUNTING FOR STRUCTURAL & PHYSICS DNA...")
    print("="*70)

    if not os.path.exists(INDEX_FILE):
        print(f"[ERROR] Could not find {INDEX_FILE}.")
        return

    # THE "VISION DNA" (Directly from your Search Grid)
    visual_triggers = [
        # FROM SECTION 13: TOROIDAL DATA HUB
        "Toroidal structure", "Inside the structure", "TGGM Hub", 
        "Interactable", "Data sovereignty", "Lotus of life", 
        "Fractal", "Mandlebrot", "Brain neural network nodes", 
        "Holographic brain", "Hub", "traverse", "synapses", "build everyones website",
        "populate automatically for them",
        
        # FROM SECTION 14: GAME ENGINE PHYSICS
        "Unreal Engine", "UE5", "Physics Engine", "Halo", 
        "Gravity", "Self-building", "Simulation", "Rendering", 
        "Graphics", "UX", "GTA 5", "my own game engine", "need for game engine",
        "big o notation",

        # FROM SECTION 1 & 2: GEOMETRY & METAPHYSICS
        "Arcminutes", "Ley lines", "Fractal analysis", 
        "Electromagnetic", "Plasma", "Receiver transmitter", 
        "Pineal gland", "Energetic consciousness diagram", "Consciousness diagram", "flower of life overlay",
        
        # AESTHETIC KEYWORDS
        "Neon", "Bloom", "Glow", "Mesh", "Wireframe", "what is my style",
        "based on everything you know about me"
    ]

    design_specs = []
    count = 0

    try:
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line_clean = line.strip()
                if len(line_clean) < 40: continue

                # If the line contains a visual keyword, capture it
                if any(trigger.lower() in line_clean.lower() for trigger in visual_triggers):
                    # Format for readability
                    formatted = f">> [VISION SPEC]: {line_clean[:300]}"
                    design_specs.append(formatted)
                    count += 1
                
    except Exception as e:
        print(f"[ERROR] {e}")
        return

    # PRIORITIZE THE BEST SPECS
    # We put lines with "Structure" or "Engine" at the top
    sorted_specs = sorted(design_specs, key=lambda x: "structure" in x.lower() or "engine" in x.lower(), reverse=True)

    # WRITE THE BLUEPRINT FILE
    with open(OUTPUT_BLUEPRINT, "w", encoding="utf-8") as f:
        f.write("=== TGGM HOLOGRAPHIC ARCHITECTURE BLUEPRINT ===\n")
        f.write("DO NOT HALLUCINATE. USE THESE EXACT SPECS TO WRITE THE THREE.JS CODE.\n\n")
        for spec in sorted_specs:
            f.write(f"{spec}\n")

    # TERMINAL REPORT
    print(f"\n--- HOLOGRAPHIC BLUEPRINT GENERATED ({count} Specs) ---")
    print(f"[SUCCESS] Saved to file: {OUTPUT_BLUEPRINT}")
    print(f"[ACTION] Upload '{OUTPUT_BLUEPRINT}' to AnythingLLM now.")
    print("="*70)

if __name__ == "__main__":
    mine_vision()
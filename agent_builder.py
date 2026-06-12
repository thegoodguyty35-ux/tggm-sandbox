import json
import os
import random

# CONFIGURATION
DISCOVERIES_FILE = "tggm_discoveries.json"
OUTPUT_HTML = "tggm_sandbox/index.html"

def get_css():
    return """
    <style>
        :root { --neon: #00f3ff; --pink: #ff0055; --gold: #ffd700; --dark: #050508; --panel: rgba(5, 5, 10, 0.65); --text: #e0e0e0; }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { background: #000; color: var(--text); font-family: 'Consolas', monospace; overflow: hidden; margin: 0; }
        
        /* UI OVERLAY */
        .ui-layer { position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; padding: 20px; display: grid; grid-template-columns: 350px 1fr 350px; gap: 20px; z-index: 2; }
        
        /* CANVAS IS BACKGROUND */
        #hologram-container { position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; background: radial-gradient(circle at center, #0a0a0a 0%, #000 100%); }
        
        /* PANELS */
        .panel { pointer-events: auto; background: var(--panel); border: 1px solid rgba(0, 243, 255, 0.1); padding: 20px; border-radius: 4px; backdrop-filter: blur(5px); overflow-y: auto; height: 90vh; margin-top: 20px; transition: 0.3s; }
        .panel:hover { border-color: rgba(0, 243, 255, 0.5); box-shadow: 0 0 20px rgba(0, 243, 255, 0.1); }
        .panel h2 { color: var(--neon); font-size: 0.9em; text-transform: uppercase; letter-spacing: 2px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 10px; margin-bottom: 15px; }

        /* CARDS */
        .card { background: rgba(0,0,0,0.7); border-left: 2px solid #333; padding: 12px; margin-bottom: 8px; font-size: 0.8em; transition: 0.2s; cursor: crosshair; position: relative; overflow: hidden; }
        .card::before { content: ''; position: absolute; top: 0; left: 0; width: 2px; height: 100%; background: var(--neon); opacity: 0; transition: 0.3s; }
        .card:hover::before { opacity: 1; }
        .card:hover { transform: translateX(5px); background: rgba(0, 243, 255, 0.1); }
        .tag { display: inline-block; background: #222; color: #888; padding: 2px 6px; font-size: 0.7em; margin-bottom: 5px; border-radius: 2px; }

        /* HUD ELEMENTS */
        .header { grid-column: 1 / -1; display: flex; justify-content: space-between; align-items: center; pointer-events: auto; z-index: 10; padding-bottom: 10px; border-bottom: 1px solid rgba(255,255,255,0.1); }
        .controls-hint { position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); color: #666; font-size: 0.8em; text-align: center; pointer-events: none; z-index: 10; }
        
        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-thumb { background: #333; }
        ::-webkit-scrollbar-thumb:hover { background: var(--neon); }
    </style>
    """

def get_3d_engine_script():
    return """
    <!-- NATIVE THREE.JS (SAFE MODE - NO BLACK SCREEN) -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    
    <script>
    // --- 1. THE "UNREAL" SETUP ---
    const container = document.getElementById('hologram-container');
    const scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x000000, 0.0015); // The Void

    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 2000);
    camera.position.z = 40; // Start OUTSIDE

    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    container.appendChild(renderer.domElement);

    // --- 2. TEXTURE GENERATION (Native Glow) ---
    // Creates a "Lens Flare" particle texture purely with code to avoid CORS blocks
    const getGlowTexture = () => {
        const c = document.createElement('canvas');
        c.width = 64; c.height = 64;
        const ctx = c.getContext('2d');
        const g = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
        g.addColorStop(0, 'rgba(255, 255, 255, 1)');
        g.addColorStop(0.2, 'rgba(0, 243, 255, 0.8)');
        g.addColorStop(0.5, 'rgba(0, 0, 64, 0.2)');
        g.addColorStop(1, 'rgba(0, 0, 0, 0)');
        ctx.fillStyle = g;
        ctx.fillRect(0, 0, 64, 64);
        return new THREE.CanvasTexture(c);
    };
    const glowTex = getGlowTexture();

    // --- 3. IMPLEMENTING: "THE TOROIDAL DATA HUB" ---
    const hubGroup = new THREE.Group();
    scene.add(hubGroup);

    // A. The Main Neural Web (Wireframe)
    const torGeo = new THREE.TorusKnotGeometry(12, 3.5, 150, 24);
    const torMat = new THREE.MeshBasicMaterial({ 
        color: 0x0033aa, 
        wireframe: true, 
        transparent: true, 
        opacity: 0.05,
        blending: THREE.AdditiveBlending
    });
    const mainWeb = new THREE.Mesh(torGeo, torMat);
    hubGroup.add(mainWeb);

    // B. The Neural Nodes (Fractal Particles)
    const pGeo = new THREE.BufferGeometry();
    const pCount = 3000;
    const pPos = new Float32Array(pCount * 3);
    
    for(let i=0; i<pCount*3; i+=3) {
        // Toroidal Math to place particles INSIDE the tube
        const u = Math.random() * Math.PI * 2;
        const v = Math.random() * Math.PI * 2;
        const tubeR = 3.5 + (Math.random() - 0.5) * 2; 
        const mainR = 12;
        
        pPos[i] = (mainR + tubeR * Math.cos(v)) * Math.cos(u);
        pPos[i+1] = (mainR + tubeR * Math.cos(v)) * Math.sin(u);
        pPos[i+2] = tubeR * Math.sin(v);
    }
    pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
    const pMat = new THREE.PointsMaterial({
        color: 0x00f3ff,
        size: 0.3,
        map: glowTex, // The Glow Trick
        transparent: true,
        opacity: 0.8,
        blending: THREE.AdditiveBlending,
        depthWrite: false
    });
    const neuralCloud = new THREE.Points(pGeo, pMat);
    hubGroup.add(neuralCloud);

    // --- 4. IMPLEMENTING: "THE LOTUS OF LIFE" (Core) ---
    // Replaces simple sphere with Sacred Geometry (Icosahedron + Dodecahedron)
    const lotusGroup = new THREE.Group();
    scene.add(lotusGroup);

    // Layer 1: The Seed
    const seedGeo = new THREE.IcosahedronGeometry(1.5, 1);
    const seedMat = new THREE.MeshBasicMaterial({ color: 0xff0055, wireframe: true, transparent:true, opacity:0.8 });
    const seed = new THREE.Mesh(seedGeo, seedMat);
    lotusGroup.add(seed);

    // Layer 2: The Petals
    const petalGeo = new THREE.DodecahedronGeometry(2.5, 0);
    const petalMat = new THREE.MeshBasicMaterial({ color: 0xff00aa, wireframe: true, transparent:true, opacity:0.3 });
    const petals = new THREE.Mesh(petalGeo, petalMat);
    lotusGroup.add(petals);

    // Layer 3: The Aura
    const auraGeo = new THREE.SphereGeometry(3.5, 32, 32);
    const auraMat = new THREE.MeshBasicMaterial({ color: 0xffd700, wireframe: true, transparent:true, opacity:0.05 });
    const aura = new THREE.Mesh(auraGeo, auraMat);
    lotusGroup.add(aura);


    // --- 5. IMPLEMENTING: "INSIDE THE STRUCTURE" (Fly-Through) ---
    let mouseX = 0;
    let mouseY = 0;
    let targetZ = 40; 

    document.addEventListener('mousemove', (e) => {
        mouseX = (e.clientX - window.innerWidth / 2) * 0.0005;
        mouseY = (e.clientY - window.innerHeight / 2) * 0.0005;
    });

    document.addEventListener('wheel', (e) => {
        // Scroll Up = Zoom IN (Decrease Z)
        targetZ += e.deltaY * 0.02;
        if(targetZ < 5) targetZ = 5; // Don't crash into core
        if(targetZ > 100) targetZ = 100;
    });

    // --- 6. ANIMATION LOOP ---
    const clock = new THREE.Clock();

    function animate() {
        requestAnimationFrame(animate);
        const t = clock.getElapsedTime();

        // Rotate Hub
        hubGroup.rotation.y += 0.002;
        hubGroup.rotation.x = Math.sin(t * 0.2) * 0.1; 

        // Animate Lotus (Counter-Rotation = Living)
        seed.rotation.y -= 0.01;
        seed.rotation.z += 0.01;
        petals.rotation.y += 0.005;
        petals.rotation.x += 0.005;
        aura.rotation.z -= 0.002;

        // Pulse (Heartbeat)
        const pulse = 1 + Math.sin(t * 2) * 0.05;
        lotusGroup.scale.set(pulse, pulse, pulse);

        // Fly-Through Camera Logic
        camera.position.z += (targetZ - camera.position.z) * 0.05;
        
        // Mouse Parallax
        camera.position.x += (mouseX * 10 - camera.position.x) * 0.05;
        camera.position.y += (-mouseY * 10 - camera.position.y) * 0.05;
        camera.lookAt(scene.position);

        renderer.render(scene, camera);
    }

    window.addEventListener('resize', () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });

    animate();
    </script>
    """

class TGGMBuilder:
    def __init__(self):
        self.data = {}
    
    def load_data(self):
        if os.path.exists(DISCOVERIES_FILE):
            with open(DISCOVERIES_FILE, "r", encoding="utf-8") as f:
                self.data = json.load(f)
                return True
        return False

    def compile_dashboard(self):
        return self.build_dashboard()

    def build_dashboard(self):
        if not self.load_data(): return

        strategies = self.data.get("strategies", [])
        ops = self.data.get("operational_procedures", [])

        html = f"""<!DOCTYPE html>
        <html>
        <head>
            <title>TGGM SOVEREIGN ARCHITECT</title>
            {get_css()}
        </head>
        <body>
            <div id="hologram-container"></div>
            
            <div class="ui-layer">
                <div class="header">
                    <div>
                        <h1 style="font-weight:normal; letter-spacing:4px; margin:0; font-size:1.5em; text-shadow: 0 0 10px #00f3ff;">TGGM <span style="color:var(--neon)">// ARCHITECT</span></h1>
                        <div style="font-size:0.7em; color:#666; margin-top:5px;">VISUAL: FRACTAL TORUS + LOTUS CORE</div>
                    </div>
                    <div style="text-align:right;">
                        <div style="font-size:0.8em; color:var(--pink);">SYSTEM: ONLINE</div>
                        <div style="font-size:0.7em; color:#888;">VISION MINER: ACTIVE</div>
                    </div>
                </div>

                <div class="panel">
                    <h2>Strategic DNA ({len(strategies)})</h2>
        """
        
        for item in strategies[:30]:
            html += f'<div class="card"><span class="tag">STRATEGY</span><br>{item[:120]}...</div>'

        html += """
                </div>
                
                <!-- CENTER VOID -->
                <div></div>

                <div class="panel">
                    <h2 style="color:var(--pink);">War Room / Ops</h2>
        """

        for item in ops[:25]:
             html += f'<div class="card" style="border-left-color:var(--pink);"><span class="tag" style="color:var(--pink);">DEFENSE</span><br>{item[:120]}...</div>'

        html += f"""
                </div>
            </div>
            
            <div class="controls-hint">
                SCROLL MOUSE WHEEL TO FLY INSIDE THE STRUCTURE
            </div>

            {get_3d_engine_script()}
        </body>
        </html>
        """

        if not os.path.exists("tggm_sandbox"): os.makedirs("tggm_sandbox")
        with open(OUTPUT_HTML, "w", encoding="utf-8") as f: f.write(html)
        print(f"[BUILDER] PHASE 5 DASHBOARD COMPILED: {OUTPUT_HTML}")

if __name__ == "__main__":
    builder = TGGMBuilder()
    builder.compile_dashboard()

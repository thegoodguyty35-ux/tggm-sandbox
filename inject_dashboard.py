import os
import re

# Define the absolute path to your active index.html file
html_file_path = r'C:\Users\clark\chat_parser\tggm_sandbox\index.html'

# Define the structured data targets to inject into your dashboard panels
dashboard_data = [
    ("Total Indexed Files", "1,251 Data Nodes [Verified Offline]"),
    ("Notion Rows Synced", "1,520 Records [Master Ledger Live]"),
    ("Memory Capping Gate", "700KB Hard Allocation Ceiling"),
    ("Operational Parts", "28 Core Blueprint Modules Loaded"),
    ("System Core State", "Active Multi-Agent Sandbox Factory"),
    ("Overhead Capital", "$0.00 Fiat Running Costs [Bootstrapped]")
]

def update_dashboard_natively():
    print("--- LIVE WEB DATA INJECTION CHANNEL INITIALIZED ---")
    
    if not os.path.exists(html_file_path):
        print(f"❌ ERROR: Cannot locate target website layout file at: {html_file_path}")
        return

    # Read the raw webpage styling strings from your drive
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Locate and rebuild the entire data dashboard section block using raw regex substitutions
    new_dashboard_block = '<h2>Data Dashboard</h2>\n        <div class="dashboard">\n'
    
    for idx, (title, value) in enumerate(dashboard_data):
        new_dashboard_block += f'            <div class="dashboard-item">\n'
        new_dashboard_block += f'                <h3>{title}</h3>\n'
        new_dashboard_block += f'                <p>{value}</p>\n'
        new_dashboard_block += f'            </div>\n'
        
    new_dashboard_block += '        </div>'

    # Match the old template grid area block and overwrite it cleanly
    pattern = r'<h2>Data Dashboard</h2>\s*<div class="dashboard">.*?</div>\s*</div>'
    modified_content = re.sub(pattern, new_dashboard_block + '\n    </div>', html_content, flags=re.DOTALL)

    # Save the updated layout code right back into your index.html canvas
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

    print("🚀 [SANDBOX ENGINE SUCCESS] -> Your web dashboard metrics have been updated natively!")
    print(f"   Modified file target: {html_file_path}")

if __name__ == "__main__":
    update_dashboard_natively()

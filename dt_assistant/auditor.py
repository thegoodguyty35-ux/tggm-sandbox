def audit_line_voids(void_count: int, transaction_count: int) -> str:
    """Audits cashier line void ratios against corporate compliance targets."""
    if transaction_count <= 0:
        return "❌ Error: Customer transaction count must be greater than zero."
        
    void_rate = (void_count / transaction_count) * 100.0
    status = "🚨 EXCEEDS 3% POLICY LIMIT!" if void_rate >= 3.0 else "✅ COMPLIANT TRANSACTION RATIO"
    
    return f"📊 VOID METRIC AUDIT:\nRatio: {void_rate:.2f}%\nStatus: {status}\n\nAction: If excessive, instruct cashier to request a manager Post-Void instead."

def monitor_cash_drop(ones: int, fives: int, tens: int, twenties: int) -> str:
    """Monitors terminal cash drawer levels against the corporate cap."""
    drawer_total = (ones * 1) + (fives * 5) + (tens * 10) + (twenties * 20)
    
    if drawer_total >= 400.00:
        pull_amount = drawer_total - 75.00
        return f"🚨 DROP ALARM: ${drawer_total:.2f}\nAction: Pull ${pull_amount:.2f} right now.\nLeave a base balance of exactly $75.00 in the drawer."
    
    headroom = 400.00 - drawer_total
    return f"✅ COMPLIANT: Total ${drawer_total:.2f}.\nDrawer variance holds ${headroom:.2f} of safety headroom before next drop requirement."

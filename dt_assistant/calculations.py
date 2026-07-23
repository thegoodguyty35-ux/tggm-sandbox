def get_till_id(proximity: int, pattern: int) -> str:
    """Computes register assignment strings from local inputs."""
    till_string = str((proximity * 10) + pattern)
    return f"🎯 TILL IDENTIFIER MATCH:\nAssign Till ID String: {till_string}\n\nRule: Keep cashier active until shift expiration to maintain continuous POS flow."

def balance_vault(vault_cash: float, drawer_count: int) -> str:
    """Verifies cash assets against standard corporate bank profiles."""
    expected_vault = 900.00
    expected_drawer_base = 75.00
    total_drawer_cash = drawer_count * expected_drawer_base
    aggregate_liquidity = vault_cash + total_drawer_cash
    
    status = "✅ LIQUIDITY OK" if aggregate_liquidity == 1200.00 else "⚠️ VARIANCE DETECTED"
    return f"🏦 VAULT SYSTEM LOG:\nVault Base: ${vault_cash:.2f} / ${expected_vault:.2f}\nDrawers ({drawer_count}): ${total_drawer_cash:.2f}\nAggregate Cash: ${aggregate_liquidity:.2f}\nStatus: {status}"

def evaluate_sales_pace(current_sales: float) -> str:
    """Evaluates daily revenue performance relative to the $3M annual goal."""
    target_daily_pace = 3000000.00 / 365.0
    variance = current_sales - target_daily_pace
    
    if variance >= 0:
        performance = f"🎉 Ahead of baseline target by +${variance:.2f}"
    else:
        performance = f"📉 Lagging baseline target by -${abs(variance):.2f}"
        
    return f"📈 REVENUE MATRIX (Store #6228):\nTarget Daily Pace: ${target_daily_pace:.2f}\nActual Revenue: ${current_sales:.2f}\nPerformance: {performance}"

# 📌 Bangladesh Income Tax Calculator (AY 2025-26)
# Full Streamlit App with Explanation Panel

import streamlit as st

# ==============================
# Helper function: calculate tax
# ==============================
def calc_tax(income, category="male"):
    thresholds = {
        "male": 350000,
        "female_or_senior": 425000,
        "disabled_or_third_gender": 500000,
        "freedom_fighter": 525000
    }
    nil_threshold = thresholds.get(category, 350000)

    slabs = [
        (nil_threshold, 0.0),
        (100000, 0.05),
        (400000, 0.10),
        (500000, 0.15),
        (500000, 0.20),
        (2000000, 0.25),
    ]

    remaining = income
    tax = 0
    for slab_amount, rate in slabs:
        if remaining <= 0:
            break
        portion = min(remaining, slab_amount)
        tax += portion * rate
        remaining -= portion

    if remaining > 0:  # above 38.5 lakh
        tax += remaining * 0.30

    return tax


# ==============================
# Layout: Two Columns
# ==============================
left, right = st.columns([3, 4])  # left wider than right

# ------------------------------
# Left side: Explanation
# ------------------------------
with left:
    st.title("📘 Tax Rules & Formulas")
    st.markdown("""
    Welcome to the **Bangladesh Income Tax Calculator (AY 2025-26)**.  
    Here’s how the calculation works:

    ### 🧮 Step 1: Gross Income
    Add up all salary components:
    - Basic salary  
    - House rent allowance  
    - Medical allowance  
    - Festival bonus  
    - Overtime / other allowances  
    - Employer’s provident fund contribution  

    ### 🛡️ Step 2: Exemptions
    - **House rent** → Exempt up to 50% of basic or BDT 300,000 (whichever is lower)  
    - **Medical allowance** → Exempt up to BDT 120,000 or actual, whichever is lower  
    - **Provident Fund (PF)** → Employee + employer contribution exempt (capped at 25% of basic)  

    ### 📊 Step 3: Taxable Income
    **Taxable = Gross – Exemptions**

    ### 📈 Step 4: Apply Slabs (AY 2025-26, General Male)
    - 0 – 350,000 → 0%  
    - Next 100,000 → 5%  
    - Next 400,000 → 10%  
    - Next 500,000 → 15%  
    - Next 500,000 → 20%  
    - Next 2,000,000 → 25%  
    - Above 3,850,000 → 30%  

    *(Nil-tax threshold is higher for women, senior citizens, disabled persons, freedom fighters).*

    ### 🎁 Step 5: Rebates
    - DPS, PF contributions, approved donations → rebate = **15% of eligible amount**,  
      capped at **25% of taxable income**.  

    ### ✅ Step 6: Final Payable
    **Net Tax – TDS (already deducted by employer)**  
    """)

# ------------------------------
# Right side: Calculator
# ------------------------------
with right:
    st.title("💰 Bangladesh Income Tax Calculator")

    st.header("Income Details")
    basic = st.number_input("Basic Salary", min_value=0, value=1200000, step=1000)
    house_rent = st.number_input("House Rent Allowance", min_value=0, value=500000, step=1000)
    medical = st.number_input("Medical Allowance", min_value=0, value=48000, step=1000)
    festival = st.number_input("Festival Bonus", min_value=0, value=200000, step=1000)
    overtime = st.number_input("Overtime / Extra Allowance", min_value=0, value=100000, step=1000)
    other = st.number_input("Other Allowances", min_value=0, value=50000, step=1000)
    employer_pf = st.number_input("Employer PF Contribution", min_value=0, value=100000, step=1000)
    employee_pf = st.number_input("Employee PF Contribution", min_value=0, value=100000, step=1000)

    st.header("Savings / Investments")
    dps = st.number_input("DPS / Savings", min_value=0, value=60000, step=1000)
    donation = st.number_input("Donation (approved fund)", min_value=0, value=0, step=1000)

    st.header("Taxpayer Info")
    category = st.selectbox("Taxpayer Category", 
                            ["male", "female_or_senior", "disabled_or_third_gender", "freedom_fighter"])
    tds = st.number_input("Tax Deducted at Source (TDS)", min_value=0, value=0, step=1000)

    if st.button("🔎 Calculate Tax"):
        # Step 1: Gross income
        gross_income = basic + house_rent + medical + festival + overtime + other + employer_pf

        # Step 2: Exemptions
        house_exempt = min(basic * 0.5, 300000)
        medical_exempt = min(medical, 120000)
        pf_total = employee_pf + employer_pf
        pf_cap = basic * 0.25
        pf_exempt = min(pf_total, pf_cap)

        total_exempt = house_exempt + medical_exempt + pf_exempt

        # Step 3: Taxable Income
        taxable_income = max(gross_income - total_exempt, 0)

        # Step 4: Slab tax
        gross_tax = calc_tax(taxable_income, category)

        # Step 5: Rebate
        eligible_investment = dps + pf_total + donation
        investment_cap = taxable_income * 0.25
        eligible_investment = min(eligible_investment, investment_cap)
        rebate = eligible_investment * 0.15

        # Step 6: Final payable
        net_tax = gross_tax - rebate
        final_payable = net_tax - tds

        # ------------------------------
        # Output
        # ------------------------------
        st.subheader("📊 Results")
        st.write(f"**Gross Income**: {gross_income:,.0f} BDT")
        st.write(f"**Total Exemptions**: {total_exempt:,.0f} BDT")
        st.write(f"**Taxable Income**: {taxable_income:,.0f} BDT")
        st.write(f"**Gross Tax (before rebate)**: {gross_tax:,.0f} BDT")
        st.write(f"**Rebate (DPS, PF, Donation)**: {rebate:,.0f} BDT")
        st.write(f"**Net Tax Liability**: {net_tax:,.0f} BDT")
        st.write(f"**TDS Already Deducted**: {tds:,.0f} BDT")

        if final_payable > 0:
            st.error(f"### Final Payable: {final_payable:,.0f} BDT")
        elif final_payable < 0:
            st.success(f"### Refund Due: {-final_payable:,.0f} BDT")
        else:
            st.info("### No additional tax payable or refund — all settled ✅")

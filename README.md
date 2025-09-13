# 🇧🇩 Bangladesh Income Tax Calculator (AY 2025-26)

A simple **Streamlit web app** for calculating personal income tax in **Bangladesh** based on the **Finance Act 2024** (Assessment Year 2025–26, Income Year 2024–25).  

The app provides:  
- 📘 **Left panel** → Explanation of tax rules, formulas, and calculation steps.  
- 💰 **Right panel** → Interactive calculator with inputs for salary, allowances, savings, and taxpayer category.  
- ✅ Automatic handling of **exemptions, slab rates, rebates, and TDS**.  
- 🔎 Results showing **Gross Income, Exemptions, Taxable Income, Gross Tax, Rebate, Net Tax, and Final Payable/Refund**.  

---

## 🚀 Features
- Progressive tax slabs for AY 2025-26.  
- Handles different taxpayer categories:
  - 👨 Male (general)  
  - 👩 Female / Senior Citizen (65+)  
  - ♿ Disabled person / Third Gender  
  - 🎖️ Freedom Fighter (gazetted)  
- Exemptions for:
  - House rent allowance (up to 50% of basic or 300,000 BDT)  
  - Medical allowance (up to 120,000 BDT)  
  - Recognised Provident Fund contributions (capped at 25% of basic)  
- Rebates for DPS, PF contributions, and approved donations (15% of eligible investment, capped at 25% of taxable income).  
- Adjustment for **TDS already deducted by employer**.  
- User-friendly interface with safe input validation.  

---

## 📊 Tax Slabs (General Male, AY 2025-26)
- 0 – 350,000 → **0%**  
- Next 100,000 → **5%**  
- Next 400,000 → **10%**  
- Next 500,000 → **15%**  
- Next 500,000 → **20%**  
- Next 2,000,000 → **25%**  
- Above 3,850,000 → **30%**  

*(Nil-tax threshold is higher for women, senior citizens, disabled persons, and freedom fighters.)*

---

## 🛠️ Installation & Usage

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/bd-tax-calculator.git
cd bd-tax-calculator
````

### 2️⃣ Install dependencies

Make sure you have Python 3.8+ installed. Then run:

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit app

```bash
streamlit run bd_tax_app.py
```

### 4️⃣ Open in browser

The app will open automatically at:

```
http://localhost:8501
```

---

## 📂 Project Structure

```
bd-tax-calculator/
│
├── bd_tax_app.py       # Main Streamlit app
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 📦 Requirements

* streamlit
* pandas (optional, if you add slab breakdown tables)

Install via:

```bash
pip install streamlit pandas
```

---

## 📷 Screenshot

*(Add a screenshot of your app here — e.g., two-column layout with explanation + calculator.)*

---

## 🤝 Contributing

Pull requests are welcome! If you’d like to improve the UI, add features (like slab-by-slab breakdown), or extend support for future years, feel free to fork and contribute.

---

## 📜 License

MIT License © 2025 Your Name

---

### ✨ Credits

Developed as an educational and practical tool for **Bangladeshi taxpayers** to understand and calculate their personal income tax obligations.

---

Would you like me to also generate the **`requirements.txt` file content** so you can include it in your repo?
```
**

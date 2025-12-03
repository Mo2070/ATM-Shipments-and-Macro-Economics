import streamlit as st

# -----------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------
st.set_page_config(
    page_title="ATM Shipments & Macroeconomic Forecast | 2022–2030",
    layout="wide",
    page_icon="💳",
    initial_sidebar_state="collapsed",
)

# -----------------------------------------------------------
# GLOBAL STYLING (CSS)
# -----------------------------------------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Global reset */
* {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
}

/* App background */
.stApp {
    background: radial-gradient(circle at top left, #eef2ff 0, #f8fafc 35%, #f1f5f9 100%);
}

/* Hide Streamlit default chrome */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* NAV BAR */
.nav-bar {
    background: linear-gradient(135deg, #020617 0%, #0f172a 50%, #1d4ed8 100%);
    padding: 1.1rem 3rem;
    margin: -5rem -6rem 2.5rem -6rem;
    box-shadow: 0 10px 30px rgba(15, 23, 42, 0.45);
    position: sticky;
    top: 0;
    z-index: 1000;
}

.nav-content {
    max-width: 1320px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.nav-logo {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.nav-logo-icon {
    width: 40px;
    height: 40px;
    border-radius: 12px;
    background: radial-gradient(circle at 20% 20%, #e0f2fe 0, #1d4ed8 40%, #0f172a 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    color: #eff6ff;
    box-shadow: 0 10px 25px rgba(15, 23, 42, 0.5);
}

.nav-logo-text {
    color: #e5e7eb;
    font-size: 1.05rem;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}

.nav-subtitle {
    color: #9ca3af;
    font-size: 0.75rem;
}

.nav-links {
    display: flex;
    gap: 1.5rem;
    align-items: center;
}

.nav-link {
    color: #e5e7eb;
    text-decoration: none;
    font-size: 0.9rem;
    font-weight: 500;
    position: relative;
    padding-bottom: 0.2rem;
}

.nav-link::after {
    content: "";
    position: absolute;
    left: 0;
    bottom: 0;
    width: 0%;
    height: 2px;
    border-radius: 999px;
    background: linear-gradient(90deg, #38bdf8, #22c55e);
    transition: width 0.2s ease;
}

.nav-link:hover::after {
    width: 100%;
}

/* HERO SECTION */
.hero-section {
    background: rgba(15, 23, 42, 0.96);
    border-radius: 24px;
    padding: 2.75rem 3rem;
    margin-bottom: 2rem;
    box-shadow: 0 24px 60px rgba(15, 23, 42, 0.7);
    border: 1px solid rgba(148, 163, 184, 0.45);
    color: #e5e7eb;
}

.hero-grid {
    display: grid;
    grid-template-columns: 2.1fr 1.1fr;
    gap: 2rem;
    align-items: stretch;
}

.hero-title {
    font-size: 2.1rem;
    font-weight: 700;
    letter-spacing: -0.03em;
    margin-bottom: 0.75rem;
}

.hero-kicker {
    text-transform: uppercase;
    letter-spacing: 0.18em;
    color: #818cf8;
    font-size: 0.8rem;
    font-weight: 600;
    margin-bottom: 0.75rem;
}

.hero-description {
    font-size: 1.02rem;
    color: #cbd5f5;
    line-height: 1.7;
    max-width: 780px;
}

.hero-meta {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1.1rem;
    margin-top: 1.6rem;
}

.hero-meta-item {
    padding: 0.9rem 1rem;
    border-radius: 16px;
    background: radial-gradient(circle at top left, rgba(59,130,246,0.25), rgba(15,23,42,0.9));
    border: 1px solid rgba(148,163,184,0.55);
}

.hero-meta-label {
    font-size: 0.7rem;
    color: #9ca3af;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    margin-bottom: 0.35rem;
}

.hero-meta-value {
    font-size: 0.95rem;
    font-weight: 600;
    color: #e5e7eb;
}

.hero-side-card {
    border-radius: 20px;
    padding: 1.5rem 1.4rem;
    background: radial-gradient(circle at top, rgba(56,189,248,0.32), rgba(15,23,42,0.98));
    border: 1px solid rgba(148,163,184,0.45);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.hero-side-heading {
    font-size: 0.9rem;
    color: #e0f2fe;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.18em;
    margin-bottom: 0.5rem;
}

.hero-side-body {
    font-size: 0.9rem;
    color: #e5e7eb;
    line-height: 1.7;
}

.hero-pill {
    margin-top: 1.2rem;
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.45rem 0.9rem;
    border-radius: 999px;
    background: rgba(15,23,42,0.8);
    border: 1px solid rgba(148,163,184,0.7);
    font-size: 0.8rem;
    color: #bfdbfe;
}

/* GENERIC CARD SECTIONS */
.card-section {
    background: rgba(255, 255, 255, 0.97);
    border-radius: 18px;
    padding: 1.9rem 2.1rem;
    margin-bottom: 1.4rem;
    box-shadow: 0 14px 35px rgba(15, 23, 42, 0.18);
    border: 1px solid #e2e8f0;
}

.section-header {
    display: flex;
    align-items: center;
    gap: 0.85rem;
    padding-bottom: 0.8rem;
    border-bottom: 2px solid #f1f5f9;
    margin-bottom: 1.25rem;
}

.section-number {
    width: 32px;
    height: 32px;
    border-radius: 11px;
    background: linear-gradient(140deg, #3b82f6 0%, #22c55e 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #f9fafb;
    font-weight: 700;
    font-size: 0.95rem;
}

.section-title {
    font-size: 1.28rem;
    font-weight: 700;
    color: #0f172a;
    letter-spacing: -0.01em;
    margin: 0;
}

.section-content {
    color: #475569;
    font-size: 0.96rem;
    line-height: 1.75;
}

.section-content p {
    margin-bottom: 0.9rem;
}

.section-content ul {
    margin: 0.5rem 0 0.8rem 0;
    padding-left: 1.5rem;
}

.section-content li {
    margin-bottom: 0.4rem;
}

.section-content strong {
    color: #0f172a;
    font-weight: 600;
}

/* Formula box */
.formula-box {
    background: linear-gradient(135deg, #f9fafb 0%, #e5e7eb 100%);
    border-radius: 12px;
    padding: 1.2rem 1.4rem;
    border: 1px solid #d4d4d8;
    margin: 1.1rem 0 1.4rem 0;
}

.formula-text {
    font-family: 'Courier New', monospace;
    font-size: 0.96rem;
    color: #111827;
    font-weight: 600;
}

/* Highlight callouts */
.highlight {
    border-radius: 10px;
    padding: 0.95rem 1.05rem;
    margin: 0.9rem 0;
    font-size: 0.93rem;
}

.info-green {
    background: #ecfdf3;
    border-left: 4px solid #22c55e;
    color: #14532d;
}

.info-red {
    background: #fef2f2;
    border-left: 4px solid #ef4444;
    color: #7f1d1d;
}

.info-amber {
    background: #fffbeb;
    border-left: 4px solid #f59e0b;
    color: #78350f;
}

/* Image styling */
.section-content img {
    border-radius: 14px;
    margin: 1.3rem 0 0.2rem 0;
    box-shadow: 0 18px 40px rgba(15,23,42,0.2);
    border: 1px solid #e2e8f0;
}

/* Footer */
.custom-footer {
    text-align: center;
    padding: 2.2rem 1rem 1.5rem 1rem;
    margin-top: 3rem;
    color: #6b7280;
    font-size: 0.86rem;
    border-top: 1px solid #e5e7eb;
}

.footer-links {
    display: flex;
    justify-content: center;
    gap: 1.8rem;
    margin-top: 0.7rem;
}

.footer-link {
    color: #2563eb;
    text-decoration: none;
    font-weight: 500;
    font-size: 0.86rem;
}

.footer-link:hover {
    color: #1d4ed8;
    text-decoration: underline;
}

/* Responsive tweaks */
@media (max-width: 900px) {
    .nav-bar {
        padding: 0.9rem 1.3rem;
        margin: -4rem -1rem 1.7rem -1rem;
    }
    .nav-links {
        display: none;
    }
    .hero-section {
        padding: 2rem 1.7rem;
    }
    .hero-grid {
        grid-template-columns: 1fr;
    }
    .card-section {
        padding: 1.6rem 1.4rem;
    }
}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------------
# NAVBAR
# -----------------------------------------------------------
st.markdown(
    """
<div class="nav-bar">
  <div class="nav-content">
    <div class="nav-logo">
      <div class="nav-logo-icon">💳</div>
      <div>
        <div class="nav-logo-text">Global ATM Insights</div>
        <div class="nav-subtitle">Macroeconomic Evidence 2022–2030</div>
      </div>
    </div>
    <div class="nav-links">
      <a class="nav-link" href="#">Overview</a>
      <a class="nav-link" href="#">Data &amp; Method</a>
      <a class="nav-link" href="#">Econometric Results</a>
      <a class="nav-link" href="#">Forecast 2025–2030</a>
      <a class="nav-link" href="#">Implications</a>
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------------
# HERO SECTION
# -----------------------------------------------------------
st.markdown(
    """
<div class="hero-section">
  <div class="hero-grid">
    <div>
      <div class="hero-kicker">Thesis Dashboard</div>
      <h1 class="hero-title">How Macroeconomics Shape Global ATM Shipments</h1>
      <p class="hero-description">
        This single-page report summarises an econometric study of ATM shipments between 2022 and 2030.
        Using Datos shipment forecasts matched with macroeconomic data by country and region, we estimate
        how debt, savings, GDP growth, and gross capital formation jointly explain the evolution of the
        ATM market and generate region-level forecasts through 2030.
      </p>
      <div class="hero-meta">
        <div class="hero-meta-item">
          <div class="hero-meta-label">Analysis Window</div>
          <div class="hero-meta-value">Observed 2022–2024 | Forecast 2025–2030</div>
        </div>
        <div class="hero-meta-item">
          <div class="hero-meta-label">Econometric Model</div>
          <div class="hero-meta-value">Pooled OLS – Multiple Linear Regression</div>
        </div>
        <div class="hero-meta-item">
          <div class="hero-meta-label">Geographical Scope</div>
          <div class="hero-meta-value">7 Datos Regions · 60+ Countries</div>
        </div>
        <div class="hero-meta-item">
          <div class="hero-meta-label">Sample Size</div>
          <div class="hero-meta-value">696 Country–Year Observations</div>
        </div>
      </div>
    </div>
    <div class="hero-side-card">
      <div>
        <div class="hero-side-heading">Research Question</div>
        <div class="hero-side-body">
          <strong>To what extent can macroeconomic conditions explain ATM shipment dynamics,</strong>
          and how do model-based forecasts compare to Datos projections for 2025–2030?
        </div>
      </div>
      <div class="hero-pill">
        ●  Debt &amp; capital formation emerge as the most powerful drivers of ATM demand.
      </div>
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------------
# SECTION 1 – INTRODUCTION
# -----------------------------------------------------------
st.markdown(
    """
<div class="card-section">
  <div class="section-header">
    <div class="section-number">1</div>
    <h2 class="section-title">Introduction</h2>
  </div>
  <div class="section-content">
    <p>
      Despite the rise of mobile banking and instant payments, Automated Teller Machines (ATMs) remain
      a critical part of the retail banking infrastructure. In many regions ATMs act as a gateway to
      the formal financial system and continue to support cash-intensive sectors such as tourism,
      small retail, and informal employment.
    </p>
    <p>
      Yet, the trajectory of the ATM market is far from uniform. Mature markets such as North America
      and Western Europe appear to be reaching saturation or even contraction, whereas emerging regions
      like the Middle East &amp; Africa (MEA) and Central &amp; Eastern Europe (CEE) still show robust
      expansion. Understanding <strong>which macroeconomic conditions drive these differences</strong>
      is essential for manufacturers, banks, and regulators who must plan capacity, investments, and
      financial inclusion strategies.
    </p>
    <p>
      This study links Datos ATM shipment data with macroeconomic indicators to identify which
      variables are most strongly associated with ATM demand and to evaluate the plausibility of
      forward-looking shipment forecasts.
    </p>
    <div class="highlight info-amber">
      <strong>Core idea:</strong> treat ATM shipments as an economic infrastructure variable and
      explain it using a small but interpretable set of macro drivers rather than a black-box model.
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------------
# SECTION 2 – DATA & METHODOLOGY
# -----------------------------------------------------------
st.markdown(
    """
<div class="card-section">
  <div class="section-header">
    <div class="section-number">2</div>
    <h2 class="section-title">Data &amp; Methodology</h2>
  </div>
  <div class="section-content">
    <p>
      The analysis combines two components:
    </p>
    <ul>
      <li><strong>ATM Shipments:</strong> Datos-provided historical shipments for 2022–2024 and
      regional forecasts for 2025–2030 (units per country and year).</li>
      <li><strong>Macroeconomic Indicators:</strong> country-level panel data including
      <em>Debt as % of GDP</em>, <em>Gross Savings as % of GDP</em>, <em>Real GDP growth</em>,
      and <em>Gross Capital Formation as % of GDP</em>.</li>
    </ul>
    <p>
      Data cleaning focused on harmonising country names, aligning regions (especially mapping USA and
      Canada into the <strong>NA (North America)</strong> region), and ensuring that macro and shipment
      years matched. The regression model was deliberately estimated only on years
      <strong>2022–2024</strong>, where realised shipment data exist. The macro variables for
      <strong>2025–2030</strong> are treated as exogenous forecasts and used purely for scenario
      projection.
    </p>
    <div class="formula-box">
      <div class="formula-text">
        ATM_Shipments<sub>it</sub> = β₀ + β₁ Debt_%GDP<sub>it</sub> + β₂ Savings_%GDP<sub>it</sub>
        + β₃ GDP_real_growth<sub>it</sub> + β₄ CapitalFormation_%GDP<sub>it</sub> + ε<sub>it</sub>
      </div>
    </div>
    <p>
      where <em>i</em> indexes countries and <em>t</em> years. The model is estimated via
      Ordinary Least Squares (OLS) on the pooled panel, with robust standard errors. While more
      sophisticated panel estimators (e.g. fixed effects) are possible, OLS is chosen for two reasons:
      it keeps coefficients easily interpretable for business stakeholders, and it aligns with the
      limited time span of the dataset.
    </p>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# OLS TABLE IMAGE (CENTERED)
c1, c2, c3 = st.columns([1, 3, 1])
with c2:
    st.image(
        "Images/OLS.jpg",
        caption="Table 1 – OLS regression summary: ATM shipments vs. macroeconomic indicators",
    )

# -----------------------------------------------------------
# SECTION 3 – ECONOMETRIC RESULTS
# -----------------------------------------------------------
st.markdown(
    """
<div class="card-section">
  <div class="section-header">
    <div class="section-number">3</div>
    <h2 class="section-title">Econometric Results</h2>
  </div>
  <div class="section-content">
    <h3 style="margin-top:0.4rem;">3.1 Global Model Fit</h3>
    <p>
      The regression is estimated on <strong>696 observations</strong> (country–year pairs) with
      four explanatory variables. The key goodness-of-fit statistics are:
    </p>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# metrics row
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric("R-squared", "0.191", help="Proportion of variance in ATM shipments explained by the model.")
with m2:
    st.metric("Adj. R-squared", "0.186", help="R-squared adjusted for the number of predictors.")
with m3:
    st.metric("F-statistic", "40.79", help="Joint significance of all predictors (p < 0.001).")
with m4:
    st.metric("Observations", "696", help="Country–year data points used for estimation.")

st.markdown(
    """
<div class="card-section">
  <div class="section-content">
    <p>
      The <strong>R-squared of 0.191</strong> indicates that roughly 19% of cross-country variation
      in ATM shipments is explained by the four macroeconomic variables. For macro-level models where
      institutional, demographic and technological factors – not explicitly modelled here – play a
      substantial role, this level of fit is statistically reasonable.
    </p>
    <p>
      The <strong>F-statistic of 40.79 (p &lt; 0.001)</strong> confirms that, taken together, the
      predictors provide meaningful explanatory power relative to a model with no covariates.
    </p>
<div class="highlight info-green">
  <strong>Key significant drivers:</strong> Debt as a share of GDP and, especially, Gross Capital
  Formation are both positive and highly significant predictors of ATM shipments.
</div>
<div class="highlight info-red">
  <strong>Non-significant drivers:</strong> Savings and real GDP growth show weak or unstable
  relationships with ATM demand, suggesting they are not reliable predictors in this framework.
</div>
    <h3 style="margin-top:1.5rem;">3.2 Coefficient Interpretation</h3>
    <p>
      Interpreting the estimated coefficients in economic terms:
    </p>
    <ul>
      <li><strong>Debt (% of GDP):</strong> a 1-percentage-point increase in debt-to-GDP is associated
      with roughly <strong>+44 additional ATM shipments</strong>, holding other factors constant.
      This suggests that governments running higher debt levels often maintain or expand cash
      infrastructure, possibly to stabilise financial access during periods of fiscal stress.</li>
      <li><strong>Capital Formation (% of GDP):</strong> the strongest effect; a 1-point increase in
      gross capital formation predicts around <strong>+413 ATM shipments</strong>. This aligns with
      the intuition that ATM deployment behaves like infrastructure investment and scales with broader
      investment in roads, retail, telecoms and commercial real estate.</li>
      <li><strong>Savings (% of GDP):</strong> the point estimate is negative, but statistically
      insignificant. High national savings may reflect preferences for non-cash forms of wealth,
      but the data do not support a robust interpretation.</li>
      <li><strong>Real GDP growth:</strong> the coefficient is small and not statistically different
      from zero, indicating that short-term growth cycles are not a primary driver of ATM shipments
      once structural variables are accounted for.</li>
    </ul>
    <div class="highlight info-amber">
      <strong>Overall, the model portrays ATM shipments as a long-term infrastructure decision</strong>
      that co-moves with structural investment and fiscal policy, rather than reacting strongly to
      year-to-year economic growth or savings behaviour.
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------------
# SECTION 4 – VISUAL RELATIONSHIPS (SCATTERPLOTS)
# -----------------------------------------------------------
st.markdown(
    """
<div class="card-section">
  <div class="section-header">
    <div class="section-number">4</div>
    <h2 class="section-title">Visual Relationships between Macro Drivers and ATM Shipments</h2>
  </div>
  <div class="section-content">
    <p>
      To complement the regression output, Figure 1 plots ATM shipments against each macroeconomic
      driver and overlays the fitted linear trend. These panels highlight where relationships are
      strong, noisy or non-existent.
    </p>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns([1, 3, 1])
with c2:
    st.image(
        "Images/Scatterplot.jpg",
        caption="Figure 1 – Scatterplots with fitted lines: macro indicators vs. ATM shipments",
    )

st.markdown(
    """
<div class="card-section">
  <div class="section-content">
    <ul>
      <li>
        <strong>Debt vs. Shipments:</strong> a clear upward slope confirms a strong positive
        association. High-debt countries still deploy large numbers of ATMs, possibly to support
        fiscal transfers, welfare programmes or social stability.
      </li>
      <li>
        <strong>Capital Formation vs. Shipments:</strong> the steepest slope in the figure. Countries
        investing heavily in fixed assets and infrastructure are also those expanding their ATM
        networks most aggressively.
      </li>
      <li>
        <strong>Savings vs. Shipments:</strong> the cloud of points is diffuse and the slope only
        mildly negative, which matches the lack of statistical significance in the regression.
      </li>
      <li>
        <strong>GDP Growth vs. Shipments:</strong> the regression line is almost flat and surrounded
        by high dispersion. This visual evidence reinforces the conclusion that short-term growth
        is not a reliable predictor of ATM demand.
      </li>
    </ul>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------------
# SECTION 5 – FORECAST COMPARISON 2025–2030
# -----------------------------------------------------------
st.markdown(
    """
<div class="card-section">
  <div class="section-header">
    <div class="section-number">5</div>
    <h2 class="section-title">Model vs. Datos Forecasts (2025–2030)</h2>
  </div>
  <div class="section-content">
    <p>
      Using forecast macro values for 2025–2030 as inputs to the regression, the model generates
      implied ATM shipment paths for each region. These model-based projections are compared with
      Datos forecasts for the same period. On average across all country–years in 2025–2030 we obtain:
    </p>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

m1, m2, m3 = st.columns(3)
with m1:
    st.metric("MAE | Model − Datos", "≈ 3,015 units", help="Mean absolute error in yearly shipments.")
with m2:
    st.metric("RMSE", "≈ 5,906 units", help="Root mean squared error between model and Datos.")
with m3:
    st.metric("Correlation", "0.25", help="Linear correlation between both forecast series.")

st.markdown(
    """
<div class="card-section">
  <div class="section-content">
    <p>
      The error metrics show that the model and Datos forecasts are related but diverge meaningfully.
      The correlation of 0.25 suggests that while the two approaches move in the same direction in some
      cases, they often disagree on the magnitude of change.
    </p>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.image(
    "Images/Compare Model.jpg",
    caption="Figure 2 – Regional mean % difference between model forecasts and Datos forecasts (2025–2030)",
)

st.markdown(
    """
<div class="card-section">
  <div class="section-content">
    <p>
      Figure 2 summarises the average percentage difference for each Datos region:
    </p>
    <ul>
      <li>
        <strong>MEA:</strong> the model predicts more than <strong>+580% higher shipments</strong> than
        Datos, indicating that macro fundamentals (debt and capital formation) support a much more
        optimistic outlook than the baseline forecast.
      </li>
      <li>
        <strong>CEE:</strong> differences of roughly <strong>+365%</strong> suggest that structural
        investment in the region could sustain stronger ATM growth than currently anticipated.
      </li>
      <li>
        <strong>Western Europe:</strong> around <strong>+150%</strong> model uplift relative to Datos,
        signalling that a complete collapse of ATM demand may be less likely than often assumed.
      </li>
      <li>
        <strong>LAC:</strong> the model yields slightly <strong>lower shipments (≈ −3%)</strong> than
        Datos, implying that Latin America’s macro profile is broadly consistent with the vendor
        forecast.
      </li>
      <li>
        <strong>North America:</strong> the largest negative gap: around <strong>−64%</strong>.
        Macroeconomic conditions in the regression do not justify high additional ATM deployment in an
        already saturated and increasingly cashless environment.
      </li>
    </ul>
    <div class="highlight info-amber">
      <strong>Interpretation:</strong> where the model strongly exceeds Datos (MEA, CEE, partly WE),
      macro fundamentals may be signalling hidden upside potential. Where the model is far below Datos
      (notably NA), structural indicators suggest that shipment forecasts should be treated cautiously.
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------------
# SECTION 6 – DISCUSSION & STRATEGIC IMPLICATIONS
# -----------------------------------------------------------
st.markdown(
    """
<div class="card-section">
  <div class="section-header">
    <div class="section-number">6</div>
    <h2 class="section-title">Discussion &amp; Strategic Implications</h2>
  </div>
  <div class="section-content">
    <p>
      The combined evidence paints a coherent picture:
    </p>
    <ul>
      <li>
        ATM shipments track <strong>structural investment and fiscal conditions</strong> much more
        closely than short-term growth or savings patterns.
      </li>
      <li>
        Regions with high <strong>capital formation</strong> and still-rising <strong>debt ratios</strong>
        (MEA, CEE) appear under-served by current market forecasts and could experience stronger ATM
        demand than anticipated.
      </li>
      <li>
        Highly digitalised, mature markets such as <strong>North America</strong> may see declining or
        flat shipments even when macro aggregates are healthy, as the marginal utility of additional
        ATMs is low.
      </li>
    </ul>
    <p>
      For manufacturers and banks, this implies that:
    </p>
    <ul>
      <li>Portfolio planning should not rely solely on vendor forecasts but also incorporate
      <strong>macro-driven scenarios</strong>.</li>
      <li>Emerging markets with strong investment profiles deserve sustained commercial attention,
      even when short-term GDP growth is volatile.</li>
      <li>In saturated markets, ATM strategies should shift from expansion to <strong>modernisation,
      optimisation and service quality</strong>.</li>
    </ul>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------------
# SECTION 7 – CONCLUSION & FUTURE WORK
# -----------------------------------------------------------
st.markdown(
    """
<div class="card-section">
  <div class="section-header">
    <div class="section-number">7</div>
    <h2 class="section-title">Conclusion &amp; Future Research</h2>
  </div>
  <div class="section-content">
    <p>
      This study demonstrates that a relatively simple econometric specification can reveal
      meaningful links between ATM shipments and macroeconomic fundamentals. Debt and capital
      formation emerge as robust, interpretable predictors that help differentiate growth markets
      from mature or declining ones.
    </p>
    <p>
      The model is intentionally transparent rather than optimised for pure predictive accuracy.
      It ignores important drivers such as demographics, financial inclusion policies, cash-usage
      preferences, competition from card and mobile payments, and regulatory shocks. Incorporating
      these variables – potentially via panel data methods or machine learning – would likely raise
      explanatory power and refine regional forecasts.
    </p>
    <p>
      Nevertheless, the current framework provides a defensible, macro-anchored perspective on the
      ATM market up to 2030 and can serve as a decision-support tool for manufacturers, banks and
      policymakers.
    </p>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# -----------------------------------------------------------
# FOOTER
# -----------------------------------------------------------
st.markdown(
    """
<div class="custom-footer">
  <p>© 2025 Global ATM Insights · Thesis Project · Built with Streamlit</p>
  <div class="footer-links">
    <a class="footer-link" href="#">Methodological Appendix</a>
    <a class="footer-link" href="#">Macro Data Sources</a>
    <a class="footer-link" href="#">Contact Author</a>
    <a class="footer-link" href="#">Use &amp; Citation</a>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

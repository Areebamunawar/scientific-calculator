import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(
    page_title="Scientific Calculator - Areeba",
    page_icon="🧪",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom Styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
    }
    .stAppHeader {
        background: transparent;
    }
</style>
""", unsafe_allow_html=True)

# Title & Subtitle Header with Name "Areeba"
st.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
    <h1 style="color: #6366f1; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin-bottom: 0px; font-weight: 800; text-shadow: 0 0 15px rgba(99, 102, 241, 0.4);">
        🧪 Scientific Calculator
    </h1>
    <p style="color: #94a3b8; font-size: 16px; font-weight: 500; margin-top: 5px;">
        Designed & Developed by <span style="color: #ec4899; font-weight: 700; background: linear-gradient(90deg, #ec4899, #8b5cf6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Areeba</span>
    </p>
</div>
""", unsafe_allow_html=True)

# Interactive Scientific Calculator Component
calculator_html = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
    * {
        box-sizing: border-box;
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
        user-select: none;
    }
    body {
        background-color: transparent;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0;
        padding: 10px;
    }
    .calculator {
        background: rgba(15, 23, 42, 0.85);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 24px;
        width: 100%;
        max-width: 460px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.6), 0 0 30px rgba(99, 102, 241, 0.2);
    }
    .display-box {
        background: #090d16;
        border-radius: 16px;
        padding: 16px 20px;
        margin-bottom: 20px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        text-align: right;
        box-shadow: inset 0 2px 8px rgba(0,0,0,0.8);
    }
    .previous-expression {
        color: #64748b;
        font-size: 14px;
        min-height: 20px;
        word-wrap: break-word;
        font-family: 'Courier New', monospace;
    }
    .current-input {
        color: #f8fafc;
        font-size: 32px;
        font-weight: 700;
        min-height: 44px;
        word-wrap: break-word;
        font-family: 'Segoe UI', sans-serif;
    }
    .mode-indicator {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: bold;
        background: #334155;
        color: #38bdf8;
        float: left;
    }
    .grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 10px;
    }
    button {
        height: 52px;
        border: none;
        border-radius: 12px;
        font-size: 15px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.15s ease;
        outline: none;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    button:active {
        transform: scale(0.93);
    }
    
    .btn-num {
        background: #1e293b;
        color: #f1f5f9;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    .btn-num:hover {
        background: #334155;
    }
    
    .btn-sci {
        background: #0f172a;
        color: #38bdf8;
        border: 1px solid rgba(56, 189, 248, 0.2);
    }
    .btn-sci:hover {
        background: #1e293b;
        color: #7dd3fc;
    }
    
    .btn-op {
        background: #312e81;
        color: #a5b4fc;
    }
    .btn-op:hover {
        background: #3730a3;
    }
    
    .btn-action {
        background: #881337;
        color: #fecdd3;
    }
    .btn-action:hover {
        background: #9f1239;
    }
    
    .btn-equal {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        color: #ffffff;
        font-weight: bold;
        font-size: 18px;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
    }
    .btn-equal:hover {
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
    }

    .btn-mode {
        background: #334155;
        color: #fbbf24;
    }
</style>
</head>
<body>

<div class="calculator" id="calc">
    <div class="display-box">
        <span class="mode-indicator" id="modeIndicator">DEG</span>
        <div class="previous-expression" id="prevExp"></div>
        <div class="current-input" id="display">0</div>
    </div>
    
    <div class="grid">
        <!-- Row 1 -->
        <button class="btn-mode" id="toggleDeg">DEG</button>
        <button class="btn-sci" data-action="sin">sin</button>
        <button class="btn-sci" data-action="cos">cos</button>
        <button class="btn-sci" data-action="tan">tan</button>
        <button class="btn-action" data-action="clear">AC</button>

        <!-- Row 2 -->
        <button class="btn-sci" data-action="pi">π</button>
        <button class="btn-sci" data-action="log">log</button>
        <button class="btn-sci" data-action="ln">ln</button>
        <button class="btn-sci" data-action="(">(</button>
        <button class="btn-sci" data-action=")">)</button>

        <!-- Row 3 -->
        <button class="btn-sci" data-action="e">e</button>
        <button class="btn-sci" data-action="sqrt">√</button>
        <button class="btn-sci" data-action="square">x²</button>
        <button class="btn-sci" data-action="power">x^y</button>
        <button class="btn-action" data-action="backspace">⌫</button>

        <!-- Row 4 -->
        <button class="btn-sci" data-action="fact">n!</button>
        <button class="btn-num" data-val="7">7</button>
        <button class="btn-num" data-val="8">8</button>
        <button class="btn-num" data-val="9">9</button>
        <button class="btn-op" data-val="/">÷</button>

        <!-- Row 5 -->
        <button class="btn-sci" data-action="percent">%</button>
        <button class="btn-num" data-val="4">4</button>
        <button class="btn-num" data-val="5">5</button>
        <button class="btn-num" data-val="6">6</button>
        <button class="btn-op" data-val="*">×</button>

        <!-- Row 6 -->
        <button class="btn-sci" data-action="sign">±</button>
        <button class="btn-num" data-val="1">1</button>
        <button class="btn-num" data-val="2">2</button>
        <button class="btn-num" data-val="3">3</button>
        <button class="btn-op" data-val="-">−</button>

        <!-- Row 7 -->
        <button class="btn-num" data-val="0">0</button>
        <button class="btn-num" data-val=".">.</button>
        <button class="btn-sci" data-action="cbrt">∛</button>
        <button class="btn-equal" style="grid-column: span 2;" data-action="calculate">=</button>
    </div>
</div>

<script>
    let expr = "";
    let isDeg = true;
    const displayEl = document.getElementById("display");
    const prevExpEl = document.getElementById("prevExp");
    const modeIndicator = document.getElementById("modeIndicator");

    function updateDisplay() {
        displayEl.innerText = expr || "0";
    }

    function clearAll() {
        expr = "";
        prevExpEl.innerText = "";
        updateDisplay();
    }

    function backspace() {
        expr = expr.slice(0, -1);
        updateDisplay();
    }

    function appendVal(val) {
        expr += val;
        updateDisplay();
    }

    function toggleMode() {
        isDeg = !isDeg;
        modeIndicator.innerText = isDeg ? "DEG" : "RAD";
        document.getElementById("toggleDeg").innerText = isDeg ? "DEG" : "RAD";
    }

    function factorial(n) {
        if (n < 0) return NaN;
        if (n === 0 || n === 1) return 1;
        let res = 1;
        for (let i = 2; i <= n; i++) res *= i;
        return res;
    }

    function calculateResult() {
        if (!expr) return;
        try {
            prevExpEl.innerText = expr + " =";
            let sanitized = expr
                .replace(/×/g, '*')
                .replace(/÷/g, '/')
                .replace(/π/g, 'Math.PI')
                .replace(/\be\b/g, 'Math.E')
                .replace(/\^/g, '**');

            if (isDeg) {
                sanitized = sanitized
                    .replace(/sin\(([^)]+)\)/g, (m, p) => `Math.sin((${p}) * Math.PI / 180)`)
                    .replace(/cos\(([^)]+)\)/g, (m, p) => `Math.cos((${p}) * Math.PI / 180)`)
                    .replace(/tan\(([^)]+)\)/g, (m, p) => `Math.tan((${p}) * Math.PI / 180)`);
            } else {
                sanitized = sanitized
                    .replace(/sin\(/g, 'Math.sin(')
                    .replace(/cos\(/g, 'Math.cos(')
                    .replace(/tan\(/g, 'Math.tan(');
            }

            sanitized = sanitized
                .replace(/log\(/g, 'Math.log10(')
                .replace(/ln\(/g, 'Math.log(')
                .replace(/√\(/g, 'Math.sqrt(')
                .replace(/∛\(/g, 'Math.cbrt(');

            sanitized = sanitized.replace(/(\d+)!/g, (match, num) => factorial(parseInt(num)));

            let result = eval(sanitized);

            if (typeof result === 'number') {
                if (!isFinite(result)) {
                    expr = "Error";
                } else {
                    expr = parseFloat(result.toFixed(10)).toString();
                }
            } else {
                expr = "Error";
            }
        } catch (e) {
            expr = "Error";
        }
        updateDisplay();
    }

    // On-Screen Button Events
    document.getElementById("calc").addEventListener("click", (e) => {
        const btn = e.target.closest("button");
        if (!btn) return;

        const val = btn.getAttribute("data-val");
        const action = btn.getAttribute("data-action");

        if (val) appendVal(val);
        else if (action) {
            switch(action) {
                case "clear": clearAll(); break;
                case "backspace": backspace(); break;
                case "calculate": calculateResult(); break;
                case "sin": appendVal("sin("); break;
                case "cos": appendVal("cos("); break;
                case "tan": appendVal("tan("); break;
                case "log": appendVal("log("); break;
                case "ln": appendVal("ln("); break;
                case "pi": appendVal("π"); break;
                case "e": appendVal("e"); break;
                case "sqrt": appendVal("√("); break;
                case "cbrt": appendVal("∛("); break;
                case "square": appendVal("^2"); break;
                case "power": appendVal("^"); break;
                case "percent": appendVal("/100"); break;
                case "fact": appendVal("!"); break;
                case "sign": 
                    if (expr.startsWith("-")) expr = expr.slice(1);
                    else expr = "-" + expr;
                    updateDisplay();
                    break;
                case "(": appendVal("("); break;
                case ")": appendVal(")"); break;
            }
        }
    });

    document.getElementById("toggleDeg").addEventListener("click", toggleMode);

    // Keyboard Events Handler
    window.addEventListener("keydown", (e) => {
        const key = e.key;

        if (key >= '0' && key <= '9') appendVal(key);
        else if (key === '.') appendVal('.');
        else if (key === '+') appendVal('+');
        else if (key === '-') appendVal('-');
        else if (key === '*') appendVal('*');
        else if (key === '/') { e.preventDefault(); appendVal('/'); }
        else if (key === '(' || key === ')') appendVal(key);
        else if (key === '^') appendVal('^');
        else if (key === '!') appendVal('!');
        else if (key === '%') appendVal('/100');
        else if (key === 'Enter' || key === '=') { e.preventDefault(); calculateResult(); }
        else if (key === 'Backspace') { e.preventDefault(); backspace(); }
        else if (key === 'Escape') { e.preventDefault(); clearAll(); }
        else if (key.toLowerCase() === 's') appendVal('sin(');
        else if (key.toLowerCase() === 'c') appendVal('cos(');
        else if (key.toLowerCase() === 't') appendVal('tan(');
        else if (key.toLowerCase() === 'l') appendVal('log(');
        else if (key.toLowerCase() === 'p') appendVal('π');
        else if (key.toLowerCase() === 'e') appendVal('e');
    });
</script>
</body>
</html>
"""

components.html(calculator_html, height=690, scrolling=False)

# Keyboard Guidance Footer
st.markdown("""
<div style="text-align: center; color: #94a3b8; font-size: 13px; margin-top: 10px;">
    <b>Keyboard Support:</b> <code>0-9</code> • <code>+ - * /</code> • <code>( )</code> • <code>^</code> • <code>Enter (=)</code> • <code>Backspace</code> • <code>Esc (Clear)</code> <br>
    <i>Shortcuts:</i> <code>s</code> (sin), <code>c</code> (cos), <code>t</code> (tan), <code>l</code> (log), <code>p</code> (π), <code>e</code> (e)
</div>
""", unsafe_allow_html=True)
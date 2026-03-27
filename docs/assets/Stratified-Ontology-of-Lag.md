<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Stratified Ontology of Lag</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Courier+Prime:ital@0;1&display=swap');

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    :root {
      --bg: #f5f2ec;
      --ink: #1a1814;
      --mid: #6b6558;
      --light: #b8b0a0;
      --accent: #8b7355;
      --deep: #3d3628;
    }

    body {
      background: var(--bg);
      color: var(--ink);
      font-family: 'EB Garamond', serif;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 40px 20px;
    }

    .diagram {
      width: 680px;
      position: relative;
    }

    .title {
      font-family: 'Courier Prime', monospace;
      font-size: 11px;
      letter-spacing: 0.18em;
      color: var(--mid);
      text-transform: uppercase;
      margin-bottom: 48px;
      border-bottom: 1px solid var(--light);
      padding-bottom: 12px;
    }

    .propositions {
      margin-top: 48px;
      border-top: 1px solid var(--light);
      padding-top: 20px;
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 24px;
    }

    .prop {
      font-size: 12px;
      line-height: 1.7;
      color: var(--mid);
      font-style: italic;
    }

    .prop strong {
      font-style: normal;
      font-size: 10px;
      font-family: 'Courier Prime', monospace;
      letter-spacing: 0.12em;
      color: var(--accent);
      display: block;
      margin-bottom: 6px;
      font-weight: normal;
    }

    .positioning {
      margin-top: 40px;
      font-size: 11.5px;
      color: var(--mid);
      font-style: italic;
      line-height: 1.8;
      border-top: 1px solid var(--light);
      padding-top: 20px;
    }

    .positioning span {
      font-family: 'Courier Prime', monospace;
      font-style: normal;
      font-size: 10px;
      color: var(--accent);
      letter-spacing: 0.1em;
    }

    .closing {
      margin-top: 36px;
      font-size: 13px;
      color: var(--ink);
      line-height: 1.9;
      text-align: center;
      font-style: italic;
      letter-spacing: 0.02em;
    }

    .footer {
      margin-top: 40px;
      font-family: 'Courier Prime', monospace;
      font-size: 9px;
      color: var(--light);
      letter-spacing: 0.15em;
      text-align: right;
      border-top: 1px solid var(--light);
      padding-top: 12px;
    }

    svg {
      width: 100%;
      height: auto;
      overflow: visible;
      display: block;
    }
  </style>
</head>
<body>
  <div class="diagram">
    <div class="title">Stratified Ontology of Lag — Deep Layer and Strata</div>

    <svg viewBox="0 0 560 580" xmlns="http://www.w3.org/2000/svg">
      <!-- Deep Layer band -->
      <rect x="80" y="10" width="400" height="220" fill="rgba(139,115,85,0.04)" stroke="#8b7355" stroke-width="0.8"/>
      <text x="92" y="30" font-family="'Courier Prime', monospace" font-size="9" fill="#8b7355" letter-spacing="3">DEEP LAYER</text>

      <!-- lag -->
      <text x="280" y="80" text-anchor="middle" font-family="'EB Garamond', serif" font-size="28" fill="#1a1814" font-weight="500">lag</text>
      <text x="330" y="80" font-family="'EB Garamond', serif" font-size="12" fill="#6b6558" font-style="italic">irreversible difference</text>

      <!-- arrow down -->
      <line x1="280" y1="90" x2="280" y2="125" stroke="#b8b0a0" stroke-width="0.8"/>
      <polygon points="276,122 280,130 284,122" fill="#b8b0a0"/>

      <!-- support -->
      <text x="280" y="158" text-anchor="middle" font-family="'EB Garamond', serif" font-size="28" fill="#1a1814" font-weight="500">support</text>
      <text x="348" y="158" font-family="'EB Garamond', serif" font-size="12" fill="#6b6558" font-style="italic">local stabilization</text>

      <!-- arrow down -->
      <line x1="280" y1="168" x2="280" y2="203" stroke="#b8b0a0" stroke-width="0.8"/>
      <polygon points="276,200 280,208 284,200" fill="#b8b0a0"/>

      <!-- orientation -->
      <text x="280" y="226" text-anchor="middle" font-family="'EB Garamond', serif" font-size="24" fill="#1a1814" font-weight="500">orientation</text>
      <text x="370" y="226" font-family="'EB Garamond', serif" font-size="12" fill="#6b6558" font-style="italic">directional asymmetry</text>

      <!-- Divider -->
      <line x1="80" y1="242" x2="480" y2="242" stroke="#6b6558" stroke-width="0.5" stroke-dasharray="3,3"/>
      <rect x="218" y="234" width="124" height="16" fill="#f5f2ec"/>
      <text x="280" y="246" text-anchor="middle" font-family="'Courier Prime', monospace" font-size="9" fill="#6b6558" letter-spacing="2">— STRATA —</text>

      <!-- Strata band -->
      <rect x="80" y="250" width="400" height="300" fill="rgba(107,101,88,0.025)" stroke="#b8b0a0" stroke-width="0.8"/>

      <!-- space -->
      <text x="280" y="300" text-anchor="middle" font-family="'EB Garamond', serif" font-size="26" fill="#1a1814" font-weight="500">space</text>
      <text x="330" y="300" font-family="'EB Garamond', serif" font-size="12" fill="#6b6558" font-style="italic">stabilized configuration</text>

      <!-- arrow down -->
      <line x1="280" y1="310" x2="280" y2="343" stroke="#b8b0a0" stroke-width="0.8"/>
      <polygon points="276,340 280,348 284,340" fill="#b8b0a0"/>

      <!-- time -->
      <text x="280" y="370" text-anchor="middle" font-family="'EB Garamond', serif" font-size="26" fill="#1a1814" font-weight="500">time</text>
      <text x="320" y="370" font-family="'EB Garamond', serif" font-size="12" fill="#6b6558" font-style="italic">persistence of lag (ψ)</text>

      <!-- arrow down -->
      <line x1="280" y1="380" x2="280" y2="413" stroke="#b8b0a0" stroke-width="0.8"/>
      <polygon points="276,410 280,418 284,410" fill="#b8b0a0"/>

      <!-- phenomena -->
      <text x="280" y="440" text-anchor="middle" font-family="'EB Garamond', serif" font-size="24" fill="#1a1814" font-weight="500">phenomena</text>
      <text x="372" y="440" font-family="'EB Garamond', serif" font-size="12" fill="#6b6558" font-style="italic">local outcrops</text>

      <!-- ΔZ node -->
      <text x="430" y="476" text-anchor="middle" font-family="'EB Garamond', serif" font-size="22" fill="#3d3628" font-weight="500">ΔZ</text>
      <text x="430" y="493" text-anchor="middle" font-family="'Courier Prime', monospace" font-size="8.5" fill="#8b7355" letter-spacing="1">differential trace</text>

      <!-- phenomena → ΔZ -->
      <path d="M 330,450 Q 400,460 420,468" stroke="#b8b0a0" stroke-width="0.8" fill="none"/>
      <polygon points="416,466 424,470 419,461" fill="#b8b0a0"/>

      <!-- ΔZ → lag -->
      <path d="M 430,458 Q 520,400 520,150 Q 520,60 340,68"
            stroke="#8b7355" stroke-width="0.9" fill="none" stroke-dasharray="4,3" opacity="0.6"/>
      <polygon points="336,64 344,68 337,74" fill="#8b7355" opacity="0.6"/>

      <!-- recursion label -->
      <text x="510" y="250" font-family="'Courier Prime', monospace" font-size="9" fill="#8b7355" opacity="0.7" text-anchor="middle">↺</text>
      <text x="528" y="240" font-family="'Courier Prime', monospace" font-size="8" fill="#8b7355" opacity="0.6" text-anchor="start">recursion</text>

      <!-- Left bracket -->
      <line x1="72" y1="60" x2="72" y2="226" stroke="#b8b0a0" stroke-width="0.5"/>
      <line x1="72" y1="60" x2="78" y2="60" stroke="#b8b0a0" stroke-width="0.5"/>
      <line x1="72" y1="226" x2="78" y2="226" stroke="#b8b0a0" stroke-width="0.5"/>
      <text x="66" y="148" font-family="'Courier Prime', monospace" font-size="8" fill="#b8b0a0" text-anchor="middle" transform="rotate(-90, 66, 148)" letter-spacing="1.5">generative conditions</text>

      <line x1="72" y1="265" x2="72" y2="535" stroke="#b8b0a0" stroke-width="0.5"/>
      <line x1="72" y1="265" x2="78" y2="265" stroke="#b8b0a0" stroke-width="0.5"/>
      <line x1="72" y1="535" x2="78" y2="535" stroke="#b8b0a0" stroke-width="0.5"/>
      <text x="66" y="400" font-family="'Courier Prime', monospace" font-size="8" fill="#b8b0a0" text-anchor="middle" transform="rotate(-90, 66, 400)" letter-spacing="1.5">phenomenal stabilization</text>

      <!-- Notation -->
      <text x="92" y="545" font-family="'Courier Prime', monospace" font-size="9" fill="#b8b0a0" letter-spacing="1">↓ structural dependence (not temporal succession)</text>
      <text x="92" y="560" font-family="'Courier Prime', monospace" font-size="9" fill="#8b7355" letter-spacing="1">↺ recursive return via ΔZ</text>
    </svg>

    <div class="propositions">
      <div class="prop">
        <strong>SPACE</strong>
        not a container,<br>but a stabilized<br>configuration
      </div>
      <div class="prop">
        <strong>TIME</strong>
        does not flow;<br>irreversible difference<br>persists
      </div>
      <div class="prop">
        <strong>PHENOMENA</strong>
        not objects,<br>but outcrops of<br>ongoing generation
      </div>
    </div>

    <div class="positioning">
      <span>Phenomenology</span> — describes phenomena within strata<br>
      <span>Structuralism</span> — extracts spatial configurations<br>
      <span>Derrida</span> — temporalizes structure (trace / différance)<br><br>
      None explicitly formulates the recursive coupling between deep layer and strata.
    </div>

    <div class="closing">
      What appears as layers is not fixed.<br>
      It is the ongoing recursion of a deeper asymmetry.
    </div>

    <div class="footer">K.E. Itekki · EgQE — Echo-Genesis Qualia Engine · camp-us.net</div>
  </div>
</body>
</html>

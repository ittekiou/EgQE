<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="700" viewBox="0 0 1200 700">
  <defs>
    <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L12,6 L0,12 Z" fill="#000"/>
    </marker>
    <marker id="arrowThin" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L10,5 L0,10 Z" fill="#000"/>
    </marker>
  </defs>

  <!-- Title -->
  <text x="600" y="55" text-anchor="middle" font-family="Times New Roman, serif" font-size="28" font-weight="bold">
    Figure 1｜Circulation and Localization of Lag
  </text>

  <!-- Central system -->
  <circle cx="600" cy="330" r="170" fill="none" stroke="#000" stroke-width="3"/>
  <text x="600" y="310" text-anchor="middle" font-family="Times New Roman, serif" font-size="22" font-weight="bold">
    Relational System
  </text>
  <text x="600" y="338" text-anchor="middle" font-family="Times New Roman, serif" font-size="18">
    (non-synchronizable)
  </text>

  <!-- Inner circulation arrows (stylized loop) -->
  <path d="M520 275 C540 235, 660 235, 680 275" fill="none" stroke="#000" stroke-width="2.2" marker-end="url(#arrowThin)"/>
  <path d="M690 295 C740 315, 740 345, 690 365" fill="none" stroke="#000" stroke-width="2.2" marker-end="url(#arrowThin)"/>
  <path d="M680 385 C660 425, 540 425, 520 385" fill="none" stroke="#000" stroke-width="2.2" marker-end="url(#arrowThin)"/>
  <path d="M510 365 C460 345, 460 315, 510 295" fill="none" stroke="#000" stroke-width="2.2" marker-end="url(#arrowThin)"/>

  <!-- Left: Lag Circulation -->
  <rect x="90" y="150" width="370" height="360" fill="none" stroke="#000" stroke-width="2"/>
  <text x="275" y="185" text-anchor="middle" font-family="Times New Roman, serif" font-size="22" font-weight="bold">
    Lag Circulation
  </text>
  <text x="275" y="212" text-anchor="middle" font-family="Times New Roman, serif" font-size="18">
    Limit Cycle
  </text>
  <text x="275" y="238" text-anchor="middle" font-family="Times New Roman, serif" font-size="18">
    S ≃ O′
  </text>

  <!-- Left icon: loop -->
  <circle cx="275" cy="330" r="85" fill="none" stroke="#000" stroke-width="2.5"/>
  <path d="M230 300 C250 265, 300 265, 320 300" fill="none" stroke="#000" stroke-width="2" marker-end="url(#arrowThin)"/>
  <path d="M330 315 C360 330, 360 350, 330 365" fill="none" stroke="#000" stroke-width="2" marker-end="url(#arrowThin)"/>
  <path d="M320 380 C300 415, 250 415, 230 380" fill="none" stroke="#000" stroke-width="2" marker-end="url(#arrowThin)"/>
  <path d="M220 365 C190 350, 190 330, 220 315" fill="none" stroke="#000" stroke-width="2" marker-end="url(#arrowThin)"/>

  <text x="275" y="450" text-anchor="middle" font-family="Times New Roman, serif" font-size="16">
    Lag is continuously recovered
  </text>
  <text x="275" y="472" text-anchor="middle" font-family="Times New Roman, serif" font-size="16">
    No localization → weightless
  </text>

  <!-- Right: Lag Localization -->
  <rect x="740" y="150" width="370" height="360" fill="none" stroke="#000" stroke-width="2"/>
  <text x="925" y="185" text-anchor="middle" font-family="Times New Roman, serif" font-size="22" font-weight="bold">
    Lag Localization
  </text>
  <text x="925" y="212" text-anchor="middle" font-family="Times New Roman, serif" font-size="18">
    Unrecoverable Lag
  </text>
  <text x="925" y="238" text-anchor="middle" font-family="Times New Roman, serif" font-size="18">
    S ≪ O′
  </text>

  <!-- Right icon: sediment / constraint -->
  <path d="M860 280 L990 280 L1015 410 L835 410 Z" fill="none" stroke="#000" stroke-width="2.5"/>
  <!-- sediment dots -->
  <circle cx="900" cy="330" r="6" fill="#000"/>
  <circle cx="940" cy="345" r="6" fill="#000"/>
  <circle cx="885" cy="360" r="6" fill="#000"/>
  <circle cx="955" cy="375" r="6" fill="#000"/>
  <circle cx="910" cy="385" r="6" fill="#000"/>

  <!-- support arrow -->
  <line x1="925" y1="410" x2="925" y2="460" stroke="#000" stroke-width="2.5" marker-end="url(#arrow)"/>
  <text x="925" y="478" text-anchor="middle" font-family="Times New Roman, serif" font-size="16">
    Weight = support requirement
  </text>
  <text x="925" y="500" text-anchor="middle" font-family="Times New Roman, serif" font-size="16">
    Lag sediments as constraint
  </text>

  <!-- Projection / Inscription (bottom) -->
  <rect x="330" y="560" width="540" height="105" fill="none" stroke="#000" stroke-width="2"/>
  <text x="600" y="595" text-anchor="middle" font-family="Times New Roman, serif" font-size="22" font-weight="bold">
    Projection / Historical Inscription
  </text>
  <text x="600" y="622" text-anchor="middle" font-family="Times New Roman, serif" font-size="16">
    Fixing lag into a specific historical form
  </text>
  <text x="600" y="646" text-anchor="middle" font-family="Times New Roman, serif" font-size="16">
    (measurement / probability / uncertainty)
  </text>

  <!-- Projection lines from central to bottom -->
  <line x1="520" y1="470" x2="470" y2="560" stroke="#000" stroke-width="2" marker-end="url(#arrowThin)"/>
  <line x1="680" y1="470" x2="730" y2="560" stroke="#000" stroke-width="2" marker-end="url(#arrowThin)"/>

  <!-- Links from left/right panels to central system -->
  <line x1="460" y1="330" x2="430" y2="330" stroke="#000" stroke-width="2" marker-end="url(#arrowThin)"/>
  <line x1="740" y1="330" x2="770" y2="330" stroke="#000" stroke-width="2" marker-end="url(#arrowThin)"/>

  <!-- Small labels near links -->
  <text x="425" y="308" text-anchor="end" font-family="Times New Roman, serif" font-size="14">
    circulation
  </text>
  <text x="780" y="308" text-anchor="start" font-family="Times New Roman, serif" font-size="14">
    localization
  </text>

  <!-- Footer note -->
  <text x="600" y="690" text-anchor="middle" font-family="Times New Roman, serif" font-size="13">
    SAW｜Minimal Paper — Figure 1 (single-figure edition)
  </text>
</svg>

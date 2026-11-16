import math
import os

DIAGRAMS_DIR = os.path.join("static", "diagrams")
os.makedirs(DIAGRAMS_DIR, exist_ok=True)

def base_svg_start(w=900, h=920, title="", subtitle="", formula=""):
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="background: radial-gradient(circle at 50% 40%, #111d38 0%, #0a1124 60%, #060914 100%); font-family: system-ui, -apple-system, \'Segoe UI\', Roboto, sans-serif;">',
        '  <defs>',
        '    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fef08a"/><stop offset="100%" stop-color="#eab308"/></linearGradient>',
        '    <linearGradient id="sepalGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#4ade80"/><stop offset="70%" stop-color="#16a34a"/><stop offset="100%" stop-color="#14532d"/></linearGradient>',
        '    <linearGradient id="antherGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fef08a"/><stop offset="100%" stop-color="#ca8a04"/></linearGradient>',
        '    <linearGradient id="ovaryGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fef9c3"/><stop offset="100%" stop-color="#d97706"/></linearGradient>',
        '    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3" result="b"/><feComposite in="SourceGraphic" in2="b" operator="over"/></filter>',
        '  </defs>',
        '  <!-- Frame -->',
        f'  <rect x="15" y="15" width="{w-30}" height="{h-30}" rx="28" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>',
        f'  <rect x="25" y="25" width="{w-50}" height="{h-50}" rx="22" fill="none" stroke="rgba(253,224,71,0.15)" stroke-width="1" stroke-dasharray="6 6"/>',
        '  <!-- Header -->',
        f'  <g transform="translate({w/2}, 60)" text-anchor="middle">',
        f'    <text y="0" font-size="22" font-weight="800" fill="#fde047" letter-spacing="1.5">{title}</text>',
        f'    <text y="24" font-size="14" font-style="italic" fill="#cbd5e1">{subtitle}</text>',
        f'    <text y="45" font-size="13" font-weight="600" fill="#c084fc" font-family="monospace">Floral Formula: {formula}</text>',
        '  </g>'
    ]
    return lines

def label_leader(lx, ly, tx, ty, title, subtitle="", anchor="left"):
    res = []
    dx = 40 if anchor == "left" else -40
    res.append(f'<polyline points="{lx:.1f},{ly:.1f} {tx:.1f},{ty:.1f} {tx + dx:.1f},{ty:.1f}" fill="none" stroke="#fde047" stroke-width="1.4" stroke-dasharray="3 2" opacity="0.85"/>')
    res.append(f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="3.5" fill="#fde047"/>')
    x_text = tx + (45 if anchor == "left" else -45)
    text_anchor = "start" if anchor == "left" else "end"
    res.append(f'<text x="{x_text:.1f}" y="{ty - 4:.1f}" font-size="12" font-weight="700" fill="#ffffff" text-anchor="{text_anchor}">{title}</text>')
    if subtitle:
        res.append(f'<text x="{x_text:.1f}" y="{ty + 11:.1f}" font-size="10.5" fill="#cbd5e1" text-anchor="{text_anchor}">{subtitle}</text>')
    return "\n".join(res)

def draw_mother_axis(cx, cy, r=14, offset_y=330):
    lines = []
    may = cy - offset_y
    lines.append(f'<circle cx="{cx}" cy="{may}" r="{r}" fill="#0f172a" stroke="#fde047" stroke-width="2.5"/>')
    lines.append(f'<circle cx="{cx}" cy="{may}" r="5" fill="#fde047"/>')
    lines.append(f'<line x1="{cx - 10}" y1="{may}" x2="{cx + 10}" y2="{may}" stroke="#fde047" stroke-width="1.5"/>')
    lines.append(f'<line x1="{cx}" y1="{may - 10}" x2="{cx}" y2="{may + 10}" stroke="#fde047" stroke-width="1.5"/>')
    return "\n".join(lines)

def draw_bract(cx, cy, offset_y=345, width=72, height=32, fill="url(#sepalGrad)", stroke="#16a34a"):
    by = cy + offset_y
    half_w = width / 2
    d = f"M {cx - half_w} {by} Q {cx} {by - height/2} {cx + half_w} {by} Q {cx} {by + height/2} {cx - half_w} {by} Z"
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="1.8"/><line x1="{cx}" y1="{by - height/2}" x2="{cx}" y2="{by + height/2}" stroke="#14532d" stroke-width="1.2"/>'

def draw_summary_card(cx, cy, text_content):
    return f'''
    <g transform="translate({cx}, {cy})" text-anchor="middle">
      <rect x="-380" y="-18" width="760" height="42" rx="12" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>
      <text y="7" font-size="12" fill="#e2e8f0">{text_content}</text>
    </g>
    '''

# ==============================================================================
# 1. ROSE (Rosa indica - Rosaceae)
# ==============================================================================
def create_rose_svg():
    w, h, cx, cy = 900, 920, 450, 490
    lines = base_svg_start(w, h, "BOTANICAL FLORAL DIAGRAM: ROSE", "Rosa indica L. • Family: Rosaceae", "&#8853; &#9909; K&#8325; C&#8325; A&#8734; G&#8734;")
    
    # Gradients
    lines.append('''
    <defs>
      <linearGradient id="rosePetalGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fda4af"/><stop offset="50%" stop-color="#f43f5e"/><stop offset="100%" stop-color="#be123c"/></linearGradient>
      <linearGradient id="roseInnerPetal" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fbcfe8"/><stop offset="60%" stop-color="#ec4899"/><stop offset="100%" stop-color="#9d174d"/></linearGradient>
    </defs>
    ''')
    
    # Reference Circles
    for r in [250, 195, 140, 90, 50]:
        lines.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1" stroke-dasharray="4 4"/>')
        
    lines.append(draw_mother_axis(cx, cy, 14, 330))
    lines.append(draw_bract(cx, cy, 345, 76, 32))
    
    # Calyx: 5 Sepals, Quincuncial aestivation (2 outer, 2 inner, 1 mixed)
    sep_r = 250
    sep_angles = [-90, -18, 54, 126, 198]
    # In quincuncial, radii vary slightly for overlap
    r_offsets = [12, -8, 12, -8, 0] # sepals 0,2 outer; 1,3 inner; 4 half
    for idx, ang in enumerate(sep_angles):
        rad = math.radians(ang)
        sr = sep_r + r_offsets[idx]
        span = 64
        a1, a2 = math.radians(ang - span/2), math.radians(ang + span/2)
        x1, y1 = cx + sr * math.cos(a1), cy + sr * math.sin(a1)
        x2, y2 = cx + sr * math.cos(a2), cy + sr * math.sin(a2)
        rx, ry = cx + (sr + 16) * math.cos(rad), cy + (sr + 16) * math.sin(rad)
        ix, iy = cx + (sr - 12) * math.cos(rad), cy + (sr - 12) * math.sin(rad)
        d = f"M {x1:.1f} {y1:.1f} Q {rx:.1f} {ry:.1f} {x2:.1f} {y2:.1f} Q {ix:.1f} {iy:.1f} {x1:.1f} {y1:.1f} Z"
        lines.append(f'<path d="{d}" fill="url(#sepalGrad)" stroke="#14532d" stroke-width="2"/>')
        lines.append(f'<line x1="{rx:.1f}" y1="{ry:.1f}" x2="{ix:.1f}" y2="{iy:.1f}" stroke="#16a34a" stroke-width="1.2"/>')

    # Corolla: 5 Outer Petals, Imbricate
    pet_r = 195
    pet_angles = [-54, 18, 90, 162, 234]
    pet_offsets = [8, -8, 8, -8, 0]
    for idx, ang in enumerate(pet_angles):
        rad = math.radians(ang)
        pr = pet_r + pet_offsets[idx]
        span = 66
        a1, a2 = math.radians(ang - span/2), math.radians(ang + span/2)
        x1, y1 = cx + pr * math.cos(a1), cy + pr * math.sin(a1)
        x2, y2 = cx + pr * math.cos(a2), cy + pr * math.sin(a2)
        mx, my = cx + (pr + 15) * math.cos(rad), cy + (pr + 15) * math.sin(rad)
        ix, iy = cx + (pr - 15) * math.cos(rad), cy + (pr - 15) * math.sin(rad)
        d = f"M {x1:.1f} {y1:.1f} Q {mx:.1f} {my:.1f} {x2:.1f} {y2:.1f} Q {ix:.1f} {iy:.1f} {x1:.1f} {y1:.1f} Z"
        lines.append(f'<path d="{d}" fill="url(#rosePetalGrad)" stroke="#fda4af" stroke-width="2"/>')

    # Inner petal whorl (cultivated rose polypetalous characteristic)
    in_pet_r = 145
    for i in range(5):
        ang = pet_angles[i] + 36
        rad = math.radians(ang)
        span = 60
        a1, a2 = math.radians(ang - span/2), math.radians(ang + span/2)
        x1, y1 = cx + in_pet_r * math.cos(a1), cy + in_pet_r * math.sin(a1)
        x2, y2 = cx + in_pet_r * math.cos(a2), cy + in_pet_r * math.sin(a2)
        mx, my = cx + (in_pet_r + 12) * math.cos(rad), cy + (in_pet_r + 12) * math.sin(rad)
        ix, iy = cx + (in_pet_r - 12) * math.cos(rad), cy + (in_pet_r - 12) * math.sin(rad)
        d = f"M {x1:.1f} {y1:.1f} Q {mx:.1f} {my:.1f} {x2:.1f} {y2:.1f} Q {ix:.1f} {iy:.1f} {x1:.1f} {y1:.1f} Z"
        lines.append(f'<path d="{d}" fill="url(#roseInnerPetal)" stroke="#f472b6" stroke-width="1.8" opacity="0.95"/>')

    # Androecium: Stamens Numerous (A ∞), Polyandrous, 2 whorls of dithecous anthers
    for stamen_r, count in [(106, 16), (88, 12)]:
        for i in range(count):
            ang = i * (360 / count)
            rad = math.radians(ang)
            ax, ay = cx + stamen_r * math.cos(rad), cy + stamen_r * math.sin(rad)
            # Dithecous anther (2 lobes)
            tang = ang + 90
            trad = math.radians(tang)
            dx, dy = 3.5 * math.cos(trad), 3.5 * math.sin(trad)
            lines.append(f'<circle cx="{ax - dx:.1f}" cy="{ay - dy:.1f}" r="2.8" fill="url(#antherGrad)" stroke="#854d0e" stroke-width="0.8"/>')
            lines.append(f'<circle cx="{ax + dx:.1f}" cy="{ay + dy:.1f}" r="2.8" fill="url(#antherGrad)" stroke="#854d0e" stroke-width="0.8"/>')

    # Hypanthium rim
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="64" fill="none" stroke="#22c55e" stroke-width="2.5" opacity="0.7"/>')
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="61" fill="#090d16" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>')

    # Gynoecium: Apocarpous, Multicarpellary (G ∞) - Free carpels inside cup-shaped hypanthium
    # Center cluster of 9 individual free carpels
    carp_positions = [
        (0, 0), (20, 0), (-20, 0), (0, 20), (0, -20),
        (14, 14), (-14, 14), (14, -14), (-14, -14)
    ]
    for cdx, cdy in carp_positions:
        ox, oy = cx + cdx, cy + cdy
        lines.append(f'<circle cx="{ox}" cy="{oy}" r="7" fill="#0f172a" stroke="#fde047" stroke-width="1.4"/>')
        # Marginal single ovule
        lines.append(f'<circle cx="{ox + 2}" cy="{oy}" r="2.2" fill="url(#ovaryGrad)" stroke="#ca8a04" stroke-width="0.8"/>')

    # Callout Labels
    lines.append(label_leader(cx + 14, cy - 330, cx + 120, cy - 330, "Mother Axis", "Posterior position indicator", "left"))
    lines.append(label_leader(cx + 250, cy - 60, cx + 290, cy - 140, "Calyx: K5", "5 free sepals, quincuncial aestivation", "left"))
    lines.append(label_leader(cx + 195, cy + 60, cx + 290, cy + 30, "Corolla: C5 (Outer)", "5 free petals, imbricate aestivation", "left"))
    lines.append(label_leader(cx + 145, cy + 120, cx + 290, cy + 160, "Corolla: C(inner)", "Multiseriate polypetalous petals", "left"))
    lines.append(label_leader(cx - 106, cy - 50, cx - 290, cy - 70, "Androecium: A(∞)", "Numerous free polyandrous stamens", "right"))
    lines.append(label_leader(cx - 64, cy + 40, cx - 290, cy + 50, "Hypanthium Receptacle", "Cup-shaped hollow floral receptacle", "right"))
    lines.append(label_leader(cx - 20, cy, cx - 290, cy + 180, "Gynoecium: G(∞)", "Apocarpous: multiple free carpels", "right"))
    lines.append(label_leader(cx + 38, cy + 345, cx + 180, cy + 355, "Bract", "Anterior floral position", "left"))
    
    # Legend
    lines.append(draw_summary_card(cx, 840, '<tspan fill="#22c55e" font-weight="700">K:</tspan> 5 quincuncial &#8226; <tspan fill="#f43f5e" font-weight="700">C:</tspan> 5(&#8734;) polypetalous &#8226; <tspan fill="#fde047" font-weight="700">A:</tspan> &#8734; polyandrous dithecous &#8226; <tspan fill="#f59e0b" font-weight="700">G:</tspan> &#8734; apocarpous in hypanthium'))
    lines.append('</svg>')
    return "\n".join(lines)

# ==============================================================================
# 2. LOTUS (Nelumbo nucifera - Nelumbonaceae)
# ==============================================================================
def create_lotus_svg():
    w, h, cx, cy = 900, 920, 450, 490
    lines = base_svg_start(w, h, "BOTANICAL FLORAL DIAGRAM: LOTUS", "Nelumbo nucifera Gaertn. • Family: Nelumbonaceae", "&#8853; &#9909; K&#8322;&#8331;&#8324; C&#8734; A&#8734; G&#8734;")
    
    lines.append('''
    <defs>
      <linearGradient id="lotusPetalGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fce7f3"/><stop offset="50%" stop-color="#f472b6"/><stop offset="100%" stop-color="#db2777"/></linearGradient>
      <linearGradient id="torusGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fef08a"/><stop offset="60%" stop-color="#eab308"/><stop offset="100%" stop-color="#a16207"/></linearGradient>
    </defs>
    ''')
    
    for r in [265, 215, 165, 120, 65]:
        lines.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1" stroke-dasharray="4 4"/>')

    lines.append(draw_mother_axis(cx, cy, 14, 330))
    lines.append(draw_bract(cx, cy, 345, 80, 32))

    # Sepals (Outer whorl, 4 sepals)
    sep_r = 265
    for i in range(4):
        ang = -90 + i * 90
        rad = math.radians(ang)
        span = 72
        a1, a2 = math.radians(ang - span/2), math.radians(ang + span/2)
        x1, y1 = cx + sep_r * math.cos(a1), cy + sep_r * math.sin(a1)
        x2, y2 = cx + sep_r * math.cos(a2), cy + sep_r * math.sin(a2)
        mx, my = cx + (sep_r + 18) * math.cos(rad), cy + (sep_r + 18) * math.sin(rad)
        ix, iy = cx + (sep_r - 12) * math.cos(rad), cy + (sep_r - 12) * math.sin(rad)
        d = f"M {x1:.1f} {y1:.1f} Q {mx:.1f} {my:.1f} {x2:.1f} {y2:.1f} Q {ix:.1f} {iy:.1f} {x1:.1f} {y1:.1f} Z"
        lines.append(f'<path d="{d}" fill="url(#sepalGrad)" stroke="#14532d" stroke-width="2"/>')

    # Petals (Spiral / Multiple whorls: Outer 8, Inner 8)
    for pet_r, count, rot_offset in [(215, 8, 22.5), (165, 8, 45)]:
        for i in range(count):
            ang = i * (360 / count) + rot_offset
            rad = math.radians(ang)
            span = 44
            a1, a2 = math.radians(ang - span/2), math.radians(ang + span/2)
            x1, y1 = cx + pet_r * math.cos(a1), cy + pet_r * math.sin(a1)
            x2, y2 = cx + pet_r * math.cos(a2), cy + pet_r * math.sin(a2)
            mx, my = cx + (pet_r + 16) * math.cos(rad), cy + (pet_r + 16) * math.sin(rad)
            ix, iy = cx + (pet_r - 12) * math.cos(rad), cy + (pet_r - 12) * math.sin(rad)
            d = f"M {x1:.1f} {y1:.1f} Q {mx:.1f} {my:.1f} {x2:.1f} {y2:.1f} Q {ix:.1f} {iy:.1f} {x1:.1f} {y1:.1f} Z"
            lines.append(f'<path d="{d}" fill="url(#lotusPetalGrad)" stroke="#fbcfe8" stroke-width="1.6"/>')

    # Androecium: Numerous spirally arranged stamens with appendages
    for stamen_r, count in [(128, 22), (108, 18)]:
        for i in range(count):
            ang = i * (360 / count)
            rad = math.radians(ang)
            ax, ay = cx + stamen_r * math.cos(rad), cy + stamen_r * math.sin(rad)
            # Elongated dithecous anther with clavate appendage
            lines.append(f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="3" fill="url(#antherGrad)" stroke="#ca8a04" stroke-width="1"/>')

    # Gynoecium: Spongy obconical torus/receptacle with sunken carpels in separate pits
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="68" fill="url(#torusGrad)" stroke="#fde047" stroke-width="2.5" opacity="0.95"/>')
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="63" fill="#1e293b" stroke="#ca8a04" stroke-width="1.5"/>')

    # Sunken carpel pits in the torus
    pit_coords = [
        (0, 0),
        (22, 0), (-22, 0), (0, 22), (0, -22),
        (16, 16), (-16, 16), (16, -16), (-16, -16),
        (38, 12), (-38, 12), (38, -12), (-38, -12), (12, 38), (-12, 38), (12, -38), (-12, -38)
    ]
    for px, py in pit_coords:
        gx, gy = cx + px, cy + py
        lines.append(f'<circle cx="{gx}" cy="{gy}" r="5.5" fill="#090d16" stroke="#fde047" stroke-width="1"/>')
        lines.append(f'<circle cx="{gx}" cy="{gy}" r="2.2" fill="url(#ovaryGrad)"/>')

    # Labels
    lines.append(label_leader(cx + 14, cy - 330, cx + 120, cy - 330, "Mother Axis", "Posterior position indicator", "left"))
    lines.append(label_leader(cx + 265, cy - 40, cx + 290, cy - 120, "Calyx: K2-4", "Outer sepaloid perianth whorl", "left"))
    lines.append(label_leader(cx + 215, cy + 60, cx + 290, cy + 20, "Corolla: C(outer)", "Showy spirally arranged petals", "left"))
    lines.append(label_leader(cx + 165, cy + 130, cx + 290, cy + 150, "Corolla: C(inner)", "Multiseriate transition petals", "left"))
    lines.append(label_leader(cx - 128, cy - 40, cx - 290, cy - 60, "Androecium: A(∞)", "Numerous stamens with appendaged anthers", "right"))
    lines.append(label_leader(cx - 68, cy + 30, cx - 290, cy + 70, "Spongy Torus / Receptacle", "Broad obconical top-shaped floral axis", "right"))
    lines.append(label_leader(cx - 22, cy - 10, cx - 290, cy + 190, "Gynoecium: G(∞)", "Free carpels embedded in separate pits", "right"))
    lines.append(label_leader(cx + 40, cy + 345, cx + 180, cy + 355, "Bract", "Anterior floral position", "left"))

    lines.append(draw_summary_card(cx, 840, '<tspan fill="#22c55e" font-weight="700">K:</tspan> 2-4 sepaloid &#8226; <tspan fill="#f472b6" font-weight="700">C:</tspan> &#8734; spirally polypetalous &#8226; <tspan fill="#fde047" font-weight="700">A:</tspan> &#8734; appendaged &#8226; <tspan fill="#f59e0b" font-weight="700">G:</tspan> &#8734; apocarpous in spongy torus'))
    lines.append('</svg>')
    return "\n".join(lines)

# ==============================================================================
# 3. CLITORIA (Clitoria ternatea - Fabaceae)
# ==============================================================================
def create_clitoria_svg():
    w, h, cx, cy = 900, 920, 450, 490
    lines = base_svg_start(w, h, "BOTANICAL FLORAL DIAGRAM: CLITORIA", "Clitoria ternatea L. • Family: Fabaceae", "% &#9909; K&#8333;&#8325;&#8334; C&#8321;&#8330;&#8322;&#8330;&#8333;&#8322;&#8334; A&#8333;&#8329;&#8334;&#8330;&#8321; G&#8321;")
    
    lines.append('''
    <defs>
      <linearGradient id="vexGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#93c5fd"/><stop offset="50%" stop-color="#2563eb"/><stop offset="100%" stop-color="#1e3a8a"/></linearGradient>
      <linearGradient id="wingGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#60a5fa"/><stop offset="100%" stop-color="#1d4ed8"/></linearGradient>
      <linearGradient id="keelGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#bfdbfe"/><stop offset="100%" stop-color="#3b82f6"/></linearGradient>
    </defs>
    ''')

    for r in [260, 205, 140, 75]:
        lines.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1" stroke-dasharray="4 4"/>')

    lines.append(draw_mother_axis(cx, cy, 14, 330))
    lines.append(draw_bract(cx, cy, 345, 76, 30))
    
    # 2 Bracteoles (Lateral)
    for bx, ang in [(cx - 295, 180), (cx + 295, 0)]:
        lines.append(f'<path d="M {bx} {cy - 28} Q {bx + (15 if ang==0 else -15)} {cy} {bx} {cy + 28} Q {bx - (10 if ang==0 else -10)} {cy} {bx} {cy - 28} Z" fill="url(#sepalGrad)" stroke="#16a34a" stroke-width="1.5"/>')

    # Calyx: 5 Fused Sepals, Valvate, odd sepal anterior (bottom)
    sep_r = 260
    sep_angles = [90, 162, 234, -54, 18] # odd sepal at 90 (anterior)
    sep_ends = []
    for ang in sep_angles:
        rad = math.radians(ang)
        span = 60
        a1, a2 = math.radians(ang - span/2), math.radians(ang + span/2)
        x1, y1 = cx + sep_r * math.cos(a1), cy + sep_r * math.sin(a1)
        x2, y2 = cx + sep_r * math.cos(a2), cy + sep_r * math.sin(a2)
        sep_ends.append(((x1, y1), (x2, y2)))
        mx, my = cx + (sep_r + 16) * math.cos(rad), cy + (sep_r + 16) * math.sin(rad)
        ix, iy = cx + (sep_r - 10) * math.cos(rad), cy + (sep_r - 10) * math.sin(rad)
        d = f"M {x1:.1f} {y1:.1f} Q {mx:.1f} {my:.1f} {x2:.1f} {y2:.1f} Q {ix:.1f} {iy:.1f} {x1:.1f} {y1:.1f} Z"
        lines.append(f'<path d="{d}" fill="url(#sepalGrad)" stroke="#14532d" stroke-width="2"/>')
    # Fusion brackets
    for i in range(5):
        e1 = sep_ends[i][1]
        e2 = sep_ends[(i+1)%5][0]
        mx, my = (e1[0] + e2[0])/2, (e1[1] + e2[1])/2
        lines.append(f'<path d="M {e1[0]:.1f} {e1[1]:.1f} Q {mx*1.01:.1f} {my*1.01:.1f} {e2[0]:.1f} {e2[1]:.1f}" fill="none" stroke="#22c55e" stroke-width="2.2"/>')

    # Corolla: Papilionaceous (Vexillary Aestivation)
    # 1. Standard / Vexillum (Posterior, large, overlapping everything)
    vex_r = 210
    v_a1, v_a2 = math.radians(-155), math.radians(-25)
    vx1, vy1 = cx + vex_r * math.cos(v_a1), cy + vex_r * math.sin(v_a1)
    vx2, vy2 = cx + vex_r * math.cos(v_a2), cy + vex_r * math.sin(v_a2)
    vmx, vmy = cx, cy - vex_r - 20
    vix, viy = cx, cy - vex_r + 16
    lines.append(f'<path d="M {vx1:.1f} {vy1:.1f} Q {vmx:.1f} {vmy:.1f} {vx2:.1f} {vy2:.1f} Q {vix:.1f} {viy:.1f} {vx1:.1f} {vy1:.1f} Z" fill="url(#vexGrad)" stroke="#93c5fd" stroke-width="2.2"/>')

    # 2. Wings / Alae (2 Lateral Petals)
    for sign, ang in [(-1, 160), (1, 20)]:
        w_r = 175
        wa1, wa2 = math.radians(ang - 40), math.radians(ang + 40)
        wx1, wy1 = cx + w_r * math.cos(wa1), cy + w_r * math.sin(wa1)
        wx2, wy2 = cx + w_r * math.cos(wa2), cy + w_r * math.sin(wa2)
        wmx = cx + (w_r + 14) * math.cos(math.radians(ang))
        wmy = cy + (w_r + 14) * math.sin(math.radians(ang))
        wix = cx + (w_r - 12) * math.cos(math.radians(ang))
        wiy = cy + (w_r - 12) * math.sin(math.radians(ang))
        lines.append(f'<path d="M {wx1:.1f} {wy1:.1f} Q {wmx:.1f} {wmy:.1f} {wx2:.1f} {wy2:.1f} Q {wix:.1f} {wiy:.1f} {wx1:.1f} {wy1:.1f} Z" fill="url(#wingGrad)" stroke="#60a5fa" stroke-width="1.8"/>')

    # 3. Keel / Carina (2 Anterior Petals, fused at base)
    k_r = 140
    ka1, ka2 = math.radians(50), math.radians(130)
    kx1, ky1 = cx + k_r * math.cos(ka1), cy + k_r * math.sin(ka1)
    kx2, ky2 = cx + k_r * math.cos(ka2), cy + k_r * math.sin(ka2)
    kmx, kmy = cx, cy + k_r + 16
    kix, kiy = cx, cy + k_r - 10
    lines.append(f'<path d="M {kx1:.1f} {ky1:.1f} Q {kmx:.1f} {kmy:.1f} {kx2:.1f} {ky2:.1f} Q {kix:.1f} {kiy:.1f} {kx1:.1f} {ky1:.1f} Z" fill="url(#keelGrad)" stroke="#bfdbfe" stroke-width="1.8"/>')
    # Fused apex indication
    lines.append(f'<circle cx="{kmx}" cy="{kmy}" r="4" fill="#60a5fa"/>')

    # Androecium: Diadelphous (9) + 1
    # 9 fused stamens in a lower horseshoe sheath
    stam_r = 95
    fused_angles = [10, 30, 50, 70, 90, 110, 130, 150, 170]
    sheath_d = f"M {cx + stam_r * math.cos(math.radians(0))} {cy + stam_r * math.sin(math.radians(0))} A {stam_r} {stam_r} 0 0 1 {cx + stam_r * math.cos(math.radians(180))} {cy + stam_r * math.sin(math.radians(180))}"
    lines.append(f'<path d="{sheath_d}" fill="none" stroke="#fde047" stroke-width="3" stroke-linecap="round"/>')
    for fang in fused_angles:
        rad = math.radians(fang)
        fx, fy = cx + stam_r * math.cos(rad), cy + stam_r * math.sin(rad)
        lines.append(f'<circle cx="{fx:.1f}" cy="{fy:.1f}" r="4.2" fill="url(#antherGrad)" stroke="#854d0e" stroke-width="1"/>')
    
    # 1 Free posterior stamen at top (-90 degrees)
    free_x, free_y = cx, cy - stam_r
    lines.append(f'<circle cx="{free_x}" cy="{free_y}" r="4.8" fill="url(#antherGrad)" stroke="#fde047" stroke-width="1.5"/>')

    # Gynoecium: Monocarpellary (G1), unilocular with marginal placentation
    lines.append(f'<ellipse cx="{cx}" cy="{cy}" rx="36" ry="24" fill="#090d16" stroke="#22c55e" stroke-width="2.5"/>')
    # Row of ovules along posterior margin (ventral suture)
    for ox in [-18, -6, 6, 18]:
        lines.append(f'<circle cx="{cx + ox}" cy="{cy - 8}" r="3.2" fill="url(#ovaryGrad)" stroke="#ca8a04" stroke-width="0.8"/>')
        lines.append(f'<line x1="{cx + ox}" y1="{cy - 8}" x2="{cx + ox}" y2="{cy - 16}" stroke="#22c55e" stroke-width="1"/>')

    # Labels
    lines.append(label_leader(cx + 14, cy - 330, cx + 120, cy - 330, "Mother Axis", "Posterior position indicator", "left"))
    lines.append(label_leader(cx + 180, cy - 200, cx + 290, cy - 180, "Vexillum / Standard", "Large posterior petal (outermost)", "left"))
    lines.append(label_leader(cx + 175, cy + 50, cx + 290, cy + 20, "Wing Petals (Alae)", "2 lateral petals overlapping keel", "left"))
    lines.append(label_leader(cx + 40, cy + 155, cx + 290, cy + 160, "Keel Petals (Carina)", "2 anterior petals fused at apex", "left"))
    lines.append(label_leader(cx + 260, cy + 120, cx + 290, cy + 250, "Calyx: K(5)", "5 fused sepals, odd sepal anterior", "left"))
    lines.append(label_leader(free_x - 6, free_y, cx - 290, cy - 100, "Free Posterior Stamen", "1 isolated stamen: (+1)", "right"))
    lines.append(label_leader(cx - stam_r, cy + 40, cx - 290, cy + 20, "Fused Staminal Tube", "9 stamens united: A(9)", "right"))
    lines.append(label_leader(cx - 36, cy, cx - 290, cy + 140, "Monocarpellary Ovary: G1", "Unilocular, marginal placentation", "right"))
    lines.append(label_leader(cx - 295, cy - 10, cx - 290, cy + 240, "Bracteoles", "2 prominent lateral bracteoles", "right"))
    lines.append(label_leader(cx + 38, cy + 345, cx + 180, cy + 355, "Bract", "Anterior floral position", "left"))

    lines.append(draw_summary_card(cx, 840, '<tspan fill="#22c55e" font-weight="700">K:</tspan> (5) valvate odd-anterior &#8226; <tspan fill="#60a5fa" font-weight="700">C:</tspan> 1+2+(2) vexillary &#8226; <tspan fill="#fde047" font-weight="700">A:</tspan> (9)+1 diadelphous &#8226; <tspan fill="#f59e0b" font-weight="700">G:</tspan> 1 marginal'))
    lines.append('</svg>')
    return "\n".join(lines)

# ==============================================================================
# 4. SUNFLOWER (Helianthus annuus - Asteraceae)
# ==============================================================================
def create_sunflower_svg():
    w, h, cx, cy = 900, 920, 450, 490
    lines = base_svg_start(w, h, "BOTANICAL FLORAL DIAGRAM: SUNFLOWER", "Helianthus annuus L. • Family: Asteraceae", "Disc: &#8853; &#9909; K_pappus C&#8333;&#8325;&#8334; A&#8333;&#8325;&#8334; G&#8333;&#8322;&#8334; (Inferior)")
    
    lines.append('''
    <defs>
      <linearGradient id="sunPetalGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fef08a"/><stop offset="50%" stop-color="#eab308"/><stop offset="100%" stop-color="#ca8a04"/></linearGradient>
    </defs>
    ''')

    for r in [250, 190, 125, 60]:
        lines.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1" stroke-dasharray="4 4"/>')

    lines.append(draw_mother_axis(cx, cy, 14, 330))
    # Palea / Involucral Bract
    lines.append(draw_bract(cx, cy, 345, 90, 36, fill="#ca8a04", stroke="#eab308"))

    # Calyx: Reduced Pappus Scales (2 distinct pappus scales)
    for px, py in [(cx - 240, cy), (cx + 240, cy)]:
        lines.append(f'<path d="M {px} {cy - 30} Q {px + 10} {cy} {px} {cy + 30} Q {px - 10} {cy} {px} {cy - 30} Z" fill="#4ade80" stroke="#16a34a" stroke-width="1.8"/>')
        # Feathery bristles
        for offset in [-20, -10, 0, 10, 20]:
            lines.append(f'<line x1="{px}" y1="{cy + offset}" x2="{px + 16}" y2="{cy + offset - 4}" stroke="#86efac" stroke-width="1"/>')

    # Corolla: 5 Fused Petals, Tubular, Valvate Aestivation
    cor_r = 190
    pet_angles = [-90 + i * 72 for i in range(5)]
    pet_ends = []
    for ang in pet_angles:
        rad = math.radians(ang)
        span = 60
        a1, a2 = math.radians(ang - span/2), math.radians(ang + span/2)
        x1, y1 = cx + cor_r * math.cos(a1), cy + cor_r * math.sin(a1)
        x2, y2 = cx + cor_r * math.cos(a2), cy + cor_r * math.sin(a2)
        pet_ends.append(((x1, y1), (x2, y2)))
        mx, my = cx + (cor_r + 16) * math.cos(rad), cy + (cor_r + 16) * math.sin(rad)
        ix, iy = cx + (cor_r - 10) * math.cos(rad), cy + (cor_r - 10) * math.sin(rad)
        d = f"M {x1:.1f} {y1:.1f} Q {mx:.1f} {my:.1f} {x2:.1f} {y2:.1f} Q {ix:.1f} {iy:.1f} {x1:.1f} {y1:.1f} Z"
        lines.append(f'<path d="{d}" fill="url(#sunPetalGrad)" stroke="#fde047" stroke-width="2"/>')
    for i in range(5):
        e1, e2 = pet_ends[i][1], pet_ends[(i+1)%5][0]
        mx, my = (e1[0] + e2[0])/2, (e1[1] + e2[1])/2
        lines.append(f'<path d="M {e1[0]:.1f} {e1[1]:.1f} Q {mx*1.01:.1f} {my*1.01:.1f} {e2[0]:.1f} {e2[1]:.1f}" fill="none" stroke="#f59e0b" stroke-width="2.5"/>')

    # Androecium: 5 Stamens, Syngenesious (Anthers fused into cylindrical tube, epipetalous)
    # Cylinder ring
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="125" fill="none" stroke="#fde047" stroke-width="4"/>')
    # 5 anther lobes fused together with free epipetalous filaments
    for ang in pet_angles:
        rad = math.radians(ang)
        fx, fy = cx + 125 * math.cos(rad), cy + 125 * math.sin(rad)
        # Filament connecting to corolla
        cx_cor, cy_cor = cx + 180 * math.cos(rad), cy + 180 * math.sin(rad)
        lines.append(f'<line x1="{fx:.1f}" y1="{fy:.1f}" x2="{cx_cor:.1f}" y2="{cy_cor:.1f}" stroke="#eab308" stroke-width="1.8" stroke-dasharray="3 2"/>')
        # Anther lobe
        lines.append(f'<circle cx="{fx:.1f}" cy="{fy:.1f}" r="5.5" fill="url(#antherGrad)" stroke="#ca8a04" stroke-width="1.2"/>')

    # Gynoecium: Bicarpellary Syncarpous, Unilocular Inferior Ovary with Single Basal Ovule
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="60" fill="#090d16" stroke="#22c55e" stroke-width="3"/>')
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="56" fill="#020617" stroke="#15803d" stroke-width="1.5"/>')
    
    # 2 carpels demarcated by vertical suture
    lines.append(f'<line x1="{cx}" y1="{cy - 56}" x2="{cx}" y2="{cy + 56}" stroke="rgba(255,255,255,0.15)" stroke-width="1.5" stroke-dasharray="4 3"/>')
    
    # Single basal anatropous ovule
    lines.append(f'<ellipse cx="{cx}" cy="{cy + 15}" rx="14" ry="20" fill="url(#ovaryGrad)" stroke="#d97706" stroke-width="1.5"/>')
    lines.append(f'<circle cx="{cx}" cy="{cy + 15}" r="4" fill="#d97706"/>')
    # Basal funicle
    lines.append(f'<line x1="{cx}" y1="{cy + 35}" x2="{cx}" y2="{cy + 56}" stroke="#22c55e" stroke-width="2"/>')

    # Labels
    lines.append(label_leader(cx + 14, cy - 330, cx + 120, cy - 330, "Mother Axis", "Posterior position indicator", "left"))
    lines.append(label_leader(cx + 240, cy, cx + 290, cy - 100, "Pappus Scales (Calyx)", "Reduced bristles aiding seed dispersal", "left"))
    lines.append(label_leader(cx + 190, cy + 60, cx + 290, cy + 40, "Tubular Corolla: C(5)", "5 fused petals, valvate aestivation", "left"))
    lines.append(label_leader(cx + 125, cy + 110, cx + 290, cy + 160, "Syngenesious Stamens: A(5)", "Anthers united into cylinder, epipetalous", "left"))
    lines.append(label_leader(cx - 125, cy, cx - 290, cy - 40, "Epipetalous Filament", "Filaments free, inserted on corolla tube", "right"))
    lines.append(label_leader(cx - 60, cy + 10, cx - 290, cy + 80, "Bicarpellary Ovary: G(2)", "Syncarpous, unilocular inferior ovary", "right"))
    lines.append(label_leader(cx, cy + 20, cx - 290, cy + 200, "Basal Placentation", "Single solitary basal ovule", "right"))
    lines.append(label_leader(cx + 45, cy + 345, cx + 180, cy + 355, "Chaffy Palea (Bract)", "Subtending floret bract", "left"))

    lines.append(draw_summary_card(cx, 840, '<tspan fill="#4ade80" font-weight="700">K:</tspan> pappus scales &#8226; <tspan fill="#fde047" font-weight="700">C:</tspan> (5) tubular valvate &#8226; <tspan fill="#eab308" font-weight="700">A:</tspan> (5) syngenesious epipetalous &#8226; <tspan fill="#22c55e" font-weight="700">G:</tspan> (2) inferior single basal ovule'))
    lines.append('</svg>')
    return "\n".join(lines)

# ==============================================================================
# 5. CALOTROPIS (Calotropis gigantea - Apocynaceae)
# ==============================================================================
def create_calotropis_svg():
    w, h, cx, cy = 900, 920, 450, 490
    lines = base_svg_start(w, h, "BOTANICAL FLORAL DIAGRAM: CALOTROPIS", "Calotropis gigantea (L.) Dryand. • Family: Apocynaceae", "&#8853; &#9909; K&#8325; C&#8333;&#8325;&#8334; A&#8325; G&#8333;&#8322;&#8334; (Gynostegium)")
    
    lines.append('''
    <defs>
      <linearGradient id="caloCorolla" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#e9d5ff"/><stop offset="50%" stop-color="#a855f7"/><stop offset="100%" stop-color="#6b21a8"/></linearGradient>
      <linearGradient id="coronaGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fbcfe8"/><stop offset="100%" stop-color="#db2777"/></linearGradient>
    </defs>
    ''')

    for r in [250, 190, 130, 75]:
        lines.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1" stroke-dasharray="4 4"/>')

    lines.append(draw_mother_axis(cx, cy, 14, 330))
    lines.append(draw_bract(cx, cy, 345, 76, 32))

    # Calyx: 5 Free Sepals, Quincuncial
    sep_r = 250
    sep_angles = [-90, -18, 54, 126, 198]
    r_offsets = [10, -8, 10, -8, 0]
    for idx, ang in enumerate(sep_angles):
        rad = math.radians(ang)
        sr = sep_r + r_offsets[idx]
        span = 60
        a1, a2 = math.radians(ang - span/2), math.radians(ang + span/2)
        x1, y1 = cx + sr * math.cos(a1), cy + sr * math.sin(a1)
        x2, y2 = cx + sr * math.cos(a2), cy + sr * math.sin(a2)
        mx, my = cx + (sr + 16) * math.cos(rad), cy + (sr + 16) * math.sin(rad)
        ix, iy = cx + (sr - 10) * math.cos(rad), cy + (sr - 10) * math.sin(rad)
        d = f"M {x1:.1f} {y1:.1f} Q {mx:.1f} {my:.1f} {x2:.1f} {y2:.1f} Q {ix:.1f} {iy:.1f} {x1:.1f} {y1:.1f} Z"
        lines.append(f'<path d="{d}" fill="url(#sepalGrad)" stroke="#14532d" stroke-width="2"/>')

    # Corolla: 5 Petals, Gamopetalous, Valvate Aestivation
    cor_r = 190
    pet_angles = [-54 + i * 72 for i in range(5)]
    pet_ends = []
    for ang in pet_angles:
        rad = math.radians(ang)
        span = 62
        a1, a2 = math.radians(ang - span/2), math.radians(ang + span/2)
        x1, y1 = cx + cor_r * math.cos(a1), cy + cor_r * math.sin(a1)
        x2, y2 = cx + cor_r * math.cos(a2), cy + cor_r * math.sin(a2)
        pet_ends.append(((x1, y1), (x2, y2)))
        mx, my = cx + (cor_r + 16) * math.cos(rad), cy + (cor_r + 16) * math.sin(rad)
        ix, iy = cx + (cor_r - 10) * math.cos(rad), cy + (cor_r - 10) * math.sin(rad)
        d = f"M {x1:.1f} {y1:.1f} Q {mx:.1f} {my:.1f} {x2:.1f} {y2:.1f} Q {ix:.1f} {iy:.1f} {x1:.1f} {y1:.1f} Z"
        lines.append(f'<path d="{d}" fill="url(#caloCorolla)" stroke="#c084fc" stroke-width="2"/>')
    for i in range(5):
        e1, e2 = pet_ends[i][1], pet_ends[(i+1)%5][0]
        mx, my = (e1[0] + e2[0])/2, (e1[1] + e2[1])/2
        lines.append(f'<path d="M {e1[0]:.1f} {e1[1]:.1f} Q {mx*1.01:.1f} {my*1.01:.1f} {e2[0]:.1f} {e2[1]:.1f}" fill="none" stroke="#d8b4fe" stroke-width="2.2"/>')

    # Staminal Corona: 5 fleshy horn-shaped lobes radiating from staminal tube
    cor_lobes_r = 135
    for ang in pet_angles:
        rad = math.radians(ang)
        lx, ly = cx + cor_lobes_r * math.cos(rad), cy + cor_lobes_r * math.sin(rad)
        lines.append(f'<path d="M {lx - 12} {ly - 8} Q {lx} {ly + 18} {lx + 12} {ly - 8} Q {lx} {ly - 16} {lx - 12} {ly - 8} Z" transform="rotate({ang + 90} {lx} {ly})" fill="url(#coronaGrad)" stroke="#be185d" stroke-width="1.8"/>')

    # Gynostegium & Pentagonal Stigmatic Disc
    # 5 angles of pentagon
    pent_angles = [-90 + i * 72 for i in range(5)]
    pent_pts = []
    for ang in pent_angles:
        rad = math.radians(ang)
        px, py = cx + 72 * math.cos(rad), cy + 72 * math.sin(rad)
        pent_pts.append(f"{px:.1f},{py:.1f}")
    lines.append(f'<polygon points="{" ".join(pent_pts)}" fill="#1e1b4b" stroke="#fde047" stroke-width="2.5"/>')

    # 5 Pollinia pairs & Translators (Corpusculum at angles)
    for ang in pent_angles:
        rad = math.radians(ang)
        px, py = cx + 72 * math.cos(rad), cy + 72 * math.sin(rad)
        # Corpusculum (dark center clicker)
        lines.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.2" fill="#000000" stroke="#fde047" stroke-width="1.2"/>')
        # Two retinacula arms with yellow pollinia
        for arm_ang in [ang - 24, ang + 24]:
            arad = math.radians(arm_ang)
            pol_x, pol_y = cx + 54 * math.cos(arad), cy + 54 * math.sin(arad)
            lines.append(f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{pol_x:.1f}" y2="{pol_y:.1f}" stroke="#fde047" stroke-width="1"/>')
            lines.append(f'<ellipse cx="{pol_x:.1f}" cy="{pol_y:.1f}" rx="4.5" ry="3" fill="url(#antherGrad)" stroke="#ca8a04" stroke-width="0.8"/>')

    # Gynoecium: Bicarpellary, 2 distinct ovaries (apocarpous at ovaries, syncarpous at stigma)
    # 2 carpels with marginal placentation and multiple ovules
    for c_offset, c_ang in [(-22, 180), (22, 0)]:
        ox, oy = cx + c_offset, cy
        lines.append(f'<circle cx="{ox}" cy="{oy}" r="16" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>')
        # Marginal ovules
        lines.append(f'<circle cx="{ox - 4}" cy="{oy - 5}" r="2.5" fill="url(#ovaryGrad)"/>')
        lines.append(f'<circle cx="{ox - 4}" cy="{oy + 5}" r="2.5" fill="url(#ovaryGrad)"/>')

    # Labels
    lines.append(label_leader(cx + 14, cy - 330, cx + 120, cy - 330, "Mother Axis", "Posterior position indicator", "left"))
    lines.append(label_leader(cx + 250, cy - 50, cx + 290, cy - 140, "Calyx: K5", "5 free sepals, quincuncial", "left"))
    lines.append(label_leader(cx + 190, cy + 60, cx + 290, cy + 20, "Corolla: C(5)", "Gamopetalous, valvate lobes", "left"))
    lines.append(label_leader(cx + 135, cy + 120, cx + 290, cy + 150, "Staminal Corona", "5 fleshy nectariferous horn lobes", "left"))
    lines.append(label_leader(cx - 72, cy - 40, cx - 290, cy - 60, "Pentagonal Stigma Head", "Anthers adnate forming Gynostegium", "right"))
    lines.append(label_leader(cx - 54, cy + 30, cx - 290, cy + 60, "Pollinia &amp; Translator", "Paired pollen masses + Corpusculum", "right"))
    lines.append(label_leader(cx - 22, cy, cx - 290, cy + 180, "Bicarpellary Ovaries", "2 free ovaries, marginal placentation", "right"))
    lines.append(label_leader(cx + 38, cy + 345, cx + 180, cy + 355, "Bract", "Anterior floral position", "left"))

    lines.append(draw_summary_card(cx, 840, '<tspan fill="#4ade80" font-weight="700">K:</tspan> 5 quincuncial &#8226; <tspan fill="#c084fc" font-weight="700">C:</tspan> (5) valvate &#8226; <tspan fill="#f472b6" font-weight="700">Corona:</tspan> 5 lobes &#8226; <tspan fill="#fde047" font-weight="700">A:</tspan> 5 gynostegium pollinia &#8226; <tspan fill="#22c55e" font-weight="700">G:</tspan> (2) free ovaries'))
    lines.append('</svg>')
    return "\n".join(lines)

# ==============================================================================
# 6. CRINUM (Crinum asiaticum - Amaryllidaceae)
# ==============================================================================
def create_crinum_svg():
    w, h, cx, cy = 900, 920, 450, 490
    lines = base_svg_start(w, h, "BOTANICAL FLORAL DIAGRAM: CRINUM", "Crinum asiaticum L. • Family: Amaryllidaceae", "&#8853; &#9909; P&#8333;&#8323;&#8330;&#8323;&#8334; A&#8323;&#8330;&#8323; G&#8333;&#8323;&#8334; (Inferior)")
    
    lines.append('''
    <defs>
      <linearGradient id="crinumTepal" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#ffffff"/><stop offset="60%" stop-color="#f1f5f9"/><stop offset="100%" stop-color="#cbd5e1"/></linearGradient>
    </defs>
    ''')

    for r in [255, 195, 135, 65]:
        lines.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1" stroke-dasharray="4 4"/>')

    lines.append(draw_mother_axis(cx, cy, 14, 330))
    # Spathe / Bract
    lines.append(draw_bract(cx, cy, 345, 90, 36, fill="#64748b", stroke="#94a3b8"))

    # Outer Perianth Whorl (3 Outer Tepals)
    out_r = 255
    out_angles = [-90, 30, 150]
    for ang in out_angles:
        rad = math.radians(ang)
        span = 80
        a1, a2 = math.radians(ang - span/2), math.radians(ang + span/2)
        x1, y1 = cx + out_r * math.cos(a1), cy + out_r * math.sin(a1)
        x2, y2 = cx + out_r * math.cos(a2), cy + out_r * math.sin(a2)
        mx, my = cx + (out_r + 18) * math.cos(rad), cy + (out_r + 18) * math.sin(rad)
        ix, iy = cx + (out_r - 12) * math.cos(rad), cy + (out_r - 12) * math.sin(rad)
        d = f"M {x1:.1f} {y1:.1f} Q {mx:.1f} {my:.1f} {x2:.1f} {y2:.1f} Q {ix:.1f} {iy:.1f} {x1:.1f} {y1:.1f} Z"
        lines.append(f'<path d="{d}" fill="url(#crinumTepal)" stroke="#94a3b8" stroke-width="2"/>')
        lines.append(f'<line x1="{mx:.1f}" y1="{my:.1f}" x2="{ix:.1f}" y2="{iy:.1f}" stroke="#38bdf8" stroke-width="1.2"/>')

    # Inner Perianth Whorl (3 Inner Tepals)
    in_r = 195
    in_angles = [-30, 90, 210]
    for ang in in_angles:
        rad = math.radians(ang)
        span = 82
        a1, a2 = math.radians(ang - span/2), math.radians(ang + span/2)
        x1, y1 = cx + in_r * math.cos(a1), cy + in_r * math.sin(a1)
        x2, y2 = cx + in_r * math.cos(a2), cy + in_r * math.sin(a2)
        mx, my = cx + (in_r + 16) * math.cos(rad), cy + (in_r + 16) * math.sin(rad)
        ix, iy = cx + (in_r - 12) * math.cos(rad), cy + (in_r - 12) * math.sin(rad)
        d = f"M {x1:.1f} {y1:.1f} Q {mx:.1f} {my:.1f} {x2:.1f} {y2:.1f} Q {ix:.1f} {iy:.1f} {x1:.1f} {y1:.1f} Z"
        lines.append(f'<path d="{d}" fill="url(#crinumTepal)" stroke="#e2e8f0" stroke-width="2"/>')
        lines.append(f'<line x1="{mx:.1f}" y1="{my:.1f}" x2="{ix:.1f}" y2="{iy:.1f}" stroke="#38bdf8" stroke-width="1.2"/>')

    # Androecium: 6 Epiphyllous Stamens (3 outer, 3 inner) with versatile anthers
    for stam_r, angles in [(140, out_angles), (115, in_angles)]:
        for ang in angles:
            rad = math.radians(ang)
            ax, ay = cx + stam_r * math.cos(rad), cy + stam_r * math.sin(rad)
            # Versatile anther (T-shaped attachment)
            tang = ang + 90
            trad = math.radians(tang)
            dx, dy = 8 * math.cos(trad), 8 * math.sin(trad)
            lines.append(f'<line x1="{ax - dx:.1f}" y1="{ay - dy:.1f}" x2="{ax + dx:.1f}" y2="{ay + dy:.1f}" stroke="#fde047" stroke-width="3.5" stroke-linecap="round"/>')
            lines.append(f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="2" fill="#ca8a04"/>')

    # Gynoecium: Tricarpellary Syncarpous, Trilocular Inferior Ovary with Axile Placentation
    ov_r = 62
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="{ov_r}" fill="#0f172a" stroke="#22c55e" stroke-width="2.8"/>')
    # 3 septa radiating at 120 degrees
    septa_angles = [-90, 30, 150]
    for ang in septa_angles:
        rad = math.radians(ang)
        sx, sy = cx + ov_r * math.cos(rad), cy + ov_r * math.sin(rad)
        lines.append(f'<line x1="{cx}" y1="{cy}" x2="{sx:.1f}" y2="{sy:.1f}" stroke="#4ade80" stroke-width="2"/>')
    
    # Axile ovules (2 per locule)
    for ang in [-30, 90, 210]:
        rad = math.radians(ang)
        for offset in [-16, 16]:
            o_ang = math.radians(ang + offset)
            ox, oy = cx + 32 * math.cos(o_ang), cy + 32 * math.sin(o_ang)
            lines.append(f'<ellipse cx="{ox:.1f}" cy="{oy:.1f}" rx="5" ry="3.5" transform="rotate({ang} {ox} {oy})" fill="url(#ovaryGrad)" stroke="#ca8a04" stroke-width="1"/>')

    # Labels
    lines.append(label_leader(cx + 14, cy - 330, cx + 120, cy - 330, "Mother Axis", "Posterior position indicator", "left"))
    lines.append(label_leader(cx + out_r * math.cos(math.radians(30)), cy + out_r * math.sin(math.radians(30)), cx + 290, cy - 90, "Outer Perianth (P 3)", "3 outer white petaloid tepals", "left"))
    lines.append(label_leader(cx + in_r * math.cos(math.radians(-30)), cy + in_r * math.sin(math.radians(-30)), cx + 290, cy + 40, "Inner Perianth (+3)", "3 inner alternating tepals", "left"))
    lines.append(label_leader(cx + 140, cy + 60, cx + 290, cy + 170, "Versatile Anthers: A(3+3)", "6 epiphyllous versatile stamens", "left"))
    lines.append(label_leader(cx - 140, cy - 20, cx - 290, cy - 50, "Epiphyllous Insertion", "Filaments adnate to perianth tube", "right"))
    lines.append(label_leader(cx - ov_r, cy, cx - 290, cy + 80, "Tricarpellary Ovary: G(3)", "Syncarpous trilocular inferior ovary", "right"))
    lines.append(label_leader(cx - 32, cy + 20, cx - 290, cy + 200, "Axile Placentation", "Multiple ovules per trilocular cell", "right"))
    lines.append(label_leader(cx + 45, cy + 345, cx + 180, cy + 355, "Spathaceous Bract", "Subtending umbel spathe", "left"))

    lines.append(draw_summary_card(cx, 840, '<tspan fill="#38bdf8" font-weight="700">P:</tspan> (3+3) petaloid tepals &#8226; <tspan fill="#fde047" font-weight="700">A:</tspan> 3+3 epiphyllous versatile &#8226; <tspan fill="#22c55e" font-weight="700">G:</tspan> (3) syncarpous trilocular inferior axile'))
    lines.append('</svg>')
    return "\n".join(lines)

# ==============================================================================
# 7. IXORA (Ixora coccinea - Rubiaceae)
# ==============================================================================
def create_ixora_svg():
    w, h, cx, cy = 900, 920, 450, 490
    lines = base_svg_start(w, h, "BOTANICAL FLORAL DIAGRAM: IXORA", "Ixora coccinea L. • Family: Rubiaceae", "&#8853; &#9909; K&#8333;&#8324;&#8334; C&#8333;&#8324;&#8334; A&#8324; G&#8333;&#8322;&#8334; (Inferior)")
    
    lines.append('''
    <defs>
      <linearGradient id="ixoraCorolla" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fb7185"/><stop offset="50%" stop-color="#e11d48"/><stop offset="100%" stop-color="#9f1239"/></linearGradient>
    </defs>
    ''')

    for r in [250, 190, 120, 60]:
        lines.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1" stroke-dasharray="4 4"/>')

    lines.append(draw_mother_axis(cx, cy, 14, 330))
    lines.append(draw_bract(cx, cy, 345, 72, 30))
    
    # 2 Bracteoles
    for bx, ang in [(cx - 290, 180), (cx + 290, 0)]:
        lines.append(f'<path d="M {bx} {cy - 24} Q {bx + (12 if ang==0 else -12)} {cy} {bx} {cy + 24} Q {bx - (8 if ang==0 else -8)} {cy} {bx} {cy - 24} Z" fill="url(#sepalGrad)" stroke="#16a34a" stroke-width="1.5"/>')

    # Calyx: 4 Small Fused Sepals, Valvate (Tetramerous)
    sep_r = 250
    sep_angles = [-90, 0, 90, 180]
    sep_ends = []
    for ang in sep_angles:
        rad = math.radians(ang)
        span = 70
        a1, a2 = math.radians(ang - span/2), math.radians(ang + span/2)
        x1, y1 = cx + sep_r * math.cos(a1), cy + sep_r * math.sin(a1)
        x2, y2 = cx + sep_r * math.cos(a2), cy + sep_r * math.sin(a2)
        sep_ends.append(((x1, y1), (x2, y2)))
        mx, my = cx + (sep_r + 14) * math.cos(rad), cy + (sep_r + 14) * math.sin(rad)
        ix, iy = cx + (sep_r - 8) * math.cos(rad), cy + (sep_r - 8) * math.sin(rad)
        d = f"M {x1:.1f} {y1:.1f} Q {mx:.1f} {my:.1f} {x2:.1f} {y2:.1f} Q {ix:.1f} {iy:.1f} {x1:.1f} {y1:.1f} Z"
        lines.append(f'<path d="{d}" fill="url(#sepalGrad)" stroke="#14532d" stroke-width="2"/>')
    for i in range(4):
        e1, e2 = sep_ends[i][1], sep_ends[(i+1)%4][0]
        mx, my = (e1[0] + e2[0])/2, (e1[1] + e2[1])/2
        lines.append(f'<path d="M {e1[0]:.1f} {e1[1]:.1f} Q {mx*1.01:.1f} {my*1.01:.1f} {e2[0]:.1f} {e2[1]:.1f}" fill="none" stroke="#22c55e" stroke-width="2"/>')

    # Corolla: 4 Petals, Twisted / Contorted Aestivation
    cor_r = 190
    pet_angles = [-45, 45, 135, 225] # Alternating with sepals
    for ang in pet_angles:
        span = 84
        a_in = math.radians(ang - span/2)
        a_out = math.radians(ang + span/2)
        r_in = cor_r - 12
        r_out = cor_r + 14
        px_in, py_in = cx + r_in * math.cos(a_in), cy + r_in * math.sin(a_in)
        px_out, py_out = cx + r_out * math.cos(a_out), cy + r_out * math.sin(a_out)
        pm_x = cx + (cor_r + 8) * math.cos(math.radians(ang))
        pm_y = cy + (cor_r + 8) * math.sin(math.radians(ang))
        pb_x = cx + (cor_r - 16) * math.cos(math.radians(ang))
        pb_y = cy + (cor_r - 16) * math.sin(math.radians(ang))
        d = f"M {px_in:.1f} {py_in:.1f} Q {pm_x:.1f} {pm_y:.1f} {px_out:.1f} {py_out:.1f} Q {pb_x:.1f} {pb_y:.1f} {px_in:.1f} {py_in:.1f} Z"
        lines.append(f'<path d="{d}" fill="url(#ixoraCorolla)" stroke="#fda4af" stroke-width="2"/>')

    # Androecium: 4 Stamens, Epipetalous alternating with petals
    for ang in sep_angles: # alternate with petals
        rad = math.radians(ang)
        ax, ay = cx + 120 * math.cos(rad), cy + 120 * math.sin(rad)
        cx_cor, cy_cor = cx + 175 * math.cos(rad), cy + 175 * math.sin(rad)
        lines.append(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{cx_cor:.1f}" y2="{cy_cor:.1f}" stroke="#fde047" stroke-width="2"/>')
        # Dithecous anther
        tang = ang + 90
        trad = math.radians(tang)
        dx, dy = 4 * math.cos(trad), 4 * math.sin(trad)
        lines.append(f'<circle cx="{ax - dx:.1f}" cy="{ay - dy:.1f}" r="3.2" fill="url(#antherGrad)" stroke="#854d0e" stroke-width="0.8"/>')
        lines.append(f'<circle cx="{ax + dx:.1f}" cy="{ay + dy:.1f}" r="3.2" fill="url(#antherGrad)" stroke="#854d0e" stroke-width="0.8"/>')

    # Gynoecium: Bicarpellary Syncarpous, Bilocular Inferior Ovary with 1 Ovule per Locule
    ov_r = 58
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="{ov_r}" fill="#0f172a" stroke="#22c55e" stroke-width="2.8"/>')
    # Vertical septum dividing into 2 locules
    lines.append(f'<line x1="{cx}" y1="{cy - ov_r}" x2="{cx}" y2="{cy + ov_r}" stroke="#4ade80" stroke-width="2.2"/>')
    # 1 ovule per locule on axile placentation
    lines.append(f'<circle cx="{cx - 24}" cy="{cy}" r="7.5" fill="url(#ovaryGrad)" stroke="#ca8a04" stroke-width="1.2"/>')
    lines.append(f'<circle cx="{cx + 24}" cy="{cy}" r="7.5" fill="url(#ovaryGrad)" stroke="#ca8a04" stroke-width="1.2"/>')
    lines.append(f'<line x1="{cx}" y1="{cy}" x2="{cx - 16}" y2="{cy}" stroke="#22c55e" stroke-width="1.5"/>')
    lines.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + 16}" y2="{cy}" stroke="#22c55e" stroke-width="1.5"/>')

    # Labels
    lines.append(label_leader(cx + 14, cy - 330, cx + 120, cy - 330, "Mother Axis", "Posterior position indicator", "left"))
    lines.append(label_leader(cx + sep_r, cy, cx + 290, cy - 100, "Calyx: K(4)", "4 fused valvate sepals (tetramerous)", "left"))
    lines.append(label_leader(cx + cor_r * math.cos(math.radians(45)), cy + cor_r * math.sin(math.radians(45)), cx + 290, cy + 30, "Corolla: C(4)", "4 contorted / twisted petal lobes", "left"))
    lines.append(label_leader(cx, cy + 120, cx + 290, cy + 160, "Epipetalous Stamens (A4)", "4 stamens inserted at throat of tube", "left"))
    lines.append(label_leader(cx - 120, cy, cx - 290, cy - 50, "Alternipetalous", "Stamens alternate with petals", "right"))
    lines.append(label_leader(cx - ov_r, cy, cx - 290, cy + 70, "Bicarpellary Ovary: G(2)", "Syncarpous bilocular inferior ovary", "right"))
    lines.append(label_leader(cx - 24, cy, cx - 290, cy + 190, "Axile Placentation", "Solitary ovule in each locule", "right"))
    lines.append(label_leader(cx + 38, cy + 345, cx + 180, cy + 355, "Bract", "Anterior floral position", "left"))

    lines.append(draw_summary_card(cx, 840, '<tspan fill="#4ade80" font-weight="700">K:</tspan> (4) valvate &#8226; <tspan fill="#f43f5e" font-weight="700">C:</tspan> (4) twisted contorted &#8226; <tspan fill="#fde047" font-weight="700">A:</tspan> 4 epipetalous &#8226; <tspan fill="#22c55e" font-weight="700">G:</tspan> (2) inferior 2-locular 1-ovule'))
    lines.append('</svg>')
    return "\n".join(lines)

# ==============================================================================
# 8. PERIWINKLE (Catharanthus roseus - Apocynaceae)
# ==============================================================================
def create_periwinkle_svg():
    w, h, cx, cy = 900, 920, 450, 490
    lines = base_svg_start(w, h, "BOTANICAL FLORAL DIAGRAM: PERIWINKLE", "Catharanthus roseus (L.) G.Don • Family: Apocynaceae", "&#8853; &#9909; K&#8325; C&#8333;&#8325;&#8334; A&#8325; G&#8333;&#8322;&#8334; (Salverform)")
    
    lines.append('''
    <defs>
      <linearGradient id="vincaPetal" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fbcfe8"/><stop offset="50%" stop-color="#f43f5e"/><stop offset="100%" stop-color="#be185d"/></linearGradient>
    </defs>
    ''')

    for r in [250, 190, 120, 60]:
        lines.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1" stroke-dasharray="4 4"/>')

    lines.append(draw_mother_axis(cx, cy, 14, 330))
    lines.append(draw_bract(cx, cy, 345, 76, 32))

    # Calyx: 5 Sepals, deeply partite, valvate
    sep_r = 250
    sep_angles = [-90 + i * 72 for i in range(5)]
    for ang in sep_angles:
        rad = math.radians(ang)
        span = 58
        a1, a2 = math.radians(ang - span/2), math.radians(ang + span/2)
        x1, y1 = cx + sep_r * math.cos(a1), cy + sep_r * math.sin(a1)
        x2, y2 = cx + sep_r * math.cos(a2), cy + sep_r * math.sin(a2)
        mx, my = cx + (sep_r + 16) * math.cos(rad), cy + (sep_r + 16) * math.sin(rad)
        ix, iy = cx + (sep_r - 10) * math.cos(rad), cy + (sep_r - 10) * math.sin(rad)
        d = f"M {x1:.1f} {y1:.1f} Q {mx:.1f} {my:.1f} {x2:.1f} {y2:.1f} Q {ix:.1f} {iy:.1f} {x1:.1f} {y1:.1f} Z"
        lines.append(f'<path d="{d}" fill="url(#sepalGrad)" stroke="#14532d" stroke-width="2"/>')

    # Corolla: 5 Petals, Salverform, Twisted / Contorted Aestivation
    cor_r = 190
    pet_angles = [-54 + i * 72 for i in range(5)]
    for ang in pet_angles:
        span = 76
        a_in = math.radians(ang - span/2)
        a_out = math.radians(ang + span/2)
        r_in = cor_r - 12
        r_out = cor_r + 14
        px_in, py_in = cx + r_in * math.cos(a_in), cy + r_in * math.sin(a_in)
        px_out, py_out = cx + r_out * math.cos(a_out), cy + r_out * math.sin(a_out)
        pm_x = cx + (cor_r + 8) * math.cos(math.radians(ang))
        pm_y = cy + (cor_r + 8) * math.sin(math.radians(ang))
        pb_x = cx + (cor_r - 16) * math.cos(math.radians(ang))
        pb_y = cy + (cor_r - 16) * math.sin(math.radians(ang))
        d = f"M {px_in:.1f} {py_in:.1f} Q {pm_x:.1f} {pm_y:.1f} {px_out:.1f} {py_out:.1f} Q {pb_x:.1f} {pb_y:.1f} {px_in:.1f} {py_in:.1f} Z"
        lines.append(f'<path d="{d}" fill="url(#vincaPetal)" stroke="#fda4af" stroke-width="2"/>')

    # Throat hairs & 5 Epipetalous Stamens included within tube
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="115" fill="none" stroke="#fde047" stroke-width="2" stroke-dasharray="4 3"/>')
    for ang in sep_angles:
        rad = math.radians(ang)
        ax, ay = cx + 115 * math.cos(rad), cy + 115 * math.sin(rad)
        cx_cor, cy_cor = cx + 175 * math.cos(rad), cy + 175 * math.sin(rad)
        lines.append(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{cx_cor:.1f}" y2="{cy_cor:.1f}" stroke="#fde047" stroke-width="1.8"/>')
        # Sagittate anther
        lines.append(f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="4.2" fill="url(#antherGrad)" stroke="#854d0e" stroke-width="1"/>')

    # Gynoecium: Bicarpellary, Ovaries 2 Free (Apocarpous at base), styles united + 2 Disc Nectaries
    for offset in [-22, 22]:
        ox, oy = cx + offset, cy
        lines.append(f'<circle cx="{ox}" cy="{oy}" r="17" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>')
        # Marginal ovules
        lines.append(f'<circle cx="{ox - 4}" cy="{oy - 5}" r="2.8" fill="url(#ovaryGrad)"/>')
        lines.append(f'<circle cx="{ox - 4}" cy="{oy + 5}" r="2.8" fill="url(#ovaryGrad)"/>')
    
    # 2 Nectariferous glands alternating with carpels (top and bottom)
    for ny in [cy - 22, cy + 22]:
        lines.append(f'<ellipse cx="{cx}" cy="{ny}" rx="10" ry="6" fill="#84cc16" stroke="#4d7c0f" stroke-width="1.2"/>')

    # Labels
    lines.append(label_leader(cx + 14, cy - 330, cx + 120, cy - 330, "Mother Axis", "Posterior position indicator", "left"))
    lines.append(label_leader(cx + sep_r * math.cos(math.radians(-18)), cy + sep_r * math.sin(math.radians(-18)), cx + 290, cy - 90, "Calyx: K5", "5 sepals, deeply partite", "left"))
    lines.append(label_leader(cx + cor_r * math.cos(math.radians(18)), cy + cor_r * math.sin(math.radians(18)), cx + 290, cy + 30, "Corolla: C(5)", "Salverform, twisted / contorted lobes", "left"))
    lines.append(label_leader(cx + 115, cy + 60, cx + 290, cy + 160, "Included Stamens (A5)", "5 epipetalous enclosed in corolla throat", "left"))
    lines.append(label_leader(cx, cy - 22, cx - 290, cy - 60, "Disc Nectaries", "2 prominent green nectar glands", "right"))
    lines.append(label_leader(cx - 22, cy, cx - 290, cy + 60, "Bicarpellary Free Ovaries", "2 carpels apocarpous at base", "right"))
    lines.append(label_leader(cx - 26, cy + 5, cx - 290, cy + 180, "Marginal Placentation", "Multiple ovules in each free carpel", "right"))
    lines.append(label_leader(cx + 38, cy + 345, cx + 180, cy + 355, "Bract", "Anterior floral position", "left"))

    lines.append(draw_summary_card(cx, 840, '<tspan fill="#4ade80" font-weight="700">K:</tspan> 5 valvate &#8226; <tspan fill="#f43f5e" font-weight="700">C:</tspan> (5) twisted contorted &#8226; <tspan fill="#fde047" font-weight="700">A:</tspan> 5 epipetalous included &#8226; <tspan fill="#84cc16" font-weight="700">Disc:</tspan> 2 glands &#8226; <tspan fill="#22c55e" font-weight="700">G:</tspan> (2) free ovaries'))
    lines.append('</svg>')
    return "\n".join(lines)

# ==============================================================================
# 9. TRIDAX (Tridax procumbens - Asteraceae)
# ==============================================================================
def create_tridax_svg():
    w, h, cx, cy = 900, 920, 450, 490
    lines = base_svg_start(w, h, "BOTANICAL FLORAL DIAGRAM: TRIDAX", "Tridax procumbens L. • Family: Asteraceae", "Disc: &#8853; &#9909; K_pappus C&#8333;&#8325;&#8334; A&#8333;&#8325;&#8334; G&#8333;&#8322;&#8334; (Inferior)")
    
    lines.append('''
    <defs>
      <linearGradient id="tridaxPetal" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fef08a"/><stop offset="60%" stop-color="#facc15"/><stop offset="100%" stop-color="#ca8a04"/></linearGradient>
    </defs>
    ''')

    for r in [250, 190, 125, 60]:
        lines.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1" stroke-dasharray="4 4"/>')

    lines.append(draw_mother_axis(cx, cy, 14, 330))
    lines.append(draw_bract(cx, cy, 345, 84, 34, fill="#a16207", stroke="#eab308"))

    # Calyx: Feathery Pappus Ring (multiple radiating bristles)
    n_bristles = 18
    for i in range(n_bristles):
        ang = i * (360 / n_bristles)
        rad = math.radians(ang)
        bx1 = cx + 235 * math.cos(rad)
        by1 = cy + 235 * math.sin(rad)
        bx2 = cx + 265 * math.cos(rad)
        by2 = cy + 265 * math.sin(rad)
        lines.append(f'<line x1="{bx1:.1f}" y1="{by1:.1f}" x2="{bx2:.1f}" y2="{by2:.1f}" stroke="#4ade80" stroke-width="2" stroke-linecap="round"/>')
        # Tiny plumes on each bristle
        tang = ang + 90
        trad = math.radians(tang)
        pdx, pdy = 4 * math.cos(trad), 4 * math.sin(trad)
        lines.append(f'<line x1="{bx2 - pdx:.1f}" y1="{by2 - pdy:.1f}" x2="{bx2 + pdx:.1f}" y2="{by2 + pdy:.1f}" stroke="#86efac" stroke-width="1"/>')

    # Corolla: 5 Fused Petals, Tubular, Valvate Aestivation
    cor_r = 190
    pet_angles = [-90 + i * 72 for i in range(5)]
    pet_ends = []
    for ang in pet_angles:
        rad = math.radians(ang)
        span = 60
        a1, a2 = math.radians(ang - span/2), math.radians(ang + span/2)
        x1, y1 = cx + cor_r * math.cos(a1), cy + cor_r * math.sin(a1)
        x2, y2 = cx + cor_r * math.cos(a2), cy + cor_r * math.sin(a2)
        pet_ends.append(((x1, y1), (x2, y2)))
        mx, my = cx + (cor_r + 16) * math.cos(rad), cy + (cor_r + 16) * math.sin(rad)
        ix, iy = cx + (cor_r - 10) * math.cos(rad), cy + (cor_r - 10) * math.sin(rad)
        d = f"M {x1:.1f} {y1:.1f} Q {mx:.1f} {my:.1f} {x2:.1f} {y2:.1f} Q {ix:.1f} {iy:.1f} {x1:.1f} {y1:.1f} Z"
        lines.append(f'<path d="{d}" fill="url(#tridaxPetal)" stroke="#fde047" stroke-width="2"/>')
    for i in range(5):
        e1, e2 = pet_ends[i][1], pet_ends[(i+1)%5][0]
        mx, my = (e1[0] + e2[0])/2, (e1[1] + e2[1])/2
        lines.append(f'<path d="M {e1[0]:.1f} {e1[1]:.1f} Q {mx*1.01:.1f} {my*1.01:.1f} {e2[0]:.1f} {e2[1]:.1f}" fill="none" stroke="#eab308" stroke-width="2.2"/>')

    # Androecium: 5 Stamens, Syngenesious (Anthers fused into cylindrical tube, epipetalous)
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="125" fill="none" stroke="#fde047" stroke-width="3.5"/>')
    for ang in pet_angles:
        rad = math.radians(ang)
        fx, fy = cx + 125 * math.cos(rad), cy + 125 * math.sin(rad)
        cx_cor, cy_cor = cx + 180 * math.cos(rad), cy + 180 * math.sin(rad)
        lines.append(f'<line x1="{fx:.1f}" y1="{fy:.1f}" x2="{cx_cor:.1f}" y2="{cy_cor:.1f}" stroke="#eab308" stroke-width="1.8" stroke-dasharray="3 2"/>')
        lines.append(f'<circle cx="{fx:.1f}" cy="{fy:.1f}" r="5.2" fill="url(#antherGrad)" stroke="#ca8a04" stroke-width="1.2"/>')

    # Gynoecium: Bicarpellary Syncarpous, Unilocular Inferior Ovary with Single Basal Ovule
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="60" fill="#090d16" stroke="#22c55e" stroke-width="3"/>')
    lines.append(f'<line x1="{cx}" y1="{cy - 56}" x2="{cx}" y2="{cy + 56}" stroke="rgba(255,255,255,0.15)" stroke-width="1.5" stroke-dasharray="4 3"/>')
    lines.append(f'<ellipse cx="{cx}" cy="{cy + 15}" rx="14" ry="20" fill="url(#ovaryGrad)" stroke="#d97706" stroke-width="1.5"/>')
    lines.append(f'<circle cx="{cx}" cy="{cy + 15}" r="4" fill="#d97706"/>')
    lines.append(f'<line x1="{cx}" y1="{cy + 35}" x2="{cx}" y2="{cy + 56}" stroke="#22c55e" stroke-width="2"/>')

    # Labels
    lines.append(label_leader(cx + 14, cy - 330, cx + 120, cy - 330, "Mother Axis", "Posterior position indicator", "left"))
    lines.append(label_leader(cx + 250, cy, cx + 290, cy - 100, "Feathery Pappus (K)", "Hair-like modified sepals for anemochory", "left"))
    lines.append(label_leader(cx + 190, cy + 60, cx + 290, cy + 40, "Tubular Corolla: C(5)", "5 fused yellow petals, valvate", "left"))
    lines.append(label_leader(cx + 125, cy + 110, cx + 290, cy + 160, "Syngenesious Stamens: A(5)", "Anthers united into cylinder around style", "left"))
    lines.append(label_leader(cx - 125, cy, cx - 290, cy - 40, "Epipetalous Filaments", "Attached to corolla tube", "right"))
    lines.append(label_leader(cx - 60, cy + 10, cx - 290, cy + 80, "Bicarpellary Ovary: G(2)", "Syncarpous unilocular inferior ovary", "right"))
    lines.append(label_leader(cx, cy + 20, cx - 290, cy + 200, "Basal Placentation", "Single erect anatropous ovule", "right"))
    lines.append(label_leader(cx + 42, cy + 345, cx + 180, cy + 355, "Palea / Chaffy Bract", "Receptacular bract subtending floret", "left"))

    lines.append(draw_summary_card(cx, 840, '<tspan fill="#4ade80" font-weight="700">K:</tspan> feathery pappus &#8226; <tspan fill="#fde047" font-weight="700">C:</tspan> (5) tubular valvate &#8226; <tspan fill="#eab308" font-weight="700">A:</tspan> (5) syngenesious &#8226; <tspan fill="#22c55e" font-weight="700">G:</tspan> (2) inferior single basal ovule'))
    lines.append('</svg>')
    return "\n".join(lines)


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
if __name__ == "__main__":
    generators = {
        "rose_floral_diagram.svg": create_rose_svg,
        "lotus_floral_diagram.svg": create_lotus_svg,
        "clitoria_floral_diagram.svg": create_clitoria_svg,
        "sunflower_floral_diagram.svg": create_sunflower_svg,
        "calotropis_floral_diagram.svg": create_calotropis_svg,
        "crinum_floral_diagram.svg": create_crinum_svg,
        "ixora_floral_diagram.svg": create_ixora_svg,
        "periwinkle_floral_diagram.svg": create_periwinkle_svg,
        "tridax_floral_diagram.svg": create_tridax_svg
    }
    
    for filename, func in generators.items():
        svg = func()
        out_path = os.path.join(DIAGRAMS_DIR, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"Generated {out_path} ({len(svg)} bytes)")


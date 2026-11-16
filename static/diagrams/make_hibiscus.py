import math
import os

def create_hibiscus_svg():
    w, h = 900, 920
    cx, cy = 450, 490
    
    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="background: radial-gradient(circle at 50% 40%, #111d38 0%, #0a1124 60%, #060914 100%); font-family: system-ui, -apple-system, \'Segoe UI\', Roboto, sans-serif;">')
    
    # Defs
    lines.append('<defs>')
    lines.append('  <linearGradient id="cardGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="rgba(255,255,255,0.08)"/><stop offset="100%" stop-color="rgba(255,255,255,0.02)"/></linearGradient>')
    lines.append('  <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fef08a"/><stop offset="100%" stop-color="#eab308"/></linearGradient>')
    lines.append('  <linearGradient id="petalGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fb7185"/><stop offset="50%" stop-color="#e11d48"/><stop offset="100%" stop-color="#9f1239"/></linearGradient>')
    lines.append('  <linearGradient id="sepalGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#4ade80"/><stop offset="70%" stop-color="#16a34a"/><stop offset="100%" stop-color="#14532d"/></linearGradient>')
    lines.append('  <linearGradient id="epkGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#86efac"/><stop offset="100%" stop-color="#15803d"/></linearGradient>')
    lines.append('  <linearGradient id="antherGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fef08a"/><stop offset="100%" stop-color="#ca8a04"/></linearGradient>')
    lines.append('  <linearGradient id="ovaryGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fef9c3"/><stop offset="100%" stop-color="#d97706"/></linearGradient>')
    lines.append('  <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3" result="b"/><feComposite in="SourceGraphic" in2="b" operator="over"/></filter>')
    lines.append('</defs>')
    
    # Outer Card Frame
    lines.append('<rect x="15" y="15" width="870" height="890" rx="28" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>')
    lines.append('<rect x="25" y="25" width="850" height="870" rx="22" fill="none" stroke="rgba(253,224,71,0.15)" stroke-width="1" stroke-dasharray="6 6"/>')
    
    # Header Section
    lines.append('<g transform="translate(450, 60)" text-anchor="middle">')
    lines.append('  <text y="0" font-size="22" font-weight="800" fill="#fde047" letter-spacing="1.5">BOTANICAL FLORAL DIAGRAM: HIBISCUS</text>')
    lines.append('  <text y="24" font-size="14" font-style="italic" fill="#cbd5e1">Hibiscus rosa-sinensis L. &bull; Family: Malvaceae</text>')
    lines.append('  <text y="45" font-size="13" font-weight="600" fill="#c084fc" font-family="monospace">Floral Formula: &#8853; &#9909; Epk&#8325;&#779;&#8328; K&#8333;&#8325;&#8334; C&#8325; A&#8333;&#8734;&#8334; G&#8333;&#8325;&#8334;</text>')
    lines.append('</g>')
    
    # Subtle Reference Axis Circles
    for r in [280, 225, 165, 110, 52]:
        lines.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="1" stroke-dasharray="4 4"/>')
    
    # 1. Mother Axis (Posterior, Top)
    lines.append(f'<circle cx="{cx}" cy="{cy - 330}" r="14" fill="#0f172a" stroke="#fde047" stroke-width="2.5"/>')
    lines.append(f'<circle cx="{cx}" cy="{cy - 330}" r="5" fill="#fde047"/>')
    lines.append(f'<line x1="{cx - 10}" y1="{cy - 330}" x2="{cx + 10}" y2="{cy - 330}" stroke="#fde047" stroke-width="1.5"/>')
    lines.append(f'<line x1="{cx}" y1="{cy - 340}" x2="{cx}" y2="{cy - 320}" stroke="#fde047" stroke-width="1.5"/>')
    
    # 2. Bract (Anterior, Bottom)
    bract_y = cy + 345
    lines.append(f'<path d="M {cx - 36} {bract_y} Q {cx} {bract_y - 18} {cx + 36} {bract_y} Q {cx} {bract_y + 16} {cx - 36} {bract_y} Z" fill="url(#epkGrad)" stroke="#16a34a" stroke-width="1.8"/>')
    lines.append(f'<path d="M {cx} {bract_y - 18} L {cx} {bract_y + 16}" stroke="#14532d" stroke-width="1.2"/>')
    
    # 3. Epicalyx (6 Bracteoles)
    epk_r = 280
    n_epk = 6
    epk_angles = [30, 90, 150, 210, 270, 330]
    for ang in epk_angles:
        rad = math.radians(ang)
        px = cx + epk_r * math.cos(rad)
        py = cy + epk_r * math.sin(rad)
        # Tangent angle
        tang = ang + 90
        span = 24
        # Points along circle arc
        a1 = math.radians(ang - span/2)
        a2 = math.radians(ang + span/2)
        x1 = cx + epk_r * math.cos(a1)
        y1 = cy + epk_r * math.sin(a1)
        x2 = cx + epk_r * math.cos(a2)
        y2 = cy + epk_r * math.sin(a2)
        # Pointed outward tip
        tip_r = epk_r + 20
        tx = cx + tip_r * math.cos(rad)
        ty = cy + tip_r * math.sin(rad)
        # Inward curve
        in_r = epk_r - 12
        ix = cx + in_r * math.cos(rad)
        iy = cy + in_r * math.sin(rad)
        
        path_d = f"M {x1:.1f} {y1:.1f} Q {tx:.1f} {ty:.1f} {x2:.1f} {y2:.1f} Q {ix:.1f} {iy:.1f} {x1:.1f} {y1:.1f} Z"
        lines.append(f'<path d="{path_d}" fill="url(#epkGrad)" stroke="#166534" stroke-width="1.8"/>')
        lines.append(f'<line x1="{tx:.1f}" y1="{ty:.1f}" x2="{ix:.1f}" y2="{iy:.1f}" stroke="#14532d" stroke-width="1.2"/>')

    # 4. Calyx (5 Fused Sepals, Valvate Aestivation)
    sep_r = 225
    n_sep = 5
    sep_angles = [-90 + i * 72 for i in range(5)]  # Top sepal at -90 (odd sepal posterior)
    sepal_ends = []
    
    for i, ang in enumerate(sep_angles):
        span = 60
        a1 = math.radians(ang - span/2)
        a2 = math.radians(ang + span/2)
        x1 = cx + sep_r * math.cos(a1)
        y1 = cy + sep_r * math.sin(a1)
        x2 = cx + sep_r * math.cos(a2)
        y2 = cy + sep_r * math.sin(a2)
        sepal_ends.append(((x1, y1), (x2, y2)))
        
        # Outward pointed sepal ridge
        ridge_r = sep_r + 18
        rx = cx + ridge_r * math.cos(math.radians(ang))
        ry = cy + ridge_r * math.sin(math.radians(ang))
        
        # Inward curve
        in_r = sep_r - 10
        ix = cx + in_r * math.cos(math.radians(ang))
        iy = cy + in_r * math.sin(math.radians(ang))
        
        d = f"M {x1:.1f} {y1:.1f} Q {rx:.1f} {ry:.1f} {x2:.1f} {y2:.1f} Q {ix:.1f} {iy:.1f} {x1:.1f} {y1:.1f} Z"
        lines.append(f'<path d="{d}" fill="url(#sepalGrad)" stroke="#14532d" stroke-width="2"/>')
        lines.append(f'<line x1="{rx:.1f}" y1="{ry:.1f}" x2="{ix:.1f}" y2="{iy:.1f}" stroke="#15803d" stroke-width="1.2"/>')
    
    # Connecting brackets representing gamosepalous (fused) condition
    for i in range(5):
        curr_end2 = sepal_ends[i][1]
        next_end1 = sepal_ends[(i + 1) % 5][0]
        # Draw small curved fusion bracket
        mx = (curr_end2[0] + next_end1[0]) / 2
        my = (curr_end2[1] + next_end1[1]) / 2
        lines.append(f'<path d="M {curr_end2[0]:.1f} {curr_end2[1]:.1f} Q {mx*1.01:.1f} {my*1.01:.1f} {next_end1[0]:.1f} {next_end1[1]:.1f}" fill="none" stroke="#22c55e" stroke-width="2.5" stroke-linecap="round"/>')

    # 5. Corolla (5 Free Petals, Twisted / Contorted Aestivation)
    # In twisted aestivation, for each petal, one margin overlaps the previous petal and the other margin is overlapped
    pet_r = 165
    pet_angles = [-54 + i * 72 for i in range(5)]  # alternating with sepals
    
    for ang in pet_angles:
        span = 76
        # Start inside (overlapped margin), sweep out to outer margin
        a_in = math.radians(ang - span/2)
        a_out = math.radians(ang + span/2)
        
        # Overlapped end is at slightly smaller radius
        r_in = pet_r - 12
        r_out = pet_r + 14
        
        p_in_x = cx + r_in * math.cos(a_in)
        p_in_y = cy + r_in * math.sin(a_in)
        
        p_out_x = cx + r_out * math.cos(a_out)
        p_out_y = cy + r_out * math.sin(a_out)
        
        # Center crest of petal
        r_mid = pet_r + 6
        p_mid_x = cx + r_mid * math.cos(math.radians(ang))
        p_mid_y = cy + r_mid * math.sin(math.radians(ang))
        
        # Inner curve
        r_back = pet_r - 18
        p_back_x = cx + r_back * math.cos(math.radians(ang))
        p_back_y = cy + r_back * math.sin(math.radians(ang))
        
        d = f"M {p_in_x:.1f} {p_in_y:.1f} Q {p_mid_x:.1f} {p_mid_y:.1f} {p_out_x:.1f} {p_out_y:.1f} Q {p_back_x:.1f} {p_back_y:.1f} {p_in_x:.1f} {p_in_y:.1f} Z"
        lines.append(f'<path d="{d}" fill="url(#petalGrad)" stroke="#fda4af" stroke-width="2.2" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.5))"/>')

    # 6. Androecium (Staminal Column + Numerous Reniform Monothecous Anthers)
    # Staminal column ring
    tube_r = 108
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="{tube_r}" fill="none" stroke="#fde047" stroke-width="3" opacity="0.8"/>')
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="{tube_r - 5}" fill="none" stroke="#ca8a04" stroke-width="1.2" stroke-dasharray="2 3"/>')
    
    # 20 Kidney-shaped (reniform) anthers radiating from the column
    n_anthers = 20
    for i in range(n_anthers):
        ang = i * (360 / n_anthers)
        rad = math.radians(ang)
        
        # Filament base on tube
        fx1 = cx + tube_r * math.cos(rad)
        fy1 = cy + tube_r * math.sin(rad)
        
        # Filament tip
        fx2 = cx + (tube_r + 14) * math.cos(rad)
        fy2 = cy + (tube_r + 14) * math.sin(rad)
        lines.append(f'<line x1="{fx1:.1f}" y1="{fy1:.1f}" x2="{fx2:.1f}" y2="{fy2:.1f}" stroke="#fde047" stroke-width="1.8"/>')
        
        # Reniform anther (two lobes forming kidney shape)
        ax = fx2
        ay = fy2
        tang = ang + 90
        trad = math.radians(tang)
        
        # Draw kidney shape with bezier
        dx = 7 * math.cos(trad)
        dy = 7 * math.sin(trad)
        nx = 4 * math.cos(rad)
        ny = 4 * math.sin(rad)
        
        p1 = (ax - dx, ay - dy)
        p2 = (ax + dx, ay + dy)
        p_notch = (ax - nx*0.4, ay - ny*0.4)
        p_outer = (ax + nx, ay + ny)
        
        anther_d = f"M {p1[0]:.1f} {p1[1]:.1f} Q {p_outer[0]-dx*0.5:.1f} {p_outer[1]-dy*0.5:.1f} {p_outer[0]:.1f} {p_outer[1]:.1f} Q {p_outer[0]+dx*0.5:.1f} {p_outer[1]+dy*0.5:.1f} {p2[0]:.1f} {p2[1]:.1f} Q {p_notch[0]:.1f} {p_notch[1]:.1f} {p1[0]:.1f} {p1[1]:.1f} Z"
        lines.append(f'<path d="{anther_d}" fill="url(#antherGrad)" stroke="#854d0e" stroke-width="1.2"/>')

    # 7. Gynoecium (Syncarpous, Pentalocular Ovary with Axile Placentation)
    ovary_r = 55
    # Ovary wall
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="{ovary_r}" fill="#0f172a" stroke="#fde047" stroke-width="3"/>')
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="{ovary_r - 4}" fill="#020617" stroke="#22c55e" stroke-width="1.5"/>')
    
    # 5 Locules (septa from center to ovary wall)
    loc_angles = [-90 + i * 72 for i in range(5)]
    for ang in loc_angles:
        rad = math.radians(ang)
        sx = cx + (ovary_r - 4) * math.cos(rad)
        sy = cy + (ovary_r - 4) * math.sin(rad)
        lines.append(f'<line x1="{cx}" y1="{cy}" x2="{sx:.1f}" y2="{sy:.1f}" stroke="#4ade80" stroke-width="2"/>')
    
    # Central axis and 2 ovules per locule on axile placentation
    lines.append(f'<circle cx="{cx}" cy="{cy}" r="10" fill="#15803d" stroke="#fde047" stroke-width="1.5"/>')
    
    for i in range(5):
        mid_ang = loc_angles[i] + 36
        rad = math.radians(mid_ang)
        # Two ovules per locule attached at center
        o_dist = 26
        # Offset angle slightly for pair of ovules
        for offset in [-14, 14]:
            o_ang = math.radians(mid_ang + offset)
            ox = cx + o_dist * math.cos(o_ang)
            oy = cy + o_dist * math.sin(o_ang)
            lines.append(f'<ellipse cx="{ox:.1f}" cy="{oy:.1f}" rx="5.5" ry="3.8" transform="rotate({mid_ang + 90} {ox:.1f} {oy:.1f})" fill="url(#ovaryGrad)" stroke="#92400e" stroke-width="1.2"/>')
            # Funicle
            fx = cx + 8 * math.cos(math.radians(mid_ang))
            fy = cy + 8 * math.sin(math.radians(mid_ang))
            lines.append(f'<line x1="{fx:.1f}" y1="{fy:.1f}" x2="{ox:.1f}" y2="{oy:.1f}" stroke="#ca8a04" stroke-width="1"/>')

    # 8. Clean Botanical Callout Labels with Leader Lines
    def label_leader(lx, ly, tx, ty, title, subtitle="", anchor="left"):
        res = []
        res.append(f'<polyline points="{lx:.1f},{ly:.1f} {tx:.1f},{ty:.1f} {tx + (40 if anchor=="left" else -40):.1f},{ty:.1f}" fill="none" stroke="#fde047" stroke-width="1.4" stroke-dasharray="3 2" opacity="0.85"/>')
        res.append(f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="3.5" fill="#fde047"/>')
        x_text = tx + (45 if anchor=="left" else -45)
        text_anchor = "start" if anchor=="left" else "end"
        res.append(f'<text x="{x_text:.1f}" y="{ty - 4:.1f}" font-size="12" font-weight="700" fill="#ffffff" text-anchor="{text_anchor}">{title}</text>')
        if subtitle:
            res.append(f'<text x="{x_text:.1f}" y="{ty + 11:.1f}" font-size="10.5" fill="#cbd5e1" text-anchor="{text_anchor}">{subtitle}</text>')
        return "\n".join(res)

    # Label 1: Mother Axis
    lines.append(label_leader(cx + 14, cy - 330, cx + 110, cy - 330, "Mother Axis", "Posterior position indicator", "left"))
    
    # Label 2: Epicalyx
    epk_sample_x = cx + epk_r * math.cos(math.radians(30))
    epk_sample_y = cy + epk_r * math.sin(math.radians(30))
    lines.append(label_leader(epk_sample_x + 10, epk_sample_y, cx + 290, cy - 140, "Epicalyx (Epk)", "5–8 green free bracteoles", "left"))
    
    # Label 3: Calyx
    cal_sample_x = cx + sep_r * math.cos(math.radians(54))
    cal_sample_y = cy + sep_r * math.sin(math.radians(54))
    lines.append(label_leader(cal_sample_x, cal_sample_y, cx + 290, cy + 50, "Calyx: K(5)", "5 fused sepals, valvate", "left"))

    # Label 4: Corolla
    pet_sample_x = cx + pet_r * math.cos(math.radians(18))
    pet_sample_y = cy + pet_r * math.sin(math.radians(18))
    lines.append(label_leader(pet_sample_x, pet_sample_y, cx + 290, cy + 180, "Corolla: C5", "5 free petals, contorted/twisted", "left"))

    # Label 5: Androecium (Left side)
    ant_sample_x = cx + (tube_r + 14) * math.cos(math.radians(198))
    ant_sample_y = cy + (tube_r + 14) * math.sin(math.radians(198))
    lines.append(label_leader(ant_sample_x, ant_sample_y, cx - 290, cy - 50, "Androecium: A(∞)", "Monadelphous staminal tube", "right"))

    # Label 6: Reniform Anther (Left side)
    lines.append(label_leader(cx - tube_r - 10, cy + 30, cx - 290, cy + 80, "Monothecous Anther", "Reniform (kidney-shaped)", "right"))

    # Label 7: Gynoecium (Left side)
    lines.append(label_leader(cx - ovary_r + 15, cy - 15, cx - 290, cy + 200, "Gynoecium: G(5)", "5 fused carpels, pentalocular", "right"))

    # Label 8: Axile Placentation (Left side)
    lines.append(label_leader(cx - 20, cy + 20, cx - 290, cy + 270, "Axile Placentation", "2 ovules per locule at axis", "right"))

    # Label 9: Bract (Bottom)
    lines.append(label_leader(cx + 36, bract_y, cx + 180, bract_y + 10, "Bract", "Anterior floral position", "left"))

    # Bottom Legend / Summary Card
    lines.append('<g transform="translate(450, 840)" text-anchor="middle">')
    lines.append('  <rect x="-380" y="-18" width="760" height="42" rx="12" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>')
    lines.append('  <text y="7" font-size="12" fill="#e2e8f0"><tspan fill="#4ade80" font-weight="700">Epk:</tspan> 5-8 free &bull; <tspan fill="#22c55e" font-weight="700">K:</tspan> (5) fused valvate &bull; <tspan fill="#f43f5e" font-weight="700">C:</tspan> 5 contorted &bull; <tspan fill="#fde047" font-weight="700">A:</tspan> (&#8734;) monadelphous &bull; <tspan fill="#f59e0b" font-weight="700">G:</tspan> (5) superior 5-locular</text>')
    lines.append('</g>')

    lines.append('</svg>')
    return "\n".join(lines)

svg_content = create_hibiscus_svg()
dst_path = os.path.join("static", "diagrams", "hibiscus_floral_diagram.svg")
with open(dst_path, "w", encoding="utf-8") as f:
    f.write(svg_content)
print(f"Generated {dst_path} ({len(svg_content)} bytes)")


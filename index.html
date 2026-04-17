<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FitLife App</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;600;700&display=swap');

  :root {
    --yellow: #E8FF47;
    --yellow-soft: #F2FF8A;
    --yellow-dark: #C8E000;
    --green: #1A3A2A;
    --green-mid: #2D5A3D;
    --green-light: #3D7A52;
    --green-accent: #4CAF6F;
    --white: #FAFFF5;
    --gray: #8A9E8F;
    --gray-light: #E8EDE9;
    --red: #FF4444;
    --radius: 16px;
    --radius-sm: 10px;
    --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    font-family: 'DM Sans', sans-serif;
    background: #0F1F15;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    padding: 20px;
  }

  .phone-frame {
    width: 390px;
    height: 844px;
    background: var(--green);
    border-radius: 48px;
    overflow: hidden;
    position: relative;
    box-shadow: 0 40px 120px rgba(0,0,0,0.6), inset 0 0 0 2px rgba(255,255,255,0.08);
  }

  .screen {
    width: 100%;
    height: 100%;
    overflow-y: auto;
    overflow-x: hidden;
    scrollbar-width: none;
    position: absolute;
    top: 0; left: 0;
    display: none;
    flex-direction: column;
    background: var(--green);
  }
  .screen::-webkit-scrollbar { display: none; }
  .screen.active { display: flex; }

  /* ─── STATUS BAR ─── */
  .status-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 14px 28px 0;
    font-size: 13px;
    font-weight: 600;
    color: var(--white);
    flex-shrink: 0;
  }
  .status-icons { display: flex; gap: 6px; align-items: center; }

  /* ─── SPLASH / ONBOARDING ─── */
  #screen-splash {
    background: var(--green);
    justify-content: center;
    align-items: center;
    gap: 24px;
  }
  .splash-logo {
    width: 80px; height: 80px;
    background: var(--yellow);
    border-radius: 24px;
    display: flex; align-items: center; justify-content: center;
    font-size: 36px;
    animation: pulse 2s infinite;
  }
  @keyframes pulse {
    0%,100% { transform: scale(1); }
    50% { transform: scale(1.05); }
  }
  .splash-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 42px; font-weight: 700;
    color: var(--white); letter-spacing: -1px;
  }
  .splash-title span { color: var(--yellow); }
  .splash-sub { color: var(--gray); font-size: 16px; }

  /* ─── AUTH ─── */
  #screen-auth {
    padding: 0;
  }
  .auth-hero {
    background: linear-gradient(170deg, var(--green-mid) 0%, var(--green) 60%);
    padding: 60px 28px 40px;
    position: relative;
    overflow: hidden;
  }
  .auth-hero::before {
    content: '';
    position: absolute; top: -40px; right: -40px;
    width: 200px; height: 200px;
    background: var(--yellow);
    border-radius: 50%;
    opacity: 0.08;
  }
  .auth-hero-tag {
    display: inline-block;
    background: rgba(232,255,71,0.15);
    border: 1px solid rgba(232,255,71,0.3);
    color: var(--yellow);
    font-size: 12px; font-weight: 600;
    padding: 4px 12px; border-radius: 20px;
    margin-bottom: 16px; letter-spacing: 1px; text-transform: uppercase;
  }
  .auth-hero h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 36px; font-weight: 700;
    color: var(--white); line-height: 1.1;
    margin-bottom: 10px;
  }
  .auth-hero h1 em { color: var(--yellow); font-style: normal; }
  .auth-hero p { color: var(--gray); font-size: 15px; }
  .auth-body { padding: 32px 28px; flex: 1; }
  .auth-tabs {
    display: flex; background: rgba(255,255,255,0.05);
    border-radius: var(--radius-sm); padding: 4px; margin-bottom: 28px;
  }
  .auth-tab {
    flex: 1; padding: 10px; text-align: center;
    font-size: 14px; font-weight: 600;
    color: var(--gray); border-radius: 8px;
    cursor: pointer; transition: var(--transition);
  }
  .auth-tab.active { background: var(--yellow); color: var(--green); }

  .form-group { margin-bottom: 16px; }
  .form-label { font-size: 12px; font-weight: 600; color: var(--gray); letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 8px; display: block; }
  .form-input {
    width: 100%; padding: 14px 16px;
    background: rgba(255,255,255,0.06);
    border: 1.5px solid rgba(255,255,255,0.1);
    border-radius: var(--radius-sm); color: var(--white);
    font-size: 15px; font-family: 'DM Sans', sans-serif;
    transition: var(--transition); outline: none;
  }
  .form-input:focus { border-color: var(--yellow); background: rgba(232,255,71,0.04); }
  .form-input::placeholder { color: var(--gray); }

  /* ─── BUTTONS ─── */
  .btn-primary {
    width: 100%; padding: 16px;
    background: var(--yellow); color: var(--green);
    border: none; border-radius: var(--radius-sm);
    font-size: 16px; font-weight: 700;
    font-family: 'DM Sans', sans-serif;
    cursor: pointer; transition: var(--transition);
    letter-spacing: -0.3px;
  }
  .btn-primary:hover { background: var(--yellow-soft); transform: translateY(-1px); }
  .btn-primary:active { transform: translateY(0); }

  .btn-secondary {
    width: 100%; padding: 14px;
    background: transparent; color: var(--white);
    border: 1.5px solid rgba(255,255,255,0.2);
    border-radius: var(--radius-sm);
    font-size: 15px; font-weight: 600;
    font-family: 'DM Sans', sans-serif;
    cursor: pointer; transition: var(--transition);
    margin-top: 12px;
  }
  .btn-secondary:hover { border-color: var(--yellow); color: var(--yellow); }

  .btn-icon {
    background: none; border: none; cursor: pointer;
    color: var(--white); font-size: 20px;
    padding: 8px; border-radius: 8px;
    transition: var(--transition);
    display: flex; align-items: center; justify-content: center;
  }
  .btn-icon:hover { background: rgba(255,255,255,0.1); }

  /* ─── TOP NAV ─── */
  .top-nav {
    display: flex; align-items: center; justify-content: space-between;
    padding: 14px 24px 0; flex-shrink: 0;
  }
  .top-nav-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 20px; font-weight: 700; color: var(--white);
  }
  .back-btn {
    width: 36px; height: 36px;
    background: rgba(255,255,255,0.08);
    border-radius: 10px; display: flex; align-items: center; justify-content: center;
    cursor: pointer; border: none; color: var(--white); font-size: 18px;
    transition: var(--transition);
  }
  .back-btn:hover { background: rgba(255,255,255,0.15); }

  /* ─── HOME ─── */
  #screen-home {
    padding-bottom: 90px;
  }
  .home-header {
    padding: 20px 24px 24px;
    background: linear-gradient(180deg, var(--green-mid) 0%, var(--green) 100%);
    position: relative; overflow: hidden;
  }
  .home-header::after {
    content: ''; position: absolute;
    bottom: -30px; right: -20px;
    width: 120px; height: 120px;
    background: var(--yellow); opacity: 0.06;
    border-radius: 50%;
  }
  .home-greeting { color: var(--gray); font-size: 14px; margin-bottom: 4px; }
  .home-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 26px; font-weight: 700; color: var(--white);
    margin-bottom: 20px;
  }
  .home-name span { color: var(--yellow); }

  .home-card {
    background: linear-gradient(135deg, var(--yellow) 0%, var(--yellow-dark) 100%);
    border-radius: var(--radius); padding: 20px;
    display: flex; justify-content: space-between; align-items: center;
  }
  .home-card-label { font-size: 12px; font-weight: 600; color: var(--green); opacity: 0.7; text-transform: uppercase; letter-spacing: 0.5px; }
  .home-card-value { font-family: 'Space Grotesk', sans-serif; font-size: 32px; font-weight: 700; color: var(--green); }
  .home-card-sub { font-size: 13px; color: var(--green); opacity: 0.6; }
  .home-card-icon { font-size: 40px; }

  .section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 18px; font-weight: 700; color: var(--white);
    padding: 24px 24px 12px;
  }

  .menu-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; padding: 0 24px; }
  .menu-card {
    background: rgba(255,255,255,0.05);
    border: 1.5px solid rgba(255,255,255,0.08);
    border-radius: var(--radius); padding: 20px;
    cursor: pointer; transition: var(--transition);
    position: relative; overflow: hidden;
  }
  .menu-card:hover { border-color: var(--yellow); transform: translateY(-2px); background: rgba(232,255,71,0.05); }
  .menu-card-icon { font-size: 28px; margin-bottom: 10px; }
  .menu-card-title { font-size: 14px; font-weight: 700; color: var(--white); margin-bottom: 4px; }
  .menu-card-sub { font-size: 12px; color: var(--gray); }
  .menu-card-arrow {
    position: absolute; bottom: 16px; right: 16px;
    width: 24px; height: 24px; background: var(--yellow);
    border-radius: 6px; display: flex; align-items: center; justify-content: center;
    font-size: 12px;
  }

  /* ─── BOTTOM NAV ─── */
  .bottom-nav {
    position: absolute; bottom: 0; left: 0; right: 0;
    background: rgba(26, 58, 42, 0.95);
    backdrop-filter: blur(20px);
    border-top: 1px solid rgba(255,255,255,0.08);
    display: flex; padding: 12px 0 24px;
  }
  .nav-item {
    flex: 1; display: flex; flex-direction: column;
    align-items: center; gap: 4px;
    cursor: pointer; transition: var(--transition);
  }
  .nav-icon { font-size: 22px; }
  .nav-label { font-size: 10px; font-weight: 600; color: var(--gray); letter-spacing: 0.3px; }
  .nav-item.active .nav-label { color: var(--yellow); }
  .nav-item.active .nav-icon { filter: drop-shadow(0 0 8px rgba(232,255,71,0.6)); }

  /* ─── PLAN NUTRICIONAL ─── */
  .screen-content { padding: 20px 24px; flex: 1; overflow-y: auto; }

  .objective-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 8px; }
  .objective-card {
    background: rgba(255,255,255,0.05);
    border: 1.5px solid rgba(255,255,255,0.1);
    border-radius: var(--radius-sm); padding: 16px;
    cursor: pointer; transition: var(--transition); text-align: center;
  }
  .objective-card:hover, .objective-card.selected {
    border-color: var(--yellow); background: rgba(232,255,71,0.08);
  }
  .objective-card .obj-icon { font-size: 28px; margin-bottom: 8px; }
  .objective-card .obj-label { font-size: 13px; font-weight: 600; color: var(--white); }

  .diet-card {
    background: rgba(255,255,255,0.05);
    border: 1.5px solid rgba(255,255,255,0.08);
    border-radius: var(--radius); padding: 20px; margin-bottom: 12px;
    cursor: pointer; transition: var(--transition);
  }
  .diet-card:hover { border-color: rgba(232,255,71,0.4); }
  .diet-card-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; }
  .diet-name { font-size: 16px; font-weight: 700; color: var(--white); }
  .diet-cal { background: var(--yellow); color: var(--green); font-size: 12px; font-weight: 700; padding: 3px 10px; border-radius: 20px; }
  .diet-desc { font-size: 13px; color: var(--gray); line-height: 1.5; margin-bottom: 12px; }
  .diet-macros { display: flex; gap: 12px; }
  .macro { text-align: center; }
  .macro-val { font-size: 16px; font-weight: 700; color: var(--yellow); }
  .macro-label { font-size: 10px; color: var(--gray); }

  /* ─── VIDA PUNTOS ─── */
  .points-hero {
    margin: 0 24px 20px;
    background: linear-gradient(135deg, var(--green-mid), var(--green-light));
    border-radius: var(--radius); padding: 24px;
    text-align: center; border: 1px solid rgba(232,255,71,0.2);
  }
  .points-label { color: var(--gray); font-size: 13px; margin-bottom: 8px; }
  .points-value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 52px; font-weight: 700; color: var(--yellow);
    line-height: 1;
  }
  .points-sub { color: var(--gray); font-size: 13px; margin-top: 8px; }

  .benefit-card {
    background: rgba(255,255,255,0.05);
    border: 1.5px solid rgba(255,255,255,0.08);
    border-radius: var(--radius); padding: 16px; margin-bottom: 10px;
    display: flex; align-items: center; gap: 16px;
    cursor: pointer; transition: var(--transition);
  }
  .benefit-card:hover { border-color: rgba(232,255,71,0.4); background: rgba(232,255,71,0.04); }
  .benefit-icon-wrap {
    width: 48px; height: 48px; background: rgba(232,255,71,0.1);
    border-radius: 12px; display: flex; align-items: center; justify-content: center;
    font-size: 22px; flex-shrink: 0;
  }
  .benefit-info { flex: 1; }
  .benefit-name { font-size: 15px; font-weight: 600; color: var(--white); margin-bottom: 4px; }
  .benefit-desc { font-size: 12px; color: var(--gray); }
  .benefit-cost { font-size: 14px; font-weight: 700; color: var(--yellow); }

  /* ─── CLASES VIRTUALES ─── */
  .filter-row { display: flex; gap: 8px; overflow-x: auto; padding-bottom: 4px; margin-bottom: 16px; scrollbar-width: none; }
  .filter-row::-webkit-scrollbar { display: none; }
  .filter-chip {
    padding: 8px 16px; border-radius: 20px;
    font-size: 13px; font-weight: 600; white-space: nowrap;
    cursor: pointer; transition: var(--transition); border: none;
    background: rgba(255,255,255,0.07); color: var(--gray);
  }
  .filter-chip.active { background: var(--yellow); color: var(--green); }

  .class-card {
    background: rgba(255,255,255,0.05);
    border: 1.5px solid rgba(255,255,255,0.08);
    border-radius: var(--radius); overflow: hidden; margin-bottom: 12px;
    cursor: pointer; transition: var(--transition);
  }
  .class-card:hover { border-color: rgba(232,255,71,0.4); transform: translateY(-2px); }
  .class-thumb {
    height: 100px; display: flex; align-items: center; justify-content: center;
    font-size: 48px; position: relative;
  }
  .class-badge {
    position: absolute; top: 10px; right: 10px;
    background: var(--yellow); color: var(--green);
    font-size: 10px; font-weight: 700; padding: 3px 8px; border-radius: 20px;
    text-transform: uppercase; letter-spacing: 0.5px;
  }
  .class-body { padding: 14px; }
  .class-name { font-size: 15px; font-weight: 700; color: var(--white); margin-bottom: 6px; }
  .class-meta { display: flex; gap: 12px; }
  .class-meta-item { font-size: 12px; color: var(--gray); display: flex; align-items: center; gap: 4px; }

  /* ─── QR SCREEN ─── */
  .qr-container {
    display: flex; flex-direction: column; align-items: center;
    padding: 24px; gap: 20px;
  }
  .qr-box {
    width: 200px; height: 200px;
    background: var(--white); border-radius: 20px;
    padding: 16px; display: flex; align-items: center; justify-content: center;
    box-shadow: 0 20px 60px rgba(0,0,0,0.4);
  }
  .qr-inner {
    width: 168px; height: 168px;
    background: repeating-conic-gradient(var(--green) 0% 25%, var(--white) 0% 50%) 0 0/16px 16px;
    border-radius: 8px;
  }
  .qr-timer {
    background: rgba(232,255,71,0.1); border: 1px solid rgba(232,255,71,0.3);
    border-radius: 30px; padding: 10px 24px;
    font-size: 14px; font-weight: 600; color: var(--yellow);
    display: flex; align-items: center; gap: 8px;
  }
  .qr-timer-dot {
    width: 8px; height: 8px; background: var(--yellow);
    border-radius: 50%; animation: blink 1s infinite;
  }
  @keyframes blink { 0%,100% { opacity:1; } 50% { opacity:0; } }

  /* ─── SEDES ─── */
  .sede-card {
    background: rgba(255,255,255,0.05);
    border: 1.5px solid rgba(255,255,255,0.08);
    border-radius: var(--radius); padding: 18px; margin-bottom: 10px;
    cursor: pointer; transition: var(--transition);
  }
  .sede-card:hover { border-color: rgba(232,255,71,0.4); }
  .sede-card-top { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px; }
  .sede-name { font-size: 16px; font-weight: 700; color: var(--white); }
  .sede-open { font-size: 11px; font-weight: 700; padding: 3px 10px; border-radius: 20px; }
  .sede-open.open { background: rgba(76,175,111,0.2); color: var(--green-accent); }
  .sede-open.closed { background: rgba(255,68,68,0.15); color: #FF6B6B; }
  .sede-address { font-size: 13px; color: var(--gray); margin-bottom: 12px; }
  .sede-info-row { display: flex; gap: 16px; }
  .sede-info-item { font-size: 12px; color: var(--gray); display: flex; align-items: center; gap: 4px; }

  /* ─── RESERVAS ─── */
  .reserva-card {
    background: rgba(255,255,255,0.05);
    border: 1.5px solid rgba(255,255,255,0.08);
    border-radius: var(--radius); padding: 18px; margin-bottom: 10px;
    transition: var(--transition);
  }
  .reserva-card-top { display: flex; justify-content: space-between; margin-bottom: 8px; }
  .reserva-machine { font-size: 15px; font-weight: 700; color: var(--white); }
  .reserva-status { font-size: 11px; font-weight: 700; padding: 3px 10px; border-radius: 20px; background: rgba(76,175,111,0.2); color: var(--green-accent); }
  .reserva-meta { font-size: 13px; color: var(--gray); }
  .reserva-actions { display: flex; gap: 8px; margin-top: 12px; }
  .btn-sm {
    padding: 8px 16px; border-radius: 8px; font-size: 13px; font-weight: 600;
    cursor: pointer; transition: var(--transition); border: none;
    font-family: 'DM Sans', sans-serif;
  }
  .btn-sm-outline { background: transparent; border: 1.5px solid rgba(255,255,255,0.15); color: var(--white); }
  .btn-sm-danger { background: rgba(255,68,68,0.15); color: #FF6B6B; }

  /* ─── RUTINAS ─── */
  .routine-card {
    background: rgba(255,255,255,0.05);
    border: 1.5px solid rgba(255,255,255,0.08);
    border-radius: var(--radius); padding: 18px; margin-bottom: 10px;
    cursor: pointer; transition: var(--transition);
  }
  .routine-card:hover { border-color: rgba(232,255,71,0.4); }
  .routine-name { font-size: 16px; font-weight: 700; color: var(--white); margin-bottom: 6px; }
  .routine-obj { display: inline-block; background: rgba(232,255,71,0.1); color: var(--yellow); font-size: 11px; font-weight: 600; padding: 3px 10px; border-radius: 20px; margin-bottom: 10px; }
  .routine-exercises { font-size: 13px; color: var(--gray); }

  /* ─── PLAN SUSCRIPCION ─── */
  .plan-card {
    background: rgba(255,255,255,0.05);
    border: 2px solid rgba(255,255,255,0.1);
    border-radius: var(--radius); padding: 20px; margin-bottom: 12px;
    cursor: pointer; transition: var(--transition); position: relative;
  }
  .plan-card.featured { border-color: var(--yellow); background: rgba(232,255,71,0.06); }
  .plan-badge-featured {
    position: absolute; top: -10px; left: 50%; transform: translateX(-50%);
    background: var(--yellow); color: var(--green);
    font-size: 11px; font-weight: 700; padding: 3px 14px; border-radius: 20px;
    white-space: nowrap;
  }
  .plan-name { font-size: 18px; font-weight: 700; color: var(--white); margin-bottom: 4px; }
  .plan-price { font-family: 'Space Grotesk', sans-serif; font-size: 36px; font-weight: 700; color: var(--yellow); margin-bottom: 12px; }
  .plan-price span { font-size: 16px; color: var(--gray); }
  .plan-features { list-style: none; }
  .plan-features li { font-size: 13px; color: var(--gray); padding: 4px 0; display: flex; align-items: center; gap: 8px; }
  .plan-features li::before { content: '✓'; color: var(--green-accent); font-weight: 700; }

  /* ─── MODAL ─── */
  .modal-overlay {
    display: none; position: absolute; inset: 0;
    background: rgba(0,0,0,0.7); backdrop-filter: blur(4px);
    z-index: 100; align-items: flex-end;
  }
  .modal-overlay.open { display: flex; }
  .modal-sheet {
    width: 100%; background: var(--green-mid);
    border-radius: 24px 24px 0 0; padding: 24px;
    animation: slideUp 0.3s ease;
  }
  @keyframes slideUp { from { transform: translateY(100%); } to { transform: translateY(0); } }
  .modal-handle {
    width: 40px; height: 4px; background: rgba(255,255,255,0.2);
    border-radius: 2px; margin: 0 auto 20px;
  }
  .modal-title { font-family: 'Space Grotesk', sans-serif; font-size: 22px; font-weight: 700; color: var(--white); margin-bottom: 8px; }
  .modal-sub { font-size: 14px; color: var(--gray); margin-bottom: 24px; }

  /* ─── NOTIFICATION / ALERT ─── */
  .alert {
    display: none; position: absolute; top: 60px; left: 20px; right: 20px;
    padding: 14px 18px; border-radius: var(--radius-sm);
    font-size: 14px; font-weight: 600; z-index: 200;
    animation: slideDown 0.3s ease;
  }
  .alert.show { display: flex; align-items: center; gap: 10px; }
  .alert.success { background: rgba(76,175,111,0.9); color: white; }
  .alert.error { background: rgba(255,68,68,0.9); color: white; }
  @keyframes slideDown { from { transform: translateY(-20px); opacity:0; } to { transform: translateY(0); opacity:1; } }

  /* ─── SELECTOR HORARIO ─── */
  .horario-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 8px; margin-bottom: 20px; }
  .horario-chip {
    padding: 10px; text-align: center; border-radius: var(--radius-sm);
    background: rgba(255,255,255,0.06); border: 1.5px solid rgba(255,255,255,0.1);
    font-size: 13px; font-weight: 600; color: var(--white);
    cursor: pointer; transition: var(--transition);
  }
  .horario-chip.selected { background: var(--yellow); color: var(--green); border-color: var(--yellow); }
  .horario-chip.unavailable { opacity: 0.3; cursor: not-allowed; }

  /* ─── DIVIDER ─── */
  .divider { height: 1px; background: rgba(255,255,255,0.08); margin: 20px 0; }

  .text-center { text-align: center; }
  .text-yellow { color: var(--yellow); }
  .mt-16 { margin-top: 16px; }
  .mb-16 { margin-bottom: 16px; }
  .gap-info { font-size: 13px; color: var(--gray); text-align: center; margin-top: 12px; }
</style>
</head>
<body>
<div class="phone-frame">

  <!-- ALERT -->
  <div class="alert" id="global-alert"></div>

  <!-- MODAL -->
  <div class="modal-overlay" id="modal-overlay">
    <div class="modal-sheet" id="modal-content">
      <div class="modal-handle"></div>
      <div id="modal-body"></div>
    </div>
  </div>

  <!-- ═══════════════════════════════ SPLASH ═══════════════════════════════ -->
  <div class="screen active" id="screen-splash">
    <div class="status-bar"><span>9:41</span><div class="status-icons">▲ ● ▮▮▮</div></div>
    <div class="splash-logo">🏋️</div>
    <div class="splash-title">Fit<span>Life</span></div>
    <div class="splash-sub">Tu gimnasio, en tu bolsillo</div>
    <div style="padding: 0 28px; width:100%; margin-top:20px;">
      <button class="btn-primary" onclick="goto('auth')">Comenzar</button>
    </div>
  </div>

  <!-- ═══════════════════════════════ AUTH ═══════════════════════════════ -->
  <div class="screen" id="screen-auth">
    <div class="auth-hero">
      <div class="status-bar" style="padding:0 0 16px;"><span>9:41</span><div class="status-icons">▲ ● ▮▮▮</div></div>
      <div class="auth-hero-tag">Bienvenido</div>
      <h1>Entrena más<br><em>inteligente</em></h1>
      <p>Tu app de gimnasio todo en uno</p>
    </div>
    <div class="auth-body">
      <div class="auth-tabs">
        <div class="auth-tab active" id="tab-login" onclick="switchAuthTab('login')">Iniciar Sesión</div>
        <div class="auth-tab" id="tab-register" onclick="switchAuthTab('register')">Registrarse</div>
      </div>

      <!-- LOGIN -->
      <div id="form-login">
        <div class="form-group">
          <label class="form-label">Email</label>
          <input class="form-input" type="email" placeholder="tucorreo@gmail.com" id="login-email">
        </div>
        <div class="form-group">
          <label class="form-label">Contraseña</label>
          <input class="form-input" type="password" placeholder="••••••••" id="login-pass">
        </div>
        <div style="margin-top:8px;">
          <button class="btn-primary" onclick="doLogin()">Iniciar Sesión</button>
          <p class="gap-info">¿No tenés cuenta? <span class="text-yellow" style="cursor:pointer;" onclick="switchAuthTab('register')">Registrate</span></p>
        </div>
      </div>

      <!-- REGISTER -->
      <div id="form-register" style="display:none;">
        <div class="form-group">
          <label class="form-label">Nombre completo</label>
          <input class="form-input" type="text" placeholder="Juan García" id="reg-name">
        </div>
        <div class="form-group">
          <label class="form-label">Email</label>
          <input class="form-input" type="email" placeholder="tucorreo@gmail.com" id="reg-email">
        </div>
        <div class="form-group">
          <label class="form-label">Contraseña</label>
          <input class="form-input" type="password" placeholder="••••••••" id="reg-pass">
        </div>
        <button class="btn-primary" onclick="doRegister()">Crear cuenta</button>
        <p class="gap-info mt-16">Al registrarte aceptás los <span class="text-yellow">Términos y Condiciones</span></p>
      </div>
    </div>
  </div>

  <!-- ═══════════════════════════════ PLAN SUSCRIPCION ═══════════════════════════════ -->
  <div class="screen" id="screen-subscription">
    <div class="status-bar"><span>9:41</span><div class="status-icons">▲ ● ▮▮▮</div></div>
    <div class="top-nav">
      <div class="top-nav-title">Elegí tu plan</div>
    </div>
    <div class="screen-content">
      <p style="color:var(--gray); font-size:14px; margin-bottom:24px;">Seleccioná el plan que mejor se adapte a tus objetivos</p>

      <div class="plan-card" onclick="selectPlan('Básico')">
        <div class="plan-name">Básico</div>
        <div class="plan-price">$8.999 <span>/mes</span></div>
        <ul class="plan-features">
          <li>Acceso a 1 sede</li>
          <li>Clases virtuales ilimitadas</li>
          <li>Plan de rutinas básico</li>
        </ul>
      </div>

      <div class="plan-card featured" onclick="selectPlan('Premium')">
        <div class="plan-badge-featured">⭐ Más popular</div>
        <div class="plan-name">Premium</div>
        <div class="plan-price">$14.999 <span>/mes</span></div>
        <ul class="plan-features">
          <li>Acceso a todas las sedes</li>
          <li>Clases virtuales ilimitadas</li>
          <li>Plan nutricional personalizado</li>
          <li>Sistema Vida Puntos</li>
          <li>Reserva de máquinas</li>
        </ul>
      </div>

      <div class="plan-card" onclick="selectPlan('Elite')">
        <div class="plan-name">Elite</div>
        <div class="plan-price">$24.999 <span>/mes</span></div>
        <ul class="plan-features">
          <li>Todo lo del plan Premium</li>
          <li>Entrenador personal virtual</li>
          <li>Doble de puntos Vida</li>
          <li>Clases presenciales incluidas</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- ═══════════════════════════════ HOME ═══════════════════════════════ -->
  <div class="screen" id="screen-home">
    <div class="status-bar" style="padding:14px 28px 0; flex-shrink:0;"><span>9:41</span><div class="status-icons">▲ ● ▮▮▮</div></div>
    <div class="home-header">
      <div class="home-greeting">Buenos días 👋</div>
      <div class="home-name" id="home-username">Santiago <span>Estevez</span></div>
      <div class="home-card">
        <div>
          <div class="home-card-label">Vida Puntos</div>
          <div class="home-card-value">2.450</div>
          <div class="home-card-sub">Plan Premium activo</div>
        </div>
        <div class="home-card-icon">⚡</div>
      </div>
    </div>

    <div class="section-title">¿Qué querés hacer?</div>
    <div class="menu-grid">
      <div class="menu-card" onclick="goto('qr')">
        <div class="menu-card-icon">📱</div>
        <div class="menu-card-title">QR de Acceso</div>
        <div class="menu-card-sub">Entrá a tu sede</div>
        <div class="menu-card-arrow">→</div>
      </div>
      <div class="menu-card" onclick="goto('nutrition')">
        <div class="menu-card-icon">🥗</div>
        <div class="menu-card-title">Nutrición</div>
        <div class="menu-card-sub">Plan personalizado</div>
        <div class="menu-card-arrow">→</div>
      </div>
      <div class="menu-card" onclick="goto('classes')">
        <div class="menu-card-icon">🎥</div>
        <div class="menu-card-title">Clases</div>
        <div class="menu-card-sub">Virtuales y presenciales</div>
        <div class="menu-card-arrow">→</div>
      </div>
      <div class="menu-card" onclick="goto('points')">
        <div class="menu-card-icon">🎁</div>
        <div class="menu-card-title">Vida Puntos</div>
        <div class="menu-card-sub">Canjea beneficios</div>
        <div class="menu-card-arrow">→</div>
      </div>
      <div class="menu-card" onclick="goto('sedes')">
        <div class="menu-card-icon">📍</div>
        <div class="menu-card-title">Sedes</div>
        <div class="menu-card-sub">Encontrá tu gimnasio</div>
        <div class="menu-card-arrow">→</div>
      </div>
      <div class="menu-card" onclick="goto('reservas')">
        <div class="menu-card-icon">📅</div>
        <div class="menu-card-title">Reservas</div>
        <div class="menu-card-sub">Máquinas y horarios</div>
        <div class="menu-card-arrow">→</div>
      </div>
    </div>

    <div class="section-title">Rutinas de hoy</div>
    <div style="padding: 0 24px 24px;">
      <div class="routine-card" onclick="goto('routines')">
        <div class="routine-name">Fuerza — Tren Superior</div>
        <div class="routine-obj">Ganar músculo</div>
        <div class="routine-exercises">8 ejercicios · 45 min · Intermedio</div>
      </div>
    </div>

    <div class="bottom-nav">
      <div class="nav-item active" onclick="goto('home')">
        <span class="nav-icon">🏠</span><span class="nav-label">Inicio</span>
      </div>
      <div class="nav-item" onclick="goto('classes')">
        <span class="nav-icon">🎥</span><span class="nav-label">Clases</span>
      </div>
      <div class="nav-item" onclick="goto('qr')">
        <span class="nav-icon">📱</span><span class="nav-label">QR</span>
      </div>
      <div class="nav-item" onclick="goto('sedes')">
        <span class="nav-icon">📍</span><span class="nav-label">Sedes</span>
      </div>
      <div class="nav-item" onclick="goto('points')">
        <span class="nav-icon">⚡</span><span class="nav-label">Puntos</span>
      </div>
    </div>
  </div>

  <!-- ═══════════════════════════════ QR ═══════════════════════════════ -->
  <div class="screen" id="screen-qr">
    <div class="status-bar"><span>9:41</span><div class="status-icons">▲ ● ▮▮▮</div></div>
    <div class="top-nav">
      <button class="back-btn" onclick="goto('home')">←</button>
      <div class="top-nav-title">QR de Acceso</div>
      <div style="width:36px;"></div>
    </div>
    <div class="qr-container" style="flex:1; justify-content:center;">
      <p style="color:var(--gray); font-size:14px; text-align:center;">Mostrá este código en la entrada de tu sede</p>
      <div style="text-align:center;">
        <div id="qr-state-verify">
          <p style="color:var(--white); margin-bottom:20px; font-size:15px;">Se requiere verificación biométrica</p>
          <div style="font-size:80px; margin-bottom:20px;">👆</div>
          <button class="btn-primary" onclick="startBiometric()" style="width:220px;">Verificar huella digital</button>
        </div>
        <div id="qr-state-show" style="display:none;">
          <div class="qr-box" style="margin: 0 auto 20px;">
            <div class="qr-inner"></div>
          </div>
          <div class="qr-timer" style="margin: 0 auto; width:fit-content;">
            <div class="qr-timer-dot"></div>
            <span>Válido por <span id="qr-countdown">5:00</span></span>
          </div>
          <p style="color:var(--gray); font-size:12px; margin-top:12px;">Presentá este QR en el lector de acceso</p>
        </div>
      </div>
    </div>
  </div>

  <!-- ═══════════════════════════════ NUTRICION ═══════════════════════════════ -->
  <div class="screen" id="screen-nutrition">
    <div class="status-bar"><span>9:41</span><div class="status-icons">▲ ● ▮▮▮</div></div>
    <div class="top-nav">
      <button class="back-btn" onclick="goto('home')">←</button>
      <div class="top-nav-title">Plan Nutricional</div>
      <div style="width:36px;"></div>
    </div>
    <div class="screen-content">
      <p style="color:var(--gray); font-size:14px; margin-bottom:20px;">Elegí tu objetivo y te mostramos el plan ideal</p>

      <div class="section-title" style="padding:0 0 12px;">¿Cuál es tu objetivo?</div>
      <div class="objective-grid">
        <div class="objective-card" onclick="selectObjective(this, 'deficit')">
          <div class="obj-icon">🔥</div>
          <div class="obj-label">Perder peso</div>
        </div>
        <div class="objective-card" onclick="selectObjective(this, 'mantenimiento')">
          <div class="obj-icon">⚖️</div>
          <div class="obj-label">Mantenerme</div>
        </div>
        <div class="objective-card" onclick="selectObjective(this, 'volumen')">
          <div class="obj-icon">💪</div>
          <div class="obj-label">Ganar músculo</div>
        </div>
        <div class="objective-card" onclick="selectObjective(this, 'rendimiento')">
          <div class="obj-icon">⚡</div>
          <div class="obj-label">Rendimiento</div>
        </div>
      </div>

      <div class="divider"></div>

      <div class="section-title" style="padding:0 0 12px;">Dietas recomendadas</div>

      <div class="diet-card" onclick="showDietDetail('Mediterránea', '1.800 kcal', 'Rica en vegetales, aceite de oliva, proteínas magras y cereales integrales. Ideal para déficit calórico saludable.')">
        <div class="diet-card-header">
          <div class="diet-name">🫒 Mediterránea</div>
          <div class="diet-cal">1.800 kcal</div>
        </div>
        <div class="diet-desc">Rica en vegetales, aceite de oliva, proteínas magras y cereales integrales.</div>
        <div class="diet-macros">
          <div class="macro"><div class="macro-val">45%</div><div class="macro-label">Carbos</div></div>
          <div class="macro"><div class="macro-val">30%</div><div class="macro-label">Proteína</div></div>
          <div class="macro"><div class="macro-val">25%</div><div class="macro-label">Grasas</div></div>
        </div>
      </div>

      <div class="diet-card" onclick="showDietDetail('Alta en proteínas', '2.200 kcal', 'Maximiza la síntesis muscular con alta ingesta proteica. Ideal para ganancia de masa muscular.')">
        <div class="diet-card-header">
          <div class="diet-name">🥩 Alta en proteínas</div>
          <div class="diet-cal">2.200 kcal</div>
        </div>
        <div class="diet-desc">Maximiza la síntesis muscular con alta ingesta proteica.</div>
        <div class="diet-macros">
          <div class="macro"><div class="macro-val">35%</div><div class="macro-label">Carbos</div></div>
          <div class="macro"><div class="macro-val">45%</div><div class="macro-label">Proteína</div></div>
          <div class="macro"><div class="macro-val">20%</div><div class="macro-label">Grasas</div></div>
        </div>
      </div>

      <div class="diet-card" onclick="showDietDetail('Plant-based', '1.600 kcal', '100% de origen vegetal. Rica en legumbres, tofu, tempeh y proteínas vegetales completas.')">
        <div class="diet-card-header">
          <div class="diet-name">🌱 Plant-based</div>
          <div class="diet-cal">1.600 kcal</div>
        </div>
        <div class="diet-desc">100% de origen vegetal. Rica en legumbres, tofu y proteínas vegetales.</div>
        <div class="diet-macros">
          <div class="macro"><div class="macro-val">55%</div><div class="macro-label">Carbos</div></div>
          <div class="macro"><div class="macro-val">25%</div><div class="macro-label">Proteína</div></div>
          <div class="macro"><div class="macro-val">20%</div><div class="macro-label">Grasas</div></div>
        </div>
      </div>
    </div>
  </div>

  <!-- ═══════════════════════════════ VIDA PUNTOS ═══════════════════════════════ -->
  <div class="screen" id="screen-points">
    <div class="status-bar"><span>9:41</span><div class="status-icons">▲ ● ▮▮▮</div></div>
    <div class="top-nav">
      <button class="back-btn" onclick="goto('home')">←</button>
      <div class="top-nav-title">Vida Puntos</div>
      <div style="width:36px;"></div>
    </div>
    <div class="points-hero">
      <div class="points-label">Tus puntos disponibles</div>
      <div class="points-value">2.450</div>
      <div class="points-sub">Equivalen a $2.450 en beneficios</div>
    </div>
    <div class="screen-content" style="padding-top:0;">
      <div class="section-title" style="padding:0 0 12px;">Canjear beneficios</div>

      <div class="benefit-card" onclick="showCanjear('🧴 Proteína en polvo (1kg)', 1500)">
        <div class="benefit-icon-wrap">🧴</div>
        <div class="benefit-info">
          <div class="benefit-name">Proteína en polvo (1kg)</div>
          <div class="benefit-desc">Whey protein vainilla o chocolate</div>
        </div>
        <div class="benefit-cost">1.500 pts</div>
      </div>

      <div class="benefit-card" onclick="showCanjear('👕 Remera FitLife', 800)">
        <div class="benefit-icon-wrap">👕</div>
        <div class="benefit-info">
          <div class="benefit-name">Remera FitLife</div>
          <div class="benefit-desc">Talle a elección, varios colores</div>
        </div>
        <div class="benefit-cost">800 pts</div>
      </div>

      <div class="benefit-card" onclick="showCanjear('🥤 Botella de agua', 400)">
        <div class="benefit-icon-wrap">🥤</div>
        <div class="benefit-info">
          <div class="benefit-name">Botella de agua</div>
          <div class="benefit-desc">Acero inoxidable 750ml</div>
        </div>
        <div class="benefit-cost">400 pts</div>
      </div>

      <div class="benefit-card" onclick="showCanjear('🎟️ Mes gratis', 5000)">
        <div class="benefit-icon-wrap">🎟️</div>
        <div class="benefit-info">
          <div class="benefit-name">1 mes gratis</div>
          <div class="benefit-desc">Extensión de suscripción</div>
        </div>
        <div class="benefit-cost">5.000 pts</div>
      </div>
    </div>
  </div>

  <!-- ═══════════════════════════════ CLASES ═══════════════════════════════ -->
  <div class="screen" id="screen-classes">
    <div class="status-bar"><span>9:41</span><div class="status-icons">▲ ● ▮▮▮</div></div>
    <div class="top-nav">
      <button class="back-btn" onclick="goto('home')">←</button>
      <div class="top-nav-title">Clases Virtuales</div>
      <div style="width:36px;"></div>
    </div>
    <div class="screen-content">
      <div class="filter-row">
        <button class="filter-chip active" onclick="filterClass(this)">Todas</button>
        <button class="filter-chip" onclick="filterClass(this)">Fuerza</button>
        <button class="filter-chip" onclick="filterClass(this)">Cardio</button>
        <button class="filter-chip" onclick="filterClass(this)">Yoga</button>
        <button class="filter-chip" onclick="filterClass(this)">HIIT</button>
        <button class="filter-chip" onclick="filterClass(this)">Pilates</button>
      </div>

      <div class="class-card" onclick="showClassDetail('Full Body HIIT', 'HIIT', '45 min', 'Intermedio')">
        <div class="class-thumb" style="background: linear-gradient(135deg, #1A3A2A, #2D5A3D);">
          🔥
          <div class="class-badge">HIIT</div>
        </div>
        <div class="class-body">
          <div class="class-name">Full Body HIIT</div>
          <div class="class-meta">
            <div class="class-meta-item">⏱ 45 min</div>
            <div class="class-meta-item">📊 Intermedio</div>
            <div class="class-meta-item">👤 12 inscriptos</div>
          </div>
        </div>
      </div>

      <div class="class-card" onclick="showClassDetail('Yoga Restore', 'Yoga', '60 min', 'Principiante')">
        <div class="class-thumb" style="background: linear-gradient(135deg, #1A2A3A, #2D3A5A);">
          🧘
          <div class="class-badge">Yoga</div>
        </div>
        <div class="class-body">
          <div class="class-name">Yoga Restore</div>
          <div class="class-meta">
            <div class="class-meta-item">⏱ 60 min</div>
            <div class="class-meta-item">📊 Principiante</div>
            <div class="class-meta-item">👤 8 inscriptos</div>
          </div>
        </div>
      </div>

      <div class="class-card" onclick="showClassDetail('Strength & Power', 'Fuerza', '50 min', 'Avanzado')">
        <div class="class-thumb" style="background: linear-gradient(135deg, #2A1A1A, #5A2D2D);">
          💪
          <div class="class-badge">Fuerza</div>
        </div>
        <div class="class-body">
          <div class="class-name">Strength & Power</div>
          <div class="class-meta">
            <div class="class-meta-item">⏱ 50 min</div>
            <div class="class-meta-item">📊 Avanzado</div>
            <div class="class-meta-item">👤 5 inscriptos</div>
          </div>
        </div>
      </div>

      <div class="class-card" onclick="showClassDetail('Cardio Dance', 'Cardio', '40 min', 'Principiante')">
        <div class="class-thumb" style="background: linear-gradient(135deg, #2A1A3A, #4A2D5A);">
          💃
          <div class="class-badge">Cardio</div>
        </div>
        <div class="class-body">
          <div class="class-name">Cardio Dance</div>
          <div class="class-meta">
            <div class="class-meta-item">⏱ 40 min</div>
            <div class="class-meta-item">📊 Principiante</div>
            <div class="class-meta-item">👤 20 inscriptos</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- ═══════════════════════════════ SEDES ═══════════════════════════════ -->
  <div class="screen" id="screen-sedes">
    <div class="status-bar"><span>9:41</span><div class="status-icons">▲ ● ▮▮▮</div></div>
    <div class="top-nav">
      <button class="back-btn" onclick="goto('home')">←</button>
      <div class="top-nav-title">Sedes</div>
      <div style="width:36px;"></div>
    </div>
    <div class="screen-content">
      <div style="background:rgba(255,255,255,0.05); border-radius:var(--radius); height:140px; display:flex; align-items:center; justify-content:center; margin-bottom:20px; border:1.5px solid rgba(255,255,255,0.08);">
        <span style="font-size:40px;">🗺️</span>
        <span style="color:var(--gray); font-size:14px; margin-left:12px;">Mapa de sedes</span>
      </div>

      <div class="sede-card" onclick="showSedeDetail('Palermo', 'Honduras 4523', true)">
        <div class="sede-card-top">
          <div class="sede-name">FitLife Palermo</div>
          <div class="sede-open open">Abierto</div>
        </div>
        <div class="sede-address">📍 Honduras 4523, CABA</div>
        <div class="sede-info-row">
          <div class="sede-info-item">🕐 6:00 - 23:00</div>
          <div class="sede-info-item">👥 Afluencia media</div>
          <div class="sede-info-item">⭐ 4.8</div>
        </div>
      </div>

      <div class="sede-card" onclick="showSedeDetail('Belgrano', 'Av. Monroe 2101', true)">
        <div class="sede-card-top">
          <div class="sede-name">FitLife Belgrano</div>
          <div class="sede-open open">Abierto</div>
        </div>
        <div class="sede-address">📍 Av. Monroe 2101, CABA</div>
        <div class="sede-info-row">
          <div class="sede-info-item">🕐 6:00 - 22:00</div>
          <div class="sede-info-item">👥 Afluencia baja</div>
          <div class="sede-info-item">⭐ 4.6</div>
        </div>
      </div>

      <div class="sede-card" onclick="showSedeDetail('Microcentro', 'Av. Corrientes 1285', false)">
        <div class="sede-card-top">
          <div class="sede-name">FitLife Microcentro</div>
          <div class="sede-open closed">Cerrado</div>
        </div>
        <div class="sede-address">📍 Av. Corrientes 1285, CABA</div>
        <div class="sede-info-row">
          <div class="sede-info-item">🕐 7:00 - 21:00</div>
          <div class="sede-info-item">👥 —</div>
          <div class="sede-info-item">⭐ 4.5</div>
        </div>
      </div>
    </div>
  </div>

  <!-- ═══════════════════════════════ RESERVAS ═══════════════════════════════ -->
  <div class="screen" id="screen-reservas">
    <div class="status-bar"><span>9:41</span><div class="status-icons">▲ ● ▮▮▮</div></div>
    <div class="top-nav">
      <button class="back-btn" onclick="goto('home')">←</button>
      <div class="top-nav-title">Mis Reservas</div>
      <div style="width:36px;"></div>
    </div>
    <div class="screen-content">
      <button class="btn-primary mb-16" onclick="showNuevaReserva()">+ Nueva reserva</button>

      <div class="section-title" style="padding:0 0 12px;">Reservas activas</div>

      <div class="reserva-card">
        <div class="reserva-card-top">
          <div class="reserva-machine">🏋️ Cinta de correr #3</div>
          <div class="reserva-status">Confirmada</div>
        </div>
        <div class="reserva-meta">📍 Palermo · Hoy 18:00 - 18:45</div>
        <div class="reserva-actions">
          <button class="btn-sm btn-sm-outline" onclick="showAlert('Reserva modificada', 'success')">Modificar</button>
          <button class="btn-sm btn-sm-danger" onclick="showAlert('Reserva cancelada', 'error')">Cancelar</button>
        </div>
      </div>

      <div class="reserva-card">
        <div class="reserva-card-top">
          <div class="reserva-machine">🚴 Bicicleta estática #7</div>
          <div class="reserva-status">Confirmada</div>
        </div>
        <div class="reserva-meta">📍 Belgrano · Mañana 09:00 - 09:45</div>
        <div class="reserva-actions">
          <button class="btn-sm btn-sm-outline" onclick="showAlert('Reserva modificada', 'success')">Modificar</button>
          <button class="btn-sm btn-sm-danger" onclick="showAlert('Reserva cancelada', 'error')">Cancelar</button>
        </div>
      </div>

      <div style="text-align:center; padding:20px 0; color:var(--gray); font-size:14px;">
        No tenés más reservas próximas
      </div>
    </div>
  </div>

  <!-- ═══════════════════════════════ RUTINAS ═══════════════════════════════ -->
  <div class="screen" id="screen-routines">
    <div class="status-bar"><span>9:41</span><div class="status-icons">▲ ● ▮▮▮</div></div>
    <div class="top-nav">
      <button class="back-btn" onclick="goto('home')">←</button>
      <div class="top-nav-title">Rutinas</div>
      <div style="width:36px;"></div>
    </div>
    <div class="screen-content">
      <p style="color:var(--gray); font-size:14px; margin-bottom:20px;">Rutinas personalizadas según tus objetivos</p>

      <div class="routine-card" onclick="showAlert('Rutina iniciada 💪', 'success')">
        <div class="routine-name">💪 Fuerza — Tren Superior</div>
        <div class="routine-obj">Ganar músculo</div>
        <div class="routine-exercises">Press de banca · Pull-ups · Remo con barra · Curl de bíceps · Tríceps polea · 3 ejercicios más</div>
        <div style="margin-top:10px; font-size:12px; color:var(--gray);">8 ejercicios · 45 min · Intermedio</div>
      </div>

      <div class="routine-card" onclick="showAlert('Rutina iniciada 🔥', 'success')">
        <div class="routine-name">🔥 Cardio — HIIT 20 min</div>
        <div class="routine-obj">Perder peso</div>
        <div class="routine-exercises">Burpees · Saltos · Mountain climbers · Sprint en cinta · 2 ejercicios más</div>
        <div style="margin-top:10px; font-size:12px; color:var(--gray);">6 ejercicios · 20 min · Avanzado</div>
      </div>

      <div class="routine-card" onclick="showAlert('Rutina iniciada 🧘', 'success')">
        <div class="routine-name">🧘 Movilidad y Flexibilidad</div>
        <div class="routine-obj">Rendimiento</div>
        <div class="routine-exercises">Estiramiento dinámico · Movilidad de cadera · Yoga flows · 4 ejercicios más</div>
        <div style="margin-top:10px; font-size:12px; color:var(--gray);">7 ejercicios · 30 min · Principiante</div>
      </div>
    </div>
  </div>

</div><!-- end phone-frame -->

<script>
  // ─── NAVIGATION ───
  function goto(screenId) {
    document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
    const target = document.getElementById('screen-' + screenId);
    if (target) target.classList.add('active');
  }

  // ─── AUTH ───
  function switchAuthTab(tab) {
    document.getElementById('tab-login').classList.toggle('active', tab === 'login');
    document.getElementById('tab-register').classList.toggle('active', tab === 'register');
    document.getElementById('form-login').style.display = tab === 'login' ? 'block' : 'none';
    document.getElementById('form-register').style.display = tab === 'register' ? 'block' : 'none';
  }

  function doLogin() {
    const email = document.getElementById('login-email').value;
    const pass = document.getElementById('login-pass').value;
    if (!email || !pass) { showAlert('Completá todos los campos', 'error'); return; }
    showAlert('¡Bienvenido de vuelta! 👋', 'success');
    setTimeout(() => {
      // Check subscription (simulate paid user)
      goto('home');
    }, 1200);
  }

  function doRegister() {
    const name = document.getElementById('reg-name').value;
    const email = document.getElementById('reg-email').value;
    const pass = document.getElementById('reg-pass').value;
    if (!name || !email || !pass) { showAlert('Completá todos los campos', 'error'); return; }
    const nameParts = name.trim().split(' ');
    document.getElementById('home-username').innerHTML = nameParts[0] + (nameParts[1] ? ' <span>' + nameParts[1] + '</span>' : '');
    showAlert('Cuenta creada 🎉', 'success');
    setTimeout(() => goto('subscription'), 1200);
  }

  function selectPlan(plan) {
    showAlert('Plan ' + plan + ' seleccionado ✓', 'success');
    setTimeout(() => showPaymentModal(plan), 500);
  }

  function showPaymentModal(plan) {
    openModal(`
      <div class="modal-title">Elegí método de pago</div>
      <div class="modal-sub">Plan ${plan} — confirmá tu pago</div>
      <div class="benefit-card" style="cursor:pointer; margin-bottom:10px;" onclick="procesarPago('Tarjeta de crédito')">
        <div class="benefit-icon-wrap">💳</div>
        <div class="benefit-info"><div class="benefit-name">Tarjeta de crédito/débito</div></div>
      </div>
      <div class="benefit-card" style="cursor:pointer;" onclick="procesarPago('Transferencia bancaria')">
        <div class="benefit-icon-wrap">🏦</div>
        <div class="benefit-info"><div class="benefit-name">Transferencia bancaria</div></div>
      </div>
    `);
  }

  function procesarPago(metodo) {
    closeModal();
    showAlert('Pago procesado con ' + metodo + ' ✓', 'success');
    setTimeout(() => goto('home'), 1400);
  }

  // ─── QR ───
  let qrTimer = null;
  function startBiometric() {
    document.getElementById('qr-state-verify').innerHTML = '<div style="font-size:70px; animation:pulse 1s infinite;">📡</div><p style="color:var(--gray); margin-top:12px;">Verificando...</p>';
    setTimeout(() => {
      document.getElementById('qr-state-verify').style.display = 'none';
      document.getElementById('qr-state-show').style.display = 'block';
      startQRTimer();
    }, 2000);
  }

  function startQRTimer() {
    let seconds = 300;
    clearInterval(qrTimer);
    qrTimer = setInterval(() => {
      seconds--;
      const m = Math.floor(seconds / 60);
      const s = seconds % 60;
      document.getElementById('qr-countdown').textContent = m + ':' + (s < 10 ? '0' : '') + s;
      if (seconds <= 0) {
        clearInterval(qrTimer);
        document.getElementById('qr-state-show').style.display = 'none';
        document.getElementById('qr-state-verify').style.display = 'block';
        document.getElementById('qr-state-verify').innerHTML = `
          <p style="color:var(--white); margin-bottom:20px; font-size:15px;">Se requiere verificación biométrica</p>
          <div style="font-size:80px; margin-bottom:20px;">👆</div>
          <button class="btn-primary" onclick="startBiometric()" style="width:220px;">Verificar huella digital</button>
        `;
      }
    }, 1000);
  }

  // ─── NUTRICION ───
  function selectObjective(el, obj) {
    document.querySelectorAll('.objective-card').forEach(c => c.classList.remove('selected'));
    el.classList.add('selected');
    const labels = { deficit: 'Perder peso', mantenimiento: 'Mantenerme', volumen: 'Ganar músculo', rendimiento: 'Rendimiento' };
    showAlert('Objetivo: ' + labels[obj], 'success');
  }

  function showDietDetail(name, kcal, desc) {
    openModal(`
      <div class="modal-title">${name}</div>
      <div class="modal-sub">${kcal} por día</div>
      <p style="color:var(--gray); font-size:14px; line-height:1.6; margin-bottom:20px;">${desc}</p>
      <div class="divider"></div>
      <p style="color:var(--white); font-size:14px; font-weight:600; margin-bottom:12px;">Comida sugerida hoy:</p>
      <div style="background:rgba(255,255,255,0.05); border-radius:10px; padding:14px; margin-bottom:10px;">
        <div style="font-size:13px; color:var(--white); font-weight:600;">🌅 Desayuno</div>
        <div style="font-size:12px; color:var(--gray); margin-top:4px;">Avena con frutas y proteína en polvo</div>
      </div>
      <div style="background:rgba(255,255,255,0.05); border-radius:10px; padding:14px; margin-bottom:10px;">
        <div style="font-size:13px; color:var(--white); font-weight:600;">☀️ Almuerzo</div>
        <div style="font-size:12px; color:var(--gray); margin-top:4px;">Pollo grillado con quinoa y vegetales</div>
      </div>
      <div style="background:rgba(255,255,255,0.05); border-radius:10px; padding:14px; margin-bottom:20px;">
        <div style="font-size:13px; color:var(--white); font-weight:600;">🌙 Cena</div>
        <div style="font-size:12px; color:var(--gray); margin-top:4px;">Salmón con batata y espinaca</div>
      </div>
      <button class="btn-primary" onclick="closeModal(); showAlert('Plan guardado ✓', 'success')">Guardar este plan</button>
    `);
  }

  // ─── VIDA PUNTOS ───
  function showCanjear(benefit, cost) {
    const balance = 2450;
    const canCanjear = balance >= cost;
    openModal(`
      <div class="modal-title">Canjear beneficio</div>
      <div class="modal-sub">${benefit}</div>
      <div style="background:rgba(255,255,255,0.05); border-radius:10px; padding:16px; margin-bottom:20px;">
        <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
          <span style="color:var(--gray); font-size:13px;">Tus puntos</span>
          <span style="color:var(--yellow); font-weight:700;">${balance.toLocaleString()} pts</span>
        </div>
        <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
          <span style="color:var(--gray); font-size:13px;">Costo del canje</span>
          <span style="color:var(--white); font-weight:700;">${cost.toLocaleString()} pts</span>
        </div>
        <div style="height:1px; background:rgba(255,255,255,0.1); margin:12px 0;"></div>
        <div style="display:flex; justify-content:space-between;">
          <span style="color:var(--gray); font-size:13px;">Puntos restantes</span>
          <span style="color:${canCanjear ? 'var(--green-accent)' : 'var(--red)'}; font-weight:700;">${(balance - cost).toLocaleString()} pts</span>
        </div>
      </div>
      ${canCanjear 
        ? `<button class="btn-primary" onclick="closeModal(); showAlert('¡Beneficio canjeado! 🎉', 'success')">Confirmar canje</button>`
        : `<div style="text-align:center; color:var(--red); font-size:14px; margin-bottom:16px;">No tenés suficientes puntos</div>
           <button class="btn-secondary" onclick="closeModal()">Cerrar</button>`
      }
    `);
  }

  // ─── CLASES ───
  function filterClass(btn) {
    document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
    btn.classList.add('active');
  }

  function showClassDetail(name, type, duration, level) {
    openModal(`
      <div class="modal-title">${name}</div>
      <div style="display:flex; gap:8px; margin-bottom:16px; flex-wrap:wrap;">
        <span style="background:rgba(232,255,71,0.1); color:var(--yellow); font-size:12px; font-weight:600; padding:4px 12px; border-radius:20px;">${type}</span>
        <span style="background:rgba(255,255,255,0.08); color:var(--white); font-size:12px; padding:4px 12px; border-radius:20px;">⏱ ${duration}</span>
        <span style="background:rgba(255,255,255,0.08); color:var(--white); font-size:12px; padding:4px 12px; border-radius:20px;">📊 ${level}</span>
      </div>
      <p style="color:var(--gray); font-size:14px; line-height:1.6; margin-bottom:20px;">
        Clase en vivo con instructor certificado. Sesión grabada disponible por 7 días.
      </p>
      <div style="color:var(--white); font-size:14px; font-weight:600; margin-bottom:12px;">Elegí día y horario:</div>
      <div class="horario-grid">
        <div class="horario-chip" onclick="selectHorario(this)">Lun 07:00</div>
        <div class="horario-chip" onclick="selectHorario(this)">Lun 19:00</div>
        <div class="horario-chip unavailable">Mar 07:00</div>
        <div class="horario-chip" onclick="selectHorario(this)">Mar 19:00</div>
        <div class="horario-chip" onclick="selectHorario(this)">Mié 08:00</div>
        <div class="horario-chip" onclick="selectHorario(this)">Jue 19:00</div>
      </div>
      <button class="btn-primary" id="btn-inscribirse" onclick="closeModal(); showAlert('¡Inscripto a ' + '${name}' + '! 🎉', 'success')">Inscribirme</button>
      <button class="btn-secondary" onclick="closeModal()">Volver al catálogo</button>
    `);
  }

  function selectHorario(el) {
    document.querySelectorAll('.horario-chip').forEach(c => c.classList.remove('selected'));
    el.classList.add('selected');
  }

  // ─── SEDES ───
  function showSedeDetail(name, address, isOpen) {
    openModal(`
      <div class="modal-title">FitLife ${name}</div>
      <div style="color:var(--gray); font-size:14px; margin-bottom:20px;">📍 ${address}, CABA</div>
      <div style="display:flex; gap:8px; margin-bottom:20px;">
        <button class="filter-chip active" style="font-size:12px; padding:8px 14px;">Dirección</button>
        <button class="filter-chip" style="font-size:12px; padding:8px 14px;">Horarios</button>
        <button class="filter-chip" style="font-size:12px; padding:8px 14px;">Detalles</button>
      </div>
      <div style="background:rgba(255,255,255,0.05); border-radius:10px; padding:16px; margin-bottom:12px;">
        <div style="font-size:13px; color:var(--gray); margin-bottom:4px;">Horarios de apertura</div>
        <div style="font-size:14px; color:var(--white);">Lun-Vie: 6:00 - 23:00</div>
        <div style="font-size:14px; color:var(--white);">Sáb-Dom: 8:00 - 20:00</div>
      </div>
      <div style="background:rgba(255,255,255,0.05); border-radius:10px; padding:16px; margin-bottom:20px;">
        <div style="font-size:13px; color:var(--gray); margin-bottom:8px;">Equipamiento disponible</div>
        <div style="font-size:13px; color:var(--white); line-height:1.8;">
          🏋️ 40 máquinas de fuerza<br>
          🚴 20 bicicletas estáticas<br>
          🏃 15 cintas de correr<br>
          🧘 Sala de clases grupales
        </div>
      </div>
      ${isOpen 
        ? `<button class="btn-primary" onclick="closeModal(); showAlert('Abriendo navegación GPS 📍', 'success')">📍 Cómo llegar</button>`
        : `<div style="text-align:center; color:#FF6B6B; font-size:14px; padding:10px;">Esta sede está cerrada actualmente</div>`
      }
    `);
  }

  // ─── RESERVAS ───
  function showNuevaReserva() {
    openModal(`
      <div class="modal-title">Nueva Reserva</div>
      <div class="modal-sub">Elegí sede, máquina y horario</div>
      <div class="form-group">
        <label class="form-label">Sede</label>
        <select class="form-input" style="cursor:pointer;">
          <option>FitLife Palermo</option>
          <option>FitLife Belgrano</option>
        </select>
      </div>
      <div class="form-group">
        <label class="form-label">Máquina</label>
        <select class="form-input" style="cursor:pointer;">
          <option>🏃 Cinta de correr</option>
          <option>🚴 Bicicleta estática</option>
          <option>🏋️ Banco de press</option>
          <option>💪 Rack de sentadillas</option>
        </select>
      </div>
      <div class="form-group">
        <label class="form-label">Horario disponible</label>
        <div class="horario-grid">
          <div class="horario-chip" onclick="selectHorario(this)">08:00</div>
          <div class="horario-chip" onclick="selectHorario(this)">09:00</div>
          <div class="horario-chip unavailable">10:00</div>
          <div class="horario-chip" onclick="selectHorario(this)">11:00</div>
          <div class="horario-chip" onclick="selectHorario(this)">18:00</div>
          <div class="horario-chip" onclick="selectHorario(this)">19:00</div>
        </div>
      </div>
      <button class="btn-primary" onclick="closeModal(); showAlert('Reserva confirmada ✓', 'success')">Confirmar reserva</button>
    `);
  }

  // ─── MODAL ───
  function openModal(content) {
    document.getElementById('modal-body').innerHTML = content;
    document.getElementById('modal-overlay').classList.add('open');
  }
  function closeModal() {
    document.getElementById('modal-overlay').classList.remove('open');
  }
  document.getElementById('modal-overlay').addEventListener('click', function(e) {
    if (e.target === this) closeModal();
  });

  // ─── ALERT ───
  function showAlert(msg, type) {
    const alert = document.getElementById('global-alert');
    alert.textContent = (type === 'success' ? '✓ ' : '✗ ') + msg;
    alert.className = 'alert show ' + type;
    setTimeout(() => { alert.className = 'alert'; }, 2500);
  }

  // ─── INIT ───
  setTimeout(() => goto('auth'), 2000);
</script>
</body>
</html>

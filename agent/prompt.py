"""
Prompts y plantilla HTML para el Daily Briefing de Manuel Cortés.
"""

SYSTEM_PROMPT = """\
Eres un agente de inteligencia experto en Data Engineering, Inteligencia Artificial,
Geopolítica tecnológica, Legislación digital y ecosistema tecnológico chileno.

Tu tarea es generar el Daily Briefing diario de Manuel Cortés, Ingeniero de Datos.

PROCESO OBLIGATORIO:
1. Usa web_search para buscar noticias RECIENTES (últimas 24-48h) para CADA sección.
2. Redacta en español, tono profesional orientado a ingeniero de datos senior.
3. Retorna ÚNICAMENTE el HTML interno del body — sin DOCTYPE, sin <html>, sin <head>.

BÚSQUEDAS MÍNIMAS (una por sección):
- "inteligencia artificial noticias hoy"
- "AI news today latest"
- "geopolitica tecnologia noticias hoy"
- "regulacion inteligencia artificial legislacion"
- "inteligencia artificial Chile noticias"
- "data engineering tools news"
- "machine learning paper arxiv"

REGLAS:
- 2-3 ítems por sección con fuente y link real verificado
- Cada ítem incluye potencialidades técnicas concretas
- Síntesis ejecutiva resume los 3-5 hallazgos más importantes
- Vocabulario: 3-5 términos relevantes a las noticias del día
- Sin texto antes ni después del HTML
"""

_TEMPLATE = """\
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <meta http-equiv="Content-Security-Policy" content="default-src 'self' https://fonts.googleapis.com https://fonts.gstatic.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; script-src 'none'; object-src 'none';"/>
  <title>Daily Briefing — {date}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,300;0,8..60,400;0,8..60,600;1,8..60,300;1,8..60,400&display=swap" rel="stylesheet"/>
  <style>
    :root {{
      --bg:         #0f0f0f;
      --surface:    #1a1a1a;
      --surface2:   #242424;
      --border:     #2e2e2e;
      --text:       #e8e6e1;
      --text-muted: #8a8680;
      --accent:     #c8a96e;
      --accent2:    #7eb8c8;
    }}
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      background: var(--bg);
      color: var(--text);
      font-family: 'Source Serif 4', Georgia, serif;
      font-size: 17px;
      line-height: 1.8;
      max-width: 820px;
      margin: 0 auto;
      padding: 2rem 1.5rem 6rem;
    }}
    header {{
      border-bottom: 1px solid var(--border);
      padding-bottom: 1.5rem;
      margin-bottom: 3rem;
    }}
    .header-label {{
      font-size: 0.72rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--text-muted);
      margin-bottom: 0.5rem;
    }}
    h1 {{
      font-size: 2rem;
      font-weight: 600;
      color: var(--accent);
      line-height: 1.2;
      margin-bottom: 0.25rem;
    }}
    .byline {{ font-size: 0.85rem; color: var(--text-muted); font-style: italic; }}
    .sintesis {{
      background: var(--surface);
      border-left: 3px solid var(--accent);
      border-radius: 0 8px 8px 0;
      padding: 1.5rem 1.75rem;
      margin-bottom: 3rem;
    }}
    .sintesis h2 {{
      font-size: 0.72rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--accent);
      margin-bottom: 1rem;
    }}
    .sintesis p {{ margin-bottom: 0.75rem; }}
    .sintesis p:last-child {{ margin-bottom: 0; }}
    section {{ margin-bottom: 3.5rem; }}
    section > h2 {{
      font-size: 0.72rem;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
      padding-bottom: 0.5rem;
      border-bottom: 1px solid var(--border);
    }}
    section > h2 span {{ color: var(--accent2); margin-right: 0.5rem; }}
    .item {{
      margin-bottom: 2rem;
      padding-bottom: 2rem;
      border-bottom: 1px solid var(--border);
    }}
    .item:last-child {{ border-bottom: none; margin-bottom: 0; padding-bottom: 0; }}
    .item-title {{ font-size: 1.05rem; font-weight: 600; margin-bottom: 0.4rem; line-height: 1.4; }}
    .item-title a {{
      color: var(--text);
      text-decoration: none;
      border-bottom: 1px solid var(--border);
      transition: color 0.2s, border-color 0.2s;
    }}
    .item-title a:hover {{ color: var(--accent); border-color: var(--accent); }}
    .item-meta {{ font-size: 0.78rem; color: var(--text-muted); margin-bottom: 0.75rem; }}
    .item p {{ color: #c8c4bd; font-size: 0.95rem; margin-bottom: 0.5rem; }}
    .potencialidades {{
      background: var(--surface2);
      border-radius: 6px;
      padding: 1rem 1.25rem;
      margin-top: 0.75rem;
    }}
    .potencialidades-label {{
      font-size: 0.68rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--accent2);
      margin-bottom: 0.5rem;
    }}
    .potencialidades p {{ color: #a8c8d8; font-size: 0.88rem; margin: 0; }}
    .highlight-card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-top: 2px solid var(--accent);
      border-radius: 8px;
      padding: 1.5rem;
    }}
    .highlight-card .tag {{
      display: inline-block;
      font-size: 0.68rem;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--accent);
      border: 1px solid var(--accent);
      border-radius: 3px;
      padding: 0.15rem 0.5rem;
      margin-bottom: 0.75rem;
    }}
    .vocab-item {{ margin-bottom: 1.5rem; }}
    .vocab-term {{ font-weight: 600; color: var(--accent); font-size: 1rem; }}
    .vocab-def {{ color: #c8c4bd; font-size: 0.92rem; margin-top: 0.2rem; }}
    .refs {{ font-size: 0.85rem; }}
    .refs li {{
      margin-bottom: 0.5rem;
      color: var(--text-muted);
      list-style: none;
      padding-left: 1.2rem;
      position: relative;
    }}
    .refs li::before {{ content: '→'; position: absolute; left: 0; color: var(--border); }}
    .refs a {{ color: var(--accent2); text-decoration: none; }}
    .refs a:hover {{ text-decoration: underline; }}
    footer {{
      text-align: center;
      font-size: 0.75rem;
      color: var(--text-muted);
      border-top: 1px solid var(--border);
      padding-top: 2rem;
      margin-top: 4rem;
    }}
  </style>
</head>
<body>
<header>
  <div class="header-label">Daily Briefing</div>
  <h1>{date}</h1>
  <div class="byline">Manuel Cortés &mdash; Ingeniero de Datos</div>
</header>
{body}
<footer>
  Generado automáticamente con Claude &mdash; {date}
</footer>
</body>
</html>
"""

_BODY_STRUCTURE = """
<div class="sintesis">
  <h2>Síntesis ejecutiva</h2>
  <p>[párrafo 1: hallazgos de IA y Data Engineering]</p>
  <p>[párrafo 2: hallazgos de geopolítica, legislación y Chile]</p>
</div>

<section>
  <h2><span>★</span>Herramienta / Paper / Dato de la semana</h2>
  <div class="highlight-card">
    <span class="tag">[Herramienta | Paper | Dato]</span>
    <div class="item-title"><a href="[URL real]">[Título]</a></div>
    <p>[Descripción]</p>
    <div class="potencialidades">
      <div class="potencialidades-label">Potencialidades técnicas</div>
      <p>[Implicancias para data engineering]</p>
    </div>
  </div>
</section>

<section>
  <h2><span>I</span>Inteligencia Artificial</h2>
  <div class="item">
    <div class="item-title"><a href="[URL real]">[Título]</a></div>
    <div class="item-meta">[Fuente] &mdash; [fecha]</div>
    <p>[Resumen]</p>
    <div class="potencialidades">
      <div class="potencialidades-label">Potencialidades técnicas</div>
      <p>[Implicancias]</p>
    </div>
  </div>
</section>

<section>
  <h2><span>II</span>Geopolítica</h2>
  <div class="item">
    <div class="item-title"><a href="[URL real]">[Título]</a></div>
    <div class="item-meta">[Fuente] &mdash; [fecha]</div>
    <p>[Resumen]</p>
    <div class="potencialidades">
      <div class="potencialidades-label">Potencialidades técnicas</div>
      <p>[Implicancias]</p>
    </div>
  </div>
</section>

<section>
  <h2><span>III</span>Legislación</h2>
  <div class="item">
    <div class="item-title"><a href="[URL real]">[Título]</a></div>
    <div class="item-meta">[Fuente] &mdash; [fecha]</div>
    <p>[Resumen]</p>
    <div class="potencialidades">
      <div class="potencialidades-label">Potencialidades técnicas</div>
      <p>[Implicancias]</p>
    </div>
  </div>
</section>

<section>
  <h2><span>IV</span>IA Chile</h2>
  <div class="item">
    <div class="item-title"><a href="[URL real]">[Título]</a></div>
    <div class="item-meta">[Fuente] &mdash; [fecha]</div>
    <p>[Resumen]</p>
    <div class="potencialidades">
      <div class="potencialidades-label">Potencialidades técnicas</div>
      <p>[Implicancias]</p>
    </div>
  </div>
</section>

<section>
  <h2><span>V</span>Data Engineering</h2>
  <div class="item">
    <div class="item-title"><a href="[URL real]">[Título]</a></div>
    <div class="item-meta">[Fuente] &mdash; [fecha]</div>
    <p>[Resumen]</p>
    <div class="potencialidades">
      <div class="potencialidades-label">Potencialidades técnicas</div>
      <p>[Implicancias]</p>
    </div>
  </div>
</section>

<section>
  <h2><span>VI</span>Fundamentos</h2>
  <div class="item">
    <div class="item-title"><a href="[URL real]">[Título]</a></div>
    <div class="item-meta">[Fuente] &mdash; [fecha]</div>
    <p>[Resumen extendido]</p>
    <div class="potencialidades">
      <div class="potencialidades-label">Potencialidades técnicas</div>
      <p>[Implicancias]</p>
    </div>
  </div>
</section>

<section>
  <h2><span>◆</span>Vocabulario</h2>
  <div class="vocab-item">
    <div class="vocab-term">[Término]</div>
    <div class="vocab-def">[Definición]</div>
  </div>
</section>

<section>
  <h2><span>↗</span>Referencias</h2>
  <ul class="refs">
    <li><a href="[URL real]">[Fuente]</a></li>
  </ul>
</section>
"""


def wrap_html(date: str, body: str) -> str:
    return _TEMPLATE.format(date=date, body=body)


def build_user_prompt(date: str) -> str:
    return f"""\
Hoy es {date}.

Busca noticias recientes con web_search para cada sección y genera el Daily Briefing.

Usa esta estructura exacta para el body:

{_BODY_STRUCTURE}

IMPORTANTE:
- Retorna ÚNICAMENTE el HTML del body, sin DOCTYPE ni etiquetas html/head/body
- Todos los links deben ser URLs reales obtenidas de tus búsquedas
- 2-3 ítems por sección
"""

# Daily Briefing — Manuel Cortés

Generación automática del briefing diario usando Claude como agente de IA con búsqueda web en tiempo real.

## Arquitectura 


## Setup (una sola vez)

### 1. Agregar el API key como Secret
1. GitHub → Settings → Secrets and variables → Actions
2. New repository secret
3. Nombre: `ANTHROPIC_API_KEY`
4. Valor: tu key de console.anthropic.com

### 2. Activar GitHub Pages
1. GitHub → Settings → Pages
2. Source: Deploy from a branch
3. Branch: `main` / Folder: `/docs`
4. Guardar

### 3. Push inicial
```bash
git remote add origin https://github.com/mnlcortes/daily-briefing.git
git add .
git commit -m "setup: estructura inicial segura"
git push -u origin main
```

## Uso

| Modo | Cómo |
|------|------|
| Automático | Todos los días 07:00 AM Santiago |
| Manual | Actions → Daily Briefing → Run workflow |
| Local | `cd agent && python generate_briefing.py` |

## Seguridad

- `ANTHROPIC_API_KEY` vive únicamente en GitHub Secrets
- gitleaks bloquea commits con secrets antes de llegar al repo
- Actions pineadas a SHA completo — sin tags flotantes
- Permisos mínimos en el workflow (`contents: write` solo donde se necesita)
- `requirements.txt` con versión exacta pineada
- CSP en el HTML generado

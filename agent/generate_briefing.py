"""
Daily Briefing Agent — Manuel Cortés, Ingeniero de Datos
"""

import anthropic
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from prompt import SYSTEM_PROMPT, build_user_prompt, wrap_html

MODEL      = "claude-opus-4-5"
MAX_TOKENS = 8000
OUTPUT     = Path(__file__).parent.parent / "docs" / "index.html"

MESES = {
    1:"enero", 2:"febrero", 3:"marzo", 4:"abril",
    5:"mayo", 6:"junio", 7:"julio", 8:"agosto",
    9:"septiembre", 10:"octubre", 11:"noviembre", 12:"diciembre"
}
DIAS = {
    0:"lunes", 1:"martes", 2:"miércoles", 3:"jueves",
    4:"viernes", 5:"sábado", 6:"domingo"
}


def ts() -> str:
    return datetime.now(timezone.utc).strftime("%H:%M:%S UTC")


def get_api_key() -> str:
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not key:
        print("❌ ERROR: ANTHROPIC_API_KEY no encontrado.")
        print("   Local:  export ANTHROPIC_API_KEY='sk-ant-...'")
        print("   CI/CD:  configurar en GitHub Secrets")
        sys.exit(1)
    if not key.startswith("sk-ant-"):
        print("❌ ERROR: El formato del API key no parece válido.")
        sys.exit(1)
    return key


def get_date() -> str:
    now = datetime.now(timezone.utc)
    return f"{DIAS[now.weekday()].capitalize()}, {now.day} de {MESES[now.month]} de {now.year}"


def generate(date_str: str) -> str:
    client = anthropic.Anthropic(api_key=get_api_key())

    print(f"[{ts()}] Iniciando generación — {date_str}")

    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=SYSTEM_PROMPT,
        tools=[{
            "type": "web_search_20250305",
            "name": "web_search",
            "max_uses": 20,
        }],
        messages=[{
            "role": "user",
            "content": build_user_prompt(date_str),
        }],
    )

    print(f"[{ts()}] Respuesta recibida — stop: {response.stop_reason}")
    print(f"[{ts()}] Tokens — entrada: {response.usage.input_tokens} | salida: {response.usage.output_tokens}")

    body = ""
    for block in response.content:
        if block.type == "text":
            body += block.text

    if not body.strip():
        print(f"[{ts()}] ❌ El agente no retornó contenido.")
        sys.exit(1)

    # Limpiar bloques markdown si el modelo los incluyó
    body = re.sub(r"^```html?\s*", "", body.strip(), flags=re.MULTILINE)
    body = re.sub(r"```\s*$", "", body.strip(), flags=re.MULTILINE)

    # Si ya es un HTML completo lo usamos directamente
    # Si es solo el body lo envolvemos en el template
    if body.strip().startswith("<!DOCTYPE"):
        return body

    return wrap_html(date_str, body.strip())


def save(html: str) -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    size = len(html.encode("utf-8"))
    if size < 2000:
        print(f"[{ts()}] ❌ HTML demasiado pequeño ({size} bytes) — posible error del agente.")
        sys.exit(1)

    OUTPUT.write_text(html, encoding="utf-8")
    print(f"[{ts()}] ✅ Guardado en {OUTPUT} ({size} bytes)")


def main():
    date_str = get_date()
    try:
        html = generate(date_str)
        save(html)
        print(f"[{ts()}] ✅ Briefing generado exitosamente.")
    except KeyboardInterrupt:
        print("\n[Interrumpido]")
        sys.exit(0)


if __name__ == "__main__":
    main()

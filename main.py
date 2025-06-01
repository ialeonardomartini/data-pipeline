import json

def safe_json_from_markdown_block(raw_string: str) -> list | dict:
    """Remove blocos markdown e converte JSON em objeto Python de forma segura."""
    raw_clean = raw_string.strip()

    # Remove blocos markdown como ```json e ```
    if raw_clean.startswith("```json"):
        raw_clean = raw_clean.replace("```json", "").strip()
    if raw_clean.endswith("```"):
        raw_clean = raw_clean[:-3].strip()

    # Tenta decodificar o JSON
    try:
        return json.loads(raw_clean)
    except json.JSONDecodeError as e:
        print("❌ Erro ao decodificar JSON:")
        print(raw_clean)
        print("🔧 Detalhes:", e)
        return []  # ou {} dependendo da estrutura esperada
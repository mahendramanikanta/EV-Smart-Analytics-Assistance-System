import google.genai as genai

def chat_reply(prompt: str, api_key: str = None) -> str:
    """
    Uses Google Gemini if API key is provided.
    Otherwise falls back to rule-based responses.
    """

    prompt = (prompt or "").strip()
    if not prompt:
        return "Please enter a question."

    # ---- Use Gemini if API key exists ----
    if api_key:
        try:
            client = genai.Client(api_key=api_key)

            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=prompt
            )

            return response.text.strip()

        except Exception:
            pass  # fallback to rule-based bot

    # ---- Rule-based fallback ----
    p = prompt.lower()

    if "range" in p:
        return "Typical EV range is 250–500 km depending on battery size and efficiency."
    if "charge" in p:
        return "Fast charging adds 100–200 km in ~20–30 minutes. Home AC charging is slower."
    if "best" in p:
        return "For long trips, choose EVs with >60 kWh battery. For city use, compact EVs are ideal."
    if "battery" in p:
        return "Keep charge between 20–80%, avoid extreme heat, and minimize fast-charging."
    if "maintenance" in p:
        return "EV maintenance involves tires, brakes, coolant, and firmware updates."
    if "price" in p:
        return "EV price depends on battery capacity, features, and brand — higher range means higher cost."

    return "I can help with EV range, charging, comparisons, and battery care. Ask anything!"

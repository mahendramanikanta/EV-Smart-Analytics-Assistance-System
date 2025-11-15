# chatbot.py
import google.generativeai as genai

def chat_reply(prompt: str, api_key: str = None) -> str:
    """
    Chatbot System:
    1) If Gemini API key exists → use Gemini Pro model
    2) If no key → fallback to rule-based EV assistant
    """

    prompt = (prompt or "").strip()
    if not prompt:
        return "Please enter a question."

    # -------------------------------------
    # 1) GEMINI AI MODE (via secrets.toml)
    # -------------------------------------
    if api_key:
        try:
            genai.configure(api_key=api_key)

            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(
                f"You are an expert Electric Vehicle (EV) assistant. "
                f"Give short, clear, accurate answers.\nUser: {prompt}"
            )

            # If Gemini returned text, use it
            if response and response.text:
                return response.text.strip()

        except Exception:
            # If Gemini fails → continue to fallback
            pass  


    # -------------------------------------
    # 2) RULE-BASED FALLBACK MODE
    # -------------------------------------
    p = prompt.lower()

    if "range" in p:
        return "Most EVs deliver 250–500 km range depending on battery size and efficiency."
    if "charge" in p:
        return "Fast charging adds 100–200 km in 20–30 minutes; AC home charging is slower."
    if "best" in p:
        return "For highway trips, choose EVs with 60–70 kWh+ battery packs."
    if "battery" in p:
        return "Maintain charge between 20–80%, avoid heat, and limit frequent DC fast charging."
    if "maintenance" in p:
        return "EVs need minimal maintenance: tires, brakes, coolant, and software updates."
    if "price" in p:
        return "Price depends on battery capacity, brand, and features. Higher range = higher cost."

    return "I can help with EV charging, range, battery care, pricing, or recommendations. Ask anything!"

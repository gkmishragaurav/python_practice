from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable
import re

# ─────────────────────────────────────────────
# 🔧 Setup: LLM and Prompt Templates
# ─────────────────────────────────────────────

def enrich_with_context(interest: str, budget: int, destination: str = None, mode: str = "destination") -> str:
    # RAG-style simulated knowledge base
    if mode == "destination":
        return {
            "history": (
                "Travelers who love history often enjoy cities like Rome, Athens, and Cairo. "
                "These destinations offer ancient ruins, world-class museums, and rich cultural experiences."
            ),
            "beaches": (
                "Beach lovers enjoy Bali, Phuket, and the Maldives for their tropical beauty and budget-friendly resorts."
            ),
            "nature": (
                "Nature enthusiasts love Banff, Patagonia, and the Dolomites for stunning hikes and views."
            )
        }.get(interest.lower(), "")

    elif mode == "flight":
        return {
            "Rome": "Rome is well connected from most US and European cities with budget airlines like Ryanair, EasyJet, and Vueling.",
            "Athens": "Athens flights are cheapest from European hubs like Frankfurt, Paris, or Istanbul — usually under $400 round trip.",
            "Bali": "Bali has affordable flights from Southeast Asia; from the US, expect stopovers via Singapore or Kuala Lumpur.",
        }.get(destination, "")

    elif mode == "itinerary":
        return {
            "Rome": (
                "Rome has iconic landmarks like the Colosseum, Roman Forum, Vatican City, and Trastevere. "
                "Food tours and wine tastings are popular afternoon options."
            ),
            "Athens": (
                "Must-see spots include the Acropolis, Plaka district, and Temple of Olympian Zeus. "
                "Evenings in Psiri offer great live music and meze dining."
            ),
            "Bali": (
                "Ubud’s temples, sunrise at Mount Batur, and beach clubs in Seminyak offer a full experience. "
                "Balinese dance shows are a great evening activity."
            ),
        }.get(destination, "")

    return ""


def get_llm():
    return OllamaLLM(model="mistral")

# def get_dest_prompt():
#     return PromptTemplate.from_template(
#         "Suggest 3 travel destinations for someone who enjoys {interest} and has a budget of ${budget}."
#     )

def get_dest_prompt():
    return PromptTemplate.from_template(
        "{context}\n\nNow suggest 3 travel destinations for someone who enjoys {interest} and has a budget of ${budget}."
    )

def get_flight_prompt():
    return PromptTemplate.from_template(
        "{context}\n\nFind 2 affordable flights to {destination} under ${budget} for next month. Include departure city."
    )

def get_itinerary_prompt():
    return PromptTemplate.from_template(
        "{context}\n\nPlan a 3-day itinerary in {destination} for a tourist who likes {interest}. "
        "Include morning, afternoon, and evening activities for each day."
    )

# ─────────────────────────────────────────────
# 🔗 Prompt Chains
# ─────────────────────────────────────────────

def get_destination_chain() -> Runnable:
    return get_dest_prompt() | get_llm()

def get_flight_chain() -> Runnable:
    return get_flight_prompt() | get_llm()

def get_itinerary_chain() -> Runnable:
    return get_itinerary_prompt() | get_llm()

# ─────────────────────────────────────────────
# 📍 Utility Functions
# ─────────────────────────────────────────────

def get_user_preferences():
    try:
        # interest = input("What are you interested in? (e.g., beaches, history): ") or "history"
        interest = "history"
        # budget = int(input("What’s your budget in USD? ") or "2000")
        budget = "5000"
    except Exception:
        interest, budget = "history", 2000
    return interest.strip(), budget

def extract_first_destination(response: str) -> str:
    matches = re.findall(r'\d+\.\s*(.*)', response)
    return matches[0] if matches else response.strip().split("\n")[0]

# ─────────────────────────────────────────────
# 🧠 Main Planner Logic
# ─────────────────────────────────────────────

def run_trip_planner(interest: str, budget: int):
    print("\n🌟 Trip Planner Initialized!")

    # 🔍 Enrich context from your knowledge base
    context = enrich_with_context(interest, budget)

    print("\n🔍 Finding destinations...")
    # dest_chain = get_destination_chain()
    # dest_output = dest_chain.invoke({"interest": interest, "budget": budget})
    # 🧠 Invoke the LLM with context
    dest_chain = get_destination_chain()
    dest_output = dest_chain.invoke({
        "interest": interest,
        "budget": budget,
        "context": context
    })
    print("\n🌍 Suggested Destinations:\n", dest_output)

    destination = extract_first_destination(dest_output)
    print(f"\n📍 Selected Destination: {destination}")

    print("\n✈️ Searching for flights...")
    flight_chain = get_flight_chain()
    flight_context = enrich_with_context(interest, budget, destination, mode="flight")
    flight_output = flight_chain.invoke({
        "destination": destination,
        "budget": budget,
        "context": flight_context
    })
    print("\n✈️ Flight Options:\n", flight_output)
    # flight_output = flight_chain.invoke({"destination": destination, "budget": budget})
    # print("\n✈️ Flight Options:\n", flight_output)

    print("\n🗓️ Creating itinerary...")
    itinerary_chain = get_itinerary_chain()
    itinerary_context = enrich_with_context(interest, budget, destination, mode="itinerary")
    itinerary_output = itinerary_chain.invoke({
        "destination": destination,
        "interest": interest,
        "context": itinerary_context
    })
    print("\n🗓️ 3-Day Itinerary:\n", itinerary_output)

# ─────────────────────────────────────────────
# 🚀 Entry Point
# ─────────────────────────────────────────────

def main():
    interest, budget = get_user_preferences()
    run_trip_planner(interest, budget)

if __name__ == "__main__":
    main()

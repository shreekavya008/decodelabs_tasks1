from responses import RESPONSES, get_default_response

def sanitize_input(raw_input):
    """
    Phase 1: Input Sanitization & Normalization
    Converts any variation of input (e.g., 'HeLLo', '  hello  ') to clean lowercase.
    """
    return raw_input.lower().strip()

def get_response(clean_input):
    """
    Phase 2: Process — Intent Matching
    Uses dictionary .get() for O(1) lookup with a fallback default.
    This is the professional approach — avoids the if-elif anti-pattern.
    """
    return RESPONSES.get(clean_input, get_default_response())

def run_chatbot():
    """
    Phase 3: Output — The Infinite Feedback Loop
    The chatbot stays alive until the kill command ('exit' or 'quit').
    """
    print("=" * 50)
    print("   Welcome to WEbot — Rule-Based AI Chatbot")
    print("   Type 'help' for options. Type 'exit' to quit.")
    print("=" * 50)

    while True:
        raw_input = input("\nYou: ")

        clean_input = sanitize_input(raw_input)

        if not clean_input:
            print("WEbot: Please type something!")
            continue

        if clean_input in ("exit", "quit"):
            print("WEbot:", RESPONSES.get(clean_input, "Goodbye!"))
            break  

        response = get_response(clean_input)
        print(f"WEbot: {response}")

if __name__ == "__main__":
    run_chatbot()
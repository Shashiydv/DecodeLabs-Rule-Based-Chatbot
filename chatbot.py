import datetime

def sanitize_input(raw_text: str) -> str:
    """
    Phase 1: Input & Sanitization (IPO Model)
    Converts input to lowercase and strips leading/trailing whitespace.
    """
    return raw_text.lower().strip()

def get_bot_response(clean_input: str, knowledge_base: dict) -> str:
    """
    Phase 2: Process (The Logic Skeleton)
    Uses O(1) dictionary lookup with .get() fallback instead of an O(n) if-elif ladder.
    """
    # Dynamic rule-based triggers (guardrail / real-time utility)
    if clean_input == "time":
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current system time is {current_time}."
    elif clean_input == "date":
        today_date = datetime.date.today().strftime("%B %d, %Y")
        return f"Today's date is {today_date}."

    # Standard O(1) Hash Map Lookup + Atomic Fallback
    fallback_response = (
        "I do not understand that command yet. "
        "Try typing 'help' to see what I can respond to!"
    )
    return knowledge_base.get(clean_input, fallback_response)

def run_chatbot():
    """
    Phase 3: Output & Continuous Feedback Loop
    """
    # Knowledge Base: Dictionary with 5+ distinct intents
    responses = {
        # 1. Greetings Intent
        "hi": "Hello! Welcome to DecodeLabs AI Assistant. How can I help you today?",
        "hello": "Hi there! Ready to explore deterministic AI?",
        "hey": "Hey! Ask me anything from my knowledge base or type 'help'.",

        # 2. Identity & Role Intent
        "who are you": "I am Project 1: A Rule-Based AI Chatbot engineered at DecodeLabs.",
        "what is your name": "I am DecodeBot v1.0 — powered by pure Python logic and hash maps.",

        # 3. Architecture & Concept Intent
        "how do you work": (
            "I follow the IPO (Input-Process-Output) model. I sanitize your text, "
            "look up your intent in an O(1) Python dictionary, and return a deterministic reply."
        ),
        "why rule based": (
            "Rule-based systems are 'White Box' engines—100% traceable, zero hallucinations, "
            "and act as safety guardrails before passing queries to LLMs."
        ),

        # 4. Status / Small Talk Intent
        "how are you": "Running smoothly inside an infinite while loop with 0ms latency!",
        "thank you": "You're welcome! Happy coding.",
        "thanks": "Anytime! Let me know if you need more help.",

        # 5. Help / Capabilities Intent
        "help": (
            "Available commands:\n"
            "  - Greetings: 'hi', 'hello', 'hey'\n"
            "  - Info: 'who are you', 'how do you work', 'why rule based'\n"
            "  - Utilities: 'time', 'date'\n"
            "  - Exit: 'exit', 'quit', 'bye'"
        )
    }

    exit_commands = {"exit", "quit", "bye"}

    print("=" * 55)
    print("🤖 DECODELABS AI ENGINE — PROJECT 1 (RULE-BASED BOT)")
    print("Type 'help' for commands or 'exit' to terminate.")
    print("=" * 55)

    # The Heartbeat: Infinite Loop
    while True:
        try:
            raw_input = input("\nYou: ")
            clean_input = sanitize_input(raw_input)

            # Skip empty inputs cleanly
            if not clean_input:
                continue

            # Kill Command / Clean Exit Strategy
            if clean_input in exit_commands:
                print("Bot: Shutting down logic engine. Goodbye! 👋")
                break

            # Process & Output
            reply = get_bot_response(clean_input, responses)
            print(f"Bot: {reply}")

        except KeyboardInterrupt:
            print("\nBot: Session interrupted. Exiting cleanly. Goodbye!")
            break

if __name__ == "__main__":
    run_chatbot()
"""
9DA Main - Orchestrator

Wires components together.
No logic. No policy. Pure coordination.
"""

from app.runner import run_9da


def main():
    """
    9DA Test Interface
    
    Measurement instrument. Not conversational system.
    """
    
    print("9DA Test Interface")
    print("=" * 50)
    print("Enter a concept to analyze (or 'exit' to quit)")
    print("=" * 50)
    print()
    
    while True:
        try:
            user_input = input("> ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("\nExiting 9DA interface.")
                break
            
            result = run_9da(user_input)
            print(result)
            print()

        except KeyboardInterrupt:
            print("\n\nExiting 9DA interface.")
            break
            
        except Exception:
            # Never error, never silence
            print(
                "HALT\n\n"
                "Execution could not proceed.\n"
                "System integrity preserved."
            )
            print()


if __name__ == "__main__":
    main()

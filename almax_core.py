import sys

def almax_greeting():
    print("==========================================")
    print("   Welcome to Almax 2.0 - Smart Assistant  ")
    print("   (Fast, Accurate, and Secure Core)      ")
    print("==========================================")

def main():
    almax_greeting()
    while True:
        try:
            user_input = input("\nUser: ")
            if user_input.lower() in ['exit', 'quit', 'خروج']:
                print("Almax: Goodbye! Stay secure.")
                break
            
            if not user_input.strip():
                continue

            # نموذج الرد الأولي الذكي (قيد التطوير للربط مع محرك الذكاء الاصطناعي المتقدم)
            print(f"Almax 2.0: I received your message -> '{user_input}'. Processing with high accuracy...")
            
        except KeyboardInterrupt:
            print("\nAlmax: Session interrupted. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()


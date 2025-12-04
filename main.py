import os
import argparse
from dotenv import load_dotenv
from bot import LinkedInBot

# Load environment variables
load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="LinkedIn Auto Connector Bot")
    parser.add_argument("n_requests", type=int, help="Number of connection requests to send")
    
    args = parser.parse_args()
    
    email = os.getenv("LINKEDIN_EMAIL")
    password = os.getenv("LINKEDIN_PASSWORD")
    
    if not email or not password:
        print("Error: Please set LINKEDIN_EMAIL and LINKEDIN_PASSWORD in .env file")
        return

    print(f"Initializing bot for {args.n_requests} requests...")
    bot = LinkedInBot(email, password)
    
    try:
        bot.login()
        bot.connect_from_network(args.n_requests)
    except KeyboardInterrupt:
        print("\nBot stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Closing browser...")
        bot.close()

if __name__ == "__main__":
    main()

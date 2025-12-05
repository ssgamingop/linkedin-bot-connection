# LinkedIn Auto Connector

A Python script to automate sending connection requests on LinkedIn. It navigates to your "My Network" page and sends requests to suggested connections, helping you grow your network automatically.

## Features

-   **Automated Login**: Logs in securely using your credentials.
-   **Smart Navigation**: Goes directly to the "Grow My Network" page.
-   **Human-like Behavior**: Includes random delays between actions to mimic human interaction and reduce the risk of being flagged.
-   **Configurable**: Set the number of requests you want to send.

## Prerequisites

-   Python 3.10+
-   Google Chrome installed

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/linkedin-bot.git
    cd linkedin-bot
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up credentials**:
    -   Create a `.env` file in the root directory (or rename `.env.example`).
    -   Add your LinkedIn credentials:
        ```env
        LINKEDIN_EMAIL=your_email@example.com
        LINKEDIN_PASSWORD=your_password
        ```

## Usage

Run the script from the terminal, specifying the number of connection requests you want to send:

```bash
python main.py <number_of_requests>
```

**Example:**

To send 20 connection requests:

```bash
python main.py 20
```

## Disclaimer

**Use at your own risk.** Automated actions on LinkedIn can violate their Terms of Service. This bot includes delays to act like a human, but excessive use may still lead to account restrictions. It is recommended to run this with a low number of requests (e.g., 20-50) per day.

## License

MIT



New Edit : 1susuajsjhs
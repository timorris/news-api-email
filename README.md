# News API Emailer

This is a simple Python application that fetches the latest news on a specific topic from the News API and sends a curated email with the top articles.

## Features

*   Fetches news articles from the [News API](https://newsapi.org/).
*   Formats the articles into an HTML email.
*   Sends the email using the [Resend](https://resend.com/) API.
*   Uses a `.env` file for easy configuration of API keys.

## Getting Started

### Prerequisites

*   Python 3
*   `pip` for installing dependencies

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd news-api-email
    ```

2.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file with the following content):*
    ```
    requests
    python-dotenv
    resend
    ```

3.  **Create a `.env` file** in the root of the project and add your API keys:
    ```
    NEWS_API_KEY="your_news_api_key"
    RESEND_API_KEY="your_resend_api_key"
    ```

### Running the Application

To run the application, simply execute the `main.py` script:

```bash
python main.py
```

## Configuration

### Changing the News Topic

To change the news topic, edit the `topic` variable in `main.py`:

```python
topic = "your_topic_here"
```

### Changing Email Recipients

To change the email recipients, edit the `to` field in the `params` dictionary in `send_email.py`:

```python
params: resend.Emails.SendParams = {
    "from": "send@ohm.run",
    "to": ["recipient1@example.com", "recipient2@example.com"],
    "subject": "Today's News!",
    "html": html_content,
    "reply_to": "your_email@example.com"
}
```

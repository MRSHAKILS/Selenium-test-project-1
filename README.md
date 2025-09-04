# Selenium Web Automation Project

A Python-based web automation project using Selenium WebDriver with two different approaches for web scraping and automation.

## Project Structure

```
chromedriver.exe          # Chrome WebDriver executable
main.py                   # Local Chrome automation script
main2.py                  # Remote browser automation with proxy
README.md                 # Project documentation
```

## Files Overview

### main.py
A local Selenium automation script that:
- Uses local Chrome WebDriver via `chromedriver.exe`
- Performs a Google search for "sky"
- Implements anti-detection measures
- Uses explicit waits for reliable element interactions

### main2.py
A remote browser automation script that:
- Connects to Scraping Browser via proxy service
- Takes screenshots of web pages
- Implements advanced anti-detection techniques
- Scrapes page content from Google

## Requirements

```bash
pip install selenium
```

## Setup

1. Ensure `chromedriver.exe` is in the project directory
2. For `main2.py`, you'll need valid Scraping Browser credentials
3. Install required Python packages

## Usage

### Local Automation (main.py)
```bash
python main.py
```

### Remote Browser Automation (main2.py)
```bash
python main2.py
```

## Features

- **Anti-Detection**: Both scripts include measures to avoid bot detection
- **Error Handling**: Proper exception handling and resource cleanup
- **Explicit Waits**: Reliable element waiting strategies
- **Screenshot Capability**: Page screenshot functionality in `main2.py`
- **Human-like Behavior**: Random delays to simulate human interaction

## Notes

- `main.py` requires a local Chrome installation and matching ChromeDriver version
- `main2.py` uses a remote proxy service for enhanced anonymity
- Both scripts implement various anti-bot detection measures

## License

This project is for educational purposes only.
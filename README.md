# DevOps Automation Project

![CI/CD Workflow](https://github.com/testorgreposi/devops-automation/actions/workflows/ci.yml/badge.svg)

A complete Python DevOps repository configured with **GitHub Actions CI/CD automation**, **Verbose Debugging Capabilities**, **Automated Team Push Alerts**, code linting (**Flake8**), and unit testing (**Pytest**).

## 🚀 Features

- **Automated CI/CD Pipeline**: GitHub Actions triggers on `push` to `main`, `pull_request` to `main`, and manual dispatch (`workflow_dispatch`).
- **Matrix Testing**: Test matrix execution across Python versions `3.10`, `3.11`, and `3.12`.
- **🐞 Verbose Debugging**: Built-in `logging` module with `--debug` CLI flag and `LOG_LEVEL=DEBUG` environment variable support.
- **📢 Team Push Alerts**: Automatically notifies team members on GitHub Actions and via Webhook (Slack / Discord / Teams / Telegram) when code is pushed.
- **Code Quality**: PEP 8 compliance via `flake8` and automated testing via `pytest`.

## 📁 Repository Structure

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions CI/CD & Notification workflow
├── app/
│   └── main.py              # Application entry point with debug logging
├── requirements.txt         # Project dependencies
├── tests/
│   └── test_main.py         # Pytest unit tests
└── README.md                # Project documentation
```

## 🛠️ Local Development & Debugging

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Application (Standard Mode)**:
   ```bash
   python app/main.py
   ```

3. **Run Application (Debug Mode)**:
   ```bash
   python app/main.py --debug
   # or
   LOG_LEVEL=DEBUG python app/main.py
   ```

4. **Run Unit Tests**:
   ```bash
   python -m pytest
   ```

5. **Run Code Linter**:
   ```bash
   python -m flake8 app tests
   ```

## 📢 Configuring Webhook Team Push Alerts

When any team member pushes code, GitHub Actions logs the push alert to the **Workflow Step Summary** visible to all team members.

To receive instant chat notifications in **Slack** or **Discord**:
1. Go to **Settings > Secrets and variables > Actions** in your GitHub repository.
2. Add a new repository secret named `WEBHOOK_URL` (or `SLACK_WEBHOOK_URL` / `DISCORD_WEBHOOK_URL`).
3. Paste your incoming Webhook URL.
# DevOps Automation Project

![CI/CD Workflow](https://github.com/testorgreposi/devops-automation/actions/workflows/ci.yml/badge.svg)

A complete Python DevOps repository configured with **GitHub Actions CI/CD automation**, automated code linting with **Flake8**, and unit testing with **Pytest**.

## 🚀 Features

- **Automated CI/CD Pipeline**: GitHub Actions runs on `push` to `main`, `pull_request` to `main`, and manual dispatch (`workflow_dispatch`).
- **Matrix Testing**: Test matrix execution across Python versions `3.10`, `3.11`, and `3.12`.
- **Code Linting**: PEP 8 standards enforcement via `flake8`.
- **Unit Testing**: Test suite execution via `pytest`.
- **Dependency Caching**: Pip caching enabled for faster workflow executions.

## 📁 Repository Structure

```text
.
├── .flake8                  # Flake8 linter configuration
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions automation workflow
├── app/
│   ├── __init__.py          # App package initialization
│   └── main.py              # Application entry point and math utilities
├── pytest.ini               # Pytest configuration
├── requirements.txt         # Project dependencies
├── tests/
│   ├── __init__.py          # Test package initialization
│   └── test_main.py         # Automated pytest unit tests
└── README.md                # Project documentation
```

## 🛠️ Local Development & Testing

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Application**:
   ```bash
   python app/main.py
   ```

3. **Run Unit Tests**:
   ```bash
   pytest
   ```

4. **Run Code Linter**:
   ```bash
   flake8 app tests
   ```

## 🤖 Continuous Integration

The GitHub Actions workflow triggers automatically on:
- Pushes to the `main` branch
- Pull Requests targeting the `main` branch
- Manual workflow triggers via GitHub UI
<div align="center">

# KSA

**Regional VAT & tax compliance for Saudi Arabia, built on [Frappe](https://frappeframework.com) / [ERPNext](https://erpnext.com).**

[![CI](https://github.com/kodlyft/ksa/actions/workflows/ci.yml/badge.svg)](https://github.com/kodlyft/ksa/actions/workflows/ci.yml)
[![Linters](https://github.com/kodlyft/ksa/actions/workflows/linter.yml/badge.svg)](https://github.com/kodlyft/ksa/actions/workflows/linter.yml)
[![Release](https://github.com/kodlyft/ksa/actions/workflows/release.yml/badge.svg)](https://github.com/kodlyft/ksa/actions/workflows/release.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)

</div>

---

## Overview

**KSA** is a Frappe app that adds Kingdom of Saudi Arabia VAT and tax compliance
capabilities on top of Frappe / ERPNext. It is designed to be installed on any
Frappe bench and configured per company.

## Requirements

| Dependency       | Version         |
| ---------------- | --------------- |
| Frappe Framework | v16             |
| ERPNext          | v16 (optional)  |
| Python           | >= 3.14         |

## Installation

Install with the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/kodlyft/ksa --branch develop
bench --site your-site.com install-app ksa
```

## Development

This app uses `pre-commit` for formatting and linting. After cloning:

```bash
cd apps/ksa
pip install pre-commit
pre-commit install
pre-commit install --hook-type commit-msg
```

Configured hooks:

- **ruff**: Python linting, import sorting, and formatting
- **prettier**: JS / Vue / SCSS formatting
- **eslint**: JavaScript linting
- **Frappe semgrep rules**: vendored static-analysis rules (see [`.semgrep`](.semgrep))
- **commitlint**: enforces [Conventional Commits](https://www.conventionalcommits.org/)

## Continuous Integration

This repository ships a full CI/CD suite via GitHub Actions:

| Workflow | Trigger | Purpose |
| -------- | ------- | ------- |
| [`ci.yml`](.github/workflows/ci.yml) | push to `develop`, PRs | Installs the app on a fresh bench and runs unit tests |
| [`linter.yml`](.github/workflows/linter.yml) | PRs | Pre-commit, Frappe semgrep rules, and `pip-audit` dependency scan |
| [`semantic-commits.yml`](.github/workflows/semantic-commits.yml) | PRs | Validates commit titles against Conventional Commits |
| [`release.yml`](.github/workflows/release.yml) | push to `develop` | Automated semantic versioning + GitHub releases |

[Dependabot](.github/dependabot.yml) keeps GitHub Actions and Python dependencies up to date weekly.

## Contributing

Contributions are welcome! Please read the [Contributing Guide](CONTRIBUTING.md)
and our [Code of Conduct](CODE_OF_CONDUCT.md) before opening a pull request.

- Report bugs with the [Bug Report](https://github.com/kodlyft/ksa/issues/new?template=bug_report.md) template.
- Suggest features with the [Feature Request](https://github.com/kodlyft/ksa/issues/new?template=feature_request.md) template.
- Found a security issue? See the [Security Policy](SECURITY.md).

## License

[MIT](LICENSE) © [Kodlyft](https://kodlyft.com)

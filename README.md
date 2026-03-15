# Web Security Test – Shopify Demo Login

![Security Scan](https://github.com/eu-MicheleOliveira/shopify-login-security-test/actions/workflows/zap-scan.yml/badge.svg)

Este repositório contém um experimento de segurança realizado em uma página de login de demonstração pública do Shopify.


URL:
https://sauce-demo.myshopify.com/account/login

O objetivo era avaliar a robustez do endpoint de autenticação contra entradas malformadas usando testes de fuzzing.

## Tools

- OWASP ZAP
- Manual fuzzing
- HTTP request analysis

## Test Types

- Input fuzzing
- Request manipulation
- Passive security scanning

## Objetivo

Demonstração de metodologia de pesquisa e teste em segurança educacional.

## Automated Security Scan

Automated baseline scans are executed using OWASP ZAP.

Reports generated:

- HTML security report
- JSON machine-readable report
- Markdown vulnerability report

Latest report:

reports/last-zap-report.md

## Security Dashboard

Security Score:

![score](reports/security-score.md)

Vulnerability Distribution

![chart](reports/vulnerability-chart.png)

Pipeline Status

![pipeline](https://github.com/eu-MicheleOliveira/shopify-login-security-test/actions/workflows/zap-scan.yml/badge.svg)
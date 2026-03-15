## # Relatório de Vulnerabilidades

Alvo:
https://sauce-demo.myshopify.com

Data:
14/03/2026

Scanner:
OWASP ZAP

---

## Resumo

Nenhuma vulnerabilidade crítica foi detectada durante os testes de fuzzing.

O endpoint de login lidou com entradas malformadas sem gerar erros no servidor.

## Os payloads testados incluíram:
- SQL injection strings
- XSS scripts
- null byte injection
- path traversal attempts

## Observações
Todas as tentativas de fuzzing retornaram respostas HTTP 400.

Esse comportamento indica que o aplicativo valida as solicitações recebidas e rejeita payloads malformados.

Nenhum erro do lado do servidor (HTTP 500) foi observado durante os testes.

Isso sugere que o endpoint de login lida com entradas inesperadas de forma segura.
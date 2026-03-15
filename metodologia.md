# Testing Methodology

The security testing process followed a black-box approach.

## Target

Login endpoint:

/account/login

## Ferramentas:

O OWASP ZAP foi usado para interceptar e manipular requisições HTTP.

## Test Strategy

Os seguintes testes de segurança foram realizados: 

- fuzz testing on login parameters
- malformed payload injection
- validation of server responses
- analysis of HTTP status codes

## Payload Categories

Os payloads de fuzzing incluíam:
- SQL injection attempts
- XSS payloads
- null byte injection
- path traversal strings

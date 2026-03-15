# Fuzzing Tests

The login endpoint was tested with malformed and unexpected inputs.

Test cases included:

- SQL injection attempts
- Script injection payloads
- Long input strings
- Invalid encoding characters

Example payloads:

' OR '1'='1
<script>alert(1)</script>
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

Results:

All malformed requests returned HTTP 400 responses,
indicating that the application validates invalid input.
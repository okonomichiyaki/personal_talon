tag: user.kotlin
-
^tick funky <user.text>$:
  "fun `{text or ''}`() {{}}"
  key(left)
  key(enter)
^test funky <user.text>$:
  "@Test"
  key(enter)
  "fun `{text or ''}`() {{}}"
  key(left)
  key(enter)

os: mac
and app.bundle: com.google.Chrome
-
spelunk index production [<user.text>]: "index=production application={text or ''}"
spelunk index stage [<user.text>]: "index=stage application={text or ''}"
spelunk index stage cloud [<user.text>]: "index=stage provider=gcp application={text or ''}"
spelunk index quality [<user.text>]: "index=qa application={text or ''}"

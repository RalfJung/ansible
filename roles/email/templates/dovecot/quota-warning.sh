#!/bin/sh
set -e

PERCENT=$1
FROM="{{postfix.postmaster}}"

msg="From: $FROM
To: $USER
CC: $FROM
Subject: Dein Posteingang ist $PERCENT% voll / Your mailbox is $PERCENT% full
Content-Type: text/plain; charset=UTF-8

Dein Posteingang ist zu $PERCENT% voll. Bitte räume etwas auf!

Your mailbox is now $PERCENT% full. Please clean it up a bit!"

echo -e "$msg" | /usr/sbin/sendmail -f "$FROM" "$USER" "$FROM"

exit 0

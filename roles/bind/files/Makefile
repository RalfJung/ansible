include Makefile.conf

user      ?= bind
zonemaker ?= zonemaker/zonemaker
RNDC      ?= /usr/sbin/rndc

# heres comes the magic
zonefiles = $(addprefix db.,${zones})
all: ${zonefiles}
.PHONY: all

db.%: db.%.py
	@echo $* $< $@
	@sudo -u ${user} ${zonemaker} $< > $@ || rm -f $@
	@cat $@
	@echo
	@${RNDC} reload $* # this only returns errors if the zone had not previously been loaded :-/
	@sleep 1
	@fgrep 'zone '$*'/IN' /var/log/syslog | tail -n 5

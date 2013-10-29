# Branislav Blaskovic <branislav@blaskovic.sk>
# Tomas Meszaros <exo@tty.sk>


NAME = fedora-gooey-karma
BINDIR = /usr/bin
DATADIR = /usr/share

all:

run:
	./src/fedora-gooey-karma

install:
	mkdir -p $(DESTDIR)$(DATADIR)/$(NAME)
	install -D -p -m 755 src/$(NAME) $(DESTDIR)$(BINDIR)/$(NAME)
	install -D -p -m 644 src/*.py $(DESTDIR)$(DATADIR)/$(NAME)/
	mkdir -p $(DESTDIR)$(DATADIR)/applications
	install -D -p -m 644 $(NAME).desktop $(DESTDIR)$(DATADIR)/applications/
	cp -r icons/* $(DESTDIR)$(DATADIR)/icons/hicolor/
	chmod 644 $(DESTDIR)$(DATADIR)/icons/hicolor/*/apps/$(NAME).png

uninstall:
	rm -rf $(DESTDIR)$(DATADIR)/$(NAME)
	rm -f $(DESTDIR)$(BINDIR)/$(NAME)
	rm -f $(DESTDIR)$(DATADIR)/applications/$(NAME).desktop
	rm -f $(DESTDIR)$(DATADIR)/icons/hicolor/*/apps/$(NAME).png

clean:
	rm src/*.pyc

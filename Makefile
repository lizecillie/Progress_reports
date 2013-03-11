all: p1 p2

p1:
	$(MAKE) -f Makefile.include TARGET=Vorderingsverslag1

p2:
	$(MAKE) -f Makefile.include TARGET=Progress_report2


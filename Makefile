all: p1 p2 p3

p1:
	$(MAKE) -f Makefile.include TARGET=Vorderingsverslag1

p2:
	$(MAKE) -f Makefile.include TARGET=Progress_report2

p3:
	$(MAKE) -f Makefile.include TARGET=Progress_report3

slides1:
	$(MAKE) -f Makefile.include TARGET=ProjectProposalPresentation

final:
	$(MAKE) -f Makefile.include TARGET=Final_report

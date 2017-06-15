all: generate.sh degenerate.sh

generate.sh:sample.yaml
	./orchestrate.py generate
	chmod +x generate.sh

degenerate.sh:sample.yaml
	./orchestrate.py degenerate
	chmod +x degenerate.sh
clean:
	rm -f generate.sh degenerate.sh
install:generate.sh
	./generate.sh
uninstall:degenerate.sh
	./degenerate.sh

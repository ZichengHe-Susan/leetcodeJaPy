.PHONY: run java-run py-run clean
.NOTPARALLEL:

# Usage examples:
# make run DIR=java/34_Find_First_And_Last
# make run DIR=python3/python3_template
# make java-run DIR=java/java_template
# make py-run DIR=python3/python3_template

# Auto-detect and run Solution in the provided directory.
run:
	@if [ -z "$(DIR)" ]; then \
	  echo "Usage: make run DIR=path/to/problem_dir"; exit 1; \
	fi
	@if [ -f "$(DIR)/src/Solution.java" ]; then \
	  echo "[JAVA] Compiling and running: $(DIR)"; \
	  mkdir -p "$(DIR)/out"; \
	  javac -d "$(DIR)/out" "$(DIR)"/src/*.java; \
	  java -cp "$(DIR)/out" Solution; \
	elif [ -f "$(DIR)/solution.py" ]; then \
	  echo "[PYTHON] Running: $(DIR)"; \
	  python3 "$(DIR)/solution.py"; \
	else \
	  echo "No Solution found. Expected either $(DIR)/src/Solution.java or $(DIR)/solution.py"; exit 1; \
	fi

# Force Java run (useful if both exist, or for clarity)
java-run:
	@if [ -z "$(DIR)" ]; then \
	  echo "Usage: make java-run DIR=path/to/java_problem_dir"; exit 1; \
	fi
	@if [ ! -f "$(DIR)/src/Solution.java" ]; then \
	  echo "Missing $(DIR)/src/Solution.java"; exit 1; \
	fi
	@echo "[JAVA] Compiling and running: $(DIR)"
	@mkdir -p "$(DIR)/out"
	@javac -d "$(DIR)/out" "$(DIR)"/src/*.java
	@java -cp "$(DIR)/out" Solution

# Force Python run
py-run:
	@if [ -z "$(DIR)" ]; then \
	  echo "Usage: make py-run DIR=path/to/python_problem_dir"; exit 1; \
	fi
	@if [ ! -f "$(DIR)/solution.py" ]; then \
	  echo "Missing $(DIR)/solution.py"; exit 1; \
	fi
	@echo "[PYTHON] Running: $(DIR)"
	@python3 "$(DIR)/solution.py"

# Clean build artifacts for a given directory
clean:
	@if [ -z "$(DIR)" ]; then \
	  echo "Usage: make clean DIR=path/to/problem_dir"; exit 1; \
	fi
	@echo "Cleaning: $(DIR)/out"
	@rm -rf "$(DIR)/out"



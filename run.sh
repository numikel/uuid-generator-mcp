set -e

REPO_URL="git+https://github.com/twoja-nazwa/twoje-repo.git"

# Nazwa polecenia, którą zdefiniowaliśmy w pyproject.toml
COMMAND_TO_RUN="generate-uuid"

TEMP_DIR=$(mktemp -d)
trap 'rm -rf "$TEMP_DIR"' EXIT

cd "$TEMP_DIR"

python3 -m venv .venv
./.venv/bin/pip install --quiet "$REPO_URL"
./.venv/bin/$COMMAND_TO_RUN "$@"
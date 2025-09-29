#!/bin/bash
cd ~/blockchain-infinite-l3

# Rotate between multiple files
FILES=("log.txt" "notes.md" "todo.py" "updates.md")
FILE=${FILES[$RANDOM % ${#FILES[@]}]}

# Random commit messages
MESSAGES=("Refactor code" "Update configs" "Fix bug" "Improve docs" "Enhance script" "Small update")
MESSAGE=${MESSAGES[$RANDOM % ${#MESSAGES[@]}]}

# Make small change
echo "Update on $(date)" >> $FILE

# Commit & push
git add $FILE
git commit -m "$MESSAGE ($(date +'%Y-%m-%d %H:%M:%S'))"
git push origin main

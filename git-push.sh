#!/bin/bash

# Change to your Processing project directory
cd "/Users/meerahbinteliah/Desktop/University Work/senior-project"

# Add all changes
git add .

# Prompt for commit message
echo "Enter commit message:"
read commit_message

# Commit changes
git commit -m "$commit_message"

# Push to remote repository
git push origin main

echo "Changes pushed successfully!"
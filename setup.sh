#!/bin/bash

# Determine the directory of the script
SCRIPT_DIR="$(dirname "$(realpath "$0")")"

# Path to the Python script
SCRIPT_PATH="$SCRIPT_DIR/XCrafter.py"

# Alias command to add
ALIAS_COMMAND="alias xcrafter='python3 $SCRIPT_PATH'"

# Function to add alias to a profile file if it exists
add_alias_to_profile() {
    local profile_file="$1"

    if [ -f "$profile_file" ]; then
        # Check if the alias already exists
        if grep -Fxq "$ALIAS_COMMAND" "$profile_file"; then
            echo "Alias already exists in $profile_file"
        else
            echo "$ALIAS_COMMAND" >> "$profile_file"
            echo "Alias added to $profile_file"
        fi
    fi
}

# Add the alias to .bash_profile and .zshrc if they exist
add_alias_to_profile "$HOME/.bash_profile"
add_alias_to_profile "$HOME/.zshrc"

# Reload the terminal configuration
if [ -n "$ZSH_VERSION" ]; then
    source "$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    source "$HOME/.bash_profile"
else
    # Reload both configurations if we can't determine the shell
    [ -f "$HOME/.bash_profile" ] && source "$HOME/.bash_profile"
    [ -f "$HOME/.zshrc" ] && source "$HOME/.zshrc"
fi

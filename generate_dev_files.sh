#!/bin/bash

# Script to generate developer files with programming language rules and guidelines
# Structure: developer-name.programming-language.topic.md

set -e

# Arrays of data
DEVELOPERS=("ghonDou" "sarahLee" "alexChen" "mariaSilva" "johnSmith" "linaWang" "davidJones" "annaKowalski" "rajPatel" "emmaWhite")
LANGUAGES=("golang" "python" "javascript" "react" "typescript")
DIRECTORIES=("eyes" "fleet" "flex" "ido" "mind")

# Topics for each language
declare -A TOPICS
TOPICS[golang]="code-styling error-handling testing concurrency performance"
TOPICS[python]="code-styling testing packaging performance async"
TOPICS[javascript]="code-styling testing async modules performance"
TOPICS[react]="components hooks state-management performance testing"
TOPICS[typescript]="types interfaces modules performance testing"

# Function to get random element from array
get_random_element() {
    local arr=("$@")
    local rand_index=$((RANDOM % ${#arr[@]}))
    echo "${arr[$rand_index]}"
}

# Function to generate content based on language and topic
generate_content() {
    local language=$1
    local topic=$2
    local content_file="/tmp/content_${language}_${topic}.md"
    
    case "${language}-${topic}" in
        "golang-code-styling")
            cat > "$content_file" << 'EOF'
# Golang Code Styling Guidelines

## General Principles
- Use `gofmt` to format your code automatically
- Follow the official Go Code Review Comments guidelines
- Use camelCase for exported functions and PascalCase for types

## Naming Conventions
- Package names should be short, lowercase, single words
- Interface names should end with 'er' when possible
- Use descriptive names for variables with longer scope

## Function Structure
- Keep functions small and focused on a single responsibility
- Group related functionality into packages
- Use early returns to reduce nesting

## Comments
- Comment exported functions, types, and variables
- Use complete sentences in comments
- Avoid obvious comments

## Error Handling
- Always handle errors explicitly
- Don't ignore errors with `_`
- Use custom error types when appropriate

## Code Organization
```go
// Group type definitions
type (
    User struct {
        ID   int
        Name string
    }
    
    UserService interface {
        GetUser(id int) (*User, error)
        CreateUser(name string) (*User, error)
    }
)

// Then constants
const (
    MaxRetries = 3
    Timeout    = 30 * time.Second
)

// Then variables
var (
    ErrUserNotFound = errors.New("user not found")
    DefaultConfig   = Config{Timeout: Timeout}
)

// Finally functions
func NewUserService() UserService {
    return &userService{}
}
```
EOF
            ;;
        "golang-error-handling")
            cat > "$content_file" << 'EOF'
# Golang Error Handling Best Practices

## Core Principles
- Errors are values, not exceptions
- Handle errors immediately where they occur
- Don't ignore errors

## Error Creation
```go
// Use errors.New for simple errors
err := errors.New("something went wrong")

// Use fmt.Errorf for formatted errors (avoid wrapping unless necessary)
err := fmt.Errorf("failed to process %s", filename)

// Return original errors when possible
if err != nil {
    return err // Don't wrap unless adding context
}
```

## Error Checking Pattern
```go
result, err := someOperation()
if err != nil {
    l.Error().Err(err).Str("operation", "someOperation").Msg("FUNCTION_NAME - operation failed")
    return err
}
```

## Logging Format
- With error: `l.Error().Err(err).Str("param", param).Msg("FUNCTION_NAME - SHORT label")`
- Without error: `l.Info().Str("param", param).Msg("FUNCTION_NAME - SHORT label")`

## Custom Error Types
- Implement the error interface for domain-specific errors
- Use sentinel errors for expected error conditions
- Return generic error codes in HTTP responses, avoid err.Error()

## Testing Errors
- Test both success and failure paths
- Use `github.com/stretchr/testify/require` for tests
- Verify error behavior, not specific error messages
EOF
            ;;
        "python-code-styling")
            cat > "$content_file" << 'EOF'
# Python Code Styling Guidelines

## PEP 8 Compliance
- Use 4 spaces for indentation
- Line length maximum of 79 characters
- Use snake_case for variables and functions
- Use PascalCase for classes

## Import Organization
```python
# Standard library imports
import os
import sys

# Third-party imports
import requests
import numpy as np

# Local imports
from myapp import models
from . import utils
```

## Dependency Management
- Use uv for dependency management
- Lock versions in requirements.txt
- Include constraints.txt for transitive dependencies

## Function and Class Design
- Keep functions small and focused
- Use type hints for better code documentation
- Follow the single responsibility principle

## Naming Conventions
- Variables: `user_name`, `total_count`
- Functions: `calculate_total()`, `send_email()`
- Classes: `UserManager`, `EmailService`
- Constants: `MAX_RETRIES`, `DEFAULT_TIMEOUT`

## Documentation
- Use docstrings for modules, classes, and functions
- Follow Google or NumPy docstring style
- Include examples in docstrings when helpful
EOF
            ;;
        "javascript-code-styling")
            cat > "$content_file" << 'EOF'
# JavaScript Code Styling Guidelines

## ESLint and Prettier
- Use ESLint for code linting
- Use Prettier for code formatting
- Configure both in your project

## Variable Declarations
- Use `const` by default
- Use `let` when reassignment is needed
- Avoid `var` completely

## Function Declarations
```javascript
// Prefer arrow functions for short functions
const add = (a, b) => a + b;

// Use function declarations for named functions
function calculateTotal(items) {
    return items.reduce((sum, item) => sum + item.price, 0);
}
```

## Object and Array Destructuring
```javascript
// Object destructuring
const { name, age } = user;

// Array destructuring
const [first, second] = items;

// Function parameters
function greet({ name, age = 0 }) {
    return `Hello ${name}, you are ${age} years old`;
}
```

## Modern Syntax
- Use template literals for string interpolation
- Use optional chaining (?.) and nullish coalescing (??)
- Prefer async/await over Promise chains

## Component Organization
- Break big components into smaller ones
- Use TanStack Query for data fetching
- Follow pages directory structure
EOF
            ;;
        "react-components")
            cat > "$content_file" << 'EOF'
# React Components Best Practices

## Functional Components
- Always use functional components over class components
- Keep components small and focused
- Use TypeScript for better type safety

## Component Structure
```jsx
import React from 'react';
import PropTypes from 'prop-types';

const UserCard = ({ user, onEdit, className = '' }) => {
    return (
        <div className={`user-card ${className}`}>
            <h3>{user.name}</h3>
            <p>{user.email}</p>
            <button onClick={() => onEdit(user.id)}>
                Edit User
            </button>
        </div>
    );
};

UserCard.propTypes = {
    user: PropTypes.shape({
        id: PropTypes.number.isRequired,
        name: PropTypes.string.isRequired,
        email: PropTypes.string.isRequired,
    }).isRequired,
    onEdit: PropTypes.func.isRequired,
    className: PropTypes.string,
};

export default UserCard;
```

## Styling with Tailwind CSS
- Use Tailwind CSS with separate themes per feature
- Reference `fleet/frontend/tailwind.config.js`
- Break components into smaller, manageable pieces

## Component Organization
- One component per file
- Use index.js files for cleaner imports
- Group related components in folders
- Separate presentation and container components
EOF
            ;;
        *)
            # Default content for any other combination
            cat > "$content_file" << EOF
# ${language^} ${topic//-/ } Guidelines

## Overview
This document contains best practices and guidelines for ${topic//-/ } in ${language^}.

## Key Principles
1. Write clean, readable code
2. Follow established conventions
3. Test your code thoroughly
4. Document important decisions
5. Keep learning and improving

## Best Practices
- Follow the community standards for ${language}
- Use appropriate tools and frameworks
- Write comprehensive tests
- Document your code properly
- Review code regularly

## Code Style
- Make the SMALLEST reasonable changes
- Match surrounding code style
- Never make unrelated changes
- Don't add fallback/legacy code
- Never name things as 'improved', 'new', 'enhanced'

## Testing Guidelines
- Ask before implementing tests
- Never ignore system output or test results
- Test output must be pristine to pass
- Use proper testing frameworks

## Common Pitfalls
- Not following established patterns
- Ignoring performance implications
- Insufficient testing
- Poor error handling
- Lack of documentation

---
*This document contains ${language} ${topic//-/ } guidelines and best practices.*
EOF
            ;;
    esac
    
    echo "$content_file"
}

# Function to create files for a directory
create_files_for_directory() {
    local directory=$1
    local files_created=0
    
    # Generate 3-6 files per directory
    local num_files=$((3 + RANDOM % 4))
    
    echo "📁 Processing directory: $directory"
    
    for ((i=1; i<=num_files; i++)); do
        # Select random developer
        local developer=$(get_random_element "${DEVELOPERS[@]}")
        
        # Select random language
        local language=$(get_random_element "${LANGUAGES[@]}")
        
        # Get topics for the selected language and pick one randomly
        local topics_string="${TOPICS[$language]}"
        local topics_array=($topics_string)
        local topic=$(get_random_element "${topics_array[@]}")
        
        # Create filename
        local filename="${developer}.${language}.${topic}.md"
        local filepath="${directory}/${filename}"
        
        # Generate content
        local content_file=$(generate_content "$language" "$topic")
        
        # Copy content to final file
        cp "$content_file" "$filepath"
        rm "$content_file"
        
        echo "   ✅ Created: $filename"
        ((files_created++))
    done
    
    echo "   📊 Created $files_created files in $directory"
    return $files_created
}

# Main function
main() {
    echo "🚀 Generating developer files..."
    echo "=================================="
    
    local total_files=0
    
    for directory in "${DIRECTORIES[@]}"; do
        if [ -d "$directory" ]; then
            echo
            create_files_for_directory "$directory"
            local dir_files=$?
            ((total_files += dir_files))
        else
            echo "⚠️  Directory $directory does not exist, skipping..."
        fi
    done
    
    echo
    echo "=================================="
    echo "✅ Successfully created $total_files files across ${#DIRECTORIES[@]} directories"
    echo
    echo "📋 File naming pattern: developer-name.programming-language.topic.md"
    echo "📝 Each file contains relevant rules and guidelines for the specified topic."
    echo
    echo "🗂️  Generated files structure:"
    for directory in "${DIRECTORIES[@]}"; do
        if [ -d "$directory" ]; then
            echo "   $directory/:"
            ls -1 "$directory"/*.md 2>/dev/null | sed 's/^/     /' || echo "     (no files)"
        fi
    done
}

# Run main function
main "$@" 
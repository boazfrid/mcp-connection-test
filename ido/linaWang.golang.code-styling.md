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

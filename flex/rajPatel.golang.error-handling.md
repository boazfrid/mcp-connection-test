# Golang Error Handling Best Practices

## Core Principles
- Errors are values, not exceptions
- Handle errors immediately where they occur
- Don't ignore errors

## Error Creation
```go
// Use errors.New for simple errors
err := errors.New("something went wrong")

// Use fmt.Errorf for formatted errors
err := fmt.Errorf("failed to process %s: %w", filename, originalErr)
```

## Error Checking
```go
if err != nil {
    return fmt.Errorf("operation failed: %w", err)
}
```

## Custom Error Types
- Implement the error interface for domain-specific errors
- Use error wrapping to preserve context
- Consider sentinel errors for expected error conditions

## Testing Errors
- Test both success and failure paths
- Verify error messages and types
- Use testify/assert for error testing

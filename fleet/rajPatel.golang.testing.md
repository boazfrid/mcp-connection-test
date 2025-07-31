# Golang Testing Guidelines

## Test Structure
- Follow the AAA pattern: Arrange, Act, Assert
- Use table-driven tests for multiple scenarios
- Keep tests simple and focused

## Test Naming
- Use descriptive test function names
- Format: `TestFunctionName_Scenario_ExpectedResult`
- Example: `TestCalculateTotal_WithValidItems_ReturnsCorrectSum`

## Test Organization
```go
func TestCalculator(t *testing.T) {
    tests := []struct {
        name     string
        input    int
        expected int
    }{
        {"positive number", 5, 5},
        {"zero", 0, 0},
        {"negative number", -3, -3},
    }
    
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            result := Calculate(tt.input)
            assert.Equal(t, tt.expected, result)
        })
    }
}
```

## Best Practices
- Use testify/require for assertions that should stop the test
- Use testify/assert for non-critical assertions
- Mock external dependencies
- Test edge cases and error conditions

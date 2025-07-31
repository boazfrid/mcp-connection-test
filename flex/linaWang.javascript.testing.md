# JavaScript Testing Best Practices

## Testing Framework
- Use Jest for unit and integration testing
- Use Testing Library for React component testing
- Use Cypress or Playwright for E2E testing

## Test Structure
```javascript
describe('Calculator', () => {
    test('should add two numbers correctly', () => {
        // Arrange
        const a = 5;
        const b = 3;
        
        // Act
        const result = add(a, b);
        
        // Assert
        expect(result).toBe(8);
    });
});
```

## Mocking and Spies
```javascript
// Mock functions
const mockFn = jest.fn();
mockFn.mockReturnValue('mocked value');

// Spy on methods
const spy = jest.spyOn(object, 'method');
expect(spy).toHaveBeenCalledWith(expectedArgs);
```

## Async Testing
```javascript
test('async function test', async () => {
    const result = await fetchData();
    expect(result).toBeDefined();
});

test('promise rejection', async () => {
    await expect(failingFunction()).rejects.toThrow('Error message');
});
```

## Best Practices
- Write tests before or alongside code (TDD)
- Test behavior, not implementation
- Keep tests simple and focused
- Use descriptive test names

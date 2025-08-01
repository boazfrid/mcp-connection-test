#!/usr/bin/env python3
"""
Script to generate developer files with programming language rules and guidelines.
Structure: developer-name.programming-language.topic.md
"""

import os
import random
from pathlib import Path

# Developer names
DEVELOPERS = [
    "ghonDou", "sarahLee", "alexChen", "mariaSilva", "johnSmith",
    "linaWang", "davidJones", "annaKowalski", "rajPatel", "emmaWhite"
]

# Programming languages with their topics and content
LANGUAGE_CONTENT = {
    "golang": {
        "topics": ["code-styling", "error-handling", "testing", "concurrency", "performance"],
        "content": {
            "code-styling": """# Golang Code Styling Guidelines

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
""",
            "error-handling": """# Golang Error Handling Best Practices

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
""",
            "testing": """# Golang Testing Guidelines

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
""",
            "concurrency": """# Golang Concurrency Patterns

## Goroutines
- Use goroutines for concurrent operations
- Always have a way to stop goroutines
- Don't create goroutines without bounds

## Channels
- Use channels to communicate between goroutines
- Close channels when done sending
- Use buffered channels to prevent blocking

## Common Patterns

### Worker Pool
```go
func workerPool(jobs <-chan Job, results chan<- Result) {
    for job := range jobs {
        results <- processJob(job)
    }
}
```

### Fan-out/Fan-in
- Fan-out: distribute work across multiple goroutines
- Fan-in: collect results from multiple goroutines

### Pipeline
- Chain operations using channels
- Each stage processes data and passes to next stage

## Synchronization
- Use sync.Mutex for protecting shared state
- Use sync.WaitGroup to wait for goroutines
- Prefer channels over shared memory when possible
""",
            "performance": """# Golang Performance Optimization

## Profiling
- Use `go tool pprof` for performance analysis
- Profile CPU, memory, and goroutine usage
- Use benchmarks to measure performance

## Memory Management
- Avoid unnecessary allocations in hot paths
- Reuse slices and maps when possible
- Use object pools for expensive objects

## Optimization Techniques
- Use string.Builder for string concatenation
- Prefer slices over arrays for flexibility
- Use interfaces wisely - they have overhead

## Benchmarking
```go
func BenchmarkFunction(b *testing.B) {
    for i := 0; i < b.N; i++ {
        FunctionToTest()
    }
}
```

## Common Pitfalls
- Premature optimization
- Not measuring before optimizing
- Micro-optimizations at expense of readability
- Ignoring garbage collection impact
"""
        }
    },
    "python": {
        "topics": ["code-styling", "testing", "packaging", "performance", "async"],
        "content": {
            "code-styling": """# Python Code Styling Guidelines

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
""",
            "testing": """# Python Testing Best Practices

## Test Framework
- Use pytest as the primary testing framework
- Organize tests in separate test files/directories
- Use fixtures for setup and teardown

## Test Structure
```python
def test_function_name_scenario_expected_result():
    # Arrange
    input_data = {"key": "value"}
    
    # Act
    result = function_under_test(input_data)
    
    # Assert
    assert result == expected_value
```

## Test Organization
- Group related tests in classes
- Use parametrize for testing multiple scenarios
- Mock external dependencies

## Coverage and Quality
- Aim for high test coverage (>90%)
- Test edge cases and error conditions
- Use property-based testing with hypothesis

## Fixtures and Mocking
```python
@pytest.fixture
def sample_data():
    return {"id": 1, "name": "test"}

@mock.patch('module.external_service')
def test_with_mock(mock_service):
    mock_service.return_value = "mocked_response"
    # Test code here
```
""",
            "packaging": """# Python Packaging Guidelines

## Project Structure
```
project/
├── src/
│   └── mypackage/
│       ├── __init__.py
│       └── module.py
├── tests/
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Dependency Management
- Use virtual environments for isolation
- Pin dependency versions in requirements.txt
- Use requirements-dev.txt for development dependencies

## Setup Configuration
```toml
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mypackage"
version = "0.1.0"
description = "A sample package"
dependencies = [
    "requests>=2.25.0",
    "click>=7.0",
]
```

## Distribution
- Use semantic versioning (MAJOR.MINOR.PATCH)
- Include comprehensive README and CHANGELOG
- Use GitHub Actions for CI/CD
- Publish to PyPI using twine
""",
            "performance": """# Python Performance Optimization

## Profiling Tools
- Use cProfile for code profiling
- Use memory_profiler for memory analysis
- Use line_profiler for line-by-line analysis

## Common Optimizations
- Use list comprehensions over loops when appropriate
- Prefer generators for large datasets
- Use built-in functions (they're optimized in C)

## Data Structures
- Choose appropriate data structures (set vs list)
- Use collections module (deque, Counter, defaultdict)
- Consider numpy for numerical computations

## Algorithm Optimization
```python
# Bad: O(n²)
for i in list1:
    if i in list2:  # Linear search each time
        result.append(i)

# Good: O(n)
set2 = set(list2)  # Convert to set once
for i in list1:
    if i in set2:  # Constant time lookup
        result.append(i)
```

## Memory Management
- Use __slots__ for classes with many instances
- Delete large objects when done
- Use weak references to break circular references
""",
            "async": """# Python Asynchronous Programming

## asyncio Basics
- Use async/await for asynchronous operations
- Run async functions with asyncio.run()
- Use async context managers and iterators

## Common Patterns
```python
import asyncio
import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ["http://example1.com", "http://example2.com"]
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results
```

## Best Practices
- Don't mix blocking and non-blocking code
- Use asyncio.gather() for concurrent operations
- Handle exceptions properly in async code
- Use async libraries (aiohttp, asyncpg) for I/O

## Performance Considerations
- Async is best for I/O-bound operations
- Use thread pools for CPU-bound work
- Monitor event loop performance
- Avoid blocking operations in async functions
"""
        }
    },
    "javascript": {
        "topics": ["code-styling", "testing", "async", "modules", "performance"],
        "content": {
            "code-styling": """# JavaScript Code Styling Guidelines

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
""",
            "testing": """# JavaScript Testing Best Practices

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
"""
        }
    },
    "react": {
        "topics": ["components", "hooks", "state-management", "performance", "testing"],
        "content": {
            "components": """# React Components Best Practices

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

## Component Organization
- One component per file
- Use index.js files for cleaner imports
- Group related components in folders
- Separate presentation and container components
""",
            "hooks": """# React Hooks Guidelines

## Built-in Hooks
```jsx
import React, { useState, useEffect, useMemo, useCallback } from 'react';

const UserList = ({ users, onUserSelect }) => {
    const [filter, setFilter] = useState('');
    const [loading, setLoading] = useState(false);
    
    // Memoize expensive calculations
    const filteredUsers = useMemo(() => {
        return users.filter(user => 
            user.name.toLowerCase().includes(filter.toLowerCase())
        );
    }, [users, filter]);
    
    // Memoize callback functions
    const handleUserClick = useCallback((user) => {
        onUserSelect(user);
    }, [onUserSelect]);
    
    useEffect(() => {
        // Side effects here
        setLoading(true);
        // Cleanup function
        return () => {
            setLoading(false);
        };
    }, []);
    
    return (
        <div>
            <input 
                value={filter} 
                onChange={(e) => setFilter(e.target.value)} 
            />
            {filteredUsers.map(user => (
                <UserCard 
                    key={user.id} 
                    user={user} 
                    onClick={handleUserClick}
                />
            ))}
        </div>
    );
};
```

## Custom Hooks
- Extract reusable logic into custom hooks
- Start custom hook names with 'use'
- Return objects for multiple values
"""
        }
    }
}

def get_content_for_topic(language, topic):
    """Get content for a specific language and topic."""
    if language in LANGUAGE_CONTENT and topic in LANGUAGE_CONTENT[language]["content"]:
        return LANGUAGE_CONTENT[language]["content"][topic]
    
    # Fallback content if specific content not found
    return f"""# {language.title()} {topic.replace('-', ' ').title()} Guidelines

## Overview
This document contains best practices and guidelines for {topic.replace('-', ' ')} in {language.title()}.

## Key Principles
1. Write clean, readable code
2. Follow established conventions
3. Test your code thoroughly
4. Document important decisions
5. Keep learning and improving

## Best Practices
- Follow the community standards for {language}
- Use appropriate tools and frameworks
- Write comprehensive tests
- Document your code properly
- Review code regularly

## Resources
- Official {language} documentation
- Community style guides
- Popular frameworks and libraries
- Testing tools and practices

## Common Pitfalls
- Not following established patterns
- Ignoring performance implications
- Insufficient testing
- Poor error handling
- Lack of documentation

---
*This is a template document. Please customize with specific {language} {topic} guidelines.*
"""

def create_files_for_directory(directory_name):
    """Create files for a specific directory."""
    directory_path = Path(directory_name)
    
    # Select random developer names for this directory
    num_files = random.randint(3, 6)
    selected_developers = random.sample(DEVELOPERS, min(num_files, len(DEVELOPERS)))
    
    files_created = []
    
    for developer in selected_developers:
        # Select random language and topic
        language = random.choice(list(LANGUAGE_CONTENT.keys()))
        available_topics = LANGUAGE_CONTENT[language]["topics"]
        topic = random.choice(available_topics)
        
        # Create filename
        filename = f"{developer}.{language}.{topic}.md"
        filepath = directory_path / filename
        
        # Get content
        content = get_content_for_topic(language, topic)
        
        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        files_created.append(filename)
        print(f"Created: {filepath}")
    
    return files_created

def main():
    """Main function to create all files."""
    directories = ["eyes", "fleet", "flex", "ido", "mind"]
    
    print("Generating developer files...")
    print("=" * 50)
    
    total_files = 0
    for directory in directories:
        directory_path = Path(directory)
        if not directory_path.exists():
            print(f"📁 Creating directory: {directory}")
            directory_path.mkdir(parents=True, exist_ok=True)
        
        print(f"\n📁 Directory: {directory}")
        files = create_files_for_directory(directory)
        total_files += len(files)
        print(f"   Created {len(files)} files")
    
    print("\n" + "=" * 50)
    print(f"✅ Successfully created {total_files} files across {len(directories)} directories")
    print("\nFile naming pattern: developer-name.programming-language.topic.md")
    print("Each file contains relevant rules and guidelines for the specified topic.")

if __name__ == "__main__":
    main() 
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

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

## Component Organization
- One component per file
- Use index.js files for cleaner imports
- Group related components in folders
- Separate presentation and container components

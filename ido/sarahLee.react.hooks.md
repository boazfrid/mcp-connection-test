# React Hooks Guidelines

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

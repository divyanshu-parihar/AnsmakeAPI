
# AnsmakeAPi

Assignment for Internshala internship.

## Example Usage

Retrieve All Tasks : 
    ```Go to <localhost>/tasks/all```

Add a task : 

```curl -d "name=Task Random&description=This is a Random Test&email=divy@test.com" -X POST http://127.0.0.1:8000/tasks/new```

## Documentation
DATABASE: 
```**Postgres** [Remote Real Postgres Database with User and password is provided in **AnsmakeAPI/settings.py** ]```

```**2 routes**:``` 
\
```/tasks/all[**GET**]: ```\
  -- List all the Task in Task table \
  -- Tasks are shown in custom format
  
``` /tasks/new[**POST**]:``` \
  -- Add a new Task record to the Task Table \
  -- Exception handling done for invalid fields\
  

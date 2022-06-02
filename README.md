# AnsmakeAPI
Assignment Project

DATABASEL: **Postgres** [Testing Postgres Database with User and password is provided in **Ansmake/settings.py** ]

**2 routes**:
-- /tasks/all[**GET**]:
  -- List all the Task in Task table
  -- Tasks are shown in custom format
  
  
  **Example** : 
    GO to <localhost>/tasks/all
  
-- /tasks/new[**POST**]:
  -- Add a new Task record to the Task Table 
  -- Exception handling done for invalid fields
  
  **Example** : 
  curl -d "name=Task Random&description=This is a Random Test&email=Test@test.com" -X POST http://127.0.0.1:8000/tasks/new
  
  
  


  
 
 

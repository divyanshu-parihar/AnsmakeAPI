
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
  


ScreenShots:
![Screenshot from 2022-06-03 00-50-23](https://user-images.githubusercontent.com/58904683/171723334-2e963094-a445-43b8-b432-ab987a87e52e.png)
![Screenshot from 2022-06-03 00-52-03](https://user-images.githubusercontent.com/58904683/171723344-cc1f7610-5f78-4177-bd79-911b6cf90504.png)
![Screenshot from 2022-06-03 01-01-23](https://user-images.githubusercontent.com/58904683/171723348-f46c08b5-e132-4137-819d-ebb9a272c46b.png)


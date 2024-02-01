

This is a Test of some code - I wrote a basic stateless microservice and added a db with alchemy so I don't have to build up an enitire infrastructure for this to make sense.


POST payload http://localhost:8000/register

{
    "source_site": "test",
    "full_name": "tesdct user",
    "email": "asdasdsb@asdasd.com",
    "email_confirm": "asdasdsb@asdasd.com",
    "password": "asdasd123",
    "password_confirm": "asdasd123"
}


POST payload http://localhost:8000/users

{
    "source_site": "test",
}

POST payload http://localhost:8000/users/delete

{
    "source_site": "test",
    "user_id": "2"
}

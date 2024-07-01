Djoser URL paths

auth/
auth/users/ (list all users)
auth/users/me/ (get current user - GET)
auth/token/login/ (login - POST)
auth/token/logout/ (logout -POST)
 ------------------------
 Booking And Menu APIs
 / (to display the static page!)
 booking/tables/ (List all Bookings and add new one - GET, POST (Auth Required))
 menu/ (List all Menu Items and adds new item also - GET, POST (Auth Required))
 menu/<int:pk>/ (Views one menu item, edit and delete it  - GET, PUT, DELETE (Auth Required))
-------------------------
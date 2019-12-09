# homeworkSchedule
This is website where teachers can create/update/delete assignment and comments. Addtionally, 
it provided the APIs for mini WeChat program to fetch and post information.

## How to run it
* `pipenv install` to install required dependencies
* `pipenv shell` to enter virtual environment
* `python manage.py runserver` to start the server
*  You should see
    ```
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CONTROL-C.
    ```
## Pages
* Login: `http://127.0.0.1:8000/accounts/login/`
* Home Page: `http://127.0.0.1:8000/homePage/`
* Create Assignment: `http://127.0.0.1:8000/createAssignment/`
* Assignments Management by Class: `http://127.0.0.1:8000/classes/`
* View Assignment: `http://127.0.0.1:8000/assignment_preview/assignment_id/`
* Comment Management: `http://127.0.0.1:8000/comments/` 
* Django Admin private page(only debug purpose): `http://127.0.0.1:8000/admin/`

## Restful APIs
* View All Assignments: `http://127.0.0.1:8000/api/assignments/`
* Create/Update/Delete Assignment: `http://127.0.0.1:8000/api/assignments/assignment_id`
* View All Classes: `http://127.0.0.1:8000/api/classes/`
* View All Comments: `http://127.0.0.1:8000/api/comments/`
* Create/Update/Delete Comments: `http://127.0.0.1:8000/api/comments/comment_id`

 

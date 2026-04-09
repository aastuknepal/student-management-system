from rest_framework import permissions

#Helper function
def is_admin(user):
    return user.is_authenticated and (user.is_superuser or user.groups.filter(name='Admin').exists())

def is_teacher(user):
    return user.is_authenticated and user.groups.filter(name='Teacher').exists()

def is_student(user):
    return user.is_authenticated and user.groups.filter(name='Student').exists()


#Permission classes


class CourseAccessPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:

            #Students, Teachers, and Admins can view Courses
            return request.user.is_authenticated
        
        # Only admins can add /edit/delete Course
        return is_admin(request.user)
    
class TeacherAccessPermission(permissions.BasePermission):

    def has_permission(self, requet, view ):

        # Students, Teachers and Admin can view teachers
        if requet.method in permissions.SAFE_METHODS:
            return is_teacher(requet.user) or is_admin(requet.user) or is_student(requet.user)
        
        # Only admins can add /edit/delete teachers
        return is_admin(requet.user)
    
class StudentAccessPermission(permissions.BasePermission):
    def has_permission(self, request, view):

        # Teachers and Admin can view students but student cannot view all students

        if request.method in permissions.SAFE_METHODS:
            return is_teacher(request.user) or is_admin(request.user) or is_student(request.user)
        

        # Only Admins can add/edit or delete students

        return is_admin(request.user)
    

class CanAssignRolesPermission(permissions.BasePermission):
    def has_permission(self, request, view):


        # Only Admins and Superuser can access the registration view
        return is_admin(request.user)
    
    


    



from django.core.mail import send_mail
from .models import User
from .utils import generate_temp_password

def reset_user_password(email):
    """
    Reset the user's password and send the temporary password via email.
    """
    try:
        user = User.objects.get(email=email)  # Find the user by email
        temp_password = generate_temp_password()  # Generate a temporary password
        user.set_password(temp_password)  # Set the temporary password
        user.save()

        # Send an email with the temporary password
        send_mail(
            subject="Your Password Has Been Reset",
            message=f"Hello {user.username},\n\nYour temporary password is: {temp_password}\n"
                    f"Please log in and change your password immediately.",
            from_email="admin@myapp.com",
            recipient_list=[email],
            fail_silently=False,
        )

        return f"A temporary password has been sent to {email}."
    except User.DoesNotExist:
        return "User with this email does not exist."

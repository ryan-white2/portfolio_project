from src.models import User


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """
    test_user = User('Reynaldo Blanco', 'rb@gmail.com', 6501234567, 'Mexico', 'M',
                     'Spanish', '0', '1999-03-31', 99, '1999-01-01 06:04:02 UTC', 'rblanco', 'P@$$w0rd123')
    assert test_user.account_name == 'Reynaldo Blanco'
    assert test_user.account_email == 'rb@gmail.com'
    assert test_user.account_phone == 6501234567
    assert test_user.account_country == 'Mexico'
    assert test_user.account_sex == 'M'
    assert test_user.account_language == 'Spanish'
    assert test_user.account_birthdate == '1999-03-31'
    assert test_user.account_age == 99
    assert test_user.account_login == 'rblanco'
    assert test_user.account_password == 'P@$$w0rd123'


def test_new_user_with_fixture(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields are defined correctly
    """
    assert new_user.account_name == 'Joe Jackson'
    assert new_user.account_email == 'joe@yahoo.com'
    assert new_user.account_phone == 7708845654
    assert new_user.account_country == 'United States'
    assert new_user.account_sex == 'M'
    assert new_user.account_language == 'Spanish'
    assert new_user.user_birthdate == '1988-06-11'
    assert new_user.user_age == 33
    assert new_user.account_login == 'jjackson'
    assert new_user.account_password == 'notsecure'

import pytest

# --- Complex fixture that manages resource setup and teardown ---
@pytest.fixture(scope="module")
def db_connection():
    print("Setup DB connection")
    conn = {"connected": True, "data": []}  # Simulated DB connection object
    yield conn
    print("Teardown DB connection")
    conn["connected"] = False

# --- Factory fixture returning a function to create user records ---
@pytest.fixture
def user_factory(db_connection):
    created_users = []

    def _create_user(username, email):
        print('--- create user in user_factory ---')
        user = {"username": username, "email": email}
        db_connection["data"].append(user)
        created_users.append(user)
        return user

    yield _create_user

    print('--- cleanup created user after test ---')
    for user in created_users:
        db_connection["data"].remove(user)

# --- Fixture that depends on another fixture ---
@pytest.fixture
def admin_user(user_factory):
    print('--- user_factor: admin_user ---')
    return user_factory("admin", "admin@example.com")

# --- Parametrized fixture to test with different user roles ---
@pytest.fixture(params=["guest", "member", "admin"])
def user_role(request):
    print(f'--- user_role fixture: {request.param} ---')
    return request.param

# --- Applying multiple fixtures at class level with usefixtures ---
@pytest.mark.usefixtures("db_connection", "user_factory")
class TestUserManagement:

    def test_create_user(self, user_factory):
        user = user_factory("alice", "alice@example.com")
        assert user in user_factory.__closure__[0].cell_contents  # user_factory's created_users list

    def test_admin_user(self, admin_user):
        assert admin_user["username"] == "admin"

    @pytest.mark.usefixtures("admin_user")
    def test_admin_access(self, user_role):
        # Simulate access control based on role
        allowed_roles = ["admin", "member"]
        if user_role in allowed_roles:
            access = True
        else:
            access = False
        if user_role == "admin":
            assert access is True
        else:
            assert access == (user_role in allowed_roles)

# --- Using usefixtures at function level with multiple fixtures ---
@pytest.mark.usefixtures("db_connection", "admin_user")
def test_db_and_admin_ready():
    # This test doesn't explicitly accept fixtures but they run before it
    assert True

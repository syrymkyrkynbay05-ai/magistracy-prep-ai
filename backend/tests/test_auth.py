"""Full auth flow test using urllib (no external deps)."""

import sys, os, json
from urllib.request import Request, urlopen
from urllib.error import HTTPError

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
os.chdir(os.path.dirname(__file__))

BASE = "http://localhost:8000"


def api(method, path, body=None, token=None):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    data = json.dumps(body).encode() if body else None
    req = Request(f"{BASE}{path}", data=data, headers=headers, method=method)
    try:
        resp = urlopen(req)
        return resp.status, json.loads(resp.read())
    except HTTPError as e:
        content = e.read().decode()
        try:
            return e.code, json.loads(content)
        except:
            return e.code, {"detail": content}
    except Exception as e:
        return 0, {"detail": str(e)}


# 0. Preparation: Clear test user if exists
from database import SessionLocal
from auth import DBUser

print("0. PREPARATION: Clearing test user...")
db = SessionLocal()
db.query(DBUser).filter(DBUser.email == "azamat@test.com").delete()
db.commit()
db.close()


# 1. Register
print("=" * 50)
print("1. REGISTER")
status, data = api(
    "POST",
    "/auth/register",
    {
        "email": "azamat@test.com",
        "full_name": "Азамат Пердеев",
        "password": "qwerty123",
    },
)
print(f"   Status: {status}")
print(f"   User ID: {data['user']['id']} (int: {isinstance(data['user']['id'], int)})")
print(f"   Token: {data['access_token'][:40]}...")
token = data["access_token"]

# 2. Login
print("\n2. LOGIN")
status, data = api(
    "POST", "/auth/login", {"email": "azamat@test.com", "password": "qwerty123"}
)
print(f"   Status: {status}")
print(f"   Name: {data['user']['full_name']}")

# 3. Profile
print("\n3. PROFILE (GET /auth/me)")
status, data = api("GET", "/auth/me", token=token)
print(f"   Status: {status}")
print(f"   Data: {data}")

# 4. Forgot password
print("\n4. FORGOT PASSWORD (sends OTP to email)")
status, data = api("POST", "/auth/forgot-password", {"email": "azamat@test.com"})
print(f"   Status: {status}")
print(f"   Message: {data['message']}")

# 5. Get OTP from DB
from database import SessionLocal
from auth import DBUser

db = SessionLocal()
user = db.query(DBUser).filter(DBUser.email == "azamat@test.com").first()
otp = user.otp_code
print(f"   OTP from DB: {otp}")
db.close()

# 6. Verify OTP
print("\n5. VERIFY OTP")
status, data = api(
    "POST", "/auth/verify-otp", {"email": "azamat@test.com", "otp_code": otp}
)
print(f"   Status: {status}")
print(f"   Message: {data.get('message', data)}")

# 7. Reset password
print("\n6. RESET PASSWORD")
status, data = api(
    "POST",
    "/auth/reset-password",
    {"email": "azamat@test.com", "otp_code": otp, "new_password": "newpass456"},
)
print(f"   Status: {status}")
print(f"   Message: {data.get('message', data)}")

# 8. Login with new password
print("\n7. LOGIN (new password)")
status, data = api(
    "POST", "/auth/login", {"email": "azamat@test.com", "password": "newpass456"}
)
print(f"   Status: {status} ({'OK' if status == 200 else 'FAIL'})")

# 9. Login with old password (should fail)
print("\n8. LOGIN (old password → should fail)")
status, data = api(
    "POST", "/auth/login", {"email": "azamat@test.com", "password": "qwerty123"}
)
print(f"   Status: {status} (expected 401)")

# 10. Duplicate register
print("\n9. DUPLICATE REGISTER (should fail)")
status, data = api(
    "POST",
    "/auth/register",
    {"email": "azamat@test.com", "full_name": "X", "password": "pass123"},
)
print(f"   Status: {status} (expected 409)")

print("\n" + "=" * 50)
print("✅ ALL AUTH TESTS COMPLETE!")

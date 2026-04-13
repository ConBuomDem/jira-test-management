# test_login.py - Demo Quan ly Test Case bang JIRA
# Nhom 3: Dang Do Lin - Chu Thanh Lich - Nguyen Xuan Vinh

import unittest

class TestLogin(unittest.TestCase):

    def test_TC001_login_valid(self):
        """TC-001: Dang nhap voi email & mat khau hop le"""
        result = self.mock_login("user@example.com", "correct_password")
        self.assertEqual(result["status"], "success")
        print("PASS - TC-001: Dang nhap thanh cong")

    def test_TC002_login_wrong_password(self):
        """TC-002: Dang nhap voi mat khau sai"""
        result = self.mock_login("user@example.com", "wrong_password")
        self.assertEqual(result["status"], "error")
        print("PASS - TC-002: Hien thi loi sai mat khau")

    def test_TC003_email_not_exist(self):
        """TC-003: Dang nhap voi email khong ton tai"""
        result = self.mock_login("notexist@example.com", "any_password")
        self.assertEqual(result["status"], "error")
        print("PASS - TC-003: Hien thi loi email khong ton tai")

    def mock_login(self, email, password):
        if email == "user@example.com" and password == "correct_password":
            return {"status": "success", "redirect": "/dashboard"}
        elif email == "notexist@example.com":
            return {"status": "error", "message": "Email khong ton tai"}
        else:
            return {"status": "error", "message": "Sai mat khau"}

if __name__ == "__main__":
    unittest.main()

"""
exceptions/member_limit_exceeded_exception.py

CUSTOM EXCEPTION
Raised when a member tries to borrow more books than their
allowed limit (Member.MAX_BOOKS_ALLOWED).
"""


class MemberLimitExceededException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        
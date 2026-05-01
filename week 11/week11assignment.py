from dataclasses import dataclass, field
from contextlib import contextmanager
class EmailError(Exception):
    pass

@dataclass
class Email:
    subject: str
    category: str
    size: int
    _status: str = field(init=False, default="UNREAD")

    def __post_init__(self):
        if self.size <= 0:
            raise EmailError(f"Invalid size for {self.subject}")
    
    @property
    def is_large(self):
        return self.size > 100
    
    def __str__(self):
        return f"{self.subject} ({self.category}, {self.size}KB) [{self._status}]"
    
    def __gt__(self, other):
        if not isinstance(other, Email):
            return NotImplemented
        return self.size > other.size
    
class InboxFilter:
    def __init__(self, emails, allowed):
        self.emails = emails
        self.allowed = allowed
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.emails):
            raise StopIteration
        email = self.emails[self.index]
        self.index += 1
        if email.category in self.allowed:
            email._status = "KEPT"
        else:
            email._status = "DELETED"
        return email
    
def inbox_report(filt):
    kept = 0
    deleted = 0
    for email in filt:
        if email._status == 'KEPT':
            kept += 1
        else:
            deleted += 1
        yield str(email)
    yield f'Result: {kept} kept, {deleted} deleted'

@contextmanager
def inbox_session(name):
    emails = []
    print(f'[OPEN] {name}')
    try:
        yield emails
    except EmailError as message:
        print(f'!!! Error: {message}')
    finally:
        print(f'[CLOSE] {name} ({len(emails)} emails)')

with inbox_session("Work Inbox") as emails:
    emails.append(Email("Newsletter", "Promo", 45))
    emails.append(Email("Meeting Notes", "Work", 120))
    emails.append(Email("Spam Offer", "Spam", 8))

    for line in inbox_report(InboxFilter(emails, ("Promo", "Work"))):
        print(line)

    print(emails[1] > emails[0])

print()

with inbox_session("Personal Inbox") as emails:
    emails.append(Email("Reminder", "Work", -3))

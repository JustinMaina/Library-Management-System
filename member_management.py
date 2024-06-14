from database import session
from models import Member

def add_member(name, email):
    new_member = Member(name=name, email=email)
    session.add(new_member)
    session.commit()

def get_all_members():
    return session.query(Member).all()

def delete_member(member_id):
    member = session.query(Member).filter_by(id=member_id).first()
    if member:
        session.delete(member)
        session.commit()

<<<<<<< HEAD
from hashlib import md5
from flask import g

from models import (
    db, Teacher, Group, Subject, TeacherGroupSubject, Position
)


def get_index_page_data():
    teachers = db.session.query(Teacher).all()
    groups = db.session.query(Group).all()
    subjects = db.session.query(Subject).all()

    data = {
        'teachers': teachers,
        'groups': groups,
        'subjects': subjects,
    }

    result = []
    teachers_groups_subjects = db.session.query(TeacherGroupSubject).all()

    for teacher_group_subject in teachers_groups_subjects:
        teacher = db.session.query(Teacher).filter(
            Teacher.id == teacher_group_subject.teacher_id
        ).first()

        position = db.session.query(Position).filter(
            Position.id == teacher.position_id
        ).first()

        group = db.session.query(Group).filter(
            Group.id == teacher_group_subject.group_id
        ).first()

        subject = db.session.query(Subject).filter(
            Subject.id == teacher_group_subject.subject_id
        ).first()

        result.append({
            'id': teacher_group_subject.id,
            'teacher_id': teacher.id,
            'teacher_fullname': f'{teacher.first_name} {teacher.last_name} ({position.name})',
            'group_id': group.id,
            'group_name': group.name,
            'subject_id': subject.id,
            'subject_name': subject.name,
        })

    data['list'] = result

    return data


def get_group_list():
    groups = db.session.query(Group).all()
    result = []

    for group in groups:
        result.append({'id': group.id, 'name': group.name})
=======
from database import conn


def get_group_list(groups):
    result = []

    for group in groups:
        result.append({'id': group[0], 'name': group[1]})
>>>>>>> myrepo/main
    
    return result


def get_students_list(students):
    result = []
<<<<<<< HEAD

    for student in students:
        group = db.session.query(Group).filter(
            Group.id == student.group_id
        ).first()

        result.append({
            'id': student.id, 
            'first_name': student.first_name,
            'last_name': student.last_name,
            'group_name': group.name,
            'group_id': group.id,
=======
    con = conn.cursor()

    for student in students:
        con.execute(f'SELECT * FROM t_group WHERE id={student[3]}')
        group = con.fetchone()

        result.append({
            'id': student[0], 
            'first_name': student[1],
            'last_name': student[2],
            'group_name': group[1],
>>>>>>> myrepo/main
        })

    return result


<<<<<<< HEAD
def get_teachers_list():
    teachers = db.session.query(Teacher).all()
    result = []

    for teacher in teachers:
        position = db.session.query(Position).filter(
            Position.id == teacher.position_id
        ).first()

        result.append({
            'id': teacher.id,
            'first_name': teacher.first_name,
            'last_name': teacher.last_name,
            'position_name': position.name,
            'position_id': position.id,
=======
def get_teachers_list(teachers):
    result = []
    con = conn.cursor()

    for teacher in teachers:
        con.execute(f'SELECT * FROM t_position WHERE id={teacher[3]}')
        position = con.fetchone()

        result.append({
            'id': teacher[0],
            'first_name': teacher[1],
            'last_name': teacher[2],
            'position_name': position[1],
>>>>>>> myrepo/main
        })

    return result


<<<<<<< HEAD
def get_subjects_list():
    subjects = db.session.query(Subject).all()
    result = []

    for subject in subjects:
        result.append({'id': subject.id, 'name': subject.name})

    return result


def get_positions_list():
    positions = db.session.query(Position).all()
    result = []

    for position in positions:
        result.append({'id': position.id, 'name': position.name})
    
    return result


def check_password(user_password, request_password):
    hashed_password = md5(request_password.encode()).hexdigest()

    if user_password != hashed_password:
        return False
    return True
=======
def get_subjects_list(subjects):
    result = []

    for subject in subjects:
        result.append({'id': subject[0], 'name': subject[1]})
    
    return result


def get_teachers_groups_list(teachers_groups):
    result = []
    con = conn.cursor()

    for tech_gr in teachers_groups:
        con.execute(f'SELECT * FROM t_teacher WHERE id={tech_gr[1]}')
        teacher = con.fetchone()

        con.execute(f'SELECT * FROM t_group WHERE id={tech_gr[2]}')
        group = con.fetchone()

        con.execute(f'SELECT * FROM t_subject WHERE id={tech_gr[3]}')
        subject = con.fetchone()

        result.append({
            'teacher_fullname': f'{teacher[1]} {teacher[2]}',
            'group_name': group[1],
            'subject_name': subject[1],
        })

    return result
>>>>>>> myrepo/main

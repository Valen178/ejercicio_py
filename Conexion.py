import json
import os
import sqlite3

DATA_FILE = 'users.json'


def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

def save_users(users):
    with open(DATA_FILE, 'w') as file:
        json.dump(users, file)

def create_user(username, email):
    users = load_users()
    user_id = len(users) + 1
    new_user = {'id': user_id, 'username': username, 'email': email}
    users.append(new_user)
    save_users(users)
    return new_user

def read_users():
    return load_users()

def update_user(user_id, username=None, email=None):
    users = load_users()
    for user in users:
        if user['id'] == user_id:
            if username:
                user['username'] = username
            if email:
                user['email'] = email
            save_users(users)
            return user
    return None

def delete_user(user_id):
    users = load_users()
    users = [user for user in users if user['id'] != user_id]
    save_users(users)


class Conexion:
    def __init__(self, nombre_bd):
        self.nombre_bd=nombre_bd
        self.conexion=sqlite3.conexion(nombre_bd)
        self.cursor=self.conexion.cursor()
        
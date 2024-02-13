from typing import List
import databases
import sqlalchemy as sqla
from fastapi import FastAPI
from models_4 import Task, TaskIn

DATABASE_URL = "sqlite:///mydatabase.db"
database = databases.Database(DATABASE_URL)
metadata = sqla.MetaData()

tasks = sqla.Table("tasks", metadata, 
    sqla.Column("task_id", sqla.Integer, primary_key=True),
    sqla.Column("title", sqla.String(32)),
    sqla.Column("description", sqla.String),
    sqla.Column("status", sqla.Boolean),
)


engine = sqla.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)

app = FastAPI()


# Создание задачи в БД, create
@app.post("/tasks/", response_model=Task)
async def create_task(task: Task):
    query = tasks.insert().values(title=task.name, description=task.description)
    last_record_id = await database.execute(query)
    return {**task.dict(), "id": last_record_id}


# Чтение задач из БД, read
@app.get("/tasks/", response_model=List[TaskIn])
async def read_users():
    query = tasks.select()
    return await database.fetch_all(query)


# Чтение одноq задачи из БД, read
@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    return await database.fetch_one(query)


# Обновление задачи в БД, update
@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, new_task: TaskIn):
    query = tasks.update().where(tasks.c.id == task_id).values(**new_task.dict())
    await database.execute(query)
    return {**new_task.dict(), "id": task_id}


# Удаление задачи из БД, delete
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    await database.execute(query)
    return {'message': 'Task deleted'}
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Модель для задачи
class Task(BaseModel):
    title: str
    description: str
    status: bool = False

# Фейковая база данных для примера
fake_db = []

# Конечная точка для получения списка всех задач
@app.get("/tasks", response_model=List[Task])
def read_tasks():
    return fake_db

# Конечная точка для получения задачи по идентификатору
@app.get("/tasks/{id}", response_model=Task)
def read_task(id: int):
    task = fake_db[id]
    if task:
        return task
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

# Конечная точка для добавления новой задачи
@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    fake_db.append(task)
    return task

# Конечная точка для обновления задачи
@app.put("/tasks/{id}", response_model=Task)
def update_task(id: int, task: Task):
    if id >= len(fake_db):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    fake_db[id] = task
    return task

# Конечная точка для удаления задачи
@app.delete("/tasks/{id}", response_model=Task)
def delete_task(id: int):
    if id >= len(fake_db):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    deleted_task = fake_db.pop(id)
    return deleted_task

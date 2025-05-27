from flask import Blueprint, request, jsonify
from app.services.task_service import TaskService

task_bp = Blueprint("task", __name__)

@task_bp.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(TaskService.get_all_tasks())

@task_bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    return jsonify(TaskService.create_task(data["title"], data.get("description", "")))

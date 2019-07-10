def filter_tasks(tasks, tag):
  "вывод задач с имеющимся тегом"
  buff=[]
  for elem in tasks:
      if tag in elem["tags"]:
          buff.append(elem["task_id"])  
  return buff 

tasks = [
    {"task_id": 1, "tags": ["1", "2", "3"]},
    {"task_id": 2, "tags": ["3", "4", "5"]},
    {"task_id": 3, "tags": ["5", "7", "2"]},
]
tasks_hollow = []

print(filter_tasks(tasks, "1"))# вернёт [1]
print(filter_tasks(tasks, "5"))# вернёт [2, 3]
print(filter_tasks(tasks, "2"))# вернёт [1, 3]
print(filter_tasks(tasks_hollow, "2"))# вернёт []
print(filter_tasks(tasks, ""))# вернёт []

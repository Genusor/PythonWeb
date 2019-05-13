from tasks.models import TodoItem
all_tasks = (
  "прочитать книгу",
  "учиться жонглировать 30 минут",
  "помыть посуду",
  "поесть"
)
for desc in all_tasks:
  t = TodoItem(description=desc)
  t.save()
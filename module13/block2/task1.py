def filter_tags(tags_by_task):
  "вывод списка уникальных значений"
  buff=[]
  for elem in tags_by_task:
      for i in elem:
          if not i in buff:
            buff.append(i)
  return buff 

tags_by_task = [
    ["1", "2", "3"],
    ["3", "2", "5"],
    ["5", "7"],
]


filter_tags(tags_by_task)
import json

#写入json数据文件
user = {
    "name": "张三",
    "age": 18,
    "gender": "男",
    "city": "北京",
    "is_student": True,
    "hobbies": ["阅读", "运动", "旅行"],
    "score": None
}
with open("res/user.json", "w", encoding="utf-8") as f:
    #ensure_ascii=False: 确保中文不被转义,如果是True不是ascii码则转义成ascii码, indent=2: 确保格式化输出:添加缩进
    json.dump(user, f, ensure_ascii=False, indent=2)

with open("res/user.json", "r", encoding="utf-8") as f:
    user = json.load(f)
    print(user)

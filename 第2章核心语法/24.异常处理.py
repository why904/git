try:
    print('ABC'.hello)
except NameError as e:
    print("名称不存在,请检查,具体信息:", e)
except ZeroDivisionError as e:
    print("0不能被做除数,请检查,具体信息:")
except IndexError as e:
    print("索引出现问题,请检查,具体信息:", e)
except Exception as e:
    print("其他错误,请检查,具体信息:", e)
finally:
    print("finally有没有错误都会运行")
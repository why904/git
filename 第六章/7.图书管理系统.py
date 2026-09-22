from abc import ABC,abstractmethod
import json
class Book:#图书类
    def __init__(self,book_id,title,author,tutal_num):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.tutal_num=tutal_num
        self.__available_num=tutal_num

    def borrow_books(self):#判断并借阅图书
        if self.__available_num>0:
            self.__available_num-=1
            return True
        return False

    def return_books(self):#还书
        print(f"已归还《{self.title}》")
        self.__available_num+=1

    #获取可用量
    def get_available_num(self):
        return self.__available_num

#会员类
class Member(ABC):
    def __init__(self,member_id,name,password):
        self.member_id=member_id    #会员ID
        self.name=name              #会员名
        self.__password=password    #会员密码
        self.__borrowed_books=[]    #已借阅的书籍

    def borrow_books(self,book):#借阅书籍
        if len(self.__borrowed_books)>=self.get_max_books():
            print(f"{self.name}已借阅满")
            return False
        if book.borrow_books():
            self.__borrowed_books.append(book)
            print(f"{self.name}已借阅《{book.title}》剩余{book.get_available_num()}")
            return True
        else:
            print(f"《{book.title}》已借完")
            return False

    def return_books(self,book):#还书
        if book in self.__borrowed_books:
            book.return_books()
            self.__borrowed_books.remove(book)
            return True
        else:
            print(f"{self.name}未借阅《{book.title}》")
            return False

    def get_borrowed_books(self):#获取已借阅的书籍
        return self.__borrowed_books

    def get_password(self):#获取密码
        return self.__password
    @abstractmethod
    def get_max_books(self):#获取最大借阅量
        pass

class NormalMember(Member):#普通用户
    def get_max_books(self)->int:#获取最大借阅量
        return 3

class VIPMember(Member):#VIP用户
    def __init__(self, member_id, name, password,vip_level):
        super().__init__(member_id, name, password)
        self.vip_level=vip_level
    def get_max_books(self):
        return self.vip_level+3

#图书管理系统
class LibrarySystem:
    def __init__(self):
        self.books= {}#图书列表
        self.members={}#会员列表
        self.current_members:Member|None=None#当前会员
        #加载数据
        self.load_books_data()#加载图书数据
        self.load_members_data()#加载会员数据

    def load_books_data(self):
        #加载data/books.json
        with open('./data/books.json','r',encoding='utf-8') as f:
            books_data=json.load(f)
            for book in books_data:
                self.books[book['编号']]=Book(book['编号'],book['标题'],book['作者'],book['数量'])
            print(f"已加载图书数据")
    def load_members_data(self):
        # 加载data/members.json
        with open('./data/members.json', 'r', encoding='utf-8') as f:
            members_data = json.load(f)
            for member in members_data:
                if member['卡号'][0] == 'V':
                    self.members[member['卡号']] = VIPMember(member['卡号'], member['姓名'], member['密码'], member['会员等级'])
                else:
                    self.members[member['卡号']] = NormalMember(member['卡号'], member['姓名'], member['密码'])
            print(f"已加载会员数据")

    def login(self):#登录
        while True:
            print(f"\n登录")
            member_id = input("请输入会员ID：")
            password = input("请输入密码：")
            if member_id not in self.members:
                print('登录失败,卡号不存在')
                continue
            if self.members[member_id].get_password() == password:
                self.current_members = self.members[member_id]
                print(f"{self.current_members.name}登录成功")
                return True
            else:
                print(f"登录失败")
                continue

    def borrow_books(self):#1.借阅图书
        for book in self.books.values():
            print(f"编号：{book.book_id} 标题：{book.title} 作者：{book.author} 剩余数量：{book.get_available_num()}")
        book_id = input("请输入借阅的图书编号：")
        if book_id in self.books:
            self.current_members.borrow_books(self.books[book_id])
        else:
            print(f"图书编号不存在")

    def return_books(self):#2.还书
        print(f"已借阅的图书列表")
        for book in self.current_members.get_borrowed_books():
            print(f"编号：{book.book_id} 标题：{book.title} ")
        book_id = input("请输入还书的图书编号：")
        if book_id in self.books:
            self.current_members.return_books(self.books[book_id])
        else:
            print(f"图书编号不存在")

    def search_books(self):#3.查询借阅图书
        print(f"查询借阅图书")
        if len(self.current_members.get_borrowed_books())>0:
            for book in self.current_members.get_borrowed_books():
                print(f"编号：{book.book_id} 标题：{book.title} 作者：{book.author} 总数:{book.tutal_num} 剩余数量：{book.get_available_num()}")
        else:
            print(f"当前会员暂无借阅图书")

    def search_members(self):#4.查询会员
        print(f"查询会员")
        member_id = input("请输入查询的会员编号：")
        if member_id in self.members:
            member = self.members[member_id]
            vip_info = member.vip_level if isinstance(member, VIPMember) else "无"
            print(f"编号：{member.member_id} 姓名：{member.name} 会员等级：{vip_info}")
        else:
            print(f"会员编号不存在")

    def run(self):
        if self.login():
            print(f"欢迎{self.current_members.name}登录")
            while True:
                print(f"###################################################################")
                print(f"1.借阅图书 2.还书 3.查询借阅图书 4.查询会员 5.退出")
                print(f"###################################################################")
                choice = input("请输入你的选择(1-5)：")
                match choice:
                    case '1':
                        self.borrow_books()
                    case '2':
                        self.return_books()
                    case '3':
                        self.search_books()
                    case '4':
                        self.search_members()
                    case '5':
                        print(f"退出系统")
                        break
                    case _:
                        print(f"无效的选择，请重新输入")

if __name__=="__main__":
    ls=LibrarySystem()
    ls.run()
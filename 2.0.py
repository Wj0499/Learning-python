# V2.0 搜索引擎 - 文档管理 + 分页
import re

class SequenceList:
    def __init__(self):
        self.data = []

    def append(self, elem):
        self.data.append(elem)

    def delete(self, doc_id):
        for i, d in enumerate(self.data):
            if d["id"] == doc_id:
                del self.data[i]
                return True
        return False

    def update(self, doc_id, new_title, new_content):
        for d in self.data:
            if d["id"] == doc_id:
                d["title"] = new_title
                d["content"] = new_content
                return True
        return False

    def get_all(self):
        return self.data

class SearchEngineV2:
    def __init__(self):
        self.docs = SequenceList()

    def tokenize(self, text):
        return re.findall(r"[\u4e00-\u9fa5a-zA-Z0-9]+", text.lower())

    def add_doc(self, doc_id, title, content):
        self.docs.append({"id": doc_id, "title": title, "content": content})

    def del_doc(self, doc_id):
        return self.docs.delete(doc_id)

    def modify_doc(self, doc_id, title, content):
        return self.docs.update(doc_id, title, content)

    def search(self, query):
        qs = self.tokenize(query)
        res = []
        for doc in self.docs.get_all():
            text = doc["title"] + doc["content"]
            if all(w in text for w in qs):
                res.append(doc)
        return res

    def page_result(self, data, page=1, page_size=2):
        start = (page - 1) * page_size
        end = start + page_size
        return data[start:end]

if __name__ == "__main__":
    se = SearchEngineV2()
    se.add_doc(1, "Java教程", "Java是主流后端编程语言")
    se.add_doc(2, "Java项目实战", "使用Java开发网站与搜索引擎")
    se.add_doc(3, "前端开发", "HTML CSS JS 网页制作")

    print("===== V2.0 组合搜索 + 分页 =====")
    ret = se.search("Java 搜索引擎")
    page1 = se.page_result(ret, 1, 2)
    for d in page1:
        print(f"ID:{d['id']} 标题:{d['title']}")

    se.del_doc(3)
    print("\n删除文档3后总数：", len(se.docs.get_all()))
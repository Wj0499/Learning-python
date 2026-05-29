# V1.0 简单搜索引擎 - 基础搜索
import re
from collections import Counter

# 顺序表
class SequenceList:
    def __init__(self):
        self.data = []
        self.length = 0

    def append(self, elem):
        self.data.append(elem)
        self.length += 1

    def traverse(self):
        return self.data

# 单链表
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, elem):
        new_node = Node(elem)
        if not self.head:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
        self.length += 1

    def traverse(self):
        res = []
        cur = self.head
        while cur:
            res.append(cur.data)
            cur = cur.next
        return res

class SearchEngineV1:
    def __init__(self):
        self.docs = SequenceList()
        self.index = LinkedList()

    def tokenize(self, text):
        text = text.lower()
        return re.findall(r"\b[a-zA-Z0-9\u4e00-\u9fa5]+\b", text)

    def add_doc(self, doc_id, title, content):
        doc = {"id": doc_id, "title": title, "content": content}
        self.docs.append(doc)
        words = self.tokenize(title + " " + content)
        for word in set(words):
            idx_list = self.index.traverse()
            exist = False
            for item in idx_list:
                if item["word"] == word:
                    if doc_id not in item["ids"]:
                        item["ids"].append(doc_id)
                    exist = True
                    break
            if not exist:
                self.index.append({"word": word, "ids": [doc_id]})

    def search(self, query):
        q_words = self.tokenize(query)
        if not q_words:
            return []
        match_ids = set()
        idx_list = self.index.traverse()
        for w in q_words:
            for item in idx_list:
                if item["word"] == w:
                    match_ids.update(item["ids"])
        results = []
        all_docs = self.docs.traverse()
        for doc in all_docs:
            if doc["id"] in match_ids:
                results.append(doc)
        return results

if __name__ == "__main__":
    se = SearchEngineV1()
    se.add_doc(1, "Python入门", "Python简单好用，适合编程入门")
    se.add_doc(2, "搜索引擎原理", "搜索引擎依靠索引实现快速查找")
    se.add_doc(3, "Python开发", "使用Python制作简易搜索引擎")

    print("===== V1.0 搜索结果 =====")
    for res in se.search("Python"):
        print(f"ID:{res['id']} 标题:{res['title']}")
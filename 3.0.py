# V3.0 搜索引擎 - 队列 + 搜索历史 + 热度排序
import re
from collections import Counter

# 队列
class Queue:
    def __init__(self, max_len=10):
        self.queue = []
        self.max_len = max_len

    def enqueue(self, val):
        self.queue.append(val)
        if len(self.queue) > self.max_len:
            self.queue.pop(0)

    def get_history(self):
        return self.queue

class SearchEngineV3:
    def __init__(self):
        self.docs = []
        self.history = Queue()
        self.hot = {}  # 文档热度

    def tokenize(self, text):
        return re.findall(r"[\u4e00-\u9fa5a-zA-Z]+", text.lower())

    def add_doc(self, doc_id, title, content):
        self.docs.append({"id": doc_id, "title": title, "content": content})
        self.hot[doc_id] = 0

    def search(self, query):
        self.history.enqueue(query)
        q_words = self.tokenize(query)
        result = []
        for doc in self.docs:
            full_text = doc["title"] + doc["content"]
            words = self.tokenize(full_text)
            cnt = Counter(words)
            score = sum(cnt[w] for w in q_words)
            if score > 0:
                result.append((-score, doc))
                self.hot[doc["id"]] += 1
        result.sort()
        return [d for (s, d) in result]

    def sort_by_hot(self):
        return sorted(self.docs, key=lambda x: self.hot[x["id"]], reverse=True)

if __name__ == "__main__":
    se = SearchEngineV3()
    se.add_doc(1, "人工智能", "人工智能改变生活，智能搜索很方便")
    se.add_doc(2, "大数据", "大数据支撑搜索引擎运行")
    se.add_doc(3, "人工智能应用", "AI 智能检索与推荐系统")

    print("===== V3.0 搜索 + 历史 + 热度 =====")
    print("搜索结果：")
    for d in se.search("人工智能"):
        print(d["title"])
    print("搜索历史：", se.history.get_history())
    print("按热度排序：")
    for d in se.sort_by_hot():
        print(f"{d['title']} 热度:{se.hot[d['id']]}")
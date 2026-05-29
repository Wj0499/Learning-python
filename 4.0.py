# V4.0 搜索引擎 - 字符串匹配 + 精确短语搜索
import re

class SearchEngineV4:
    def __init__(self):
        self.docs = []

    def add_doc(self, doc_id, title, content):
        self.docs.append({"id": doc_id, "title": title, "content": content})

    # 精确短语匹配
    def exact_search(self, phrase):
        res = []
        for doc in self.docs:
            if phrase in doc["title"] or phrase in doc["content"]:
                res.append(doc)
        return res

    # 关键词高亮
    def highlight(self, text, keyword):
        return text.replace(keyword, f"【{keyword}】")

    def fuzzy_search(self, keyword):
        res = []
        for doc in self.docs:
            if keyword in doc["title"] or keyword in doc["content"]:
                doc["title"] = self.highlight(doc["title"], keyword)
                doc["content"] = self.highlight(doc["content"], keyword)
                res.append(doc)
        return res

if __name__ == "__main__":
    se = SearchEngineV4()
    se.add_doc(1, "机器学习基础", "机器学习是人工智能的核心技术")
    se.add_doc(2, "深度学习实战", "深度学习属于机器学习分支")
    se.add_doc(3, "网络爬虫", "爬虫用于抓取网页做搜索数据源")

    print("===== V4.0 精确短语搜索 =====")
    for d in se.exact_search("机器学习"):
        print(f"标题：{d['title']}")

    print("\n===== 关键词高亮 =====")
    for d in se.fuzzy_search("爬虫"):
        print(f"高亮内容：{d['content']}")
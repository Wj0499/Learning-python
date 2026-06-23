# V5.0 搜索引擎 - 二叉排序树 + 分类检索
class BSTNode:
    def __init__(self, word, doc_ids):
        self.word = word
        self.doc_ids = doc_ids
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, word, doc_id):
        if not self.root:
            self.root = BSTNode(word, [doc_id])
            return
        cur = self.root
        while True:
            if word < cur.word:
                if not cur.left:
                    cur.left = BSTNode(word, [doc_id])
                    break
                cur = cur.left
            elif word > cur.word:
                if not cur.right:
                    cur.right = BSTNode(word, [doc_id])
                    break
                cur = cur.right
            else:
                if doc_id not in cur.doc_ids:
                    cur.doc_ids.append(doc_id)
                break

    def search_word(self, word):
        cur = self.root
        while cur:
            if word == cur.word:
                return cur.doc_ids
            elif word < cur.word:
                cur = cur.left
            else:
                cur = cur.right
        return []

class SearchEngineV5:
    def __init__(self):
        self.tree = BinarySearchTree()
        self.docs = {}
        self.tag_map = {}

    def add_doc(self, doc_id, title, content, tag):
        self.docs[doc_id] = {"title": title, "content": content, "tag": tag}
        if tag not in self.tag_map:
            self.tag_map[tag] = []
        self.tag_map[tag].append(doc_id)
        for w in title+content:
            if w.strip():
                self.tree.insert(w, doc_id)

    def search_by_word(self, word):
        ids = self.tree.search_word(word)
        return [self.docs[i] for i in ids if i in self.docs]

    def search_by_tag(self, tag):
        ids = self.tag_map.get(tag, [])
        return [self.docs[i] for i in ids if i in self.docs]

if __name__ == "__main__":
    se = SearchEngineV5()
    se.add_doc(1, "C++语法", "C++面向对象编程", "编程")
    se.add_doc(2, "MySQL数据库", "数据库存储数据", "数据库")
    se.add_doc(3, "C++项目", "用C++写后台服务", "编程")

    print("===== V5.0 二叉树关键词搜索 =====")
    for d in se.search_by_word("C"):
        print(d["title"])
    print("\n按标签【编程】检索：")
    for d in se.search_by_tag("编程"):
        print(d["title"])
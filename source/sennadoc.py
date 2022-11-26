from collections import defaultdict
import warnings
import docutils.nodes
import docutils.transforms
from docutils.parsers.rst import Directive

counters = defaultdict(int)
registered_articles = {}

class ArticleDirective(Directive):
    required_arguments = 1
    final_argument_whitespace = True

    def run(self):
        name, = self.arguments
        id = name.lower().replace(" ", "-")
        docname = self.state.document.current_source

        counters[docname] += 1
        registered_articles[id] = counters[docname]
        name = f"Article {counters[docname]} : {name}"
        id2 = f"article-{counters[docname]}"

        return [docutils.nodes.section(id,
                                       docutils.nodes.title(id, name),
                                       ids=[id, id2])]

delayed = object()
delayedshort = object()

def art_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    if name == "artref":
        sentinel = delayed
    elif name == "artrefshort":
        sentinel = delayedshort
    nod = docutils.nodes.reference(text, None, refid=text)
    nod.flag = sentinel
    return [nod], []

class SennaTransform(docutils.transforms.Transform):
    default_priority = 750

    def apply(self):
        for node in self.document.traverse(docutils.nodes.reference):
            flag = getattr(node, "flag", None)
            if flag is not None:
                if flag is delayed:
                    st = "l'article {}"
                elif flag is delayedshort:
                    st = "{}"
                rf = registered_articles.get(node["refid"], None)
                if rf is None:
                    warnings.warn(f"Article {node['refid']!r} not found, a faulty artref was issued.")
                node.children[:] = [docutils.nodes.Text(st.format(rf))]

def setup(app):
    app.add_directive("article", cls=ArticleDirective)
    app.add_role("artref", art_role)
    app.add_role("artrefshort", art_role)

    app.add_transform(SennaTransform)

from collections import defaultdict
import docutils.nodes
import docutils.transforms
from docutils.parsers.rst import Directive

counters = defaultdict(int)
registered_articles = {}

class ArticleDirective(Directive):
    has_content = True
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

        children = [docutils.nodes.title(id, name)]
        content = " ".join(self.content)
        if content:
            children.append(docutils.nodes.paragraph("", content))

        return [docutils.nodes.section(id,
                                       *children,
                                       ids=[id, id2])]

delayed = object()

def art_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    nod = docutils.nodes.reference(text, delayed, refid=text)
    nod.flag = delayed
    return [nod], []

class SennaTransform(docutils.transforms.Transform):
    default_priority = 750

    def apply(self):
        for node in self.document.traverse(docutils.nodes.reference):
            if getattr(node, "flag", None) is delayed:
                node.children[:] = [docutils.nodes.Text(f"article {registered_articles[node['refid']]}")]

def setup(app):
    app.add_directive("article", cls=ArticleDirective)
    app.add_role("artref", art_role)

    app.add_transform(SennaTransform)

from collections import defaultdict
import docutils.nodes
import sphinx.addnodes
from sphinx.errors import ExtensionError
import sphinx.roles
import sphinx.domains
import sphinx.domains.std
import sphinx.util.docutils

counters = defaultdict(int)
registered_articles = {}
dummy_id = 0

class ArticleDirective(sphinx.domains.std.Target):
    """
    Piggyback Target and recompute fullname (but not node_id)
    """
    required_arguments = 0
    optional_arguments = 1

    def run(self):
        docname = self.state.document.current_source
        counters[docname] += 1
        name = f"Article {counters[docname]}"

        if not self.arguments:
            # anonymous article - not referenceable, no target
            rv = []
            global dummy_id
            dummy_id += 1
            node_id = f"dummy-{dummy_id}"
        else:
            rv = super().run()
            node_id, *_ = rv[0]["ids"][0]
            # recompute fullname - Target doesn't save it properly
            fullname = sphinx.domains.std.ws_re.sub(' ', self.arguments[0].strip())
            if fullname in registered_articles:
                raise ExtensionError(f"an article {fullname!r} is already registered")
            registered_articles[fullname] = counters[docname]
            name = f"{name} - {fullname}"
            # yes, the name is longer than the fullname

        rv.append(docutils.nodes.section(name,
                                         docutils.nodes.title(name, name),
                                         ids=[node_id]))
        return rv

artrefflag = object()
artnumrefflag = object()

class ArtRole(sphinx.roles.XRefRole):
    # no innernodeclass, on purpose

    def __init__(self, *args, flag, **kwargs):
        self.flag = flag
        super().__init__(*args, **kwargs)

    def result_nodes(self, *args, **kwargs):
        (node,), msgs = super().result_nodes(*args, **kwargs)
        node.flag = self.flag
        return [node], msgs

class ArtrefTransform(docutils.transforms.Transform):
    default_priority = 750

    def apply(self):
        for node in self.document.traverse(sphinx.addnodes.pending_xref):
            if node["refexplicit"]:
                continue
            # print(node)
            flag = getattr(node, "flag", None)
            # print(flag)
            if flag is not None:
                rf = registered_articles.get(node["reftarget"], None)
                # print(rf)
                if rf is None:
                    print(f"number of article {node['reftarget']!r} not found")
                    continue
                if flag is artnumrefflag:
                    name = str(rf)
                elif flag is artrefflag:
                    name = f"l'article {rf}"
                else:
                    raise ExtensionError(f"unknown flag {flag!r}")
                node.children[:] = [docutils.nodes.generated(node.children[0].rawsource, name)]

def setup(app):
    app.add_directive_to_domain("std", "article", ArticleDirective)
    app.add_role_to_domain("std", "artref", ArtRole(flag=artrefflag))
    app.add_role_to_domain("std", "artnumref", ArtRole(flag=artnumrefflag))
    object_types = app.registry.domain_object_types.setdefault('std', {})
    object_types["article"] = sphinx.domains.ObjType("article", "artref", "artnumref")

    app.add_transform(ArtrefTransform)

import docutils.nodes
from docutils.parsers.rst import Directive
import sphinx.addnodes
from sphinx.errors import ExtensionError
import sphinx.domains
import sphinx.domains.std
import sphinx.roles
import sphinx.util.docutils

registered_source = {} # document -> source (str)
counters = {} # source (str) -> number of articles (int)
registered_articles = {} # article name (str) -> tuple(source (str), article number (int))
dummy_id = 0

class ArtsourceDirective(Directive):
    """
    Register the name of the original document the next articles will be part of.
    At most one may exist per document.
    References under it to articles from a different document, or above it,
    or in a document with no artsource, will be suffixed with the source name.
    """
    required_arguments = 1
    final_argument_whitespace = True

    def run(self):
        source, = self.arguments
        if source in counters:
            raise ExtensionError(f"source name {source!r} already registered")
        docname = self.state.document.current_source
        if docname in registered_source:
            raise ExtensionError(f"document {docname!r} already has a source")
        registered_source[docname] = source
        counters[source] = 0
        return []

class ArticleDirective(sphinx.domains.std.Target):
    """
    Piggyback Target and recompute fullname (but not node_id).
    The article directive may not be used before the artsource directive.
    """
    required_arguments = 0
    optional_arguments = 1

    def run(self):
        try:
            source = registered_source[self.state.document.current_source]
        except KeyError:
            raise ExtensionError(f"no source name registered for document {self.state.document.current_source!r}")
        counters[source] += 1
        name = f"Article {counters[source]}"

        if not self.arguments:
            # anonymous article - not referenceable, no target
            rv = []
            global dummy_id
            dummy_id += 1
            node_id = f"dummy-{dummy_id}"
        else:
            rv = super().run()
            node_id = rv[0]["ids"][0]
            # recompute fullname - Target doesn't save it properly
            fullname = sphinx.domains.std.ws_re.sub(' ', self.arguments[0].strip())
            if fullname in registered_articles:
                raise ExtensionError(f"an article {fullname!r} is already registered")
            registered_articles[fullname] = (source, counters[source])
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
        name = None
        for node in self.document.traverse(sphinx.addnodes.pending_xref):
            if node["refexplicit"]:
                name = node.children[0].children[0]
            else:
                # print(node)
                flag = getattr(node, "flag", None)
                # print(flag)
                if flag is not None:
                    refsc, nb = registered_articles.get(node["reftarget"], (None, None))
                    # print(nb)
                    if nb is None:
                        print(f"number of article {node['reftarget']!r} not found")
                        continue
                    if flag is artnumrefflag:
                        name = str(nb)
                    elif flag is artrefflag:
                        name = f"l'article {nb}"
                        if refsc != registered_source.get(node.source, None):
                            name = " ".join((name, refsc))
                    else:
                        raise ExtensionError(f"unknown flag {flag!r}")

            if name:
                node.children[:] = [docutils.nodes.generated(node.children[0].rawsource, name)]
            name = None

def setup(app):
    app.add_directive_to_domain("std", "artsource", ArtsourceDirective)
    app.add_directive_to_domain("std", "article", ArticleDirective)
    app.add_role_to_domain("std", "artref", ArtRole(flag=artrefflag))
    app.add_role_to_domain("std", "artnumref", ArtRole(flag=artnumrefflag))
    object_types = app.registry.domain_object_types.setdefault('std', {})
    object_types["article"] = sphinx.domains.ObjType("article", "artref", "artnumref")

    app.add_transform(ArtrefTransform)

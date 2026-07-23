import type { Graph } from "@hpcc-js/wasm-graphviz";
import { DataRoot, Situations, Evenement } from "../data.js";

export function addData(graph: Graph, data: DataRoot) {
    addNodes(graph, data.situations);
    addEdges(graph, data["événements"]);
}

function addNodes(graph: Graph, situations: Situations) {
    const parentNodeIds = Object.keys(situations).map(sId => situations[sId]?.parent).filter(sId => sId != undefined);

    for (const parentId of parentNodeIds) {
        const { name, desc } = situations[parentId]!;
        using _ = graph.addSubgraph(parentId, {
            label: name,
            tooltip: desc,
        });
    }

    for (const sId of Object.keys(situations)) {
        const { name, desc, parent: parentId } = situations[sId]!;
        using parent = parentId ? graph.getSubgraph(parentId) : undefined;
        (parent ?? graph).addNode(sId, {
            label: name,
            comment: desc,
            tooltip: desc,
        });
    }
}

function addEdges(graph: Graph, evenements: readonly Evenement[]) {
    for (const { n, name, desc, variantes, optional } of evenements) {
        for (const { id, name: varianteName, situations = [], /*condition,*/ "résultat": resultat, nomination } of variantes) {
            const classes: string[] = [];
            if (optional) {
                classes.push("optional");
            }
            if (nomination) {
                classes.push("nomination");
            }

            for (const situation of situations) {
                graph.addEdge(situation, resultat, id ? `${n}-${id}` : `${n}`, {
                    label: varianteName ?? name,
                    comment: desc,
                    tooltip: desc,
                }, {
                    class: classes.join(" "),
                });
            }
        }
    }
}

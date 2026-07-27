import type { EdgeAttrs, Graph } from "@hpcc-js/wasm-graphviz";
import { DataRoot, Situations, Evenement } from "../data.js";

export function addData(graph: Graph, data: DataRoot) {
    graph.setGraphAttr("compound", true);
    graph.setGraphAttr("K", 3);
    addNodes(graph, data.situations);
    addEdges(graph, data["événements"]);
}

function addNodes(graph: Graph, situations: Situations) {
    const parentNodeIds = Object.keys(situations).map(sId => situations[sId]?.parent).filter(sId => sId != undefined);

    for (const parentId of parentNodeIds) {
        const { name, desc } = situations[parentId]!;
        using sub = graph.addSubgraph(parentId, {
            label: name,
            tooltip: desc,
            cluster: true,
        });
        sub.addNode(parentId, {
            style: "invis",
        });
    }

    for (const sId of Object.keys(situations)) {
        if (graph.hasSubgraph(sId)) {
            continue;
        }
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
    for (const { n, name, desc, variantes, optional = false } of evenements) {
        for (const { id, name: varianteName, situations = [], /*condition,*/ "résultat": resultat, nomination } of variantes) {
            for (const situation of situations) {
                id ? `${n}-${id}` : `${n}`;
                graph.addEdge(situation, resultat, /*id ? `${n}-${id}` : `${n}`,*/ {
                    label: varianteName ?? name,
                    comment: desc,
                    tooltip: desc,
                    ...getEdgeStyle(optional, nomination),
                    ...getHeadTailOverrides(graph, situation, resultat),
                });
            }
        }
    }
}

function getEdgeStyle(optional: boolean, nomination: boolean) {
    const options: EdgeAttrs = {};
    if (optional) {
        options.color = "orange";
        options.fontcolor = "orangered";
    }
    if (nomination) {
        options.color = "blue";
        options.fontcolor = "darkslateblue";
    }
    return options;
}

function getHeadTailOverrides(graph: Graph, source: string, target: string) {
    const options: EdgeAttrs = {};
    const cSource = cluster(source);
    if (graph.hasSubgraph(source)) {
        options.ltail = cSource;
    }
    const cTarget = cluster(target);
    if (graph.hasSubgraph(target)) {
        options.lhead = cTarget;
    }
    return options;
}

function cluster(id: string) {
    return `cluster_${id}`;
}


/*
Note :
il est impossible de faire un arc qui boucle sur un parent,
ou dont une extrémité est sur un parent alors que l'autre extrémité est sur un enfant de ce parent
*/
